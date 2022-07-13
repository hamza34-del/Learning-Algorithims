"""A simple replica of the range function with a step value"""

def RANGE(start,stop,step):
    var=start
    while start < (stop -var) and start != stop:
        print(start)
        start +=step
start =int(input("Enter start Number:"))
stop =int(input("Enter stop number:"))
step =int(input("Enter step value:"))
RANGE(start,stop,step)