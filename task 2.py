def revword(word:str) -> str:
    return word[::-1].lower()


def countword()->int:
    count = 0
    my_file = open("text.txt")
    for line in my_file :
        if count == 0 :
            word = line.strip().lower()
            count += 1            
        else :
            line = line.strip().split(" ")
            for text in line :
                if revword(text) == word :
                    count += 1
    return count

countword()
