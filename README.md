# Riddles in the Dark

## Introduction

Welcome to Riddles in the Dark.  Inspired by Bilbo and Gollum from the famous scene in The Hobbit where Bilbo must win a riddle game to ensure his survival and the promise of a route to escape the cave he's lost in.  Riddles in the Dark (*known henceforth as 'RITD') is a simple game which asks the players riddles and offers hints a word count in an attempt to aid players with their answers.  The game can be played by one or two players and encompassess a "lowest score wins" system. 

## Gameplay Overview

RITD combines classic riddle solving with innovative gameplay mechanics.  Players must answer x5 questions on their route to victory.  Furthermore, players must attempt to score the least amount of points possible in order to win.  The game offers the player the opportunity to take hints when they are unsure of the riddles solution.  These hints have a point penalty associated with them and therefore raise ones total score.  Players are also given a number of underscores ('_').  These are to advise the player how many letters the answer includes.  If a player get the riddle wrong at any point, regardless of hints taken, or if they make a mistake in the spelling of their answer (capitals not relevant) they will incur a points penalty.  Finally, if a player wants to skip a question altogether the player recieves a hefty 10 point fine to their total. 

The game, in addition to the 1 player game, the game offers the opportunity for a 2 player feature.  The 2 player game follows the same principles in terms of its rulings but alternates between the players, therefore the game will ask a total of 10 questions, 5 for each player. The 2 player game mode also has methodology for settling when the game ends in a tie.  This is in the form of a "sudden death" mode, wherethe first to get an incorrect answer, loses. 

## Technologies Used

RITD used the following technologies: 
- Python (Most recent version 3.12)
- Heroku
- txt. file type
- GitHub
- GitPod (IDE)
- PEP8 Validator (CI Python Linter)

## How to play
1. Game Link: https://riddlesinthedark-e09df88ee1fe.herokuapp.com/
2. Inititate Game via Heroku, follow instructions above.
3. Input your name
4. Select how many players are taking part, 1 or 2.
5. Game loads following short countdown
6. Once riddle has been asked, a selection of underscores are presented, use these as a guide for the number of letters within the expected answer, for example: _ _ _ _ could be "coin"
7. Input answer
8. Game feedback as to answers correctness
9. if answer unknown to player, type hint for a hint or skip to skip
10. Continue until 5 questions asked. 
11. Within 2 player game mode, sudden death will settle ties.  No hints are available for this gamemode so the difficulty rises exponentially. 

## Import modules

- Time.  The time module is required within the countdown function.  It allows for the implementation of the anticipoation created by the slight delay in the games start and the 3, 2, 1... countdown
- Textwrap.  Textwrap is necessary to ensure the character width limit.  It allows for the function text_wrap.
- Random.  Random allows the shuffling of querstions to prolong engagement within the game.  User would not use the game if the questions were the same everytime the game ios played.

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

## Preliminary planning 

- Flow diagram: 
 <img src="https://github.com/SamYatesSmith/RiddlesInTheDark/blob/main/assets/images/riddlegameprocedure.png">

## Deployment

- Program deployed on Heroku: https://www.heroku.com/
- 

## Further Development Opportunities

- Within 2 player ,the sudden death is unblanced.  I need to build a timer into the main game so that the player who took the longest to answer their questions owuld go first, thus recieving a lesser chance to get the 1st answer correct and subseequnetly losing the game. 
- Design and build a GUI.
- Allow for online multiplayer.
- All time high scores leaderboard.
- Add more Riddles and hints.


# Testing

### Overview
RITD was subjected to a comprehensive suite of tests.  This is to ensure all elements of the project perform as expected to supply a smooth, bug free experience for the user.  The below section outlines the tests perfromed, on which functions and the outcome of those tests.  Furthermore, I will list issues I experienced and how they were resolved.  I wanted to ensure that the tests were perfromed in a rigourous manner so i wrote classes and functions to test the majority of modules.  Priamrily I had prior knowledge as to how to test each function and so wanted to further my knowledge by writing these individual functions to ensure the principles involved were understood.  I fee lconfident in the testing evaluations carried out and therefore, am happy with the results.  

### All Imports used
- import: unittest 
- from unittest.mock import patch
- from io import StringIO

### Functions tested

### text_wrap
text_wrap is a simple function to prevent the character length of the programs text exceeding 79 characters.  This is simply imposed owing to the requirement of the deployment environment provided by Code Institute. The expected outcome of this test was to ensure that the function correctly wraps the text to the specified length. 

<img src="https://github.com/SamYatesSmith/RiddlesInTheDark/blob/main/assets/images/testing1.text_wrap.png">

