from booking.models import Room_Categories
from django.urls import reverse


def get_room_cat_url_list():
    '''
        This function returns Room Category and Room URL
        The function create a dictionary of Tuple from RoomCategories 
        The for loop populate the rooms by categories
    '''

    cat = Room_Categories.objects.all()

    room_cat_url_list=[]

    for category in cat:
          # room_category = room_categories.get(category)
      room_url = reverse('booking:RoomDetailView', kwargs={
                            'category': category.name})
      room_cat_url_list.append((category, room_url))

    return room_cat_url_list