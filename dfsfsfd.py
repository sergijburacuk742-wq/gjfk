a = [44, 60, 13, 7, 2, 6, 563, 95, 5, 22, "диня", "кавун", "лимон", "вишня", "саванна", "хліб", "ручка", "Блок", "насіння", "гуава"]
int_list = [i for i in a if isinstance(i, int)]
str_list = [i for i in a if isinstance(i, str)]



int_list.sort()

str_list.sort()

b = int_list + str_list
c = [i for i in int_list if i % 2 == 0]
cups = [i.upper() for i in str_list]



print("Головний список:", a)
print("Відсортований список (int по зростанню, str а-я):", b)
print("Числа кратні 2:", c)
print("Список з капсом:", cups)