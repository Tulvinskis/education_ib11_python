names = ''
dates = ''


def setup_profile(name, vacation_dates):
    global names, dates
    names = name
    dates = vacation_dates


def print_application_for_leave():
    print(f'Заявление на отпуск в период {dates}. {names}')


def print_holiday_money_claim(coin):
    print(f'Прошу выплатить {coin} отпускных денег. {names}')


def print_attorney_letter(sub):
    print(f'На время отпуска в период {dates} моим заместителем назначается {sub}. {names}')


setup_profile('Зубарев Александр', '1 июня - 20 июня')
print_application_for_leave()
print_application_for_leave()
print_holiday_money_claim('15 тысяч коинов')
print_attorney_letter('Гарик Харламов')