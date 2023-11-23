import anastasia.mod2

transl = input("Введіть текст для перекладу: ")
target_language = input("Введіть код мови:  ")

print("Переклад : ",anastasia.mod2.TransLate(transl, "auto", target_language))

print(anastasia.mod2.LangDetect(transl, "all"))

print(f"Мова на яку переклали {target_language}: " ,anastasia.mod2.CodeLang(target_language))

print("\nСписок мов у консолі:")
print(anastasia.mod2.LanguageList("screen", transl))

print(anastasia.mod2.LanguageList("file", transl))