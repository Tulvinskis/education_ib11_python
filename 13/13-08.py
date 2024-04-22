def check_vocabulary(dictionary, words_to_check):
  """
  Проверяет наличие слов в словаре и выводит их значения.

  Args:
    dictionary: Словарь со словами и их значениями.
    words_to_check: Список слов для проверки.

  Returns:
    Список значений или сообщений "Нет в словаре" для каждого слова.
  """

  results = []
  for word in words_to_check:
    if word in dictionary:
      results.append(dictionary[word])
    else:
      results.append("Нет в словаре")

  return results

n = int(input())
dictionary = {}
for _ in range(n):
  word, definition = input().split(maxsplit=1)
  dictionary[word] = definition

m = int(input())
words_to_check = [input() for _ in range(m)]

results = check_vocabulary(dictionary, words_to_check)
for result in results:
  print(result)
