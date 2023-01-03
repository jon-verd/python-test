# Chapter 7 - PATTERN MATCHING WITH REGULAR EXPRESSIONS

# This program checks an input to determine whether it is a number
def isPhoneNumber(text):
    if len(text) !=12:
        return False
    for i in range(0,3):
        if not text[i].isdecimal():
            return False
    if text[3] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    if text[7] != '-':
        return False
    for i in range(4,7):
        if not text[i].isdecimal():
            return False
    return True
print('is 415-555-4242 a phone number?')
print(isPhoneNumber('415-555-4242'))
print('Is Moshi Moshi a phone number?')
print(isPhoneNumber('Moshi moshi'))
# returns:
# is 415-555-4242 a phone number?
# True
# Is Moshi Moshi a phone number?
# False

# This part of the program finds a number within a larger string:

message = 'Call me at 415-555-1011 tomorrow. 415-555-9999 is my office.'
for i in range(len(message)):
    chunk = message[i:i+12]
    if isPhoneNumber(chunk):
        print('Phone number found: ' + chunk)
print('Done')
