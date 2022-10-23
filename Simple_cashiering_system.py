
print("\n\n*****WELCOME TO SIMPLE CASHIERING SYSTEM*****\n")
print("*****Jesusa' s Clothes Shop*****")
print("1. White T-Shirt with Happy Face Design ===> 250",
      "\n2. BasketBall jersey Black  ====> 350",
      "\n3. Sunflower Dress  ====> 500",
      "\n4. Black Tuxedo ====> 1200",
      "\n5. Payment",
      "\n6. Quit")

dec_loop = True
total_price = int(0)
repeat_pay = True

while (dec_loop):
    choice = int(input("Enter your choice of order: "))

    if choice == 1:
        q_choice = int(input("Enter number of Quantity: "))
        total = 250 * q_choice
        total_price += total

    elif choice == 2:
        q_choice = int(input("Enter number of Quantity: "))
        total = 350 * q_choice
        total_price += total

    elif choice == 3:
        q_choice = int(input("Enter number of Quantity: "))
        total = 500 * q_choice
        total_price += total

    elif choice ==4:
        q_choice = int(input("Enter number of Quantity: "))
        total = 1200 * q_choice
        total_price += total

    elif choice == 5:
        while (repeat_pay):
            print("Total Price is ", total_price)
            pay = int(input("Please enter how much money to pay: "))
            if total_price > pay:
                print("Error: Insufficient Fund. Please pay at exact amount or more. Thank you!")
                repeat_pay = True

            else:
                change = pay - total_price;
                print("Your change is ", change)
                print("Thank you for using Jesusa Clothes Shop.")
                repeat_pay = False
                dec_loop = False


    elif choice == 6:
        print("Thank you for using Jesusa Clothes Shop.")
        dec_loop = False

    else:
        print("Error. Please Enter a correct choices. ")
