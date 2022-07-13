def collatz(num):
    if num % 2 ==1:
        return num//2
    elif num % 2 ==0:
        return 3*num + 1

def user():
    x=int(input("enter a number:"))
    while x!=1:
        x=collatz(x)
        print(x)

user()