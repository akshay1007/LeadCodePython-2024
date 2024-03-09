if __name__ == '__main__':
    li = ["eat", "sleep", "repeat"]
    sl = "Lets learn DSA"

    obj1 = enumerate(li)
    obj2 = enumerate(sl)
    print('Print return type of obj1 ', type(obj1))
    print('Convert into enumerator ', list(obj1))
    print('Convert into enumerator ', list(obj2))

    for index, ele in enumerate(li):
        print(index, '  -  ', ele)

    for index, ele in enumerate(sl):
        print(index, '  -  ', ele)

    print('Print element tuples directly')
    for ele in enumerate(li):
        print(ele)

    print('Changing index and print ')

    for ele in enumerate(li,100):
        print(ele)

