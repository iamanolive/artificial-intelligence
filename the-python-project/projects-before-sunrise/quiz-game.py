start_quiz = input("Do you want to solve the python programming quiz? ")
if start_quiz.lower() == "yes":
    user_score = 0
    
    print("Question #1")
    print("What symbol is used to comment out a line of code in python?")
    user_answer_1 = input()
    correct_answer_1 = "#"
    if user_answer_1.lower() == correct_answer_1:
        print("You got it right!")
        user_score += 1
    else:
        print("That isn't right. We use a # to start comments. Better luck on the next one!")
    
    print("Question #2")
    print("What function do we use to print text onto the console?")
    user_answer_2 = input()
    correct_answer_2 = "print()"
    if user_answer_2.lower() == correct_answer_2:
        print("You got it right!")
        user_score += 1
    else:
        print("That isn't right. We use the print() function to print text onto the console. Better luck on the next one!")
    
    print("Question #3")
    print("Which operator is used to assign values to a variable?")
    user_answer_3 = input()
    correct_answer_3 = "="
    if user_answer_3.lower() == correct_answer_3:
        print("You got it right")
        user_score += 1
    else:
        print("That isn't right. The = operator assigns a value to a variable. Better luck on the next one!")

    print("Question #4")
    print("The value of the variable \"counter\" is initialized to 0. Increment the value of counter by 1")
    user_answer_4 = input()
    correct_answer_4_1 = "counter += 1"
    correct_answer_4_2 = "counter = counter + 1"
    if user_answer_4 == correct_answer_4_1 or user_answer_4 == correct_answer_4_2:
        print("You got it right!")
        user_score += 1
    else:
        print("Your program crashed. That can't be right. Check the python documentation")
    
    print("Question #5")
    print("What extension do python files have?")
    user_answer_5 = input()
    correct_answer_5 = ".py"
    if user_answer_5.lower() == correct_answer_5:
        print("You got it right!")
        user_score += 1
    else:
        print("No, it's .py. The benefit of failure is that you learn something new everyday!")
    
    print("Quiz over! Thanks for playing!")
    print("You answered " + str(user_score) + " of 5 questions correctly")
    print("You scored " + str((user_score / 5) * 100) + "%")