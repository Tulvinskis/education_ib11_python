def quarter(xcoord, ycoord):
    if xcoord > 0 and ycoord > 0:
        print('I четверть')
    elif xcoord < 0 and ycoord > 0:
        print('II четверть')
    elif xcoord < 0 and ycoord < 0:
        print('III четверть')
    elif xcoord > 0 and ycoord < 0:
        print('IV четверть')
    else:
        print('Лежит на оси координат')


quarter(-3, -4)