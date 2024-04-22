def word_occurrences(text):
  """
  Находит порядковые номера вхождений слов в тексте.

  Args:
    text: Строка текста.

  Returns:
    Список номеров вхождений для каждого слова.
  """

  word_counts = {}
  occurrences = []
  for word in text.split():
    if word not in word_counts:
      word_counts[word] = 0
    word_counts[word] += 1
    occurrences.append(word_counts[word])

  return occurrences

text = input()
occurrences = word_occurrences(text)
print(*occurrences)
