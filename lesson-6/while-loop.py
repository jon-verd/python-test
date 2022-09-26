# spam = 0
# while spam < 5:
#     print('Hello world')
#     spam = spam + 1

# example 2 - using continue
# A continue statement causes the execution to immediatly jump back to the start of the loop and re-check the condition.
spam = 0
while spam < 5:
    spam = spam + 1
    if spam == 3:
        continue
    print('spam is ' + str(spam))