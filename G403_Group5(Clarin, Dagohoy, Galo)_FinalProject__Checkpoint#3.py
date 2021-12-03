print("Electricity Usage and Power Consumption Costing Program")
Apparatus = {}
Exit = ["X", "x"]
ctr = 0
Total = 0

print("\nGeneral information: ")
while True:
    pf = float(input("   Power Factor: "))
    
    if not (0<pf<=1):
        print("    *Invalid input, please try again.*")
        
    else:
        break
        
while True: 
    rate = float(input("   Rate per kilowatt-hour (Php): "))
    
    if rate <= 0:
        print("    *Invalid input, please try again.*")
        
    else: 
        break
    
while True: 
    print("\n\n\nMenu:\n1 - Add apparatus\n2 - Show apparatus\n3 - Calculate\n0 - Exit")
    select = input("Please Select an Option: ")
    if select not in ("1","2","3","0"): 
        print("*Please Input from the Menu Above*")
        continue
    
    elif select == "0":
        break
        
    elif select == "1":
        print('\n\n\nPlease Specify Details:')
        print(' [if done, input "x" or "X"]')
        while True:
            name = input("\n   Name of the apparatus: ")
            if (name in Exit):
                print("\nList of Apparatus: ")
                for item,detail in Apparatus.items():
                    print(f"   {item} - [{detail} W]")    
                break 
         
            else:   
                pr = int(input("   What is its power rating in watts?: "))
                new_item = {name : pr}
                Apparatus.update(new_item)
                
    elif select == "3":
        print("\n\n\nPlease input additional details:")
        for item,detail in Apparatus.items():
            items_list = list(Apparatus)
            details = Apparatus.values()
            details_list = list(details)
            word = items_list[ctr]
            word_upper = word.upper()
            print(f"\nApparatus: {word_upper}")
            
            while True:
                quantity = int(input(" -> Quantity of Apparatus: "))
                if quantity < 0:
                    print("    *Invalid input, please try again.*")
                else: 
                    break  
                    
            while True:
                hours = float(input(" -> Hourly Usage in a Day: "))
                if  not (0 <= hours <= 24 ):
                    print("    *Invalid input, please try again.*")
                else:
                    break
                    
            while True:   
                days = int(input(" -> Days used in a Month: ")) 
                if not (0<= days <= 31):
                    print("    *Invalid input, please try again.*")
                else:
                    break
                
            partial =(((details_list[ctr])*quantity*hours*days*(1+pf)*rate)/1000)
            print(f" -> Partial Cost of Apparatus: {partial:.3f} Php")
            ctr = ctr + 1
            Total = Total + partial  
           
        print(f"\nTotal Monthly Bill: {Total:.3f} Php")
        
    elif select == "2":
        print("\n\n\nList of Apparatus: ")
        for item,detail in Apparatus.items():
            print(f"   {item} - [{detail} W]")