def solution(number_list):
    for number in number_list:
        if number > 500:
            break
        elif number > 150:
            continue
        elif number % 5 == 0:
            print(number)

numbers = [12, 75, 150, 180, 145, 525, 50]
solution(numbers)