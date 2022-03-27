from django.contrib.auth.models import AnonymousUser, User
from django.test import RequestFactory, TestCase

from .models import Room_Categories
from .views import RoomListView, BookingListView, RoomDetailView


# Test if room_list_view page is loading
class RoomListViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='tamir', email='tamir@gmail.com', password='secret')

        Room_Categories.objects.create(name='single', description='single')

    def test_details(self):
        request = self.factory.get('/')
        request.user = self.user
        response = RoomListView(request)
        self.assertEqual(response.status_code, 200)

    def tearDown(self):
        Room_Categories.objects.all().delete()


# Test if booking_list_view is loading if the user is logged-in
class BookingListViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='tamir', email='tamir@gmail.com', password='secret')

    def test_details(self):
        request = self.factory.get('/booking_list')
        request.user = self.user
        response = BookingListView.as_view()(request)
        self.assertEqual(response.status_code, 200)


# Test if room_detail_view loads for any user
class RoomDetailViewTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='tamir', email='tamir@gmail.com', password='secret')

    def test_details(self):
        request = self.factory.get('/room/single')
        request.user = self.user
        response = RoomDetailView.as_view()(request)
        self.assertEqual(response.status_code, 200)


# Test the booking form is working
class BookingTest(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='tamir', email='tamir@gmail.com', password='secret')

    def test_details(self):
        request = self.factory.post('/room/single')
        request.user = self.user
        response = RoomDetailView.as_view()(request)
        self.assertEqual(response.status_code, 200)
