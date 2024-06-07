count = 1
product = []
def add_item(name: str, cost: int):
    product.append((name, cost))

def print_receipt():
    global count
    if not product:
        return
    check = 0
    print(f"Чек {count}. Всего товаров: {len(product)}")
    for name, cost in product:
        check += cost
        print(f"{name} - {cost}")
    print(f"Итого: {check}\n-----")
    count += 1
    product.clear()


add_item('Блокнот', 100)
print_receipt()
add_item('Ручка', 70)
print_receipt()
print_receipt()
add_item('Булочка', 15)
add_item('Булочка', 15)
add_item('Чай', 5)
print_receipt()
add_item('Булочка', 15)
add_item('Булочка', 15)