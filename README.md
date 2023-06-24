# translang
Translation Service Module for other projects.


# Install
```
pip install translang
```

# Usage

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

## Bugs and Issues
Sincerely grateful for any reports on new features or bugs. Your valuable feedback on the code is highly appreciated.

## Contacts
- Core maintainer: [Daniel Park, South Korea](https://github.com/DSDanielPark) <br>
- E-mail: parkminwoo1991@gmail.com <br>
