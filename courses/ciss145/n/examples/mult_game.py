import random
random.seed()

x = random.randrange(90, 101)
y = random.randrange(90, 101)

print "What is the product of", x, "and", y, "?"
guess = input("Answer: ")

if guess == x * y:
    print "Correct!"
else:
    print "Incorrect!"

   
