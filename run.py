import time
import random
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
        self.questions = []
        self.answer = []
        self.hints = []
        self.player_scores = [0, 0]
        self.current_player = 0
        self.player_mode = 1
        self.player_names = ["Player 1", "Player 2"]
        if filepath: 
            self.load_questions(filepath)

    def load_questions(self, filepath):
        """
        Loads questions, answers and hints from a specified file.
        """
        try:
            with open(filepath, 'r') as file:
                lines = file.readlines()

            temp_hints = []
            for line in lines:
                line = line.strip()
                if line.startswith("Q: "):
                    self.questions.append(line[3:])
                    if temp_hints:
                        self.hints.append(temp_hints)
                        temp_hints = []
                elif line.startswith("A: "):
                    self.answer.append(line[3:])
                else:
                    temp_hints.append(line)
            if temp_hints:
                    self.hints.append(temp_hints)
        except FileNotFoundError:
            print("Error: The file path provided does not exist.  Please check the file path and give it another whirl.")

    def print_loaded_data(self):
        for i, question in enumerate(self.questions):
            print(f"Question {i+1}: {question}")
            print(f"Answer: {self.answer[i]}")
            print(f"Hints:")
            for hint in self.hints[i]:
                print(f" - {hint}")
            print()    

    def choose_game_mode(self):
        """
        Prompts the user to choose the game mode, either single player or two players. Enquire after player names.
        """
        mode_input = input("Choose your game mode: Key '1' for Single player and '2' for 2 player. 1/2: ")
        self.player_mode = int(mode_input)
        if self.player_mode == 1:
            name = input(wrap_text("Enter your name: "))
        if self.player_mode == 2:
            name1 = input(wrap_text("Enter name for Player 1: "))
            name2 = input(wrap_text("Enter name for Player 2: "))

    # def shuffle_questions(self):
    #     """
    #     Randomly shuffles the order of questions, answers
    #     """

    # def get_user_input(self):
    #     """
    #     Gets user input with a specific prompt
    #     """

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


    def display_letter_count_hint(self, answer):
        """
        Dispalys a hint for the current riddle, shows the number of letters in the answer as underscores
        """
        letter_count_hint = "_" * len(answer)
        print(wrap_text(f"Answer letter count: {letter_count_hint}"))

    def offer_hint(self):
        """
        Hint management, increments score if hint is requested
        """
        if len(self.hints[self.current_quesiton_index]) > self.hints_given:
            self.player_scores[self.current_player] += 1
            print(f"Hint: {self.hints[self.current_question_index][selfhints_given]}")
            self.hints_given += 1
        else:
            print("No more hints available.")

    def handle_question(self, question, answer, hints):
        """
        Handles logic for asking a question. Takes users response, provides hint and skips
        """

        print(f"Question for {self.player_names[self.current_player]}:", question)
        self.display_letter_count_hint(answer)
        hints_given = 0

        while True:
            response = self.get_user_input(f"{self.player_names[self.current_player]}, type your answer (OR type 'hint' for a hint, 'skip' to Skip the question, remember, if you skip, you'll incur a 10 point penalty!)", lower = False)
            
            if response.lower() == 'hint':
                if hints_given < len(hints):
                    self.offer_hint(hints[hints_given])
                    hints_given += 1
                else:
                    print("No more hints available.")
                    break
            elif response.lower() == answer.lower():
                print("Correct answer!")
                break
            else:
                self.player_scores[self.current_player] += 2
                print(f"Incorrect.  Try again, or use a hint.  Your current score: {self.player_scores[self.current_player]}.")
                
            if response.lower() == "skip":
                self.player_scores[self.current_player] += 10
                print(f"Skipped.  This costs you 10 points.  Current point total: {self.player_scores[self.current_player]}")
                break

    # def handle_turn(self):
    #     """
    #     Manages a single turn for a player by presenting them woth a question
    #     """

    # def next_player(self):
    #     """
    #     Switches th ecurrent player in 2-player game mode
    #     """

    def countdown(self):
        """
        Displays a countdown from 3 to 1 to signal the beginning of the game
        """
        print("Get Ready!")
        for i in range(3, 0, -1):
            print(i)
            # time.sleep(1)

    # def play_game():
    #     """
    #     Starts and manages games flow, from choosing the games mode to conclusion
    #     """

    # def conclude_game(self):
    #     """
    #     Wraps up the game by dispalying the total scores and determining the winner
    #     """
    
    # def sudden_death(self):
    #     """
    #     Initiates sudden death mode following a 2 player tie
    #     """

    def play(self):
        """
        Calls the method to play the game
        """
        self.display_intro_message()
        self.handle_question()
        self.choose_game_mode()
        print(f"Game mode selected: {'Single Player' if game.player_mode == 1 else 'Two Players'}")
        print(f"Player names: {game.player_names}")
    

game = RiddleGame(filepath='requirements.txt')
game.play()
# game.print_loaded_data()

