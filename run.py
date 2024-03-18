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
        self.answers = []
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
            
            temp_hints = []
            for line in lines:
                if line.startswith("Q: "):
                    if temp_hints:
                        self.hints.append(temp_hints)
                        temp_hints = []
                    self.questions.append(line[3:])
                elif line.startswith("A: "):
                    self.answers.append(line[3:])
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
        while True:
            try:
                mode = input(wrap_text("Choose your game mode: Key '1' for Single player and '2' for 2 player. 1/2:\n"))
                self.player_mode = int(mode)
                if self.player_mode not in [1, 2]:
                    raise ValueError
                break
            except ValueError:
                print(wrap_text("Invalid input. Please enter '1' for Single player game, or '2' for Two player game."))

        if self.player_mode == 1:
            self.player_names[0] = input("Enter your name:\n")
        if self.player_mode == 2:
            self.player_names[0] = input("Enter name for Player 1:\n")
            self.player_names[1] = input("Enter name for Player 2:\n")

    def shuffle_questions(self):
        """
        Randomly shuffles the order of questions and subsequent answers&hints
        """
        combined = list(zip(self.questions, self.answers, self.hints))
        random.shuffle(combined)
        self.questions, self.answers, self.hints = map(list, zip(*combined)) if combined else ([], [], [])

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
        "Riddles in the Dark is a short riddle based game. In order to claim victory, "
        "the player must accrue as few points as possible. Points are incremented by "
        "answering riddles incorrectly, asking for hints, using too many hints and skipping "
        "the current question.\n\n"
        "Players are allowed 5 hints per question. These hints will accrue 1 point each.\n\n"
        "However, if a player uses more than 5 hints, they are punished with an incorrect "
        "answer's point value.\n\n"
        "When a player answers incorrectly, they receive 2 points.\n\n"
        "When a player skips the question, they will receive a 10 point penalty.\n\n"
        "Players are provided with underscores which represent the number of letters in the answer.\n\n"
        "Good luck, and Have fun!\n\n"
    )
    paragraphs = intro_message.split('\n\n')
    wrapped_intro = '\n\n'.join(textwrap.fill(paragraph, width=80) for paragraph in paragraphs)

    print(wrapped_intro)

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
        print(wrap_text(f"Hint: {hint}"))
        print(wrap_text(f"Hint used. Current points: {self.player_scores[self.current_player]}."))

    def handle_question(self, question, answer, hints):
        """
        Handles logic for asking a question. Takes users response, provides hint and skips
        """
        question_text = f"Question for {self.player_names[self.current_player]}: {question}"
        print(wrap_text(question_text))
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
                print("Correct answer!\n\n")
                break
            else:
                self.player_scores[self.current_player] += 2
                print(wrap_text(f"Incorrect.  Try again, or use a hint.  Your current score: {self.player_scores[self.current_player]}.\n\n"))
                
            if response.lower() == "skip":
                self.player_scores[self.current_player] += 10
                print(wrap_text(f"Skipped.  This costs you 10 points.  Current point total: {self.player_scores[self.current_player]}"))
                break

    def handle_turn(self, question_index):
        """
        Manages a single turn for a player by presenting them with a question
        """
        if question_index < len(self.questions):
            print(f"{self.player_names[self.current_player]}'s turn: ")
            question, answer, hints = self.questions[question_index], self.answers[question_index], self.hints[question_index]
            self.handle_question(question, answer, hints)
        else:
            print("Error: Question index out of range.")

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
        self.shuffle_questions()

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
        
        if self.player_mode == 2 and self.player_scores[0] == self.player_scores[1]:
            self.sudden_death()
        else:
            self.conclude_game()

    def conclude_game(self):
        """
        Wraps up the game by displaying the total scores and determining the winner
        """
        if self.player_mode == 1:
            if self.player_scores[0] == 0:
                print(wrap_text(f"Flawless Victory! Incredible effort, {self.player_names[0]}. You're a riddle hero! Gollum would stand no chance!"))
            else:
                print(f"Game Over! {self.player_names[0]}, your total points: {self.player_scores[0]}.")
        else:
            print("Game Over!")
            print(wrap_text(f"{self.player_names[0]}'s total points: {self.player_scores[0]}, {self.player_names[1]}'s total points: {self.player_scores[1]}."))
            if self.player_scores[0] < self.player_scores[1]:
                if self.player_scores[0] == 0:
                    print(wrap_text(f"Flawless Victory! Incredible effort, {self.player_names[0]}. You're a riddle hero! Gollum would stand no chance!"))
                else:
                    print(f"{self.player_names[0]} wins!")
            elif self.player_scores[0] > self.player_scores[1]:
                if self.player_scores[1] == 0:
                    print(wrap_text(f"Flawless Victory! Incredible effort, {self.player_names[1]}. You're a riddle hero! Gollum would stand no chance!"))
                else:
                    print(f"{self.player_names[1]} wins!")
            else:
                print("It's a tie!")


    def sudden_death(self):
        """
        Initiates sudden death mode following a 2 player tie
        """
        print(wrap_text(f"It's a tie! Both players have {self.player_scores[0]} points."))
        print("Entering the Sudden Death round...")
        print(wrap_text("Hints are disabled in Sudden Death.  A wrong answer means you loose.  Good luck!"))

        asked_questions = 10
        sudden_death_index = asked_questions

        while sudden_death_index < len(self.questions):
            for player_index in range(2):
                self.current_player = player_index
                print(f"\n{self.player_names[self.current_player]}'s turn: ")
                question, answer = self.questions[sudden_death_index], self.answers[sudden_death_index]
                print("Question: ", question)
                self.display_letter_count_hint(answer)

                response = self.get_user_input("Your answer: ", lower=False)

                if response.lower() != answer.lower():
                    print(wrap_text(f"Worng answer! {self.player_names[self.current_player]} loses."))
                    winner = self.player_names[1 - self.current_player]
                    print(wrap_text(f"Congratulations! {winner}, you won the game!  {winner} is the Riddle King."))
                    return

                sudden_death_index +=1
                if sudden_death_index >= len(self.questions):
                    print(wrap_text("Wow wow wow wow.  Theres some very accomplished riddling taking place here.  I hold my hands up and gracefully admit defeat.  Congratulations, you both beat me, so you both win!"))
                    return

            self.next_player()

    def play(self):
        """
        Calls the method to play the game
        """
        self.play_game()

game = RiddleGame(filepath='riddleshintsanswers.txt')
game.play()

