import random as rd;

def p_list():
    play_list: list[str] = ["Song: Wallenstein \ Author: d'Artagnan", \
                            "Song: Civilization \ Author: Dan Bull", \
                            "Song: Fields of Verdun \ Author: Sabaton "];

    flag: bool = True;
    while flag:
        choice: str = input("add a song to the beginning (type start) or the end (type fin) or exit? ");

        if choice == "fin" or choice == "start":
            song: str = input("input song name: ");
            aut: str = input("input singer or band name: ");

            song_aut: str = f"Song: {song} \ Author: {aut}";

            if choice == "fin":
                play_list.append(song_aut);
            else:
                play_list.insert(0,song_aut);

        else:
            print("exiting")
            flag = False;

    else:
        print(f"Length of the playlist = {len(play_list)}\n");
        for x in play_list:
            print(x);


def n_list():
    num_list: list[int] = [];
    for i in range(0, 10):
        num_list.append(rd.randint(1, 10000));

    for x in num_list:
        print(x);

def b_list():
    bool_list: list[bool] = [];
    for i in range(0, 10):
        bool_list.append(rd.choice([True, False]));


    for x in bool_list:
        print(x);


choice: int = int(input("song playlist (0), number list (1) or boolian list(2)? "));
p_list() if choice == 0 else n_list() if choice == 1 else b_list() if choice == 2 else print("Error");

