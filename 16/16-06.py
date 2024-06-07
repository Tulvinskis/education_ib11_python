def translate(text):
    global translated_text
    vowels = 'ауоеёиыюяАУОЕЁИЫЮЯ'
    translated_words = []

    for word in text.split():
        translated_word = ''.join(i for i in word if i not in vowels and i.isalpha())
        translated_words.append(translated_word)

    translated_text = ' '.join(translated_words)


translated_text = None
translate('Удивительный факт, но текст на языке НЕРАЗБОРЧИВО оказывается довольно просто прочитать.')
print(translated_text)