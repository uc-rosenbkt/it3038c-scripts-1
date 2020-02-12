import time

start_time = time.time()
print('What is your name?') 
myName = input()
while myName != 'Max':
    if myName == 'yourname':
        print("bad joke, What's your name?")
        myName=input()
    else:
        print('That is not your name. Please, tell me your real name.')
        myName=input()


print('Hello, ' + myName + '. That is a good name.' ' How old are you?')
myAge = int(input())
if myAge < 13:
    print("You're a minor?")
elif myAge == 13:
    print("You're a teenager now... that's cool I guess")
elif myAge > 13 and myAge < 30:
    print("You're young and dumb")
elif myAge >= 30 and myAge < 65:
    print("You're adulting.")
else:
    print("You're not dead yet?")

programAge = int(time.time() - start_time)
print("%s? That's funny, I'm only %s seconds old." % (myAge, programAge))
#print("I wish I was " + str(myAge * 2) + " years old.")
print("I wish I was %s years old." % (myAge * 2))

time.sleep(3)
print("I'm tired. I go sleep sleep now")