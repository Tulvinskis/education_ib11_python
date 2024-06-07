def format_email(name, date, email, place=False, city='Нефтекамск'):
    if place:
        return "To: {}\nЗдравствуйте, {}!\nБыли бы рады видеть вас на встрече " \
               "начинающих программистов в {}, которая пройдет {}.".format(email, name, place, date)
    return "To: {}\nЗдравствуйте, {}!\nБыли бы рады видеть вас на встрече начинающих " \
           "программистов в {}ке, которая пройдет {}.".format(email, name, city[0:-1], date)

print(format_email(name= "Иван", date= "15.01.2024", email= "ivan.petrov02rus@list.ru"))