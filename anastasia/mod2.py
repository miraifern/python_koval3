from deep_translator import GoogleTranslator

from langdetect import detect, detect_langs


def TransLate(text: str, src: str, dest: str) -> str:
    try:
        dest = dest.lower()
        translator = GoogleTranslator(source=src, target=dest)
        translated_text = translator.translate(text)
        return translated_text
    except Exception as e:
        return f"Помилка : {str(e)}"


def LangDetect(text: str, set: str = "all") -> str:
    try:
        detected_langs = detect_langs(text)

        if set == "lang":
            return detected_langs[0].lang
        elif set == "confidence":
            return detected_langs[0].prob
        elif set == "all":
            return f"Мова: {detected_langs[0].lang}\nКоефіцієнт довіри: {detected_langs[0].prob}"
    except Exception as e:
        return f"Помилка перекладу: {str(e)}"


def CodeLang(lang: str) -> str:
    try:
        translator = GoogleTranslator()
        supported_languages = translator.get_supported_languages(as_dict=True)

        lang = lang.lower()
        for code, language in supported_languages.items():
            if language.lower() == lang:
                return code

        if lang in supported_languages:
            return supported_languages[lang]

        return f"Код або назва мови '{lang}' не знайдено"
    except Exception as e:
        return f"Помилка: {str(e)}"


def LanguageList(out: str = "screen", text: str = None) -> str:
    try:
        translator = GoogleTranslator()
        supported_languages = translator.get_supported_languages(as_dict=True)


        table_header = "N\tLanguage\tISO-639 code\t\tText\n" if text else "N\tLanguage\tISO-639 code\n"
        table_sep = "-" * 53 + "\n" if text else "-" * 38 + "\n"

        if out == "screen":
            if text:
                table = table_header
                table += table_sep
                for i, (lang, code) in enumerate(supported_languages.items()):
                    detected_lang = detect(text)
                    translation = GoogleTranslator(source=detected_lang, target=code).translate(text)
                    if len(lang) >= 8:
                        table += f"{i + 1}\t{lang}\t{code}\t\t\t{translation}\n"
                    else:
                        table += f"{i + 1}\t{lang}\t\t{code}\t\t\t{translation}\n"
            else:
                table = table_header
                table += table_sep
                for i, (lang, code) in enumerate(supported_languages.items()):
                    if len(lang) >= 8:
                        table += f"{i + 1}\t{lang}\t\t{code}\n"
                    else:
                        table += f"{i + 1}\t{lang}\t\t\t{code}\n"
            print(table)
            return "Ok"
        elif out == "file":
            if text:
                with open("trans1.txt", "w", encoding="utf-8") as file:
                    file.write(table_header)
                    file.write(table_sep)
                    for i, (lang, code) in enumerate(supported_languages.items()):
                        detected_lang = detect(text)
                        translation = GoogleTranslator(source=detected_lang, target=code).translate(text)
                        if len(lang) >= 8:
                            file.write(f"{i + 1}\t{lang}\t{code}\t\t\t{translation}\n")
                        else:
                            file.write(f"{i + 1}\t{lang}\t\t{code}\t\t\t{translation}\n")
                    return "Ok Таблиця перекладу збережена у {os.getcwd()}\\trans1.txt"
            else:
                with open("trans1.txt", "w", encoding="utf-8") as file:
                    file.write(table_header)
                    file.write(table_sep)
                    for i, (lang, code) in enumerate(supported_languages.items()):
                        if len(lang) >= 8:
                            file.write(f"{i + 1}\t{lang}\t{code}\n")
                        else:
                            file.write(f"{i + 1}\t{lang}\t\t{code}\n")
                    return "Ok Таблиця збережена у trans1.txt"
        else:
            return "Невірний параметр 'out'"
    except Exception as e:
        return str(e)