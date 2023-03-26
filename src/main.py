from google.cloud import translate
from typer import Typer, Argument, Option
from .config import settings
from typing import List
import pyperclip
from rich.console import Console

GOOGLE_APLICATION_CREDENTIALS = settings.google_aplication_credentials
PROJECT_ID = settings.project_id

console = Console()
app = Typer(add_completion=False)

@app.command()
def translate_text(
    text: List[str] = Argument(...,help="Text to be translated", show_default=False), 
    target_lang: str = Option("en-US", "--target", "-t", help="Target language text to be translated"), 
    source_lang: str = Option("", "--source", "-s", help="Source language of text to be translated"),
    portuguese: bool = Option(False, "--pt", "-p", help="Text will be translated into portuguese"),
    copy: bool = Option(False, "--copy", "-c", help="The output will be copied to clipboard"),
):   
    client = translate.TranslationServiceClient()
    location = "global"
    parent = f"projects/{PROJECT_ID}/locations/{location}"
    if portuguese:
        target_lang = "pt-BR"
    
    with console.status("Translating..."):
        response = client.translate_text(
            request={
                "parent": parent,
                "contents": [" ".join(text)],
                "mime_type": "text/plain",
                "source_language_code": source_lang,
                "target_language_code": target_lang,
            }
        )

    for translation in response.translations:
        console.print(translation.translated_text)
        if copy:
            pyperclip.copy(translation.translated_text)


if __name__ == "__main__":
    app()
