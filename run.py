import time
# import sleep
import textwrap

def wrap_text(text, width=80):
    """
    Wraps text to the specified width
    """
    return '\n'.join(textwrap.wrap(text, width))

class RiddleGame: 
    def __init__(self, filepath=None):
        """
        Initialises the riddle game with riddles loaded from external file
        """

    def load_questions(self, filepath):
        """
        Loads questions, answers and hints from a specified file.
        """

    def choose_game_mode(self):
        """
        Prompts the user to choose the game mode, either single player or two players. Enquire after player names.
        """

    def shuffle_questions(self):
        """
        Randomly shuffles the order of questions, answers
        """

    def get_user_input(self):
        """
        Gets user input with a specific prompt
        """

    def display_intro_message(self):
        """
        Displays introductory message of the game, explains rules & how to play
        """
        intro_message = (
            "Welcome to Riddles in the Dark!\n\n"

            "Riddles in the Dark is a short riddle based game.  In order to claim victory, the player must accrue as few points as possible. "
            "Points are incremented by answering riddles incorrectly, asking for hints, using too many hints and skipping the current question.\n" 
            "Players are allowed 5 hints per question.  These hints will accrue 1 point each.\n"
            "However, if a player users more than 5 hints, they are punished with an incorrect answers' point value.\n"
            "When a player answers incorrectly, they recieve 2 points.\n"
            "When a player skips the question, they will recieve a 10 point penalty.\n"
            "Players are provided with underscores which represent the number of letters in the answer.\n\n"
            "Good luck, and Have fun!"
        )
        print(wrap_text(intro_message))


    def display_letter_count_hint(self):
        """
        Dispalys a hint for the current riddle, shows the number of letters in the answer as underscores
        """

    def offer_hint(self):
        """
        Hint management, increments score if hint is requested
        """

    def handle_question(self, question, answer, hints):
        """
        Handles logic for askign a question. Takes users response, provides hint and skips
        """

    def handle_turn(self):
        """
        Manages a single turn for a player by presenting them woth a question
        """

    def next_player(self):
        """
        Switches th ecurrent player in 2-player game mode
        """

    def countdown(self):
        """
        Displays a countdown from 3 to 1 to signal the beginning of the game
        """

    def play_game():
        """
        Starts and manages games flow, from choosing the games mode to conclusion
        """

    def conclude_game(self):
        """
        Wraps up the game by dispalying the total scores and determining the winner
        """
    
    def sudden_death(self):
        """
        Initiates sudden death mode following a 2 player tie
        """

    def play(self):
        """
        Calls the method to play the game
        """
        self.display_intro_message()

game = RiddleGame(filepath='requirements.txt')
game.play()

    