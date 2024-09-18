x=5


def increase_number():
    global x
    x+=1
    return x

print(increase_number())

#better way
x=5

def increase_number(num):
    return num+1
  
print(increase_number(x))