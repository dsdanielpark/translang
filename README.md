# translang
Translation Service Module for other projects. Refer to the [hf-transllm](https://github.com/dsdanielpark/hf-transllm) Project for Reference.



## Install
```
pip install translang
```



## Usage
### Seamless Integration of Translation APIs through Inheritance
You can easily extend the `TranslationService` class to integrate with popular translation API services.
```python
class CustomTranslationService(TranslationService):
    def __init__(self, translator="google", deepl_api=None, bard_api=None, openai_api=None, openai_model='gpt-3.5-turbo'):
        super().__init__(translator, deepl_api, bard_api, openai_api, openai_model)

    def custom_process_with_translation(self, text: str, dest_lang: str) -> str:
        translated_text = self.translate(text, dest_lang)
        # Perform additional customization or processing if needed
        return translated_text
```

```python
translator = CustomTranslationService(translator="google")

text = "Hello, how are you?"
destination_lang = "ko"  # Korean

translated_text = asyncio.run(translator.custom_process_with_translation(text, destination_lang))
print(f"Translated Text (Custom Translation Service): {translated_text}")
```


### Static Methods

Google Translator
```python
translator = TranslationService(translator="google")

text = "Hello, how are you?"
destination_lang = "es"  # Spanish

translated_text = asyncio.run(translator.translate(text, destination_lang))
print(f"Translated Text (Google Translate): {translated_text}")
```

DeepL
```python
translator = TranslationService(translator="deepl", deepl_api="YOUR_DEEPL_API_KEY")

text = "Hello, how are you?"
destination_lang = "es"  # Spanish

translated_text = asyncio.run(translator.translate(text, destination_lang))
print(f"Translated Text (DeepL Translate): {translated_text}")
```

Bard
```python
translator = TranslationService(translator="bard", bard_api="YOUR_BARD_API_KEY")

text = "Hello, how are you?"
destination_lang = "es"  # Spanish

translated_text = asyncio.run(translator.translate(text, destination_lang))
print(f"Translated Text (Bard Translate): {translated_text}")
```

OpenAI
```python
translator = TranslationService(translator="openai", openai_api="YOUR_OPENAI_API_KEY")

text = "Hello, how are you?"
destination_lang = "es"  # Spanish

translated_text = asyncio.run(translator.translate(text, destination_lang))
print(f"Translated Text (OpenAI Translate): {translated_text}")
```


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
