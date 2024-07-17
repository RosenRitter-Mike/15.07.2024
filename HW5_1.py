zero: int = None
pos: int = None
neg: int = None
sev: int = None

for i in range(1, 11):
    num: int = int(input("Input an integer number (positive or negative): "))

    if num == -9999:
        break

    if num > 1000 or num <-1000:
        continue

    if num > 0:
        if pos == None:
            pos = 0
        pos += 1
    elif num < 0:
        if neg == None:
            neg = 0
        neg += 1
    else:
        if zero == None:
            zero = 0
        zero += 1

    if not num%7:
        if sev == None:
            sev = 0
        sev += 1

else:
    print(f"Numbers received:\nPositive: {pos}\nNegative: {neg}\nZeroes: {zero}\nDivisible by 7: {sev} ")