### Initialisations and loading questions

<img src="https://github.com/SamYatesSmith/RiddlesInTheDark/blob/main/assets/images/testing2.Initialisations.loading_questions.png">

The initialisation class test checks the following: 
1. Player scores: When the game starts, both players should have 0 points, the test therefore needs to ensure that this is the case. 
2. Current player: checks if the game is set to start with the first player, so game.curent_player shouold be [0].
3. Player mode: verifies that game starts in single player mode by default, indicated in the test by game_player_mode being 1. 
4. Player name: Checks if the default name for the players are set to "Player 1, Player 2".
5. Questions, Answers, Hints: Verifies that the lsits for questions, answers and hints are empty([]) when the game is first started because no questions have yet been loaded. 

Loading quesitons
This test checks if the game correctly loads questions and their accompanying elements from the local file, riddleshintsanswers.txt.  However, isntead of reading from a file, which would slow the test down, it uses a test feature called 'mocking'.  Heres what hapens within this test: 
1. Mocking the file: The @patch part before the method emulates the input of a user by mimmicking potential response.
2. Loading questions: the test then creates a new game object but this time, it loads from the 'mimmicked' file (using 'dummy_path.txt') as the file path, but the path isn't relevant because of the mocking. 
3. Checking results:  After pretending to load the file, it checks if the game now has a quesiton loaded ('Quesiton1'), one answer ('Answer1') and one hint (['Hint1']).  Essentially, test is making sure that the game is correctly reading the file.

Result: OK

### Choosing game mode
As this fucntion relies on user input, I needed to create another mock identity to simulate input o ngame mode preference and name.  unittest.mock.patch can be used to replace the input function with a mock, as per the previous test.  The goal of this test is to ensure all works ok, using a simulated user and aentering their name.

<img src="https://github.com/SamYatesSmith/RiddlesInTheDark/blob/main/assets/images/testing3.%20testgamemodes.png">
<img src="https://github.com/SamYatesSmith/RiddlesInTheDark/blob/main/assets/images/testing3.ok.png">

- Explaining the above tests;
- @patch Decorator modifies input function during this test so when input is caleld it returns the next value from the 'side_effect' list. Simulates user typing '1' or '2' to choose the game mode, followed by the player names.
- 'side_effect': This is used with @patch to specify a list of values that 'input' will return each time its called within the test.
- Assertions: After calling 'choose_game_mode, we check, or assert, the the game state, like player_mode and name matches what I'd expect given the mocked inputs.  

*Key Points*:  
1. Behaviour verification:  These tests ensure that the functions behave as expected given simulated inputs.
2. Path coverage: Tests cover the different logical pathways through the function.
3. Edge cases and validation: While these tests check fo correct input scenarios, they do not directly test how the function might handle invalid inputs.  This is further detailed later in the testing. 
4.  Therse tests rely on remaining code relating to player_name and player_mode being properly and correctly used within the rest of the program.   

### User_input
*Key Points*: 
1. Validation of input: Testing that the function returns the correct input when it is valid. 
2. Invalid followed by valid: Simulating an invalid input followed by a valid input and ensuring that the function eventually returns the corerct/valid input.
3. Case sensitivity: Testing how the 'lower' parameter handles input.

<img src="https://github.com/SamYatesSmith/RiddlesInTheDark/blob/main/assets/images/testing4.userinput.png">

### Display_letter_count_hint
This function captures the number of letters in an answer and converts it to underscores.  To test it, I needed to capture the output to 'stdout' and compare it to my expectations. I used the import unittest.mock for this to be achieved.   

<img src="https://github.com/SamYatesSmith/RiddlesInTheDark/blob/main/assets/images/testing5.lettercounthint.png">

*Key Points*: 
1. Mocking 'sys.stdout': This approach used @patch to mock 'sys.stdout', effectively redirecting output sent to the terminal to a 'StringIO' onbject.  This object acts like a file that can capture written strings, allowing me to inspectwhat would have been printed to the terminal.
2. Output checking: After calling 'display_user_letter_count_hint', the test retrives the captured output using the 'mocked_stdout.getvalue()' and compares it to the expected string, which represents the hint message with the correct number of underscores for the provided answer.
3. Exopected output format: Make sure to include the newline character('\n') at the end of the expected output string owing to the nature of the print() function.  Expected output needs to match this behavior.

### Offer Hint
offer_hint increments the users score by one.  I ts primary function however is to provide the user with one of the pre-listed hinbts which are associated with the various questions.  The function needed to capture the incrementation of the players current score and to provide the hint requested by the user. I again used the unittest.mock.patch to redirect sys.stdout ot a StringIO object for capturing those print statements.  

