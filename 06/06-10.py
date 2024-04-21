menu = set()
use_menu = set()
menu_not_use = set()
menu_1 = int(input())
for i in range(menu_1):
    menu.add(input())
day_menu_true = int(input())
for i in range(day_menu_true):
    menu_in_day_1 = int(input())
    for j in range(menu_in_day_1):
        use_menu.add(input())
menu_not_use = menu - use_menu
print(*menu_not_use, sep='\n')