from booking.models import Room
from django.urls import reverse


def get_room_cat_url_list():
    '''
        This function returns Room Category and Room URL
        The function create a dictionary of Tuple from RoomCategories 
        The for loop populate the rooms by categories
    '''
    room = Room.objects.all()[0]
    room_categories = dict(room.ROOM_CATEGORIES)

    room_cat_url_list=[]

    for category in room_categories:
        room_category = room_categories.get(category)
        room_url = reverse('booking:RoomDetailView', kwargs={
                            'category': category})
        room_cat_url_list.append((room_category, room_url))

    return room_cat_url_list