from googletrans import Translator


def ConfigRead(config_filename):
    config = {}
    try:
        with open(config_filename, 'r', encoding='utf-8') as config_file:
            for line in config_file:
                key, value = line.strip().split(':')
                config[key.strip()] = value.strip()
        return config
    except FileNotFoundError:
        return None


def ReadTextFromConfig(input_filename):
    try:
        with open(input_filename, 'r', encoding='utf-8') as input_file:
            text = input_file.read()
        return text
    except FileNotFoundError:
        print("Файл з текстом не знайдено.")
        return None


def TextTransl():
    config_file = ConfigRead('config.txt')

    if config_file is None:
        print("Конфігураційний файл не знайдено.")
        return

    input_filename = config_file.get('Назва файлу з текстом')
    output_mode = config_file.get('Куди вивести результат')
    target_language = config_file.get('Назва або код мови перекладання')
    max_characters = int(config_file.get('Кількість символів'))
    max_words = int(config_file.get('Кількість слів'))
    max_sentences = int(config_file.get('Кількість речень'))

    text = ReadTextFromConfig(input_filename)

    if text is None:
        return

    try:
        translator = Translator()

        translated_text = ""
        current_characters = 0
        current_words = 0
        current_sentences = 0

        for char in text:
            if char in [' ', '\n']:
                current_words += 1

            if char in ['.', '!', '?']:
                current_sentences += 1

            if current_characters >= max_characters or current_words >= max_words or current_sentences >= max_sentences:
                if char in ['.', '!', '?']:
                    translated_text += char
                break

            translated_text += char
            current_characters += 1

        translated_text = translator.translate(translated_text, dest=target_language).text

        print("\nПерекладений текст:")
        print(translated_text)

        if output_mode == 'text.txt':
            output_filename = f"texttrans.txt"
            with open(output_filename, 'w', encoding='utf-8') as output_file:
                output_file.write(translated_text)
            print("\nЗаданий текст перекладено та збережено у texttrans.txt")
        elif output_mode == 'екран':
            print("Мова перекладу:", target_language)
            print("\nПерекладений текст:")
            print(translated_text)
        else:
            print("Невірно вказаний режим виводу")

    except FileNotFoundError:
        print("Файл з текстом не знайдено.")
    except Exception as e:
        print("Помилка:", str(e))

if __name__ == "__main__":
    TextTransl()