str = input("Введите произвольную строку: ")
print("Строка без 3 символа: ")
c = 0
for i, char in enumerate(str):
    if (i + 1) == 3:
        continue
    if char == "c":
        c = 1
    if i != len(str) - 1:
        print(char, end="")
if c == 1:
    print("\nВ строке присутствует символ 'c' ")
print("\nДлина строки:", len(str))
print("\nСтрока без последнего символа:", str[:-1])
