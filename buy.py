from datetime import date
import random



def validating(read_items):
    # Get user details
    user_name = input("Enter the name of the distributor: ")
    valid_number = True
    while valid_number == True:
        phone_number = input("Enter phone number: ")
        length = len(phone_number)
        if length == 10 and phone_number[0] == "9" and phone_number.isdigit :
            valid_number = False
        else :
            print("----Invalid Phone Number----")
        

            
    laptops_by_user = []
    loop = True

    while loop == True:
        # Get laptop ID from the user
        id_validation = True
        while id_validation == True:
            try:
                user_id = int(input("Provide the ID of the laptop you want buy: "))
                if user_id <= 0 or user_id > len(read_items):
                    print("Please provide a valid laptop ID!")
                    print('\n')
                else:
                    id_validation = False
            except:
                print("----Invalid Input----")

       # Get the quantity of laptops from the user
        quantity_validation = True
        while quantity_validation == True:
            try:
                user_quantity = int(input("Provide the number of the laptop you want buy: "))
                if user_quantity <= 0 :
                    print("Dear Admin, the qunatity you are looking is not available in our shop")
                    print('\n')
                else:
                    quantity_validation = False
            except:
                print("----Invalid Input----")


        # Update the quantity of the selected laptop in the item list
        read_items[user_id][3] = int(read_items[user_id][3]) + int(user_quantity)

        file = open("items_list.txt", "w")

        for values in read_items.values():
            file.write((str(values[0])+","+str(values[1]) +","+str(values[2])+","+str(values[3])+","+str(values[4])+","+str(values[5])))
        file.close()
        print("Updated number of ", read_items[user_id][0], " is: ",read_items[user_id][3])

        # Add the selected laptop details to the purchase list
        selected_product = read_items[user_id][0]
        selected_quantity = user_quantity
        brand_name = read_items[user_id][1]
        unit_price = read_items[user_id][2]
        selected_item = read_items[user_id][2].replace("$",'')
        total_price = int(selected_item) * int(selected_quantity)

        laptops_by_user.append([selected_product, selected_quantity, unit_price, total_price,brand_name])

        user_req = input("Do you want to buy more(Y/N)?").upper()
        if user_req == "Y":
            loop = True
        else:
            # Calculate the total and grand total
            total = 0

            for i in laptops_by_user:
                total += int(i[3]) 
            vat_amount = total * 0.13
            grand_total = total + vat_amount
            today_date = date.today()
            invoice_number = random.randint(1000, 9999)
            
            # Print the invoice details
            print("\n")
            print("==============================================================================================")
            print("                                     "+str(user_name)                                               )
            print("                                    Kathamndu,Nepal                                             ")
            print("                             Phone.no :  9828238843, 9865743566                               ")
            print("==============================================================================================")
            print("+--------------------------------------- INVOICE --------------------------------------------+")
            print("|    Date: "+str(today_date)                                                                 )                                                         
            print("|    Invoice no.: "+str(invoice_number)                                                      ) 
            print("|    Customer name : Roman"                                                                   )
            print("|    Contact no. : " +str(phone_number)                                                       )
            print("+--------------------------------------------------------------------------------------------+")
            print("\n")
            print("Purchase Details are:             ")
            print("--------------------------------------------------------------------------------------------------------------------")
            print("Item Name\t\t BRAND NAME \t\t  Total Quantity \t\tUnit Price \t\t  Total ")
            print("--------------------------------------------------------------------------------------------------------------------")
            for i in laptops_by_user:
                print(i[0],"\t",i[4],"\t\t  ",i[1],"\t\t\t\t",i[2],"\t\t  ","$",i[3])
            print("--------------------------------------------------------------------------------------------------------------------")
            print("Vat amount: $"+str(vat_amount))
            print("Grand Total: $"+str(grand_total))
            print('Note: Shiping cost is also added to the grand total')
            print('--------------------------------------------------------------------------------------------------------------------')
            print("\n")


            #--------------------INVOICE-----------------------#
            file = open(str(user_name)+" "+str(today_date)+"-"+str(invoice_number)+".txt", "w")
            file.write("\n")
            file.write("==============================================================================================\n")
            file.write("                                 " + str(user_name) +                                            "\n")
            file.write("                                Kathmandu, Nepal                                                  \n") 
            file.write("                             Phone.no :  9828238843, 9865743566                              \n")
            file.write("==============================================================================================\n")
            file.write("+--------------------------------------- INVOICE --------------------------------------------+\n")
            file.write("|    Date: "+str(today_date)+                                                                "\n" )                                                         
            file.write("|    Invoice no.: "+str(invoice_number) +                                                    "\n" ) 
            file.write("|    Customer name : Roman"                                                                  "\n" )
            file.write("|    Contact no. : "+str(phone_number) +                                                      "\n" )
            file.write("+--------------------------------------------------------------------------------------------+\n")
            file.write("\n")
            file.write("Purchase Details are:             \n")
            file.write("----------------------------------------------------------------------------------------------\n")
            file.write("Item Name\t\t  BRAND NAME \t\t  Total Quantity \t\tUnit Price \t\t  Total  \n")
            file.write("----------------------------------------------------------------------------------------------\n")
            for i in laptops_by_user:
                file.write(str(i[0])+"\t  "+str(i[4])+"\t\t  "+str(i[1])+"\t\t\t\t "+str(i[2])+"\t  "+"$"+str(i[3])+"\n")
            file.write("-----------------------------------------------------------------------------------------------\n") 
            file.write("Your Vat amount is: " +str(vat_amount) +                                           "\n")
            file.write("Grand Total: $"+str(grand_total)+ "\n")
            file.write('Note: Vat amount is added to the grand total\n')
            file.write('-------------------------------------------------------------------------------------------------')
            file.write("\n")

            file.close()
            
            loop = False

                
                
                




