import time
import sleep
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

    def displays_intro_message(self):
        """
        Displays introductory message of the game, explains rules & how to play
        """

    def display_letter_count_hint(self)
        """
        Dispalys a hint for the current riddle, shows the number of letters in the answer as underscores
        """

    def offer_hint(self)
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

    def play_game()
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



    