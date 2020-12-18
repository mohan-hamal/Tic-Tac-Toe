cells = input("Enter cells: ")
print("---------")
for i in range(9):
    if i % 3 == 0:
        print("| ", end="")
    print(cells[i], "", end="")
    if (i + 1) % 3 == 0:
        print("|")
print("---------")
if 