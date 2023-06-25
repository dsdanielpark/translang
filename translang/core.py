import re
import deepl
import openai
import concurrent.futures
from deep_translator import GoogleTranslator
from bardapi import Bard
from typing import List
from google.cloud import translate_v2 as translate


class TranslationService:
    """
    A service for translating text using different translation engines.

    Args:
        translator (str, optional): The translation engine to use. Defaults to "google".
        deepl_api_key (str, optional): API key for DeepL translator. Required if translator is "deepl".
        bard_api_key (str, optional): API key for Bard translator. Required if translator is "bard".
        openai_api_key (str, optional): API key for OpenAI translator. Required if translator is "openai".
        openai_model (str, optional): The OpenAI model to use. Defaults to "gpt-3.5-turbo".
        use_cache (bool, optional): Whether to use a translation cache. Defaults to False.

    Attributes:
        translator (str): The translation engine being used.
        deepl_api_key (str): API key for DeepL translator.
        bard_api_key (str): API key for Bard translator.
        openai_api_key (str): API key for OpenAI translator.
        openai_model (str): The OpenAI model being used.
        use_cache (bool): Whether to use a translation cache.
        translation_cache (dict): Cache for storing translated texts.
        translator_engine: The translation engine object.

    """

    def __init__(self, translator="google", google_api_key=None, deepl_api_key=None, bard_api_key=None, openai_api_key=None, openai_model='gpt-3.5-turbo', use_cache=False):
        self.translator = translator
        self.google_api_key = google_api_key
        self.deepl_api_key = deepl_api_key
        self.bard_api_key = bard_api_key
        self.openai_api_key = openai_api_key
        self.openai_model = openai_model
        self.use_cache = use_cache

        self.translation_cache = {}
        self.translator_engine = None
        
        if self.translator=='google_official':
            self.translator_engine = translate.Client(api_key=google_api_key)
        elif self.translator == "google":
            pass
        elif self.translator == "deepl":
            self.translator_engine = deepl.Translator(auth_key=self.deepl_api_key)
        elif self.translator == "bard":
            self.translator_engine = Bard(token=self.bard_api_key)
        elif self.translator == "openai":
            openai.api_key = self.openai_api_key

                
    def _refine_bard_answer(self, text: str) -> str:
        """
        Extracts and returns refined text from the given input text using specific patterns.
        
        Args:
            text (str): The input text to be refined.
        
        Returns:
            str: The refined text extracted from the input text.
        """
        extracted_text = re.search(r'```(.*?)```|\*\*(.*?)\*\*', text, re.DOTALL)
        
        if extracted_text:
            return extracted_text.group(1) or extracted_text.group(2) 
        
        return text


    def translate(self, text: str, target_lang: str) -> str:
        """
        Translate the given text to the specified destination language.

        Args:
            text (str): The text to be translated.
            target_lang (str): The destination language code.

        Returns:
            str: The translated text.

        """
        if self.use_cache:
            cache_key = (text, target_lang)
            translated_text = self.translation_cache.get(cache_key)
            if translated_text is not None:
                return translated_text
        if self.translator == "google_official":
            translated_text = self.translator_engine.translate(text, target_language=target_lang)
        elif self.translator == "google":
            self.translator_engine = GoogleTranslator(source="auto", target=target_lang)
            translated_text = self.translator_engine.translate(text)
        elif self.translator == "deepl":
            translated_text = self.translator_engine.translate_text(text, target_lang=target_lang).text
        elif self.translator == "bard":
            translated = self.translator_engine.get_answer(f"Translate the following text to {target_lang}: {text}")['content']
            translated_text = self._refine_bard_answer(translated)
        elif self.translator == "openai":
            prompt = f"Translate the following text to {target_lang}: {text}"
            response = openai.Completion.create(engine=self.openai_model, prompt=prompt, max_tokens=100)
            translated_text = response.choices[0].text.strip()

        if self.use_cache:
            cache_key = (text, target_lang)
            self.translation_cache[cache_key] = translated_text

        return translated_text

    def translate_parallel(self, texts: List[str], target_lang: str) -> List[str]:
        """
        Translate a list of texts to the specified destination language in parallel.

        Args:
            texts (List[str]): The list of texts to be translated.
            target_lang (str): The destination language code.

        Returns:
            List[str]: The list of translated texts.

        """
        with concurrent.futures.ThreadPoolExecutor() as executor:
            translated_texts = list(executor.map(self.translate, texts, [target_lang] * len(texts)))
        return translated_texts
