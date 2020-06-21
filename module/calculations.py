Responses=['welcome to smart calculator','my name is smart calculator made by JAYDEEP PATIDAR','Thanks','sorry,this is beyond my ability']
def extract_numbers_from_text(text):
    l=[]
    for t in text.split(' '):
        try:
            l.append(float(t))
        except ValueError:
            pass
    return l
def lcm(a,b):
    L=a if a>b else b
    if L%a==0 and L%b==0:
        return L
    L+=1
def hcf(a,b):
    H=a if a<b else b
    while h>=1:
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
operations={'plus':add,'add':add,'addition':add,'sum':add,'minus':sub,'subtract':sub,'differentiate':sub,'difference':sub,'product':mul,'multiply':mul,'divide':div,'division':div,'hcf':hcf,'lcm':lcm}
commands={'name':myname,'close':end,'end':end,'terminate':end,'exit':end}
