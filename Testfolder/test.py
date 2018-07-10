#psuedo code practice
#ages = [5,12,3,56,24,78,1,15,44]
 #average the sum with # of elements from list : age
 #add all elements in ages
#total = sum(ages)
#print (total)
 # divide by num of elements
#average = sum(ages) / len(ages)
#print (average)
def intro():
    print()
    print("Hi, welcome to chatbox!")
    print("Please talk to me!")
    print()

def process_input(answer):
    if answer == "hello":
        say_greeting()
        #print("hello, thank you for talking to me")
    elif answer == "bye":
        say_bye()
def say_greeting():
    if answer  == "hello":
        print()
        print("Hello thank you for talking to me!")
        print()

def say_bye():
    print()
    print("see ya!")
    print()
def main(): 
    intro()
    while True:
        answer = input("What will you say?")
        process_input(answer)
        print ("That's cool!")
