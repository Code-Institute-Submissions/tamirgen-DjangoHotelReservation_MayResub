# HMS- Hotel Management System
------------------

The hotel management system is a system designed for users to be able to book rooms, see a list of booked rooms, and cancel a booking.
The Admin of the system can see a list of booked rooms and is able to cancel bookings on the Admin panel. He can also add rooms, get a list of users' emails and see all authenticated users.

[Here is a link to the live version of the game](https://tic-tac-toe-tamir.herokuapp.com/)

![Responsive Mockup](https://github.com/tamirgen/Tic-Tac-Toe/blob/main/assests/images/tic-tac-toe-AMIresponsive.jpg?raw=true)

<br>

## How the user make a booking
--------------

The booking flow is very simple and intuitive
1. The user must create an account or be logged in if he has an account.
2. The user is presented with a list of room types
3. The user selects a room and transferred to the room booking page.
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

![players names](https://github.com/tamirgen/Tic-Tac-Toe/blob/main/assests/images/ttt-ask-for-names.jpg?raw=true)

- Select a room from the rooms category

<br>

![board printed](https://github.com/tamirgen/Tic-Tac-Toe/blob/main/assests/images/ttt-show-board-and-inst.jpg?raw=true)

- Make a booking
  * Choose check-in date and time
  * Choose check-out date and time
  * Click the "Book the Room" button

 <br>

 ![validation check](https://github.com/tamirgen/Tic-Tac-Toe/blob/main/assests/images/ttt-illegal-moves.jpg?raw=true)

- If the the room is available, he will be transffered to a confirmation page

<br>

![validation check](https://github.com/tamirgen/Tic-Tac-Toe/blob/main/assests/images/ttt-illegal-moves.jpg?raw=true)

- If the room is booked, he will get an error massage

<br>

![winner announce](https://github.com/tamirgen/Tic-Tac-Toe/blob/main/assests/images/ttt-announce-the-winner.jpg?raw=true)

<br>

- Cancel a booking

![winner announce](https://github.com/tamirgen/Tic-Tac-Toe/blob/main/assests/images/ttt-announce-the-winner.jpg?raw=true)

<br>

### Admin Features
------------------
- A list of booked room is presented in the Admin panel under "Bookings". An Admin can delete the booking.

<br>

![winner announce](https://github.com/tamirgen/Tic-Tac-Toe/blob/main/assests/images/ttt-announce-the-winner.jpg?raw=true)

<br>

- A list of email address is presented in the Admin panel under "Email Addresses". The Admin can remove an email or mark it as verified.

<br>

![winner announce](https://github.com/tamirgen/Tic-Tac-Toe/blob/main/assests/images/ttt-announce-the-winner.jpg?raw=true)

<br>

- A list of users is presented in the Admin panel under "Users". The Admin can remove a user.

<br>

![winner announce](https://github.com/tamirgen/Tic-Tac-Toe/blob/main/assests/images/ttt-announce-the-winner.jpg?raw=true)

<br>

- A list of rooms and their prospective numbers is presented in the Admin panel under "Rooms". The Admin can remove or add a room.

<br>

![winner announce](https://github.com/tamirgen/Tic-Tac-Toe/blob/main/assests/images/ttt-announce-the-winner.jpg?raw=true)

### Future Features
-------------------
- Add payment system to booking process.
- Comment box for special needs


## Data Model
--------------

I have used three classes for this project:
- Board class is in charge of:
   * Creating the board.
   * Handling and checking the legal moves.
   * Checking turns between the players.

- Player class is in charge of:
   * Holding the players names and markers.
   * Getting information from a function in Board class and printing the illegal move statement.

- Game class is in charge of:
   * Swapping turns between players.
   * Holding the actual game.
   * Checking and announcing the winner or calling for a draw.

   <br>

## Testing
-----------

I have manualy tested my project by doing the following:
- Passed the code through PEP8 and made sure it is error free.
- Given invalid inputs: numbers that are not 0-8, letters instead of numbers and the same number twice.
- Tested in my local terminal and the Heroku terminal.
- Tested on an Android tablet and IOS smartphone.

<br>

## Bugs
--------

There were no bugs to fix.

<br>

## Deployment
--------------

The project was deployed using the Code Institute's mock terminal from Heroku.
The steps to deploy:
  * Fork or clone this repository.
  * Create new app on Heroku.
  * Add a key: PORT and value: 8000 to the Config Vars.
  * Set the buildback to "Python" and "NodeJS" in that order.
  * Link the Heroku app to the project repository.
  * Click on <b>Deploy<b>

<br>

## Credit
----------
- Code Institue for the deployment terminal.
- Wikipedia for the details on Tic-Tac-Toe