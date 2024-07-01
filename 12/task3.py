def lst_index(lst, index):
    try:
        element = lst[index]
        print(f"Элимент с индексом {index}: {element}")
    except IndexError:
        print(f"Индекс: {index} выходит за границу массива")

my_lst = [1,2,3,4,5,6]

lst_index(my_lst, 4)

lst_index(my_lst, 10)
