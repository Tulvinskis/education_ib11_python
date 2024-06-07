friends = {}


def add_friends(name_of_person, list_of_friends):
    if name_of_person not in friends:
        friends[name_of_person] = []
    for friend in list_of_friends:
        if friend not in friends[name_of_person]:
            friends[name_of_person].append(friend)


def are_friends(name_of_person1, name_of_person2):
    return name_of_person2 in friends.get(name_of_person1, [])


def print_friends(name_of_person):
    print(' '.join(sorted(friends.get(name_of_person, []) or ["No friends found"])))


add_friends("Алла", ["Марина", "Иван"])
print(are_friends("Алла", "Мария"))
add_friends("Алла", ["Мария"])
print(are_friends("Алла", "Мария"))