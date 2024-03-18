# Riddles in the Dark

## Introduction

Welcome to Riddles in the Dark.  Inspired by Bilbo and Gollum from the famous scene in The Hobbit where Bilbo must win a riddle game to ensure his survival and the promise of a route to escape the cave he's lost in.  Riddles in the Dark (*known henceforth as 'RITD') is a simple game which asks the players riddles and offers hints a word count in an attempt to aid players with their answers.  The game can be played by one or two players and encompassess a "lowest score wins" system. 

## Gameplay Overview

RITD combines classic riddle solving with innovative gameplay mechanics.  Players must answer x5 questions on their route to victory.  Furthermore, players must attempt to score the least amount of points possible in order to win.  The game offers the player the opportunity to take hints when they are unsure of the riddles solution.  These hints have a point penalty associated with them and therefore raise ones total score.  PLayers are also given a number of underscores ('_').  These are to advise the player how many letters the answer includes.  If a player get the riddle wrong at any point, regardless of hints taken, or if they make a mistake in the spelling of their answer (capitals not relevant) they will incur a points penalty.  Finally, if a player wants to skip a question altogether the player recieves a hefty 10 point fine to their total. 

The game, in addition to the 1 player game, the game offers the opportunity for a 2 player feature.  The 2 player game follows the same principles in terms of its rulings but alternates between the players, therefore the game will ask a total of 10 questions, 5 for each player. The 2 player game mode also has methodology for settling when the game ends in a tie.  This is in the form of a "sudden death" mode, wherethe first to get an incorrect answer, loses. 

## Technologies Used

RITD used the following technologies: 
    - Python (Most recent version 3.12)
    - Heroku
    - txt. file type
    - GitHub
    - GitPod (IDE)

## Getting started


## How to play

- Inititate Game via Heroku, follow instructions above.
- Input your name
- Select how many players are taking part, 1 or 2.
- Game loads following short countdown
- Once riddle has been asked, a selection of underscores are presented, use these as a guide for the number of letters within the expected answer, for example: _ _ _ _ could be "coin"
- Input answer
- Game feedback as to answers correctness
- if answer unknown to player, type hint for a hint or skip to skip
- Continue until 5 questions asked. 
- Within 2 player game mode, sudden death will settle ties.  No hints are available for this gamemode so the difficulty rises exponentially. 

## Import modules

- Time
- Textwrap
- Random

## Features list

- Single or two player gamemodes
- Large array of Riddles & subsequent hints
- Program ensures riddles asked at random using random import
- txt file with simple structure ensures riddle selection can be easily added to
- Personalised input.  The game addresses player by chosen name
- Cumulative, innovative scoring system
- Character limit of 80 characters owing to deployment restrictions
- User prompt based progression
- Offers a letter count hint to remove ambiguity for word length, thus somewhat alleviating issues with user inputed, similar words that are both correct
- A hint based system where each hint has a consequence
- Countdown timer, raising anticipation and immersion
- Alternating player turns
- Extensive Error prompting
- Sudden death mode in 2 player gamemode

## Preliminary considerations and planning 

- Flow diagram: 


## Deployment

## Further Development Opportunities

- Within 2 player ,the sudden death is unblanced.  I need to build a timer into the main game so that the player who took the longest to answer their questions owuld go first, thus recieving a lesser chance to get the 1st answer correct and subseequnetly losing the game. 
- Design and build a GUI
- Allow for online multiplayer
- All time high scores leaderboard
- Add more Riddles and hints

## Testing 

## Validator Approval

## Website Sources 

## Unfixed Bugs

## Feedback

## Credits

