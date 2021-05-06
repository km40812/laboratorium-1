firstNumber = int(input("podaj dolny zakres: "))
secondNumber = int(input("podaj górny zakres: "))
sum = 0
howManyTimes = 0
for i in range(firstNumber, secondNumber + 1):
    if i % 2 != 0 and i>0:
        sum = sum + i
        howManyTimes += 1
    else:
        continue

print(sum/howManyTimes)