from google.cloud import translate
from dotenv import load_dotenv
import os

load_dotenv()

GOOGLE_APPLICATION_CREDENTIALS = os.environ.get("GOOGLE_APPLICATION_CREDENTIALS")
PROJECT_ID = "metal-bus-381401"


def translate_text(text, lang="en-US", source=None):

    client = translate.TranslationServiceClient()
    location = "global"
    parent = f"projects/{PROJECT_ID}/locations/{location}"

    response = client.translate_text(
        request={
            "parent": parent,
            "contents": [text],
            "mime_type": "text/plain",
            "source_language_code": source,
            "target_language_code": lang,
        }
    )

    for translation in response.translations:
        print("Translated text: {}".format(translation.translated_text))


translate_text("ola mundo")
translate_text("always", lang="pt-BR")
translate_text("papagaio")
# translate_text_v2("pt-BR", "hello world!")
