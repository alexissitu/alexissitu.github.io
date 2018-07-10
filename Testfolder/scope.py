def say_hello(name):
    print ("Hi" + name)

def main():
    user = "Tiffanie" #local variable
    say_hello(user)


#return practice
def sub(num1, num2):
    diff = num1 - num2
    print (diff)
    return diff
#def main():
    #n = 10
    # n2 = 2
    # print(sub(n,n2))


#function2 practice
#using returns to add total
def main():
    list = [1,2,3,4,23,123,435,67,45,234,79]
    print (calc_total(list))
def calc_total(list):
    total = sum(list)
    return total
if __name__ == "__main__":
    main()

def process_input(answer):
    greetings = ["Hey", "Hi","Hello"]
    goodbyes = ["goodbye", "bye", "see ya"]

    if answer in greetings:
        say_greetings()
    elif answer == "Bye":
        say_bye 
