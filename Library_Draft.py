import sys
import membersnew
from datetime import datetime  # add date and time
import os  # operating system interaction
import csv  # to manipulate csv files

os.getcwd()  # for absolute path
""" Library class displays all items. Firstly it extracts all items from a txt file before 
    converting to a dictionary and  assigning an ID. The additional methods allow the user to
     view, borrow and return items"""
""" Code will only compile from the membersnew.py file it won't compile from the Library_Draft.py file. AttributeError: 
     (most likely due to a circular import) I cannot find the solution or cause"""

class Library(object):

    def __init__(self, list_of_items,
                 library_name):  # init method first method to be invoked when object created. Initializer
        self.list_of_items = "items.txt"
        self.library_name = library_name
        self.items_dict = {}
        itemid = 1
        # Open items.txt file with dictionary and assign ID to each new line/item
        with open(self.list_of_items) as i:
            content = i.readlines()
        for line in content:
            self.items_dict.update({str(itemid): {'item_title': line.replace("\n", ""), '': ''}})
            itemid += 1

    # Method  Display items from generated dictionary with assigned ID
    def availableitems(self):
        print("List of Available Items")
        print("=======================")
        for key, value in self.items_dict.items():  # key is itemid value is item information formatted for csv file
            print(key, "\t", value.get("item_title"))
    # Method  Borrow Item. Create or add chosen item to csv file include member ID, name and item details, date if issue is also generated
    def Borrow(self):
        now = datetime.now()
        InputDate = now.strftime("Date of Issue" + " " + "%d-%m-%y")
        file = open("lend.csv", "a", newline="")
        lend = csv.writer(file)
        borrower_id = input("Member ID : ")
        borrower_name = input("Name : ")
        item_name = input("Item Name : ")
        lend.writerow([borrower_id, borrower_name, item_name, InputDate])
        file.close()
        print("\nItem is Issued")
    # Method Return Item. Check to see if item is in lend.csv file and append to returned csv.file. Also allows for lower case input
    # for loop is appending the whole lend.csv file to the return.csv instead of the input value, could not fix.
    def Return(self):
        now = datetime.now()
        InputDate = now.strftime("Date of Return" + " " + "%d-%m-%y")
        file = open("lend.csv", "r")
        file = csv.reader(file)
        borrower_id = input("Member Number :")
        item_name = input("Item Name :")
        for row in file:
            if row[0] == "ID":
                file = open("return.csv", "a")
                Return = csv.writer(file)
                Return.writerow(row)
                file.close()
            else:
                file = open("return.csv", "a")
                Return = csv.writer(file)
                Return.writerow(row)
                if row[0] == borrower_id and row[1].lower() == item_name.lower():
                    pass
                else:
                    file.close()
            print("Item is Returned")



def main():
    #instance of library Class
    library = Library("items.txt", "Python Library")
    #Methods called from members.py file
    memnew = membersnew.Membersnew(membersnew)
    done = False
    while not done:
        print("""======Menu=======
1. Join Library
2. List of Members
3. Display Available Items
4. Borrow Item
5. Return Item
6. Loan History
7. Exit
""")    #Methods called as per menu
        choice = int(input("Enter Choice:"))
        if choice == 3:
            library.availableitems()
        elif choice == 4:
            library.Borrow()
        elif choice == 5:
            library.Return()
        elif choice == 1:
            membersnew.addUserDetail()
        elif choice == 2:
            membersnew.Membersnew.memberslist(memnew)
        elif choice == 6:
            membersnew.loanhistory()
        elif choice == 7:


            sys.exit()


main()
