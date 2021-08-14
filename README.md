# NineMenMorrisGame

## Game rules
The Morris Game, Variant-B , is a variant of Nine Men’s Morris game. It is a board game between two
players: White and Black. Each player has 9 pieces, and the game board is as shown above. Pieces can
be placed on intersections of lines. (There are a total of 21 locations for pieces.) The goal is to capture
opponents pieces by getting three pieces on a single line (a mill). The winner is the first player to reduce
the opponent to only 2 pieces, or block the opponent from any further moves. The game has three distinct
phases: opening, midgame, and endgame.

Opening: Players take turns placing their 9 pieces - one at a time - on any vacant board intersection
spot.

Opening game can be played with following files:
MiniMaxOpening.py
MiniMaxOpeningBlack.py (for second player)
MiniMaxOpeningImproved.py
ABOpening.py

Midgame: Players take turns moving one piece along a board line to any adjacent vacant spot.

Midgame can be played with following files:
MiniMaxGame.py
MiniMaxGameBlack.py (For second player)
MiniMaxGameImproved.py
ABGame.py

Endgame: A player down to only three pieces may move a piece to any open spot, not just an adjacent
one (hopping).

Mills: At any stage if a player gets three of their pieces on the same straight board line (a mill), then one
of the opponent’s isolated pieces is removed from the board. An isolated piece is a piece that is not part of
a mill.

# Running Programs:
To run any python file, you need to pass file names for Input and Output and the depth of the tree

e.g.
python MiniMaxOpening.py board1.txt board2.txt 3

where Input will be given in board1.txt and Output will be overwritten in board2.txt and 3 is the depth of the tree.

