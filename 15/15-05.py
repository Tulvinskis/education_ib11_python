def number_in_english(number):
    unit = {0: 'zero', 1: 'one', 2: 'two', 3: 'three', 4: 'four', 5: 'five',
            6: 'six', 7: 'seven', 8: 'eight', 9: 'nine'}
    ten_nineteen = {10: 'ten', 11: 'eleven', 12: 'twelve', 13: 'thirteen', 14: 'fourteen',
                    15: 'fifteen', 16: 'sixteen', 17: 'seventeen', 18: 'eighteen', 19: 'nineteen'}
    tens = {20: 'twenty', 30: 'thirty', 40: 'forty', 50: 'fifty', 60: 'sixty',
            70: 'seventy', 80: 'eighty', 90: 'ninety'}

    if number < 20:
        return unit.get(number, ten_nineteen.get(number, ''))
    elif number < 100:
        if number % 10 == 0:
            return tens[number]
        else:
            return tens[number // 10 * 10] + ' ' + unit[number % 10]
    else:
        return unit[number // 100] + ' hundred' + (' and ' + number_in_english(number % 100) if number % 100 else '')


print(number_in_english(10).lower())