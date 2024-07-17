import random as rd

while True:
    tries: int = 0;
    num: int = rd.randint(1, 100);

    while True:
        guess: int = int(input("guess the number: "))
        if guess == 99999:
            break;

        tries += 1;
        if guess > num:
            print("your number is too big");
        elif guess < num:
            print("your number is too small");
        else:
            print("BINGO!");
            print(f"you have made {tries} tries");
            print("have you heard of binary search") if tries > 7 else print("AWESOME!");
            break
    if guess == 99999:
        break;

    game: str = input("do you want to play another game? Yes/No ");

    if game.lower() == "yes":
        tries = 0;
        continue;
    else:
        break;


