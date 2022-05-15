# HMS- Hotel Management System
------------------

The hotel management system is a system designed for users to be able to book rooms, see a list of booked rooms, and cancel a booking.
The Admin of the system can see a list of booked rooms and is able to cancel bookings on the Admin panel. He can also add rooms, get a list of users' emails and see all authenticated users.

[Here is a link to the live version of the App](https://django-hotel-booking.herokuapp.com/)

![Responsive Mockup](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/am-I-responsive-screenshot.jpg?raw=true)

<br>

### Wireframe 

![Balsamiq](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/Balsamiq%20Wireframes1.png?raw=true)

## User Experience (UX)
----------------------

### Project Goals
-----------------
* The website should have an intuitive and minimalist design, appealing to the customers.
* To display the rooms available and the information about them in order to be an exact fit for their needs.
* Provide the users with post-reservation viewing and editing the reservations.
* Make sure the users data is safe by offering secure login.

### User Stories
----------------
* As a site user I can see a list of room categories so that I can choose the best room for my needs.
* As a site user I can see a calendar so that I can select the dates of my stay.
* As a site user I can see the type of rooms available so that I can choose from the available rooms.
* As a site user I can get the information about the rooms bed so that I can know if the bed size is enough for my needs.
* As a site user I can book the room so that I know that the room is booked by seeing the room in my booked room list.
* As a site user I can cancel my reservation in case I will not be using it.
* As a site user I can create an account so that I can see and manage my reservations.
* As a site user I can edit my reservation in case I will need to.

### Color Scheme
----------------
The colors used in the site are three different ones:
* The background is a darker grey color: rgb(46, 47, 48)
* The Text is a light grey color: rgb(236, 235, 228)
* The text changes color to blue when hovered with mouse: rgb(6, 137, 245)

Those colors were chosen to give the user good contrast between background and text and to be inline with the hotels basic color scheme in real life.

### Typography
--------------
The main font used in the site Sans-Serif. Lato is used for the Brand name (Hotel Regina) with Sans-Serif as fallback.

<br>


## How the user make a booking
--------------

The booking flow is very simple and intuitive
1. The user must create an account or be logged in if he has an account.
2. The user is presented with a list of room types
3. The user selects a room and is transferred to the room booking page.
4. The user selects check-in and check-out dates and hours.
5. If the room is available, he will be transferred to a "Thank you" page that has a successful booking message. If the room is not available, he will get a message that the room is not available and he should select a different category.

- In cases that the user is not logged in, he will get a message that he needs to be logged in before he can make a booking, in the room details page. 

<br>

## Existing Features
--------------------
<br>

### General
-----------

* Responsive design across all device sizes.

* Similar color scheme and design throughout all pages to effectively structure, categorize and present the information to the customers.

* **Header**
-----------
![Header image](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/HMS-header.jpg?raw=ture)
    
    - The header contains the business name and a fully responsive navigation bar positioned across the top of the screen.

    - The business name functions as a link to the landing page.

    - The navigation bar is identical on all pages and contains links to all pages to facilitate navigation across the site. It also has a hover effect that changes color to provide feedback to the user for a better user experience.

    - Has a navigation bar with links to "Register" or "Login", if a user is not logged in. 

   <br>

   ![nav bar when NOT logged in](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/HMS-nav-not-logedin.jpg?raw=ture)


    - If the user is logged in, the navigation bar changes to "Bookings" or "Logout".

   <br>

   ![nav bar when logged in](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/HMS-nav-logedin.jpg?raw=ture)
* **Footer**
------------
![Footer image](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/HMS-footer.jpg?raw=true)

    - The footer includes links to the business social media channels (not functional yet).

<br>

### Landing Page
----------------
   - Contain the h1 title of the hotel name.
   - Contains the room categories with a brief description of the room. Once a user hovers over the room card, the text color changes indicating the user can click for redirection.

![room categories](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/select-a-room.jpg?raw=true)

<br>

### Room details and booking
----------------------------
This page will have a different appearance, depending on if the user is logged in or not.

#### If he is logged in, he will have the following options:
   - Make a booking
   * Choose check-in date and time
   * Choose check-out date and time
   * Click the "Book the Room" button

 ![room details and date selection](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/room-details-dates.jpg?raw=true)

- If the room is available, he will be transferred to a confirmation page

<br>

![confirmation page](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/room-booking-confirmation.jpg?raw=true)

- If the room is booked, he will get an error message:
  "All of this category of rooms are booked!! Try another one".

#### In case the user is not registered or logged in:
- Unregistered users as well as users who are not logged in will not be able to see the booking form.
Instead, they will have links to register or to log in, in order to make a booking

<br>

![room details in case not logged or registered](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/HMS-redirect-to-login.jpg?raw=true)

### Bookings page
-----------------
- The navigation bar has a link called "Bookings" for users who are signed in and already made bookings.
- On this page, they can get all the information about room categories they have booked, as well as check-in and check-out dates.
- This page also contains links for canceling a booking or editing a booking.
- If the user is hovering over the bookings the options will appear.

<br>

![room details in case not logged or registered](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/HMS-bookings-cancel-update.jpg?raw=true)

### Cancel a booking page
--------------------

- The user will easly be able to cancel a bookig using a designated button.
- Once the booking is canceled, the user gets redirected to the bookings list page once again.

![room canceltion](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/room-cancaltion-page.jpg?raw=true)

<br>

### Update an existing booking
------------------------------

- The user will easily update his reservation by selecting check-in and check-out dates and hitting the "Update Booking" button.
- Once the booking is updated, the user gets redirected to the bookings list page once again.

![room canceltion](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/HMS-booking-update-page.jpg?raw=true)


### Admin Features
------------------
- A list of booked rooms is presented in the Admin panel under "Bookings". An Admin can delete the booking.

<br>

![admin panel booking list](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/room-cancaltion-page.jpg?raw=true)

<br>

- A list of email addresses is presented in the Admin panel under "Email Addresses". The Admin can remove an email or mark it as verified.

<br>

![admin panel email addresses list](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/admin-email-addresses.jpg?raw=true)

<br>

- A list of users is presented in the Admin panel under "Users". The Admin can remove a user.

<br>

![admin panel users list](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/admin-users-list.jpg?raw=true)

<br>

- A list of rooms and their prospective numbers is presented in the Admin panel under "Rooms". The Admin can remove or add a room.

<br>

![admin panel room list](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/admin-room-list.jpg?raw=true)

### Future Features
-------------------
- Add a payment system to the booking process.
- Comment box for special needs

## Technologies Used
---------------------

### Languages Used

* [HTML5](https://en.wikipedia.org/wiki/HTML5)
* [CSS3](https://en.wikipedia.org/wiki/CSS)

### Frameworks, Libraries and Programs Used

* [Font Awesome](https://fontawesome.com/)
     - Font Awesome was used throughout all pages to add icons in order to create a better visual experience for UX purposes.

* [GitPod](https://gitpod.io/)
     - GitPod was used for writing code, committing, and then pushing to GitHub.

* [GitHub](https://github.com/)
     - GitHub was used to store the project after pushing.

* [Balsamiq](https://balsamiq.com/)
     - Balsamiq was used to create the wireframes during the design phase of the project.

* [Am I Responsive?](http://ami.responsivedesign.is/#)
    - Am I Responsive was used in order to see responsive design throughout the process and to generate mockup imagery to be used.

* [Chrome DevTools](https://developer.chrome.com/docs/devtools/)
    - Chrome DevTools was used during development process for code review and to test responsiveness.

* [W3C Markup Validator](https://validator.w3.org/)
    - W3C Markup Validator was used to validate the HTML code.

* [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)
    - W3C CSS Validator was used to validate the CSS code.

### Authentication Features
---------------------------
- As part of the project security measures, if a customer is not logged in, the booking form will not be visible in the room_detail_view.html and instead, he will be asked to sign up or log in with links to the respective pages.
<br>

![room deatils page when not logged in](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/room-details-not-logedin%20.jpg?raw=true)

## Data Model
--------------

I have used five classes for this project:
- RoomListView class is in charge of:
   * Creating a list of rooms categories using their URLs.
   * Presenting a list of rooms to choose from and the information about them.

- BookingListView class is in charge of presenting lists per site roles and permisssions:
   * If the user is a staff member, the function will return a list of the hotel bookings.
   * If the user is a logged-in user (authenticated), the function will present a list of all his bookings.

- RoomDetailView class is in charge of the following:
   * The class will create a booking form that contains check-in, check-out and a booking button.
   * The function will check if the form is valid and, if the room is available on the selected dates:
      - If the room is free, it will transfer the user to the booking confirmation page.
      - If the room is not free, he will get a message: "All of this category of rooms are booked! Try another one".
   * The function will check if the category exists. If it doesn't, the user will get the following massage:
   "Category does not exist, please go back and choose a valid category".

   - CancelBookingView class is in charge of:
      * Handling the room cancelation.
      * Returning the user to the booking_list_view.

     - UpdateBookingView class is in charge of:
      * Handling the room updates.
      * Returning the user to the booking_list_view.

   <br>

There are three database models:

   - Room_Categories:
      * This DB contains the room's name and description.
      * Its job is to create categories and to supply the initial descriptions of them.

   - Room:
      * This DB contains the actual room information within the category and contains the room number, what category it belongs to, how many beds it has and how many guests can sleep in it.
      * Its job is to supply information across the app.

   - Booking:
      * This DB contains the relationship between the user, the room, and the dates.
      * Its job is to supply the information for the booking form.

   <br>

## Testing
-----------

### Testing User Stories
------------------------
* As a site user I can see a list of room categories so that I can choose the best room for my needs.
   - The landing page contains an intuative category breakdown with a short description of the room and how many people can sleep in it.
* As a site user I can see a calendar so that I can select the dates of my stay.
   - The booking form will pop up a calendar for an easy selecting of check-in and check-out dates.
* As a site user I can see the type of room available so that I can choose from the available rooms.
   - Once a user makes a selection and in case that the room isn't available, he will get a message that he should book from another category, as all the room is this category are booked.
* As a site user I can get the information about the room's bed so that I can know if the bed size is enough for my needs.
   - The booking details page offers information about the room type and how many guests can sleep in the room.
* As a site user I can book the room so that I know that the room is booked by seeing the room in my booked room list.
   - After finishing the booking process, the guest is redirected to a confirmation page that features all the booking information.
* As a site user I can cancel my reservation in case I will not be using it.
   - The user has an option, once logged in to go to his bookings and canacel his booking with 2 clicks.
* As a site user I can create an account so that see and manage my reservations.
   - There is an easy registion panel in the App. Once user was registered, he will be redirected to the Home page. The options to cancel or edit a room will only appear once the user is logged in.
* As a site user I can edit my reservation in case I will need to.
   - The booking update page can be accessed through the bookings page and has a similar form the booking form.

<br>

### Code validation
-------------------

* The [W3C Markup Validator](https://validator.w3.org/) and [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) services were used to validate all pages of the project in order to ensure there were no syntax errors.
- No errors were found in the HTML or the CSS files.

* Passed the code through [PEP8](http://pep8online.com/) and made sure it is error free.

* A few key features of the app were tested in the test.py file, I have tested each of my classes:
   - Test 1: Test if room_list_view page is loading.
   - Test 2: Test if booking_list_view is loading once the user is logged-in.
   - Test 3: Test if room_detail_view loads for any user.
   - Test 4: Test the booking form is working.

 **All tests passed**

### Accessibility
-----------------

* Used Lighthouse in Chrome DevTools to confirm that the colors and fonts being used throughout the website are easy to read and accessible. In addition, making sure that performance, accessibility, best practices, and SEO are on good terms (the lighthouse test was done based on sampling pages and the whole app)

* Lighthouse reports

    - **Landing Page**

    ![Lighthouse report for home page image](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/lighthouse-home.jpg?raw=true)

    - **Room details**

    ![Lighthouse report for room details page image](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/lighthouse-booking-conf.jpg?raw=true)

    - **Booking confirmation**

    ![Lighthouse report for booking confirmation page image](https://github.com/tamirgen/DjangoHotelReservation/blob/main/booking/assests/media/lighthouse-room-details.jpg?raw=true)

### Tools Testing
-----------------

* [Chrome DevTools](https://developer.chrome.com/docs/devtools/)

    - Chrome DevTools was used during the development process to test, explore and modify HTML elements and CSS styles used in the project.

* Responsiveness
    
    - [Am I Responsive?](http://ami.responsivedesign.is/#) was used to check responsiveness of the site pages across different devices.
    - Chrome DevTools was used to test responsiveness in different screen sizes during the development process.

<br>

### Manual testing:
-------------------

   - General manual tests:
      Navigation:
      - The hotel name and the "Home" button were tested from all the pages of the App and were returning the user to the landing page.
      - "Login", "Register" and "Logout" were tested and are all working and redirecting to the "Home' page.
      - The App was tested both on big screens, small screens, and medium-size screens and was fully functional.
      - The App was tested on all major browsers and was working fine (Chrome, Incognito, Explorer and Safari).
   
<br>

### Common Elements Testing:
----------------------------

  - All Pages' clickable elements were tested manually and are functioning and doing what they were designed to do.
        
      - **Header**

         - Clicking on the hotel name or "Home" will bring the customer back to the landing page.

      - **Navigation Bar**

         - Hovering on the different navigation bar's links will trigger the hover effect, highlighting the link for the customer.

         - Clicking on the navigation bar's links will bring the customer to the specified page.
        
      - **Footer**
        
         - Clicking on the social media links will open the specific website on a new tab(not working at the moment).

      - **Room list view**

         - Clicking on the category will link the user to the room detail view.

      - **Room details view**

         - When logged in,all clickable elements are functioning and clicking the "book the room" button will redirect to the booking confirmation view page.

      - **Booking confirmation view**

         - The only clickable element on the page is the "Your bookings" link to the booking list view page.

      - **Booking list view**

         - The page has 2 major links. One for canceling and the other for editing a booking from the list. 
         - They are both hidden and will pop up once hovered over a specific booking. Both redirect to the right pages.

      - **Booking update view**

         - The page has a similar form to that of the room details view page,except a different CTA, an "Update booking" button and a redirect to the booking list view page instead of a confirmation page.

      - **Booking update view**

         - The page has one button called "Cancel your booking". Clicking it will cancel the booking and redirect the user to the booking list view.


<br>

## Authentication
-----------------
<br>

The application is using the built-in "Allauth" app to authenticate users and staff members.
- For staff members, the App will present a list of email addresses of users who created accounts in the Admin panel.
The staff can then authenticate those emails or delete them from the system. In addition, it will provide a list of users and the prospective usernames in the Admin panel.

- For users, there is a simple and friendly signup process. Once a user has signed up or logged-in, he will be redirected to the room_list page. The same will happen if he logs out. 
Only signed-in users can book a room and see the booking list of their accounts.

- Allauth templates were changed to fit the style of the App and to be more appealing to the end-user.

## Bugs
--------

There were two bugs that I have found and fixed:
- When I inspected the App for a smaller screen I noticed that the navbar does not show. The issue was that it was missing the toggler button. Once fixed, the issue was resolved.
- In production, the CSS files were not loading. That was due to the fact that DEBUG was set to True. Changing it to False and pushing again fixed the issue.


<br>

## Deployment
--------------

The project was deployed using the Code Institute's mock terminal from Heroku.
The steps to deploy at the beginning of the project:
* Creating the Heroku app
* Attaching the database
* Preparing our environment and settings.py file

<br>

The steps to deploy at the end of the project:
* Setting the debug flag to False in settings.py
* Adding X_FRAME_OPTIONS = 'SAMEORIGIN' to settings.py
* Making the final deployment commiting and pushing
* In Heroku, removing from the config var the DISABLE_COLLECTSTATIC=1
* Deploying the branch

<br>

Steps to deploy in local in environment:

* Create an env.py file in the same level as your manage.py file.
* In the file import os
* Include in the file the following:
   - os.environ['CLOUDINARY_URL'] = 
   - os.environ['DATABASE_URL'] = 
   - os.environ['SECRET_KEY'] = 
Information can be found in Heroku. 
* Find the App, open settings and click on " Reveal Config Vars".
* In the terminal run "pip list".
If the list is empty, please reinstall requirements.txt file using "pip install -r requirments.txt" and after that "pip freeze > requirements.txt".

<br>

## Credit
----------
- Code Institute for the deployment terminal.
- Parts of the project are base on vidoes for the YouTube channel DarshanDev.
