def max_treasure_route(points):
  """
  Находит максимальное количество точек, которые можно посетить.
  Args:
    points: Список кортежей (x, y) - координаты точек.
  Returns:
    Максимальное количество точек в маршруте.
  """

  def can_visit(point1, point2):
    """Проверяет, можно ли перейти от point1 к point2."""
    x1, y1 = point1
    x2, y2 = point2
    return abs(x1 % 10 - x2 % 10) <= 1 and abs(y1 % 10 - y2 % 10) <= 1

  n = len(points)
  dp = [1] * n

  for i in range(1, n):
    for j in range(i):
      if can_visit(points[j], points[i]):
        dp[i] = max(dp[i], dp[j] + 1)

  return max(dp)

n = int(input())
points = []
for _ in range(n):
  x, y = map(int, input().split())
  points.append((x, y))

max_route_length = max_treasure_route(points)
print(max_route_length)
