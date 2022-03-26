# HMS- Hotel Management System
------------------

The hotel management system is a system designed for users to be able to book rooms, see a list of booked rooms, and cancel a booking.
The Admin of the system can see a list of booked rooms and is able to cancel bookings on the Admin panel. He can also add rooms, get a list of users' emails and see all authenticated users.

[Here is a link to the live version of the App](https://django-hotel-booking.herokuapp.com/)

![Responsive Mockup](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/am-I-responsive-screenshot.jpg?raw=true)

<br>

## How the user make a booking
--------------

The booking flow is very simple and intuitive
1. The user must create an account or be logged in if he has an account.
2. The user is presented with a list of room types
3. The user selects a room and is transferred to the room booking page.
4. The user selects check-in and check-out dates and hours.
5. If the room is available, he will be transferred to a "Thank you" page that has a successful booking massage. If the room is not available, he will get a message that the room is not available and he should select a different category.

- In cases that the user is not logged in, he will get a message that he needs to be logged in before he can make a booking in the room details page. 

<br>

## Existing Features
--------------------
<br>

### User Features:
- Create an account\log in to existing account

<br>

![account creation and log-in panel](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/log-in.jpg?raw=true)

- Select a room from the rooms category

<br>

![room categories](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/select-a-room.jpg?raw=true)

- Make a booking
  * Choose check-in date and time
  * Choose check-out date and time
  * Click the "Book the Room" button

 <br>

 ![room details and date selection](https://github.com/tamirgen/Tic-Tac-Toe/blob/main/assests/images/ttt-illegal-moves.jpg?raw=true)

- If the the room is available, he will be transferred to a confirmation page

<br>

![confirmation page](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/room-booking-confirmation.jpg?raw=true)

- If the room is booked, he will get an error message

<br>

![room error massage](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/sing-in-error-for-room-booking.jpg?raw=true)

<br>

- Cancel a booking

![room canceltion](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/room-cancaltion-page.jpg?raw=true)

<br>

### Admin Features
------------------
- A list of booked rooms is presented in the Admin panel under "Bookings". An Admin can delete the booking.

<br>

![admin panel booking list](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/room-cancaltion-page.jpg?raw=true)

<br>

- A list of email addresses is presented in the Admin panel under "Email Addresses". The Admin can remove an email or mark it as verified.

<br>

![admin panel email addresses list](https://github.com/tamirgen/Tic-Tac-Toe/blob/main/assests/images/ttt-announce-the-winner.jpg?raw=true)

<br>

- A list of users is presented in the Admin panel under "Users". The Admin can remove a user.

<br>

![admin panel users list](https://github.com/tamirgen/Tic-Tac-Toe/blob/main/assests/images/ttt-announce-the-winner.jpg?raw=true)

<br>

- A list of rooms and their prospective numbers is presented in the Admin panel under "Rooms". The Admin can remove or add a room.

<br>

![admin panel room list](https://github.com/tamirgen/Tic-Tac-Toe/blob/main/assests/images/ttt-announce-the-winner.jpg?raw=true)

### Future Features
-------------------
- Add a payment system to the booking process.
- Comment box for special needs


## Data Model
--------------

I have used four classes for this project:
- RoomListView class is in charge of:
   * Create a list of room categories using their URLs.
   * Present a list of rooms to choose from and the information about them.

- BookingListView class is in charge of:
   * If the user is a staff member, the function will return a list of the hotel booking.
   * If the user is a logged in user (authenticated), the function will present a list of all his bookings.

- RoomDetailView class is in charge of:
   * The class will create a booking form that contain check-in, check-out and a booking button.
   * The function will check if the form is valid and if the room is available on the selected dates:
      - If the room is free, it will direct the user to the booking confirmation page.
      - If the room is not free, he will get a message: "All of this category of rooms are booked! Try  another one".
   * The function will check if the category exists. If it is not, the user will get the following massage:
   "Category does not exist, please go back and choose a valid category".
   * The function will check if the user is logged-in. in case he is not logged-in, he will get this massage:
   "You are not signed in, to make a booking please sign in".

   - CancelBookingView class is in charge of:
      * Handling the room cancellation.
      * Return the user the booking_list_view.

   <br>

## Testing
-----------

I have manually tested my project by doing the following:
- Passed the code through PEP8 and made sure it is error free.
- By using manual tests in the test.py file, I have tested each of my classes:
   - Test 1: Test if room_list_view page is loading.
   - Test 2: Test if booking_list_view is loading if the user is logged-in.
   - Test 3: Test if room_detail_view loads for any user.
   - Test 4: 
- Tested in my local terminal and the Heroku terminal.
- Tested on an Android tablet and IOS smartphone.

<br>

## Authentication
-----------------
<br>

The application is using the built-in "Allauth" app to authenticate users and staff members.
- For staff members, the app will present a list of email addresses of users that created accounts in the Admin panel.
The staff can then authenticate those emails or delete them from the system. In addition, it will provide a list of users and the prospective user names in the Admin panel.

- For users, there is a simple and friendly signup process. Once a user has signed up or logged-in, he will be redirected to the room_list page. The same will happen if he logs out. 
Only signed-in users can book a room and see the booking list of their accounts.

## Bugs
--------

There were no bugs to fix.

<br>

## Deployment
--------------

The project was deployed using the Code Institute's mock terminal from Heroku.
The steps to deploy:
  * Fork or clone this repository.
  * Create a new app on Heroku.
  * Add a key: PORT and value: 8000 to the Config Vars.
  * Set the buildback to "Python" and "NodeJS" in that order.
  * Link the Heroku app to the project repository.
  * Click on <b>Deploy<b>

<br>

## Credit
----------
- Code Institute for the deployment terminal.
- Wikipedia for the details on Tic-Tac-Toe
