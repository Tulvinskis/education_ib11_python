phrase_l = []


def parrot(phrase):
    if phrase in phrase_l:
        print(phrase)
    else:
        phrase_l.append(phrase)


parrot('Привет!')
parrot('Как дела?')
parrot('Привет!')