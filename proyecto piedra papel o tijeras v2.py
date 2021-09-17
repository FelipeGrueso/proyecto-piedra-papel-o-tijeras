import random
posibilidades = ["scissors", "rock", "paper"]
jugadas =  {"scissors":"paper", "rock":"scissors" , "paper":"rock"}

while 1:
    user = input()
    
    pc = random.choice(posibilidades)

    if user == "!exit" or user == "scissors" or user == "rock" or user== "paper":
        
        if user == "!exit":
            print("Bye!")
            break

        if jugadas[user] == pc:
            print(f"Well done. The computer chose {pc} and failed")

        elif jugadas[pc] == user:
            print(f"Sorry, but the computer chose {pc}")

        else:
            print(f"There is a draw ({pc})")

    else:
        print("Invalid input")
