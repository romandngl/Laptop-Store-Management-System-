from datetime import date
import random


def validating(read_items):
     # Get user name
    user_name = input("Enter your name: ")
    valid_number = True
    while valid_number == True:
        phone_number = input("Enter your phone number: ")
        # Get user phone number
        length = len(phone_number)
        # Check if the phone number is valid
        if length == 10 and phone_number[0] == "9" and phone_number.isdigit :
            valid_number = False
        else :
            print("----Invalid Phone Number----")
        

            
    laptops_by_user = []
    loop = True

    while loop == True:
        id_validation = True
        while id_validation == True:
            try:
                 # Get the ID of the laptop the user wants to sell
                user_id = int(input("Provide the ID of the laptop you want to sell: "))

                  # Check if the laptop ID is valid
                if user_id <= 0 or user_id > len(read_items):
                    print("----Provide a valid laptop ID----")
                    print('\n')
                else:
                    id_validation = False
            except:
                print("----Invalid Input----")


        quantity_validation = True
        while quantity_validation == True:
            try:
                # Get the number of laptops the user wants to sell
                user_quantity = int(input("Please Provide the number of the laptop you want to sell: "))
                 # Get the quantity of the selected laptop from the inventory
                get_quantity_of_selected_laptop = read_items[user_id][3]
                
                # Check if the quantity entered by the user is valid
                if user_quantity <= 0 or user_quantity > int(get_quantity_of_selected_laptop):
                    print("Dear Admin, the quantity you are looking is not available in our shop")
                    print('\n')
                else:
                    quantity_validation = False
            except:
                print("----Invalid Input----")


        # Update the quantity of the selected laptop in the inventory
        read_items[user_id][3] = int(read_items[user_id][3]) - int(user_quantity)

       # Write the updated inventory to the file
        file = open("items_list.txt", "w")

        for values in read_items.values():
            file.write((str(values[0])+","+str(values[1]) +","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5])))
        file.close()

        # Print the remaining quantity of the selected laptop
        print("Total number of ", read_items[user_id][0], " remaining to sell is: ",read_items[user_id][3])

    # Store the details of the sold laptop in the list
        selected_product = read_items[user_id][0]
        selected_quantity = user_quantity
        brand_name = read_items[user_id][1]
        unit_price = read_items[user_id][2]
        selected_item = read_items[user_id][2].replace("$",'')
        total_price = int(selected_item) * int(selected_quantity)

        laptops_by_user.append([selected_product, selected_quantity, unit_price, total_price,brand_name])

       # Ask the user if they want to sell more laptops
        user_req = input("Do you want to sell more(Y/N)?").upper()
        if user_req == "Y":
            loop = True
        else:
            total = 0
            shipping_cost = 500

            # Calculate the total price of all the sold laptops
            for i in laptops_by_user:
                total += int(i[3]) 
            grand_total = total + shipping_cost
            today_date = date.today()
            invoice_number = random.randint(1000, 9999)

           
           
            print("\n")
            print("==============================================================================================")
            print("                                   MODERN  Electronics                                        ")
            print("                                 Kamalpokhari,  Kathmandu                                     ")
            print("==============================================================================================")
            print("+--------------------------------------- BILL ---------------------------------------------+")
            print("|    Date: "+str(today_date)                                                                 )                                                         
            print("|    Invoice no.: "+str(invoice_number)                                                      ) 
            print("|    Customer Name : "+str(user_name)                                                        )
            print("|    Contact No : "+str(phone_number)                                                        )
            print("+--------------------------------------------------------------------------------------------+")
            print("Purchase details: ")
            print("--------------------------------------------------------------------------------------------------------------------")
            print("Item Name\t\t BRAND NAME \t\t  Total Quantity \t\tUnit Price \t\t  Total ")
            print("--------------------------------------------------------------------------------------------------------------------")
            for i in laptops_by_user:
                print(i[0],"\t",i[4],"\t\t  ",i[1],"\t\t\t\t",i[2],"\t\t  ","$",i[3])
            print("--------------------------------------------------------------------------------------------------------------------")
            print("Your Shipping Cost is: ",shipping_cost)
            print("Grand Total: $"+str(grand_total))
            print('Note: Shiping cost is also added to the grand total')
            print('--------------------------------------------------------------------------------------------------------------------')
            print("\n")



                           #--------------------INVOICE-----------------------#  

            file = open(str(user_name)+" "+str(today_date)+"-"+str(invoice_number)+".txt", "w")
            file.write("\n")
            file.write("==============================================================================================\n")
            file.write("                                   MODERN  Electronics                                        \n")
            file.write("                                 Kamalpokhari,  Kathmandu                                     \n")
            file.write("                             Phone.no :  9828238843, 9865743566                               \n")
            file.write("==============================================================================================\n")
            file.write("+--------------------------------------- BILL-----------------------------------------------+\n")
            file.write("|    Date: "+str(today_date)+                                                                "\n" )                                                         
            file.write("|    Invoice no.: "+str(invoice_number) +                                                    "\n" ) 
            file.write("|    Customer Name : "+str(user_name) +                                                      "\n" )
            file.write("|    Contact No. : "+str(phone_number) +                                                      "\n" )
            file.write("+--------------------------------------------------------------------------------------------+\n")
            file.write("\n")
            file.write("----------------------------------------------------------------------------------------------\n")
            file.write("Item Name\t\t  BRAND NAME \t\t  Total Quantity \t\tUnit Price \t\t  Total  \n")
            file.write("----------------------------------------------------------------------------------------------\n")
            for i in laptops_by_user:
                file.write(str(i[0])+"\t  "+str(i[4])+"\t\t  "+str(i[1])+"\t\t\t\t "+str(i[2])+"\t  "+"$"+str(i[3])+"\n")
            file.write("-----------------------------------------------------------------------------------------------\n") 
            file.write("Your shipping cost is: " +str(shipping_cost) +                                           "\n")
            file.write("Grand Total: $"+str(grand_total)+ "\n")
            file.write('Note: Shiping cost is also added to the grand total\n')
            file.write('-------------------------------------------------------------------------------------------------')
            file.write("\n")

            file.close()
            
            loop = False

                
                
                




