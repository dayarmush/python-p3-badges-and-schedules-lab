def badge_maker(name):
    return f'Hello, my name is {name}.'

def batch_badge_creator(names):
    names_list = []

    for name in names:
        names_list.append(f'Hello, my name is {name}.')

    return names_list

def assign_rooms(names):
    x = 1
    room_list = []

    for name in names:
        room_list.append(f"Hello, {name}! You'll be assigned to room {x}!")
        x += 1

    return room_list

def printer(names):
    rooms_list = assign_rooms(names)
    
    for name in names:
       print(badge_maker(name))
    
    for room in rooms_list:
        print(room)

    return None
