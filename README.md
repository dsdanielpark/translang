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

    def custom_process_with_translation(self, text: str, dest_lang: str) -> str:
        translated_text = self.translate(text, dest_lang)
        # Perform additional customization or processing if needed
        return translated_text
```

```python
translator = CustomTranslationService(translator="google")

translated_text = translator.custom_process_with_translation("Hello", "ko")
print(translated_text)
```


### `TranslationService.translate` Methods

Google Translator
```python
fomr translang import TranslationService

translator = TranslationService(translator="google")                                                                         # Google
# translator = TranslationService(translator="deepl", deepl_api_key="YOUR_DEEPL_API_KEY")                                    # DeepL
# translator = TranslationService(translator="bard", bard_api_key="YOUR_BARD_API_KEY")                                       # Bard
# translator = TranslationService(translator="openai", openai_api_key="YOUR_OPENAI_API_KEY", openai_model="gpt-3.5-trubo")   # Open AI

translated_text = translator.translate("Hello", "ko")
print(translated_text)
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
