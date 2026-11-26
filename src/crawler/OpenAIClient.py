import csv
import time

from datetime import datetime, timezone
from pathlib import Path
from openai import OpenAI
from uuid import uuid4


class OpenAIClient:

    # Preise in USD pro 1 Mio. Tokens (Standardtarif)
    PRICES = {
        "gpt-6-luna": {"input": 0.10, "cached_input": 0.01, "output": 0.5, 'web_search': 0.01}
    }

    def __init__(self, log_path="usage.csv"):
        self.client = OpenAI()
        self.log_path = Path(log_path)

    def create(self, model, prompt, crawl_id=None, web_search=False, domains=None, schema=None, **kwargs):
        start = time.perf_counter()

        if web_search:
            tool = {"type": "web_search", "search_context_size": "medium"}

            if domains:
                tool["filters"] = {"allowed_domains": domains}

            kwargs["tools"] = [tool]
            kwargs["include"] = ["web_search_call.action.sources"]
            kwargs["tool_choice"] = "required"

        if schema is not None:
            kwargs["text"] = {
                "format": {
                    "type": "json_schema",
                    "name": "data_extraction",
                    "strict": True,
                    "schema": schema
                }
            }

        response = self.client.responses.create(
            model=model, input=prompt, service_tier="default", **kwargs
        )

        duration = time.perf_counter() - start
        self._log_usage(response, crawl_id, duration)

        return response

    def _log_usage(self, response, crawl_id, duration):
        usage = response.usage

        if usage is None:
            return

        input_tokens = usage.input_tokens
        cached_tokens = getattr(usage.input_tokens_details, "cached_tokens", 0) or 0
        output_tokens = usage.output_tokens

        # Anzahl der abrechenbaren Websuchen
        tool_usage = getattr(response, "tool_usage", None)
        web_search_usage = getattr(tool_usage, "web_search", None)
        web_search_calls = getattr(web_search_usage, "num_requests", None)

        # Fallback, falls keine Tool-Usage-Daten verfügbar sind
        if web_search_calls is None:
            web_search_calls = sum(
                item.type == "web_search_call" and getattr(item.action, "type", None) == "search"
                for item in response.output
            )

        prices = self.PRICES.get(response.model)

        token_cost = None
        web_search_cost = None
        cost = None

        if prices:
            token_cost = (
                                 (input_tokens - cached_tokens) * prices["input"]
                                 + cached_tokens * prices["cached_input"]
                                 + output_tokens * prices["output"]
                         ) / 1_000_000

            web_search_cost = web_search_calls * prices["web_search"]
            cost = token_cost + web_search_cost

        row = {
            "timestamp": datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S"),
            "crawl_id": crawl_id,
            "model": response.model,
            "input_tokens": input_tokens,
            "cached_input_tokens": cached_tokens,
            "output_tokens": output_tokens,
            "total_tokens": usage.total_tokens,
            "web_search_calls": web_search_calls,
            "duration_seconds": round(duration, 3),
            "token_cost_usd": f"{token_cost:.8f}" if token_cost is not None else None,
            "web_search_cost_usd": f"{web_search_cost:.8f}" if web_search_cost is not None else None,
            "cost_usd": f"{cost:.8f}" if cost is not None else None
        }

        write_header = not self.log_path.exists() or self.log_path.stat().st_size == 0

        with self.log_path.open("a", newline="", encoding="utf-8") as file:
            writer = csv.DictWriter(file, fieldnames=row.keys())

            if write_header:
                writer.writeheader()

            writer.writerow(row)