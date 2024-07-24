def remove(string):
    return string.replace(" ", "")

s = input("Enter a string to check if its a palindrome: ")

def palindrome_checker(s):
    s = remove(s)
    s_reverse = s[::-1]
    if s_reverse == s:
        print('Output: True')
        print('Explanation:' + s + ' is a palindrome')
    elif s_reverse != s:
        print('Output: False')
        print('Explanation:' + s + ' is not a palindrome')


palindrome_checker(s)
