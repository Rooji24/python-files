import random
randomNum = random.randint(1,10)
print("the random number is",randomNum)

if(randomNum > 5):
    print(randomNum,"is greater than 5")
elif(randomNum < 5):
    print(randomNum,"is less than 5")
else:
    print(randomNum,"is equal to 5")