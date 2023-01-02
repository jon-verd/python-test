#! python3

# mclip-project.py is a multi-clipboard program. It is a part of the 'Automate the Boring Stuff' book.

TEXT = {
    'agree' : """Yes I agree, that sounds great to me.""",
    'busy' : """Sorry, I am not available at the moment. I'll reach out when I'm back at my keyboard.""",
    'LMK' : """Let me know what you think!""" }

import sys, pyperclip

if len(sys.argv) < 2:
    print('Usage: python mclip-project.py [keyphrase] - copy phrase text')
    sys.exit()
keyphrase = sys.argv(1) #first command line arg is the keyphrase

if keyphrase in TEXT:
    pyperclip.copy(TEXT[keyphrase])
    print('Text for ' + keyphrase + 'copied to clipboard')
else:
    print('There is no text for ' + keyphrase)