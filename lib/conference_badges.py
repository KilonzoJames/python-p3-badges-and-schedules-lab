def badge_maker(name):
    return f"Hello, my name is {name}."
print(badge_maker("Arel"))

def batch_badge_creator(names):
    badge_messages = [f"Hello, my name is {name}." for name in names]
    return badge_messages
print(batch_badge_creator(["Arel", "Carol"]))

def assign_rooms(speakers):
    rooms_assigned = [f"Hello, {speakers[idx]}! You'll be assigned to room {idx+1}!"
                       for idx in range(len(speakers))]
    return rooms_assigned
print(assign_rooms(["Arel", "Catherine"]))

def printer(names):
    badge_messages = batch_badge_creator(names)
    room_assignments = assign_rooms(names)
    for badge_message in badge_messages:
        print(badge_message)
    for room_assignment in room_assignments:
        print(room_assignment)