<img src="https://github.com/SamYatesSmith/RiddlesInTheDark/blob/main/assets/images/testing6.offerhint.png">

*Key Points*: 
1. Score verification: The test first looks at the initial score of the player.  After calling 'offer_hint', it checks that the players score has incremented by 1. 
2. Output verification: Using 'patch' to mock 'sys.stdout', the test captures the output from the 'offer_hint' method. It then constructs the expected output, which includes both the hint message and the follow-up message indicating the players new score.  This then also user the wrap_text fucntion to ensure the output matches how offer_hint formats its messages.  Fianlly, there is comparison between captured and expected outputs.

*Issues with the test*

I could not understand why the test at first was not working and remembered that the print function creates a new line character that I hadn't accounted for.  A simple fix of inserting '"+ \n"' at the end of the expected_output 'score' statement resolved this issue.

### Handle Question
I had to test the handle question in 4 simple/seperate ways: 
1. Correct Answer: Verifies that when a correct answer is given, the loop exits (question is answered correctly)
2. Incorrect answer: Checks behavious when an incorrect answer is given, specifically the increment in score.
3. Hint request: Tested the functionality when a hint is requested, including the socre increment and hint limit.
4. Skip: Verifies the skip functionality and corresponding scoring penalty. 

An example of the testing performed on the correct answer element of this function: 

<img src="https://github.com/SamYatesSmith/RiddlesInTheDark/blob/main/assets/images/testing7.handlequestion.png">

### Play_Game

These are my considerations when testing 'play_game':
1. Game mode selection: Ensured the game correctly proceeded when the user confirms they are ready and exits early if the user is not ready to play. 
2. User Readiness: Verifies that the game proceeds as expected when the user confirms they are ready and if not, breaks. 
3. Question Shuffling: Ensured questions are random in nature from their host txt. file.
4. Displaying Intro Message: Ensures that the intro message initiates properly at the start of the game.
5. Successfully handles input for answers/score increment, iuncorrect answers, hints and skipping: Ensures oprogram successfully handles these parameters.
6. Turn management in 2 player mode: 2 player game must alterante between 1 and 2 players.
7. End of game conditions: Needed to be sure the game concludes properly based on what had happened during its process. Includes invoking sudden_death and conclude_game.
8. Sudden_death handling: Needed to ensure that the trigger for sudden death within 2 player mode was correct. 
9. Game conclusion messages: Ensured that the correct message was printed based on the circumstances. 
10. Integration:  Needed to be sure all compoonents both worked together and integrated, for example, transitioning from game mode selection to handling quesitons.

## Difficulties experienced

### Integrating .txt file
- I wanted to simple, easy to adjust system for integrating the library of riddles.  This was tricky as i was unsure how to persuade Python to read the riddles, answers and x5 hints.  I implemented the code within the initialisations, the load_questions and shuffle_quesitons functions.  Initially, it took me a long time to ensure that the code correctly read the .txt file and therefore needed to list pointers for the code t ofind as per the load_quesitons funciton: 

<img src="https://github.com/SamYatesSmith/RiddlesInTheDark/blob/main/assets/images/testing8.loadingquestions.png">

### Scoring
- The scoring incrementation and recording was problematic.  There are a number of way to concede points and tying these together took me some time and research. Initially i was listing the questions, answers and hints as seperate numbered sections, as opposed t ogroups including hteir own relevancies, Q, A and H's.  I adjusted load_questions to corectly read and associate each question with its corresponding answer/hint as groups.  The solution was to emply a parsing strategy that grouped the elements of the question together and looked out for expected elements as pointers, such as Q: or A: etc.  The hints needed to be parsed line by line to ensure all 5 were available. 

### Hints

Initially I struggled to implement the hint system.  After various efforts, I implemented the system of the user inputting 'hint' to request a hint.  This therefore gave me the opportunity to penalise the user for the hint, thus making the game more engaging and offering another opportunity for incrementation. I also had to ensure the program penalised the user if they took over the maximum number of 5 hints, and they were subsequently charged 10 points.  Keeping track of the various element sof incrementation throughout the program proved difficult and took me a long time to write the correct code in the correct place to ensure my bugs were ironed out.

## Validator Approval

Code Institute Python Linter PEP8 code review: 

<img src="https://github.com/SamYatesSmith/RiddlesInTheDark/blob/main/assets/images/cilinterpep8test.png">

## Website Sources 

## Unfixed Bugs

## Feedback

## Credits

