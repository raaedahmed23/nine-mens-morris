# nine-mens-morris
The code is an attempt at an AI bot that plays the game of nine men morris implementing using min-max and alpha-beta pruning methods. It is not perfect but hey, it works! 

9 Men Morris is a simple board game. In short - each player starts with 9 pieces (men) and the end goal of the game is to win by either leaving the opponenet no legal move or bring them down to 2 pieces. Detailed rules of the game can be found [here](https://www.mastersofgames.com/rules/morris-rules.htm)

The game can be played with multiple board layouts. The board for this game looks like this- 

<img width="352" alt="Screenshot 2023-09-22 at 11 51 47 PM" src="https://github.com/raaedahmed23/nine-mens-morris/assets/63556268/8a82d2d0-f1e1-43fb-95a7-5f932d14f3b9"> 



The game starts with White to play first. If there is 'black' in the filename, then it is the same code but Black plays first. 

Environment: Python 3.10+

MinMaxOpening - minmax algoritm implementation for the opening phase of the game \
MinMaxGame - minmax algorithm for the mid and ending phase of the game 

ABOpening - alpha beta pruning algorithm implementation for the opening phase of the game \
ABGame - alpha beta pruning implementation for the mid and ending phase of the game 
