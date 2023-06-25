# translang
Translation Service Module for other projects. 

## Install
```
pip install translang
```

## Usage
### Seamless Integration of Translation APIs through Inheritance
You can easily extend the `TranslationService` class to integrate with popular translation API services.
Refer to the [`inference` method](https://github.com/dsdanielpark/hf-transllm/blob/main/transllm/core.py#L75) and [`generate` method](https://github.com/dsdanielpark/hf-transllm/blob/main/transllm/core.py#L93) in [hf-transllm](https://github.com/dsdanielpark/hf-transllm) project.

```python
from translang import TranslationService

class CustomTranslationService(TranslationService):
    def __init__(self, translator="google", deepl_api_key=None, bard_api_key=None, openai_api_key=None, openai_model='gpt-3.5-turbo'):
        super().__init__(translator, deepl_api_key, bard_api_key, openai_api_key, openai_model)

    def custom_process_with_translation(self, text: str, target_lang: str) -> str:
        translated_text = self.translate(text, target_lang)
        # Perform additional customization or processing if needed
        return translated_text
```

```python
translator = CustomTranslationService(translator="google")

translated_text = translator.custom_process_with_translation("Hello", "ko")
print(translated_text)
```

<br>

### `TranslationService.translate` Method
Google Translator, DeepL, OpenAI, Bard
```python
fomr translang import TranslationService

translator = TranslationService(translator="google")                                                                         # Google
# translator = TranslationService(translator="deepl", deepl_api_key="YOUR_DEEPL_API_KEY")                                    # DeepL
# translator = TranslationService(translator="bard", bard_api_key="YOUR_BARD_API_KEY")                                       # Bard
# translator = TranslationService(translator="openai", openai_api_key="YOUR_OPENAI_API_KEY", openai_model="gpt-3.5-trubo")   # Open AI

translated_text = translator.translate("Hello", "ko")
print(translated_text)
```


<br>

### `TranslationService.translate_parallel` Method

```python
from translang import TranslationService

# Create an instance of TranslationService
translator = TranslationService(translator="google", use_cache=True)

# List of texts to translate
texts = [
    "Hello",
    "Nice to meet you",
    "Testing the translation service"
]

# Destination language code
target_lang = "ko"

# Call the translate_parallel method
translated_texts = translator.translate_parallel(texts, target_lang)

# Print the translated texts
for text, translated_text in zip(texts, translated_texts):
    print(f"Original: {text}")
    print(f"Translated: {translated_text}")
    print("-----")

```

<br><br>


### About Google Translator
Commercial use or official use of the Google Translate service is chargeable. Please provide the `translator="google_official"` and `google_api_key={YOUR_API_KEY}` arguments, Not `translator="google"`. Refer to the following [notebook file](https://github.com/dsdanielpark/translang/blob/main/scripts/google_official.ipynb) and [official link](https://cloud.google.com/translate?utm_source=google&utm_medium=cpc&utm_campaign=japac-KR-all-en-dr-BKWS-all-mv-trial-EXA-dr-1605216&utm_content=text-ad-none-none-DEV_c-CRE_631260646738-ADGP_Hybrid%20%7C%20BKWS%20-%20EXA%20%7C%20Txt%20~%20AI%20&%20ML_Translation%20AI_google%20translate%20api_main-KWID_43700073965169292-kwd-14329410560&userloc_1009871-network_g&utm_term=KW_google%20translate%20api&gclid=Cj0KCQjwy9-kBhCHARIsAHpBjHjTvBCM7NNcf4fYGsog4ViQErgJvACFXB5JCNUT0h_EpQ5kyUT-SrIaApZBEALw_wcB&gclsrc=aw.ds&hl=ko) for more information. Use the google argument only for some basic functionality testing.


## License
[MIT](https://opensource.org/license/mit/) <br>
I hold no legal responsibility; 
```
The MIT License (MIT)

Copyright (c) 2023 Minwoo Park

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
```

### Bugs and Issues
Sincerely grateful for any reports on new features or bugs. Your valuable feedback on the code is highly appreciated.

### Contacts
- Core maintainer: [Daniel Park, South Korea](https://github.com/DSDanielPark) <br>
- E-mail: parkminwoo1991@gmail.com <br>
