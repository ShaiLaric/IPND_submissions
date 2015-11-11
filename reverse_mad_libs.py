# Parts to fill in
fill_ins  = ["___1___","___2___","___3___","___4___","___5___","___6___", \
             "___7___","___8___"]

# Game paragraphs
easy_game = fill_ins[0] + " had a little " + fill_ins[1] + ", " + fill_ins[2] \
            + " " + fill_ins[3] + ", " + fill_ins[4] + " " + fill_ins[5] \
            + ".\n" + fill_ins[6] + " had a little lamb whose " + fill_ins[7] \
            + " was white as snow."

medium_game = "Barack Obama is the " + fill_ins[0] + " of the United States " \
              + "of " + fill_ins[1] + ". \n" + fill_ins[2] + " is the " \
              + "vice-president. There are 50 " + fill_ins[3] + " in the " \
              + "USA.\nThe three " + fill_ins[4] + " of government are: the " \
              + fill_ins[5] + ", represented by the\npresident, the " \
              + fill_ins[6] + ", represented by Congress, and the " \
              + "judicial,\nrepresented by the Supreme " + fill_ins[7] + "."

hard_game = "The " + fill_ins[0] + " of Gilgamesh is a poem from ancient " \
            + fill_ins[1] + ". It tells the story of\nthe king of " \
            + fill_ins[2] + ". First, the " + fill_ins[3] + " create the " \
            + "wild man " + fill_ins[4] + " to stop\nGilgamesh from " \
            + "oppressing his people. The king fights the wild man, but " \
            + "they\nsoon become close " + fill_ins[5] + ". They have several " \
            + "adventures together, including\nfighting " + fill_ins[6] \
            + ", the guardian of the Cedar Mountain and killing the " \
            + fill_ins[7] + "\nof Heaven. And that's just the first half!"

# Game answers
easy_answers = ["Mary", "lamb", "little", "lamb", "little", "lamb", "Mary", \
                "fleece"]
medium_answers = ["president", "America", "Joe Biden", "states", "branches", \
                  "executive", "legislative", "Court"]
hard_answers = ["Epic", "Mesopotamia", "Uruk", "gods", "Enkidu", "friends", \
                "Humbaba", "Bull"]

# Gets player choice of difficulty level; returns choice
def determine_difficulty():
    level = ["easy", "medium", "hard"]
    difficulty = raw_input("Please choose game difficulty by " \
                           + "entering Easy, Medium, or Hard:\n").lower()
    while difficulty not in level:
        difficulty = raw_input("Please enter one of the following words " \
                               + "to determine difficulty:\n" + \
                               "Easy, Medium, or Hard.\n").lower()
    return difficulty

# Based on difficulty level, sets the appropriate paragraph and answers
def set_texts():
    difficulty = determine_difficulty()
    if difficulty == "easy":
        game_paragraph = easy_game
        game_answers = easy_answers
    elif difficulty == "medium":
        game_paragraph = medium_game
        game_answers = medium_answers
    else:
        game_paragraph = hard_game
        game_answers = hard_answers
    return game_paragraph, game_answers

# Gets and returns the user's word choice
def get_input(current):
    user_input = raw_input("\nPlease enter a word to replace blank #" \
                           + str(fill_ins[current][3]) + ": ")
    return str(user_input)

# Checks if a word in parts_of_speech is a substring of the word passed in.
def word_in_pos(word, parts_of_speech):
    for pos in parts_of_speech:
        if pos in word:
            return pos
    return None

# Runs the game and handles choice of playing again
def play_game():
    game_paragraph, game_answers = set_texts()		# get difficulty; set appropriate game & answers
    current = 0
    print "\n" + game_paragraph
    for element in fill_ins:											# loop through blanks
        choice = get_input(current)								# ask for a guess
        while choice != game_answers[current]:		# if wrong, inform user & ask again
            print "Sorry, try again.\n" + game_paragraph	
            choice = get_input(current)
        game_paragraph = game_paragraph.replace(element, choice)	# if right, put answer in game string
        print "\n" + game_paragraph								# prepare for next guess
        current += 1															# increment counter to move on
    finished = raw_input("\nGame over! Would you like to play again? ")	# allow another play
    if str(finished).lower() == "y" or str(finished).lower() == "yes":	# if yes, start over
        play_game()
    return "Thanks for playing!"									# end game

# Starts the game
play_game()
