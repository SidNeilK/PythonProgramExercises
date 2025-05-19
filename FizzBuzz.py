def fizzBuzz(upTo):
    for i in range(1, upTo):
        if i%3 == 0 and i%5 == 0:
            print("FizzBuzz",end=" ")
        elif i%3 == 0:
            print("Fizz",end=" ")
        elif i%5 == 0:
            print("Buzz",end=" ")
        else:
            print(i,end=" ")

fizzBuzz(35)