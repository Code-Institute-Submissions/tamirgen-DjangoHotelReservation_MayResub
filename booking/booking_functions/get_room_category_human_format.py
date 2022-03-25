from booking.models import Room_Categories

def get_room_category_human_format(category):
    '''
    A function that takes computer format room_category and returns it as human format
    '''
    try:
       room_category = Room_Categories.objects.get(name=category)
    except Room_Categories.DoesNotExist:
       room_category = None
    return room_category
   
        

