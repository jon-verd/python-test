# This is a program that takes anything on the clipboard and automatically converts it into a bulleted list.

# Example text:
# Lists of animals
# Lists of aquarium life
# Lists of biologists by author abbreviation
# Lists of cultivars

# We will be using pyperclip to copy our clipboard
import pyperclip
myText = pyperclip.paste
# pyperclip.copy(myText)
# after importing our text, we will split the text where a new line begins, denoted by '\n'.
lines = myText.split('\n')
for i in range(len(lines)):
    lines[i] = '* '+ lines[1]
pyperclip.copy(my.Text)
# now that a star is added to the beginning of each new line, we need to rejoin the text to be able to paste it all as one value
myText = '/n'.join(lines)
pyperclip.copy(myText)
