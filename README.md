# Sink the ship project

The objective of this project is to develop the well-known game sink the ship, versus the PC. This project was fully made on ``python``using ``numpy``library.

## Board and boats creation

The first part of the project would be creating the "playing boards", this was simple to make as they are 10 x 10 matrix, note that we need 3 boards:

* Where the users ships are shown (``user1``)
* Where the PC ships are located (``pc1``)
* Where the user is going to shoot, linked with ``pc1``board but fully blank at the start (``user2``)

WheN creating and locating the ships, it gets more difficult as they have different lenghts, located fully inside the matrix and cannot be touching other ships. For this reason I created different functions that will endorse all this requirements.

Once we have our boats located, the game starts

## Game command

The game works as follow:

1. The user picks a row and a column independently in ``user2``
2. If the coordenate in ``pc1`` matches a boat, it will be hit, marking an "X" in ``user2`` and the user has another try, if at the location there is no ship, an "-" will be shown, denominating that a ship has not been hit, and it is the turn of the PC.
3. To make it more simple, the PC will shoot a random location in the matrix, with the same proccedure of the user.


## ENJOY
