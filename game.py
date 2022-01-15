# Array for the questions, and the information about the fails
sum_information = {
    "easy": {
        "questions": [
            "1 + 1",
            "3 - 5",
            "52 + 9",
            "-7 + 32",
            "65 - 96"
        ],

        "max_fails": 0,

        "user_fails": 0
    },

    "medium": {
        "questions": [
            "154 / 2",
            "327 + 637",
            "-643 + 960",
            "404 + 329",
            "330 * 3"
        ],

        "max_fails": 0,

        "user_fails": 0
    },

    "hard": {
        "questions": [
            "503 + 3965",
            "-5964 + 9773",
            "32 * 135",
            "1740 / 6",
            "596 * 9"
        ],

        "max_fails": 1,

        "user_fails": 0
    }
}

difficulties = list ( sum_information.keys() ) # All the difficulties
game_over = False # Check if the user lost the easy questions



# Ask the user which mode he/she wants to begin with

def startScreen():

    choosing = True # Check if the user must choose an answer

    difficulties_str = ", ".join(difficulties[:-1]) + " or " + difficulties[-1] # All the difficulty options


    print("Which mode you want to play?")


    while choosing:

        question = "You have a choice between: " + difficulties_str + ": "
        
        difficulty = input(question).lower()


        try:
            difficulties.index(difficulty) # Check if the chosen difficulty is an option

        except: 
            print("Choose between the given options")

        else:   
            choosing = False # Stop the question


    return difficulty # Return the difficulty the user wants to start with




# Ask the questions to the user

def sum_questions(difficulty):

    user_lost = False
    change_difficulty = False

    questions = sum_information[difficulty]['questions'] # Questions
    max_fails = sum_information[difficulty]['max_fails'] # Max amount of fails


    print('This questions are for the difficulty: "' + difficulty + '"')

    
    for sum_str in questions:
        
        user_fails = sum_information[difficulty]['user_fails'] # Users failed amount
    
        user_chosen = False  # Check if the user must choose an answer

        
        question = 'whats "' + sum_str + '" ?: '
    
        while not user_chosen and not change_difficulty: 

            # Say how many fails the user has left
            max_fails_text = "You can only fail " + str(max_fails - user_fails) + " more time(s)"
            print(max_fails_text) 

            user_answer = input(question)


            try:
                user_answer = int(user_answer)

            except:
                print("Choose a number")

            else:
                user_chosen = True # Stop the question

                answer = eval(sum_str) # Calculate the answer

                # If the user has it correct
                if user_answer == answer:
                    print("Thats correct!")
                
                # If the user failed
                else:
                    sum_information[difficulty]['user_fails'] += 1 # Add 1 fail to the total failed answers of the user

                    # Print the correct answer
                    fail_message = "That is not correct, the answer was: " + str( int(answer) )
                    print(fail_message)

                    # If the user has made the max amount of fails
                    if user_fails == max_fails:
                        user_lost = True

                        change_difficulty = True # Go out of the loop with the questions


    else:
        return user_lost # Return if the user won / lost




# Check if the user lost the easiest difficulty

def check_difficulty(difficulty):

    # If the user lost the easiest difficulty
    if difficulty == difficulties[0] and user_lost:
        easy_lost = True
    
    else: 
        easy_lost = False


    return easy_lost # Return if the user lost the easiest difficulty



# Check if the difficulty must be updated

def update_difficulty():

    max_fails = sum_information[difficulty]['max_fails'] # Max fails the user can make for the difficulty
    user_fails = sum_information[difficulty]['user_fails'] # Amount of the failed answers of the user

    # If the user won the hard round
    if difficulty == difficulties[-1] and user_fails <= max_fails:
        must_update = False

    else:
        must_update = True


    return must_update # Return if the difficulty must be updated




# Update the difficulty

def change_difficulty(difficulty):   

    difficulty_index = difficulties.index(difficulty) # Position of the difficulty 
    max_fails = sum_information[difficulty]['max_fails'] # Max fails the user can make for the difficulty
    user_fails = sum_information[difficulty]['user_fails'] # Amount of the failed answers of the user


    # If the user failed less than the max fails amount
    if user_fails <= max_fails:
        difficulty = difficulties[difficulty_index + 1] # Increase the difficulty

    else:
        difficulty = difficulties[difficulty_index -1] # Decrease the difficulty


    return difficulty # Return the new difficulty




difficulty = startScreen() # Ask the user which mode he wants to begin with


while not game_over:
    user_lost = sum_questions(difficulty) # Ask the questions to the user

    easy_lost = check_difficulty(difficulty) # Check if the user lost the easy round

    if not easy_lost:
        must_update = update_difficulty() # Check if the difficulty must be updated
        
        # If the user did not win the hard round
        if must_update:
            difficulty = change_difficulty(difficulty) # Increase / decrease the difficulty

        else:
            print("You win!")
            game_over = True # Stop the questions


    # If the user lost the easy round, or the chosen difficulty was already lost
    if easy_lost or sum_information[difficulty]['user_fails'] > sum_information[difficulty]['max_fails']:   
        print('Game over! \n your highest difficulty is: "' + difficulty + '"')
        game_over = True # Stop the questions