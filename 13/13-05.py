def birthday_calendar(birthdays, queries):
  """
  Находит одноклассников, родившихся в заданные месяцы.

  Args:
    birthdays: Список кортежей (имя, день, месяц).
    queries: Список месяцев для поиска.

  Returns:
    Список списков имен для каждого месяца запроса.
  """

  month_to_number = {  # Словарь для преобразования месяцев в числа
      "янв": 1, "фев": 2, "мар": 3, "апр": 4, "май": 5, "июн": 6,
      "июл": 7, "авг": 8, "сен": 9, "окт": 10, "ноя": 11, "дек": 12
  }

  birthdays_by_month = [[] for _ in range(12)]
  for name, _, month in birthdays:
    month_number = month_to_number[month] - 1
    birthdays_by_month[month_number].append(name)

  results = []
  for month in queries:
    month_number = month_to_number[month] - 1
    names = birthdays_by_month[month_number]
    names.sort()
    results.append(" ".join(names))

  return results

n = int(input())
birthdays = []
for _ in range(n):
  name, day, month = input().split()
  birthdays.append((name, int(day), month))

m = int(input())
queries = [input() for _ in range(m)]

results = birthday_calendar(birthdays, queries)
for result in results:
  print(result)
