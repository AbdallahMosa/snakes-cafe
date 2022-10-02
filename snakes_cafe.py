
def order():
    my_menu ={"wings": 0,"cookies": 0,"spring rolls": 0,"salmon": 0,"steak": 0,"meat tornado": 0,"a literal garden": 0,
    "ice cream": 0,"cake": 0,"pie": 0,
        "coffee": 0,"tea": 0,"unicorn tears": 0
    }
    res = input("> if you want to order type any things or \"quit\" to exit ")
    final_order = {}
    count_of_order = 0
    while res != "quit":
        order = input("> ")
       
        if order == "quit":
            print("Your order contains")
            for key, value in final_order.items():
                print(key, ' : ', value+1)
            print("thank you and Good Bye")
            break
        if order.lower() in  my_menu:
            final_order.update({f"{order}": my_menu[order]})
            new_order = order
            count_of_order +=1
            my_menu[order] +=1
            print(f"{my_menu[order]} of {new_order} have been added yo your meal ")
        else :
            print("This dish is not in the menu")     


print("****************************************")
print("**     welcome to the Sankes Cafe!    **")
print("**     Please see our menu below.     **")
print("**")
print("** To quit at any time, type \"quit\"  **")
print("****************************************")
format_menu= """Appetizers
----------
Wings
Cookies
Spring Rolls


Entrees
-------
Salmon
Steak
Meat Tornado
A Literal Garden


Desserts
--------
Ice Cream
Cake
Pie


Drinks
------
Coffee
Tea
Unicorn Tears
***********************************
** What would you like to order? **
***********************************
"""
print(format_menu)
order()