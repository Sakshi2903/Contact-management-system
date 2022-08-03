global data, main_data

filename = "contact_data.csv"


f = open(filename, 'r')

main_data = f.read()

main_data = main_data.split('\n')

main_data = (list(filter(None, main_data)))


class contact_system():

    def __init__(self, user_id=0, name='', email='', gender='', moile_no=0, age=0, address=''):

        self.user_id = user_id

        self.name = name

        self.email = email

        self.gender = gender

        self.moile_no = moile_no

        self.age = age

        self.address = address

    def write_file(self, list_data):

        f = open(filename, "w")

        all_data = str()

        for data in list_data:

            all_data += data+'\n'

        f.write(all_data)

        f.close()

        return True

    def show_contact(self):
        with open('contact_data.csv') as f:
            while True:
                line = f.readline()
                if not line:
                    break
                print(line)

    def add_contact(self):

        user_id = input("Creat User ID :")

        name = input("Enter Name :")

        email = input("Enter Email :")

        gender = input("Enter Gender :")

        moile_no = input("Enter Mobile_no :")

        age = input("Enter Age :")

        address = input("Enter Address :")

        data = user_id+','+name+','+email+','+gender + \
            ','+moile_no+','+age+','+address+'\n'

        f = open(filename, "a")

        f.write(data)

        f.close()

        print("Contact Added Succeffully")

    def edit_contact(self, no):

        print("User ID :", no)

        name = input("Enter Name :")

        email = input("Enter Email :")

        gender = input("Enter Gender :")

        moile_no = input("Enter Mobile_no :")

        age = input("Enter Age :")

        address = input("Enter Address :")

        new_value = no+','+name+','+email+','+gender+','+moile_no+','+age+','+address

        for data in main_data:

            split_data = data.split(',')

            if no == split_data[0]:

                main_data[main_data.index(data)] = new_value

                self.write_file(main_data)

                print("Successfully Updated")

                return True

        print("Try Again!!")

    def remove_contact(self, no):

        for data in main_data:

            split_data = data.split(',')

            if no == split_data[0]:

                main_data.remove(data)

                break

        if (self.write_file(main_data)):

            print("Successfully Deleted !")

        else:

            print("Try Again!! ")

    def search_id(self, no):

        for data in main_data:

            split_data = data.split(',')

            if no == split_data[0]:

                return True

        return False


class main():

    def __init__(self):

        self

    def menu():

        my_class = contact_system()

        print('\n'""" >>>>>>>>>>> Welcome To Contact Management System <<<<<<<<<<<<

			1.=Contact List

			2.=Add Contact

			3.=Edit Contact

			4.=Remove Contact

			5.=Exit

			""")

        try:

            user_input = int(input("Please Enter option from above (1-5) : "))

        except ValueError:

            print("That is not true.")

        finally:

            print("")

        if user_input == 1:

            my_class.show_contact()

        elif user_input == 2:

            my_class.add_contact()

        elif user_input == 3:

            num = input("Enter User ID for edit :")

            if my_class.search_id(num):

                my_class.edit_contact(num)

            else:

                print("Incorrect User ID!!")

        elif user_input == 4:

            num1 = input("Enter User ID for delete :")

            if my_class.search_id(num1):

                my_class.remove_contact(num1)

            else:

                print("Incorrect User ID!!")

        elif user_input == 5:

            print("Thankyou for Using Our Contact Management System")

            quit()

        else:

            print("Invalid Input!!")

    menu()
