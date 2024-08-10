
def title():
    print("\n\t\t\t\t\tWelcome to Our Shop's Items list")
    print("\t\t\t\t\t-----------------------------------")
    print("\t\t\t\t  These are the available items in our shop\n ")
    print("----------------------------------------------------------------------------------------------------------------------------")
    print("   Item No.       Name               Brand          Price(dollars)   \t  Quantity         Processor   \t    Graphics Card   ")
    print("--------------------------------------------------------------------------------------------------------------------------")


def items():
    # Open the file containing the item list
    file = open("items_list.txt","r")
    item_id = 1

    for line in file:
        # Display each item with its details
        print("    ", item_id,"\t\t"+line.replace(",", "       " ))
        item_id = item_id + 1
        print("---------------------------------------------------------------------------------------------------------------------------")
    # Close the file
        file.close
    print('\n')


def item_table():
    # Display the item table
    title()
    items()


