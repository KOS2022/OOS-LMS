import csv
import os
import Library_Draft
"""The Membersnew class displays all members. It extracts all members from a txt file 
    converts values to a dictionary and  assigning an ID. It also displays all members.
    there are two additional functions within the file one to add new members 
    and one to look up loan history """


class Membersnew():

    def __init__(self, members_new):
        self._members_new = "members.csv"
        self.members_dict = {}
        itemid = 1
        with open(self._members_new) as i:
            content = i.readlines()
        for line in content:
            self.members_dict.update({str(itemid): {'member_details': line.replace("\n", "")}})
            itemid += 1

    def memberslist(self):
        print("List of members")
        for key, value in self.members_dict.items():
            print(key, "\t", value.get("member_details"))

    # Generate user details from input
def addUserDetail():
    firstname = input("Please enter first name: ")
    lastname = input("Please enter lastname: ")
    email = input("Please enter email: ")
    phone = input("Please enter phone number: ")
    # create and write to csv file if it does not exist
    if not os.path.exists('members.csv'):
        with open('members.csv', 'w'):
            pass
    # when file does exist format for csv.
    with open('members.csv', 'r+') as file:
        user_id = len(file.readlines())
        writer = csv.writer(file)
        writer.writerow([user_id, firstname, lastname, email, phone])
    # file.close()
    # show member created return to menu or quit programme
    while True:
        print("New Member Created")

        option = int(input("Press 1 to return to main menu: \n Press 2 to Quit: "))
        if option == 1:
            Library_Draft.main()
        elif option == 2:
            print("Quit Programme")
            exit(2)

    # get loan history
def loanhistory():

    id = input('Enter Member ID')
    # remove characters, return list of elements in the string
    lines = [line.strip('\n\r').split(',') for line in open("lend.csv")]
    # from the list return values after input
    print('\t'.join(lines[0]))
    for line in lines[1:]:
        if line[0] == id:
            print('\t'.join(line))


