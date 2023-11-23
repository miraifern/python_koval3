from googletrans import Translator, LANGUAGES
import os
translator = Translator()

def TransLate(text: str, src: str, dest: str) -> str:
    try:
        return Translator().translate(text, src=src, dest=dest).text
    except Exception as e:
        return f"Помилка перекладу : {str(e)}"

def LangDetect(text: str, set: str = "all") -> str:
        translator = Translator()
        try:
            lang = translator.detect(text)
            if set == "lang":
                return lang.lang
            elif set == "confidence":
                return str(lang.confidence)
            else:
                return f"Мова: {lang.lang} \nКоефіцієнт довіри: {lang.confidence}"
        except Exception as e:
            return f"Помилка перекладу: {str(e)}"

def CodeLang(lang: str) -> str:
        lang = lang.lower()
        if lang in LANGUAGES:
            return LANGUAGES[lang]
        elif lang in LANGUAGES.values():
            return [k for k, v in LANGUAGES.items() if v == lang][0]
        else:
             return f"Код мови '{lang}' не знайдено"

def LanguageList(out: str, text: str = None) -> str:
    translator = Translator()
    output = ""

    output += f"N\tLanguage\tISO-639 code\t\tText\n" if text else "N\tLanguage\tISO-639 code\n"
    output += "-" * 56 + "\n"

    if text is not None:
        for idx, (code, lang) in enumerate(LANGUAGES.items(), start=1):
            translation = translator.translate(text, dest=code).text
            output += f"{idx:<2}\t {lang:<12}\t {code:<15}\t {translation}\n"
    else:
        for idx, (code, lang) in enumerate(LANGUAGES.items(), start=1):
            output += f"{idx:<2}\t {lang:<12}\t {code}\n"

    if out == "file":
        with open("trans.txt", "w", encoding='utf-8') as file:
            file.write(output)

        return f"Ok: Таблиця збережена у trans.txt"
    else:
        print(output)
        return "Ok"
