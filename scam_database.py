data_customer = []


while True:

    print("--- Hi this is your Akotech Bank Assistant ---")
    print("Enter your choice : ")
    print("1. Enter Customer Data")
    print("2. Print Database")
    print("3. Exit")
    selection = int(input("Enter your choice : "))

    if selection == 1:
        name = input("Enter your name: ")
        age = input("Enter your age: ")
        bank_account = input("Enter your bank account: ")
        password = input("Enter your password: ")

        print("Thank you for your data, you are scammed")
        data = [name, age, bank_account, password]
        data_customer.append(data)

    elif selection == 2:
        print("+------------------+-----+--------------+----------+")
        print("|          name    | age | bank account | password |")
        print("+------------------+-----+--------------+----------+")
        for x in data_customer:
            print("| ",x[0],"\t| ", x[1],"\t| ", x[2],"\t| ", x[3],"\t|")

    elif selection == 3:
        break



