import random as rd;


def get_word():
    my_word: str = "";
    w_len: int = rd.randint(5, 20);
    for i in range (0, w_len):
        my_word += rd.choice(["a","b","c"]);

    return my_word;

w_list: list[str] = [];
list_len: int = rd.randint(10,20);

for i in range (0, list_len):
    w_list.append(get_word());

for word in w_list:
    print(word);