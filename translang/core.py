import re
import openai
import asyncio
from bardapi import Bard
from googletrans import Translator


class TranslationService:
    def __init__(self, translator="google", deepl_api=None, bard_api=None, openai_api=None, openai_model='gpt-3.5-turbo'):
        self.translator = translator
        self.deepl_api = deepl_api
        self.bard_api = bard_api
        self.openai_api = openai_api
        self.openai_model = openai_model

        self.translation_cache = {}
        self.translator_obj = None

    async def translate(self, text: str, dest_lang: str) -> str:
        cache_key = (text, dest_lang)
        translated_text = self.translation_cache.get(cache_key)
        if translated_text is not None:
            return translated_text

        if self.translator_obj is None:
            self.translator_obj = self.create_translator()

        if self.translator == "google":
            translated_text = await self.async_translate_google(text, dest_lang)
        elif self.translator == "deepl":
            translated_text = await self.async_translate_deepl(text, dest_lang)
        elif self.translator == "bard":
            translated_text = await self.async_translate_bard(text, dest_lang)
        elif self.translator == "openai":
            translated_text = await self.async_translate_openai(text, dest_lang)

        self.translation_cache[cache_key] = translated_text
        return translated_text

    def create_translator(self):
        if self.translator == "google":
            return Translator()
        elif self.translator == "deepl":
            return deepl.Translator(self.deepl_api)
        elif self.translator == "bard":
            return Bard(token=self.bard_api)

    async def async_translate_google(self, text, dest_lang):
        return (await self.translator_obj.translate(text, dest=dest_lang)).text

    async def async_translate_deepl(self, text, dest_lang):
        return (await self.translator_obj.translate_text(text, target_lang=dest_lang)).text

    async def async_translate_bard(self, text, dest_lang):
        translated = (await self.translator_obj.get_answer(f"translate {text} to {dest_lang} only"))['content']
        extracted_text = re.findall(r'"([^"]*)"', translated)
        return extracted_text[0]

    async def async_translate_openai(self, text, dest_lang):
        openai.api_key = self.openai_api
        prompt = f"Translate the following text to {dest_lang}: {text}\nLanguage: {self.openai_model}\n\nTranslation:"
        response = await asyncio.get_event_loop().run_in_executor(None, openai.Completion.create, engine=self.openai_model, prompt=prompt, max_tokens=100)
        translated_text = response.choices[0].text.strip()
        return translated_text

    def translate_batch(self, texts: list, dest_lang: str) -> list:
        results = []
        for text in texts:
            result = self.translate(text, dest_lang)
            results.append(result)
        return results
