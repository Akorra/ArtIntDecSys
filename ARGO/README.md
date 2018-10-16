<div align="center">
  <a><img src="https://fenix.tecnico.ulisboa.pt/api/bennu-portal/configuration/logo"></a><br><br>
</div>

# We're Making an Effin Game Engine 

## Directories and Files
- `source/game.py`: Implementations of the Game class.
- `notebooks`: Directory containing Jupyter (IPython) notebooks used for testing and prototyping.
- `wut2do.pdf`: PDF containing the project description.

## Objective

The Goal of this project is to develop an [Atari Go](https://senseis.xmp.net/?BasicRulesOfGo) game engine to interface an existing [alpha-beta search with cutoff algorithm implementation](https://github.com/aimacode/aima-python)

<div align="center">
  <a><img src="https://senseis.xmp.net/diagrams/28/7c2a15d2373af82f4ffe173d073a9302.png"></a><br><br>
</div>

## Game Class Methods

- The engine should be implemented using only Python version 3 and Standard Library modules.
- The game engine is to be implemented as a class named `Game` with the following methods:


| Method Name   | Parameters            | Returns                                                                        |
|:--------------|:---------------------:|:-------------------------------------------------------------------------------|
| to_move       | s - state             | player p to move next given the state s                                        |
| terminal_test | s - state             | bool if s state is terminal                                                    |
| utility       | s - state, p - player | payoff of terminal state for player p (1 if p wins, -1 if loss, 0 if draw)     |
| actions       | s - state             | list of valid moves at state s                                                 |
| result        | s - state, a - action | state resulting of taking action a from state s                                |
| load_board    | s - file stream       | loads a board from an opened file stream s and returns the corresponding state |

## Game Board
Game board will be represented in a text file containing the following lines:
- `first line` has two space separated values `n p`
  - `n` -> board size;
  - `p` -> next player to move;
- The following `n` lines contain the board rows as a string of numbers where:
  - `0` represents `unocupied`;
  - `1` represents `ocupied by player 1 [black]`;
  - `2` represents `ocupied by player 2 [white]`;
  
- Example:
  - `4 1`
  - `0010`
  - `0122`
  - `0210`
  - `0000`
## States and Actions
### States
#### `TBA`
### Actions
Action representation is the following tuple:
<div align="center">
  <a><img src="https://github.com/Akorra/ArtIntDecSys/blob/master/ARGO/bin/actions.JPG?raw=true"></a>
</div>

  - `p` represents player
  - `i` represents the board row
  - `j` represents the board column

## Python 3.4 and up

This code requires Python 3.4 or later, and does not run in Python 2. You can [install Python](https://www.python.org/downloads) or use a browser-based Python interpreter such as [repl.it](https://repl.it/languages/python3).
You can run the code in an IDE, or from the command line with `python -i filename.py` where the `-i` option puts you in an interactive loop where you can run Python functions.

## Installation And Run Guide

### `TBA`

## Development Team
- Filipe Marques [[Akorra](https://github.com/Akorra)]
- Rafael Pereira [[mindblastr](https://github.com/mindblastr)]
- Beatriz Ferreira [[diverbea](https://github.com/diverbea)]
