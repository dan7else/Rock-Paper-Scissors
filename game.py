import random

choices = ["камень", "ножницы", "бумага"]
print("Ку, сыграем?")
print("камень, ножницы, бумага")

user = input("Твой выбор: ").lower()

if user not in choices:
    print("Ты что то не то ввел, игра окончена")
else:
    computer = random.choice(choices)
    print(f"Компьютер выбрал: {computer} ")

    if user == computer:
        print("Победила, дружбаа")
        
    elif (user == "камень" and computer == "ножницы")or \
         (user == "ножницы" and computer =="бумага")or \
         (user == "бумага" and computer == "камень"):
         print("Ты выиграл блин")
    else:
        print("Проиграл, попробуй еще раз!")

