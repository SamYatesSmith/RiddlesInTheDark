import time
import random
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
                lines = file.read().split("\n")
            
            self.questions, self.answers, self.hints = [], [], []
            temp_hints = []
            for line in lines:
                if line.startswith("Q: "):
                    question_text = wrap_text(line[3:])
                    if temp_hints:
                        self.hints.append([wrap_text(hint) for hint in temp_hints])
                        temp_hints = []
                    self.questions.append(question_text)
                elif line.startswith("A: "):
                    temp_hints = []
                else:
                    if line.strip():
                        temp_hints.append(line)
            if temp_hints:
                    self.hints.append(temp_hints)
        except FileNotFoundError:
            print(wrap_text("Error: The file path provided does not exist.  Please check the file path and give it another whirl."))

    def choose_game_mode(self):
        """
        Prompts the user to choose the game mode, either single player or two players. Enquire after player names.
        """
        mode = input("Choose your game mode: Key '1' for Single player and '2' for 2 player. 1/2: ")
        self.player_mode = int(mode)
        if self.player_mode == 1:
            self.player_names[0] = input(wrap_text("Enter your name: "))
        if self.player_mode == 2:
            self.player_names[0] = input(wrap_text("Enter name for Player 1: "))
            self.player_names[1] = input(wrap_text("Enter name for Player 2: "))

    def shuffle_questions(self):
        """
        Randomly shuffles the order of questions, answers
        """
        combined = list(zip(self.questions, self.answers, self.hints))
        random.shuffle(combined)
        self.quesitons, self.answers, self.hints = zip(*combined)

    def get_user_input(self, prompt, valid_responses=None, lower=True):
        """
        Gets user input with a specific prompt
        """
        while True:
            user_input = input(prompt)
            if lower:
                user_input = user_input.lower()
            if valid_responses is None or user_input in valid_responses:
                return user_input
            print(f"Invalid input.  Please enter one of the {valid_responses}.")

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
        print(f"Answer letter count: {letter_count_hint}")

    def offer_hint(self, hint):
        """
        Hint management, increments score if hint is requested
        """
        self.player_scores[self.current_player] += 1
        print(f"Hint: {hint}")
        print(f"Hint used. Current points: {self.player_scores[self.current_player]}.")

    def handle_question(self, question, answer, hints):
        """
        Handles logic for asking a question. Takes users response, provides hint and skips
        """

        print(f"Question for {self.player_names[self.current_player]}:", question)
        self.display_letter_count_hint(answer)
        hints_given = 0

        while True:
            response = self.get_user_input(f"{self.player_names[self.current_player]}, Type your answer (OR type 'hint' for a hint, 'skip' to Skip): ", lower = False)
            
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

    def handle_turn(self, player_number):
        """
        Manages a single turn for a player by presenting them with a question
        """
        print(f"{self.player_names[self.current_player]}'s turn: ")
        question, answer, hints = self.questions[player_number], self.answers[player_number], self.hints[player_number]
        self.handle_question(question, answer, hints)

    def next_player(self):
        """
        Switches the current player in 2-player game mode
        """
        self.current_player = 1 - self.current_player

    def countdown(self):
        """
        Displays a countdown from 3 to 1 to signal the beginning of the game
        """
        print("Starting in:")
        for i in range(3, 0, -1):
            print(f"{i}...")
            time.sleep(1)
        print("Go!\n")
        time.sleep(2)

    def play_game(self):
        """
        Starts and manages games flow, from choosing the games mode to conclusion
        """
        self.display_intro_message()
        self.choose_game_mode()
        ready_prompt = "Ok, so are you ready to play? (yes/no): " if self.player_mode == 1 else "Ok, so are you both ready to play? (yes/no): "
        ready = self.get_user_input(ready_prompt, ["yes", "no"], lower=True)
        
        if ready == "no":
            print("Maybe next time?!")
            return

        self.countdown()

        questions_per_player = 5
        if self.player_mode == 1:
            # In single-player mode, simply iterate through the first 5 questions
            for i in range(questions_per_player):
                print(f"Question {i+1} of {questions_per_player}: ")
                self.handle_turn(i)
        else:
            # In two-player mode, ensure unique questions for each player by correctly calculating question index
            for i in range(questions_per_player * 2): 
                current_question_index = i // 2 if i % 2 == 0 else (i // 2) + questions_per_player
                print(f"{self.player_names[self.current_player]}'s turn (Question {current_question_index % questions_per_player + 1} of {questions_per_player}):")
                self.handle_turn(current_question_index)
                self.next_player()
        
        self.conclude_game()

    def conclude_game(self):
        """
        Wraps up the game by displaying the total scores and determining the winner
        """
    
    # def sudden_death(self):
    #     """
    #     Initiates sudden death mode following a 2 player tie
    #     """

    def play(self):
        """
        Calls the method to play the game
        """
        self.play_game()

    def test_handle_question(self):
        self.display_intro_message()  # Optional, for context
        self.handle_question()

game = RiddleGame(filepath='requirements.txt')
game.play()
# game.print_loaded_data()

