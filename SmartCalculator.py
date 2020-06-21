import sys
sys.path.append('/module/')
import module
from module.calculations import *
print(Responses[0])
print(Responses[1])
while True:
    print()
    text=input('Enter a question')
    for word in text.split(' '):
        if word.upper() in operations.keys():
            try:
                l=extract_numbers_from_text(text)
                r=operations[word.upper()](l[0],l[1])
                print(r)
            except:
                print('Something went wrong...!!! please retry')
            finally:
                break
        elif word.upper() in commands.keys():
            commands[word.upper()]()
            break
    else:
        sorry()
