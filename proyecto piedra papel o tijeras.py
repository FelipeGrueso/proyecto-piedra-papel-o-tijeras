import random
posibilidades = ["scissors", "rock", "paper"]
user = input()
pc = random.choice(posibilidades)
jugadas =  {"scissors":"paper", "rock":"scissors" , "paper":"rock"}

if jugadas[user] == pc:
    print(f"Well done. The computer chose {pc} and failed")

elif jugadas[pc] == user:
    print(f"Sorry, but the computer chose {pc}")

else:
    print(f"There is a draw ({pc})")
