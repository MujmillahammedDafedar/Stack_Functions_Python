def push(val):
    list.append(val)
    print("Element has been pushed")
    print(list)
    return


def pull(val):
    list.remove(val)
    print("Element has been pulled")
    print(list)
    return


def all():
    for i in range:
        print("The stack contains following elements: ")
        print(list)
        return


if __name__ == '__main__':
    i = 0
    list = []

    print("1.PUSH")
    print("2.PULL")
    print("3.DISPLAY")
print("4.EXIT")
choice = int(input("ENTER YOUR CHOICE"))
if choice == 1:
    val = int(input("Enter pushing element: "))
    push(val)
elif choice == 2:
    pull()
elif choice == 3:
    all()
else:
    exit()
