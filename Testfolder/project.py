import time
print ("If you want the prince... ")
time.sleep(5)
print ("Solve this riddle...")
time.sleep(3)
print ("WARNING!! If you get it wrong, this will be the end...")
time.sleep(2)
print ("What has a head and a tail but no body?")
A = "snake"
B = "human"
C = "coin"
print ("A: " + A)
print ("B: " + B)
print ("C: " + C)
choice = input().upper()
if choice == "A" or choice == "a":
    print ("WRONG! MWAHAHAHAHA")
    print("GAME OVER")
if choice == "B" or choice == "b":
    print("WRONG! MWAHAHAHAHA")
    print("GAME OVER")
if choice == "C" or choice == "c":
    print("CORRECT!!")
    time.sleep(10)
    print("Thanks for saving me! I love you!")
