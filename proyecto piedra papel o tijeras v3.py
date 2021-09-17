import random
name = input("Enter your name: ")
print(f"hello, {name}")
posibilidades = ["scissors", "rock", "paper"]
jugadas =  {"scissors":"paper", "rock":"scissors" , "paper":"rock"}
score = 0

with open("rating.txt","r") as archivo:
    h = archivo.readlines()
    for i in h:
        if name in i:
            k=i.split()
            score = int(k[1])
            break


while 1:
    user = input()
    
    pc = random.choice(posibilidades)

    if user == "!exit" or user == "scissors" or user == "rock" or user== "paper" or user == "!rating":
        
        if user == "!exit":
            print("Bye!")
            break

        elif user == "!rating":
            print(f"Your rating: {score}")

        elif jugadas[user] == pc:
            print(f"Well done. The computer chose {pc} and failed")
            score += 100

        elif jugadas[pc] == user:
            print(f"Sorry, but the computer chose {pc}")

        else:
            print(f"There is a draw ({pc})")
            score += 50

    else:
        print("Invalid input")
