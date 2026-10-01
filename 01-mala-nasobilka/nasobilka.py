
def radek():
    for i in range(11):
        print("+-----", end="")
    print("+")

radek()

print("|     |", end="")
for d in range(1, 11):
    print(" %3i |" % d, end="")
print()

radek()

for i in range(1, 11):
    print("| %3i " % i, end="")

    for j in range (1, 11):
        print("| %3i " % (j*i), end="")
    print("|")

    radek()