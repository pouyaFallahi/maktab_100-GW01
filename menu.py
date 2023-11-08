import os

os.system("cls")


class Item:
    def __init__(self, name, action, *args):
        self.name = name
        self.action = action
        self.args = args

    def execute(self):
        if self.args:
            self.action(*self.args)
        else:
            self.action()


class Menu:
    def __init__(self, name, parent=None):
        self.name = name
        self.items = []
        self.parent = parent

    def add_item(self, item):
        if isinstance(item, Item):
            self.items.append(item)
        elif isinstance(item, Menu):
            self.items.append(item)

    def display(self):
        print(f"{self.name} Menu:")
        for index, item in enumerate(self.items):
            print(f"{index + 1}: {item.name}")
        if self.parent:
            print("0: Back\n")
        else:
            print("0: Exit\n")

    def execute(self):
        try:
            choice = int(input(">>> "))

        except:
            choice = -1

        if choice == 0:
            if self.parent:
                os.system("cls")
                self.parent.display()
                self.parent.execute()
            else:
                print(">>> bye bye ;*")
        elif 1 <= choice <= len(self.items):
            item = self.items[choice - 1]
            if isinstance(item, Item):
                os.system("cls")
                item.execute()
                print()
                self.display()
                self.execute()

            elif isinstance(item, Menu):
                os.system("cls")
                item.display()
                item.execute()
                print()
        else:
            os.system("cls")
            print("Invalid input..\n")
            self.display()
            self.execute()


# def test():
#     print('test')
#
#
# # --- Tests ---
# menu = Menu("Main")
#
# item1 = Item("bimar", test)
# item2 = Item("doctor", print, 4, 5, 6)
#
# menu.add_item(item1)
# menu.add_item(item2)
#
# another_menu = Menu("Another", menu)
# item3 = Item("print3", print, "hi ^^")  # mishe argument pass dad ya nadad
# another_menu.add_item(item3)
#
# menu.add_item(another_menu)
#
# menu.display()
# menu.execute()
#













