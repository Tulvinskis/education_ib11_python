def month_name(month, lang):
    if lang == "en":
        months = ['January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December']
    elif lang == "ru":
        months = ['январь', 'февраль', 'март', 'апрель', 'май', 'июнь', 'июль', 'август', 'сентябрь', 'октябрь', 'ноябрь', 'декабрь']
    else:
        return "Unsupported language"

    if 1 <= month <= 12:
        return months[month - 1]
    else:
        return "Invalid month number"


print(month_name(3, "en"))
print(month_name(3, "ru"))