"""Create required phrase.
----------------------
You are given a string of available characters and a string representing a word or a phrase that you need to generate.
Write a function that checks if you cab generate required word/phrase using the characters provided.
If you can, then please return True, otherwise return False.

"""

def required_phrase(characters, phrase):
    phrase = sorted(phrase)
    characters = sorted(characters)

    if characters == phrase:
        return True
    else:
        return False

print(required_phrase('lelho', 'hello'))
print(required_phrase('han', 'naah'))
print(required_phrase('',''))
print(required_phrase('!65','!65 '))
print(required_phrase('GO','go'))





