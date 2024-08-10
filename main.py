import display
import sale
import buy
import read


# Function to display the welcome message
def welcome():
    print("===============================================================================================")
    print("                                   MODERN  Electronics                                          ")
    print("                                 Kamalpokhari,  Kathmandu                                       ")
    print("                             Phone.no :  9860000000, 9890000909                                      ")
    print("===============================================================================================")
    
    print("WELCOME  ADMIN :)    ")
    print("\n")
    
# Call the welcome function
welcome()

# Function to display the home menu
def home():
    loop = True
    while loop == True:
        try:

            while loop == True:
                print("~~~~~~~~~~~~~~~~~~~~~~~~")
                print(" Press  1  for  selling ")
                print(" Press  2  for  buying  ")
                print(" Press  3  to  exit     ")
                print("~~~~~~~~~~~~~~~~~~~~~~~~")
            
                user_input = int(input("Enter the option: "))
                read_items = read.items_dictionary()
                
                print("\n")

                if user_input == 1:
                    display.item_table()
                    sale.validating(read_items)
                    print("\t\tTHANK YOU FOR SELLING :)\n")
                elif user_input == 2:
                    display.item_table()
                    buy.validating(read_items)
                    print("\t\tTHANK YOU FOR BUYING :)")
                elif user_input == 3:
                    print("\t\tTHANK YOU. HAVE A NICE DAY :)")
                    loop = False
                else:
                    print("\t\tPlease enter a valid option :( ")
            
        except:
            print("\n")
            print("\t\tERROR::Please enter a valid option :( ")

# Call the home function    
home()
            





