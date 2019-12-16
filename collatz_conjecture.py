# --- Collatz's Conjecture --- #
x = int(input("Pick a number!: "))
counter = 0

while (x > 0):
    if x == 1:
        break
    # --- Checks for EVEN number --- #
    elif (x % 2) == 0:
        x = int(x / 2)
        print(x)
        counter += 1
    # --- Otherwise ODD --- #
    else:
        x = int((3 * x) + 1)
        print(x)
        counter += 1
        continue
# --- Steps taken to get to 1 --- #
print("steps = {}".format(counter))