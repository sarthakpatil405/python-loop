# Python Loop Program

print("FOR LOOP (1 to 10)")
for i in range(1, 11):
    print(i)

print("\nWHILE LOOP (1 to 10)")
i = 1
while i <= 10:
    print(i)
    i += 1

print("\nSTAR PATTERN")
for i in range(1, 6):
    for j in range(i):
        print("*", end="")
    print()

print("\nSUM OF NUMBERS 1 to 10")
total = 0
for i in range(1, 11):
    total += i
print("Sum =", total)
