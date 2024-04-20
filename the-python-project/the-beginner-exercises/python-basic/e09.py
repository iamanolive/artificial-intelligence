def solution(num):
    return num == num[::-1]

original_number = input()
palindrome_number = solution(original_number)
print("The original number is " + original_number)
if palindrome_number:
    print("Yes. The given number is a palindrome number.")
else:
    print("No. The given number is not a palindrome number.")