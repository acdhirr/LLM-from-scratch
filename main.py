# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+8 to toggle the breakpoint.

    ar0 = [1,5,3,7,8,2,4,3,7,9,6,0]
    ar0.sort()
    print(ar0)
    ar1 = set(ar0)
    print(ar1)

    ar3 = [el for el in ar1 if el%2 == 0]
    print(ar3)

    for x,y,z in zip(range(0,14),range(13,24),range(100,115)):
        print(x,y,z)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
