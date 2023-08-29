# tic_tac_toe
## Implemented Adversarial Search by implementing minimax.
### Minimax : A type of algorithm in adversarial search, Minimax represents winning conditions as (-1) for one side and (+1) for the other side. Further actions will be driven by these conditions, with the minimizing side trying to get the lowest score, and the maximizer trying to get the highest score.
## Representing a Tic-Tac-Toe AI:
### S₀: Initial state (in our case, an empty 3X3 board)
### Players(s): a function that, given a state s, returns which player’s turn it is (X or O).
### Actions(s): a function that, given a state s, return all the legal moves in this state (what spots are free on the board).
### Result(s, a): a function that, given a state s and action a, returns a new state. This is the board that resulted from performing the action a on state s (making a move in the game).
### Terminal(s): a function that, given a state s, checks whether this is the last step in the game, i.e. if someone won or there is a tie. Returns True if the game has ended, False otherwise.
### Utility(s): a function that, given a terminal state s, returns the utility value of the state: -1, 0, or 1.
## I also implemented Alpha-Beta Pruning: A way to optimize Minimax, Alpha-Beta Pruning skips some of the recursive computations that are decidedly unfavorable. After establishing the value of one action, if there is initial evidence that the following action can bring the opponent to get to a better score than the already established action, there is no need to further investigate this action because it will decidedly be less favorable than the previously established one.
<img width="452" alt="comuter" src="https://github.com/samahdraz/tic_tac_toe/assets/100757002/58dfd151-708e-4d3b-b0c0-ad98f7aacc87">
