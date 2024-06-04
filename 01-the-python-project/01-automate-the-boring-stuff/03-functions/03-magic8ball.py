import random

def get_answer(answer_number):
    if answer_number == 1:
        return "it is certain"
    elif answer_number == 2:
        return "it is decidedly so"
    elif answer_number == 3:
        return "yes"
    elif answer_number == 4:
        return "reply hazy try again"
    elif answer_number == 5:
        return "ask again later"
    elif answer_number == 6:
        return "concentrate and ask again"
    elif answer_number == 7:
        return "my answer is no"
    elif answer_number == 8:
        return "outlook not so good"
    elif answer_number == 9:
        return "very doubtful"
    
# print(get_answer(random.randint(1, 9)))
r = random.randint(1, 9)
fortune = get_answer(r)
print(fortune)