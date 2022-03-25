from booking.models import Room, Room_Categories
from .availability import check_availability

def get_available_rooms(category, check_in, check_out):
    '''
    Function that takes category and returns Room List
    Initiate an empty list
    Populate the list and check for list length
    '''
    categoryObj = Room_Categories.objects.get(name=category)
    room_list = Room.objects.filter(category=categoryObj)
    
    available_rooms = []

    for room in room_list:
        if check_availability(room, check_in, check_out):
            available_rooms.append(room)

    if len(available_rooms) > 0:
        return available_rooms
    else:
        return None