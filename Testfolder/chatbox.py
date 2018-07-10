def intro():
    print()
    print("Hi, welcome to chatbox!")
    print("Please talk to me!")
    print()
def is_valid_input(answer, listOfResponses):
    #if answer is in list of listOfResponses
        #return True
    #else
        #returnFalse
    for x in listOfResponses:
        if answer in listOfResponses:
            return True
        else:
            return False


# def process_input(answer, name): #parameter
#     if answer == "Hello" or answer == "Hi" or answer == "Hey":
#         say_greeting(answer, name)
#     else:
#         say_bye()
#         #print("hello, thank you for talking to me")
def process_input(answer,user):
    greetings = ["Hey", "Hi","Hello"]
    goodbyes = ["goodbye", "bye", "see ya"]
    if is_valid_input(answer, greetings):
        say_greeting(answer,user)
    elif is_valid_input(answer, goodbyes):
        say_bye()

    if answer in greetings:
        say_greeting(answer, user)
    elif answer == "Bye":
        say_bye
def say_greeting(answer, name):
        print()
        print ("Oh hi! ")
        print("Nice to meet you, %s!" % name)
        print()
        mood = input ("How are you doing? ")
        say_goodresponse(mood)
        say_badresponse(mood)
        answerAge(age)
def reply():
    if mood == "good":
        say_goodresponse(mood)
    if mood == "bad":
        say_badresponse(mood)
def say_badresponse(mood):
    print()
    print("I'm sorry to hear that.")
    print()
def say_goodresponse(mood):
    print()
    print ("That's great to hear! ")
    print()
def say_bye():
    print()
    print("see ya! ")
    print()
def answerAge():
    age = input("How old are you? ")
    ageResponse(age)
    
def ageResponse(age):
    if age.is_integer():
        print ("nice! goodbye.")
def main():
    intro()
    while True:
        user = input("What's your name? ")
        answer = input("What will you say? ")
        process_input(answer, user)

if __name__ == "__main__":
    main()
