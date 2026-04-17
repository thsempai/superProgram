number = int(input("Entrez un nombre entre 1 et 100: "))

while number < 1 or number > 100:
    number = int(input("Entrez un nombre entre 1 et 100: "))

# total = sum(range(number+1))

total = 0
for n in range(number+1):
    total = total + n

print(total)
