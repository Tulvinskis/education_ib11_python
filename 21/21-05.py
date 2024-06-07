import datetime as dt
import math

birthday_date = input()
biorhythm_date = input()

birth_day = dt.datetime.now().strptime(birthday_date, '%d.%m.%Y')
biort_day = dt.datetime.now().strptime(biorhythm_date, '%d.%m.%Y')

days_passed = (biort_day - birth_day).days


def calculate_biorhythm(p):
    return round(math.sin(2 * math.pi * days_passed / p) * 100, 2)


psysical_biort = calculate_biorhythm(23)
emotional_biort = calculate_biorhythm(28)
intellectual_biort = calculate_biorhythm(33)

print(psysical_biort)
print(emotional_biort)
print(intellectual_biort)