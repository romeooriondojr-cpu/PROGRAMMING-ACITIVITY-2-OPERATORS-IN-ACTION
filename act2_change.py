# Name: Oriondo Jr. Romeo B.
# Section: BMET - 2101
# Task 1 - Change Calculator

amount = int(input("Enter amount in pesos: "))

pesos100 = amount // 100
amount = amount % 100

pesos20 = amount // 20
amount = amount % 20

pesos5 = amount // 5
amount = amount % 5

pesos1 = amount // 1

print("100 pesos:", pesos100)
print("20 pesos:", pesos20)
print("5 pesos:", pesos5)
print("1 peso:", pesos1)