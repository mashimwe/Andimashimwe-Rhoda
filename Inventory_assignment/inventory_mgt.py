raw_materials = {
    "BUTTER": {
        "quantity": 40,
        "quality": "High"
    },
    
    "FLOUR": {
        "quantity": 20,
        "quality": "Medium"        
    },
    
    "BAKING POWDER": {
       "quantity": 20,
       "quality": "Medium"  
    }
}

finished = {
    "CAKES": {
        "amount": 20,
    },
    
    "BISCUITS": {
        "amount": 12,
    }
    
}


        
#updating stock items      
def update_stock():
    while True:
        print("Which Category are you updating? (Raw / Finished / Quit)")
        choice = input().lower()
        
        if choice == "raw":
            print("What raw material are you updating?")
            stock_item = input().upper()
            print("How much are you updating? (use negative to reduce)")
            amt = int(input())
            
            if stock_item in raw_materials.keys():
                raw_materials[stock_item]["quantity"] += amt
                print(f"{stock_item} has been updated to {raw_materials[stock_item]["quantity"]} kgs")
            else:
                print(f"{stock_item} is not present in raw materials")
                
            print("What quality is it?")
            qlty = input().lower()
            raw_materials[stock_item]["quality"] = qlty
            print(f"{stock_item}'s quality has been updated to {raw_materials[stock_item]["quality"]} quality")
            
        elif choice == "finished":
            print("What finished product are you updating?")
            finished_item = input().upper()
            
            if finished_item not in finished.keys():
                print(f"{finished_item} is not present in finished")
            else:
                print("How much are you updating? (use negative to reduce)")
                amt2 = int(input())
                finished[finished_item]["amount"] += amt2
                print(f"{finished_item} have been updated to {finished[finished_item]["amount"]} packects")
                
        else:
            print("Thank You for Choosing Trust Inventory Management System, we hope to hear from you again")
            break
        
        
#displaying stock items
def display_stock():
   
        print("\nRaw Materials")
        for item, info in raw_materials.items():
            print(f"{item}: Quantity -> {info["quantity"]}, Quality -> {info["quality"]}")
            
        print("\nProducts on sale")
        for product, details in finished.items():
            print(f"{product}: Amount -> {details["amount"]}")
            
            
    
while True:  
    print("\nWelcome to Trust Inventory Management System")
    print("\nPlease select an option below:" )
    print("1. Display Stock")
    print("2. Update Stock")
    print("3. Exit")
    print("\n")
    option = input().lower()

    if option == "1":
                display_stock()
                
    elif option == "2":
                update_stock()

    else:
                print("Thank You for Choosing Trust Inventory Management System, we hope to hear from you again")
                break


