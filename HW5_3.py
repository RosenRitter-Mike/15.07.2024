def num_triangle():
    num: int = int(input("input your number: "));

    for i in range(0, num+1):
        for j in range(1, i+1):
            print(j, end="");

        print();

    for k in range(num-1, 0, -1):
        for s in range(1, k+1):
            print(s, end="");

        print();

def star_pyra():
    rows: int = 0;
    while not rows%2:
        rows = int(input("number of rows: "));
    else:
        k: int = 0;

        for i in range(1, rows + 1):
            for space in range (1,rows - i + 1):
                print(end=" ");
            while k != 2*i - 1:
                print("*", end="");
                k+=1;

            k = 0;
            print();



choice: int = int(input("number triangle (1) or star pyramid(2)? "));
num_triangle() if choice == 1 else star_pyra() if choice == 2 else print("Error");