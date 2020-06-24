Responses=['welcome to smart calculator','my name is smart calculator','Thanks for using smart calculator','sorry,this is beyond my ability','JAYDEEP PATIDAR \nFROM INSTITUTE OF ENGINEERING AND TECHNOLOGY - DAVV,INDORE,M.P.,INDIA','CONTACT MR. JAYDEEP PATIDAR \nCONTACT DETAILS:\nPHONE: 7745939565 \nMAIL: jaydeeppatidar87@gmail.com','you can use me as calculator i can do basic calculations like addition,subtraction,multiplication,division,logical and ,or ,xor,lcm,hcf between two numbers,square,binary,hexdecimal,octal of a number\nyou have to Enter you question with separator space between every meaningful operator and oprands,number and number,words and number\nI did not expect anything from you','nothing']
def extract_numbers_from_text(text):
    L=[]
    for t in text.split():
        try:
            L.append(float(t))
        except ValueError:
            pass
    return L
def extract_complex_from_text(text):
    l=[]
    for t in text.split():
        try:
            l.append(complex(t))
        except ValueError:
            pass
    return l
def lcmoftwo(a,b):
 L=a if a>b else b
 while L<=a*b:
     if L%a==0 and L%b==0:
         return L
     L+=1
def hcfoftwo(a,b):
 H=a if a<b else b
 while H>=1:
     if a%H==0 and b%H==0:
         return H
     h-=1
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def mul(a,b):
    return a*b
def div(a,b):
    return a/b
def div2(a,b):
    return a//b
def binary(a):
    b=bin(a)
    return b[2::]
def sqr(a):
    return (a)**2
def hexadecimal(a):
    h=hex(a)
    return h[2::]
def octal(a):
    b=oct(a)
    return b[2::]
def xoroftwo(a,b):
    return a^b
def oroftwo(a,b):
    return a|b
def andoftwo(a,b):
    return a&b
def end():
    print(Responses[2])
    input('press enter key to exit')
    exit()
def myname():
    print(Responses[1])
def sorry():
    print(Responses[3])
def made():
    print(Responses[4])
def contact():
    print(Responses[5])
def use():
    print(Responses[6])
def want():
    print(Responses[7])
def purpose():
    print("purpose to learn and taught something")
operations={'*':mul,'-':sub,'/':div,'//':div2,'+':add,'HCF':hcfoftwo,'LCM':lcmoftwo,'PLUS':add,'ADD':add,'ADDITION':add,'SUM':add,'MINUS':sub,'SUBTRACT':sub,'DIFFERENTIATE':sub,'DIFFERENCE':sub,'PRODUCT':mul,'MULTIPLY':mul,'DIVIDE':div,'DIVISION':div}
commands={'CONTACT':contact,'WANT':want,'CHARGE':want,'FEE':want,'LEARN':contact,'PURPOSE':purpose,'MISSION':purpose,'VISION':purpose,'USE':use,'DO':use,'WORK':use,'ABILITY':use,'DEVLOP':made,'MADE':made,'HOW':use,'WHO':made,'DEVLOPER':made,'NAME':myname,'CLOSE':end,'END':end,'TERMINATE':end,'EXIT':end}
operation={'SQUARE':sqr,'BINARY':binary,'HEX':hexadecimal,'HEXADECIMAL':hexadecimal,'OCTAL':octal,'OCT':octal,'BIN':binary}
logical={'OR':oroftwo,'|':oroftwo,'AND':andoftwo,'&':andoftwo,'^':xoroftwo,'XOR':xoroftwo}
