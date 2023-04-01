from typing import List

import pyperclip
from google.cloud import translate
from rich.console import Console
from typer import Argument, Option, Typer

from .config import settings

try:
    GOOGLE_APLICATION_CREDENTIALS = settings.google_aplication_credentials
    PROJECT_ID = settings.project_id
except AttributeError:
    raise Exception(
        "Please configure your credentials with the command: `tt-configure`"
    )


console = Console()
app = Typer(add_completion=False)


@app.command()
def terminal_translator(
    text: List[str] = Argument(..., help="Text to be translated", show_default=False),
    target_lang: str = Option(
        "en-US", "--target", "-t", help="Target language text to be translated"
    ),
    source_lang: str = Option(
        "", "--source", "-s", help="Source language of text to be translated"
    ),
    portuguese: bool = Option(
        False, "--pt", "-p", help="Text will be translated into portuguese"
    ),
    copy: bool = Option(
        False, "--copy", "-c", help="The output will be copied to clipboard"
    ),
):
    if portuguese:
        target_lang = "pt-BR"

    translated_text = translate_text(" ".join(text), target_lang, source_lang)

    console.print(translated_text)
    if copy:
        pyperclip.copy(translated_text)


def translate_text(text: str, target_lang: str = "en-US", source_lang: str = "") -> str:
    """Takes a text as a parameter, and returns the translation

    Args:
        text (str): text to be translated
        source_lang (str, optional): source language of the text. Defaults to ""
        target_lang (str, optional): target language to translation. Defaults to "en-US"

    Returns:
        str: translated text
    """

    client = translate.TranslationServiceClient()
    location = "global"
    parent = f"projects/{PROJECT_ID}/locations/{location}"

    with console.status("Translating..."):
        response = client.translate_text(
            request={
                "parent": parent,
                "contents": [text],
                "mime_type": "text/plain",
                "source_language_code": source_lang,
                "target_language_code": target_lang,
            }
        )

    return response.translations[0].translated_text
