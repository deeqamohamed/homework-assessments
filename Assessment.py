"""Q2: in theory file"""
"""Q3:Write a function that can define whether a word is a Palindrome or not  """
#version1
def checkPalindrome(string):
    i = len(string)
    if i == 1:
        return True
    return string == string[::-1]
print(checkPalindrome('madam'))

#version2: not sure if input was required

def checkPalindrome():
    string = input('String:')
    i = len(string)
    if i == 1:
        print('Is palindrome')
        # return True
    if string == string[::-1]:
        print('Is palindrome')
    else:
        print('Is not palindrome')
print(checkPalindrome())

"""Q4: in Assessment_test file"""
"""Q6: in theory file"""
"""Q7: in theroy file """
"""Q9: Two Number Sum"""

def two_number_set():
    my_numbers = [3, 5, -4, 8, 11, 1, -1, 6]
    target_sum = 10
    new_list = [[x, y] for x in my_numbers for y in my_numbers if x != y and target_sum == x + y]
    for [x,y] in new_list:
        return [x,y]
    else:
        return []

print(two_number_set())