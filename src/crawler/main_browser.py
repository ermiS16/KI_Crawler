import json
from pathlib import Path
from uuid import uuid4

from OpenAIClient import OpenAIClient


EXTRACTION_SCHEMA = {
    'type': 'object',
    'properties': {
        'companies': {'type': 'array', 'items': {
            'type': 'object', 'properties': {
                'company_name': {'type': 'string'}, 'federal_state': {'type': 'string'},
                'register_court': {'type': 'string'}, 'register_type': {'type': 'string'},
                'register_number': {'type': 'string'}, 'registered_office': {'type': ['string', 'null']},
                'source_url': {'type': ['string', 'null']},
                'documents': {'type': 'array', 'items': {
                    'type': 'object', 'properties': {
                        'document_type': {'type': 'string', 'enum': ['CD', 'SI']},
                        'document_url': {'type': ['string', 'null']},
                        'filename': {'type': ['string', 'null']},
                        'file_path': {'type': ['string', 'null']},
                        'download_status': {'type': 'string', 'enum': ['downloaded', 'failed', 'not_attempted']}
                        },
                        'required': ['document_type', 'document_url', 'filename', 'file_path', 'download_status'],
                        'additionalProperties': False
                }}
            },
            'required': ['company_name', 'federal_state', 'register_court', 'register_type',
                            'register_number', 'registered_office', 'source_url', 'documents'],
            'additionalProperties': False
        }},
        'notes': {'type': ['string', 'null']}
    }, 'required': ['companies', 'notes'], 'additionalProperties': False
}

prompt = """
    Bediene die öffentliche Registersuchmaske.

    Bundesland: Hamburg
    Registergericht: Amtsgericht Hamburg
    Registerart: HRB
    Maximale Anzahl Unternehmen: 1

    Extrahiere die Registerdaten aus der Ergebnisliste.

    Identifiziere die Dokumente CD und SI und verwende die
    download-Aktion, um beide Dokumente herunterzuladen.

    Übernimm die Download-URL, den Dateinamen und den lokalen
    Dateipfad aus der Rückgabe des Browser-Tools.

    Erfinde keine Informationen.
    Verwende null für unbekannte Werte.
    Umgehe keine Zugriffsbeschränkungen oder Sicherheitsabfragen.
    Beschreibe technische Hindernisse unter notes.
"""

if __name__ == '__main__':
    client = OpenAIClient()
    crawl_id = str(uuid4())
    response = client.create(
        model='gpt-6-luna', crawl_id=crawl_id, browser_use=True, web_search=False, headless=False,
        start_url='https://www.unternehmensregister.de/de/suche/registerinformationen',
        domains=['unternehmensregister.de'], schema=EXTRACTION_SCHEMA, max_steps=20,
        prompt=prompt
    )
    result = json.loads(response.output_text)
    output_dir = Path('results')
    output_dir.mkdir(parents=True, exist_ok=True)
    with (output_dir / f'{crawl_id}.json').open('w', encoding='utf-8') as file:
        json.dump(result, file, indent=4, ensure_ascii=False)
    print(json.dumps(result, indent=4, ensure_ascii=False))
