def transliterate(text):
  replacements = {
      "ё": "e", "й": "i", "ъ": "", "ь": "",
      "Ё": "E", "Й": "I", "Ъ": "", "Ь": "",
      "А": "A", "Б": "B", "В": "V", "Г": "G", "Д": "D",
      "Е": "E", "Ж": "Zh", "З": "Z", "И": "I", "К": "K",
      "Л": "L", "М": "M", "Н": "N", "О": "O", "П": "P",
      "Р": "R", "С": "S", "Т": "T", "У": "U", "Ф": "F",
      "Х": "Kh", "Ц": "Tc", "Ч": "Ch", "Ш": "Sh", "Щ": "Sch",
      "Ы": "Y", "Э": "E", "Ю": "Yu", "Я": "Ya",
  }
  result = ""
  for char in text:
    if char in replacements:
      result += replacements[char]
    else:
      result += char
  return result

text = input("Введите русский текст: ")
transliterated_text = transliterate(text)
print(transliterated_text)
