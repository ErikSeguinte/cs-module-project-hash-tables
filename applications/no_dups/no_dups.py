def no_dups(s):
    # Your code here
    word_set = set()
    words = s.strip().split()

    return_string = ""

    for word in words:
        if word not in word_set:
            word_set.add(word)
            return_string += f" {word}"

    return return_string.strip()
    



if __name__ == "__main__":
    print(no_dups(""))
    print(no_dups("hello"))
    print(no_dups("hello hello"))
    print(no_dups("cats dogs fish cats dogs"))
    print(no_dups("spam spam spam eggs spam sausage spam spam and spam"))