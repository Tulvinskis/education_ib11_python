def encode_morse(text):
    morse_code_dict = {
        'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
        'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
        'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
        'Y': '-.--', 'Z': '--..',
        '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
        '6': '-....', '7': '--...', '8': '---..', '9': '----.'
    }

    encoded_text = []
    for word in text.split():
        encoded_word = ''
        for char in word.upper():
            if char in morse_code_dict:
                encoded_word += morse_code_dict[char] + ' '
        encoded_text.append(encoded_word.strip())

    return encoded_text

def main():
    text = input("Введите текст для кодирования в азбуку Морзе: ")
    encoded_text = encode_morse(text)
    for word in encoded_text:
        print(word)

if __name__ == "__main__":
    main()
