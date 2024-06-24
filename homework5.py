immutable_var = (2, 1.5, "Hello", True)
print(immutable_var)
# кортежи в python относятся к неизменяемым типам данных. Это необходимо чтобы нельзя было изменить или добавить и удалить элементы
mutable_list = [2, 1.5, "Hello", True]
print(mutable_list)
mutable_list[0] = 3
print(mutable_list)
mutable_list[1] = 2.5
print(mutable_list)
mutable_list[2] = "Bye"
print(mutable_list)
mutable_list[3] = False
print(mutable_list)


