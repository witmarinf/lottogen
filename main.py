#import random
from faker import Faker

def generateLotto(quantity, topLimit):
   selected = []
   fake = Faker()
   i = 0
   while i < quantity:
        numb = fake.random.randint(1,topLimit)
        #liczba = random.randint(1, topLimit)
        if selected.count(numb) == 0:
            selected.append(numb)
            i = i + 1
   return sorted(selected)

def writeToFile(quantity, topLimit):
    with open('plik.txt','w') as file:
        for _ in range(1,101):
            file.write(','.join(str(elem) for elem in generateLotto(quantity,topLimit)) + '\n')

        file.close()

if __name__ == '__main__':
    #quantity = int(input("Podaj ilość typowanych liczb: "))
    #topLimit = int(input("Podaj maksymalną losowaną liczbę: "))
    #writeToFile(quantity, topLimit)
     writeToFile(6, 49)
