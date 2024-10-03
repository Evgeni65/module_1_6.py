# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
my_dict = {"Евгений": 2000,"Николай": 2010,"Павел":2020}
print(my_dict)
print(my_dict["Евгений"])
my_dict ["Петр"] = 2018
print(my_dict["Петр"])
my_dict.update({"Антон":2005,"Сергей":2015})
print(my_dict)
a = my_dict.pop("Николай")
print(my_dict)
print(a)
my_set = {1,2,3,'apple',3,2}
print(my_set)
my_set = {1,2,3,'apple',3,2,True,(1,2,3)}
print(my_set)
print(my_set.discard(1))
print(my_set)