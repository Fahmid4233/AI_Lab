lst = []
n = int(input("Enter list length: "))
for i in range(n):
    x = input("Enter list elements: ")
    if x.isdigit():
        x = int(x)
        lst.append(x)
    else:
        lst.append(x)
print(lst)

lst1 = ["Bangladesh", "India", "Pakistan", "USA", "UK"]
lst2 = [10, 14, 2, 3, 9, 27, 33]
lst3 = ['a', 'c', 'n', 'f', 'h', 'b']
lst1.pop()
print(lst1)
list1 = lst2.copy()
print(list1)
print(lst1+lst2+lst3)
lst2.sort()
print(lst2)