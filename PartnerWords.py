import random

def devam():
    user = input("devam? ")
    if user.lower() == "yes":
        return True
    elif user.lower() == "no":
        print("GoodBye")
    else:
        print("wrong input. yes or no")
        devam()



def func():
    words = []
    cntr = 0
    with open("PartnerWords.txt" , encoding='UTF-8') as file:
        for line in file:
            words.append(line)
            cntr += 1
    num = random.randint(0, cntr-1)
    print(words[num].split()[0])
    user= input("cevap? ")
    if user.lower() == words[num].split()[1]:
        print("aferin")
    else:
        print(words[num].split()[1])
        print("yanlış")

while True:
    func()
    userReturn = devam()
    if userReturn == True:
        func()
    else:
        break


