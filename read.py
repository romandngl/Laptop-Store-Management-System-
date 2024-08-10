def items_dictionary():
    # Open the file containing the laptop items
    laptop_file = open("items_list.txt", "r")
    # Create an empty dictionary to store the item information
    item_dictionary = {}
    items_id = 1

    # Iterate over each line in the file
    for line in laptop_file:
        line = line.replace("/n","")  # Remove the newline character
        item_dictionary.update({items_id: line.split(",")})  
        items_id = items_id + 1
    laptop_file.close()
    return item_dictionary
