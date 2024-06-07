def game(text):
    if text.count(' ') % 2 == 0:
        print('Вы выиграли')
    else:
        print('Вы проиграли')


text = input()
game(text)