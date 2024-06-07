# def continue_fibonacci_sequence(sequence, n):
#     for i in range(n):
#         next_element = sequence[-1] + sequence[-2] Здесь есть ошибка, так как при добавлении нового элемента в список мы создаем новый список, а не изменяем существующий. Это приводит к тому, что цикл for не будет правильно работать.
#         sequence = sequence + [next_element]

def continue_fibonacci_sequence(sequence, n):
     for i in range(n):
         next_element = sequence[-1] + sequence[-2]
         sequence.append(next_element) # Исправленная ошибка в функции


sequence = [1, 1, 2, 3, 5]
continue_fibonacci_sequence(sequence, 0)
print(*sequence)