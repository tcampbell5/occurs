def split(word):
    return[char for char in word]
def occurs():
    string = " "
    words = ""
    while True:
        string = str(input("Insert a word: "))
        string = str.lower(string)
        if string == "":
            break
        list1 = split(string)
        first_let = list1[0]
        list1.pop(0)
        if first_let in list1:
            words += string
        else:
            words = words
    return(words)
