def line(deli):
    deli_str = "The line is currently: "

    if len(deli) == 0: 
        print("The line is currently empty.")
    else:
        for i,n in enumerate(deli):
            deli_str += f"{i + 1}. {n} "
        
        print(deli_str.strip())
    
def take_a_number(deli, name):
   deli.append(name)
   print(f"Welcome, {name}. You are number {len(deli)} in line.")

    
def now_serving(deli):
    
    if len(deli) > 0:
        # print(deli)
        print(f"Currently serving {deli[0]}.")
        del deli[0]
    else:
        print("There is nobody waiting to be served!")

        #test