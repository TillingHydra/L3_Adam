def separer(list1, listn=None, listnul=None, listp=None) -> list:
    if listn is None:
        listn = []
    if listnul is None:
        listnul = []
    if listp is None:
        listp = []

    for i in list1:
        if i > 0:
            listp.append(i)
        elif i < 0:
            listn.append(i)
        else:
            listnul.append(i)

    result = listn + listnul + listp
    return result

print(separer([-6, 1, 3, 0, -4]))

            


        




     