#Prints a message addressed to the user that tells them the year that they will turn 100 years old.
name=input("Hello! Please enter your name: ")
print("Nice to meet you,", name)
try:
    age=float(input("How old are you? " ))
except:
    age=-1
bd=100-float(age)
cent=float(bd)+2018
if float(age)>=100:
    print ("Congratulations! You reached 100 years old in the year:", cent)
elif float(age)>=75:
    print("You're almost there! You will turn 100 in the year:", cent)
elif float(age)>=49:
    print("You've got more years left ahead of you than behind you! You will turn 100 in the year:", cent)
elif float(age)>=20:
    print("You haven't even reached your quarter life crisis yet! You will turn 100 in the year:", cent)
elif float(age)>=15:
    print("Buckle up because you still have a long ride ahead... You will turn 100 in the year:", cent)
elif float(age)>=5:
    print("When I was your age, I didn't even have a computer... You will turn 100 in the year", cent)
elif float(age)>=0:
    print("How are you even typing!? You will turn 100 in the year", cent)
else:
    print("Oops. You aren't really that age...")
