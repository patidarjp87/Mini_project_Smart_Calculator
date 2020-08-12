import sys
sys.path.append('/module/')
import module
from module.calculations import *
print(Responses[0])
print(Responses[1])
while True:
    print()
    text=input("Enter a question or press 'q' to exit")
    if text=='q':
        end()
    else:
        for word in text.split():
            if word.upper() in operations.keys():
                try:
                    l1=extract_numbers_from_text(text)
                    l2=extract_complex_from_text(text)
                    for x in l2:
                        if x.imag==0:
                            pass
                        else:
                          r=operations[word.upper()](l2[0],l2[1])
                          print(r)
                          break
                    else:
                        r=operations[word.upper()](l1[0],l1[1])
                        print(r)
                except:
                    print('Something went wrong...!!! please retry')
                finally:
                    break
            elif word.upper() in commands.keys():
                commands[word.upper()]()
                break
            elif word.upper() in logical.keys():
                try:
                    l=extract_numbers_from_text(text)
                    r=logical[word.upper()](int(l[0]),int(l[1]))
                    print(r)
                except:
                    print('Something went wrong...!!! please retry')
                finally:
                    break
            elif word.upper() in operation.keys():
             if word.upper()=='SQUARE' :
                try:
                    l2=extract_complex_from_text(text)
                    if len(l2)>0:
                      for x in l2:
                          if x.imag==0:
                              pass
                          else:
                            r=operation[word.upper()](l2[0])
                            print(r)
                            break
                      else:
                        for x in l2:
                            if type(x.real)==float:
                                r=operation[word.upper()](x.real)
                                print(r)
                                break
                except:
                    print('Something went wrong...!!! please retry')
                finally:
                    break
             else:
                try:
                        l1=extract_numbers_from_text(text)
                        r=operation[word.upper()](int(l1[0]))
                        print(r)
                        break
                except:
                    print('Something went wrong...!!! please retry')
                finally:
                    break
        else:
            sorry()
