import anastasia.mod1


trans = input("Введіть текст для перекладу: ")
target_language = input("Введіть код мови: ")
print()
print("Переклад тексту: ", anastasia.mod1.TransLate(trans, "auto", target_language))

print(anastasia.mod1.LangDetect(trans, "all"))

print(f"Мова на яку переклали {target_language}: ", anastasia.mod1.CodeLang(target_language))

print("\nСписок мов у консолі:")
print(anastasia.mod1.LanguageList("screen", trans))

print(anastasia.mod1.LanguageList("file", trans))