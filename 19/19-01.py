def arithmetic_operation(operator):
    operations = {
        '+': lambda x, y: x + y,
        '-': lambda x, y: x - y,
        '*': lambda x, y: x * y,
        '/': lambda x, y: x / y
    }
    return operations[operator if operator in operations else None]


operation = arithmetic_operation('+')
print(operation(1, 4))