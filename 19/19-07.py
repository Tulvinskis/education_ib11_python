def same_by(characteristic, object):
    return len(set(map(characteristic, object))) == 1 if object else True


values = [1, 2, 3, 4]
if same_by(lambda x: x % 2, values):
    print('same')
else:
    print('different')