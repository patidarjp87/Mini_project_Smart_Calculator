Responses=['welcome to smart calculator','my name is smart calculator made by JAYDEEP PATIDAR','Thanks for using smart calculator','sorry,this is beyond my ability']
def extract_numbers_from_text(text):
    L=[]
    for t in text.split(' '):
        try:
            L.append(float(t))
        except ValueError:
            pass
    return L
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
def end():
    print(Responses[2])
    input('press enter key to exit')
    exit()
def myname():
    print(Responses[1])
def sorry():
    print(Responses[3])
operations={'HCF':hcfoftwo,'LCM':lcmoftwo,'PLUS':add,'ADD':add,'ADDITION':add,'SUM':add,'MINUS':sub,'SUBTRACT':sub,'DIFFERENTIATE':sub,'DIFFERENCE':sub,'PRODUCT':mul,'MULTIPLY':mul,'DIVIDE':div,'DIVISION':div}
commands={'NAME':myname,'CLOSE':end,'END':end,'TERMINATE':end,'EXIT':end}
