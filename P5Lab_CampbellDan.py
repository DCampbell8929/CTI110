#Dan Campbell
#4/10/24
#P5LAB
#Using user Defined Functions


#Create Dictionary and list
stock = {
    "apples" : 3.69,
    "berries" : 4.00,
    "chocolate" : 2.89,
    "turkey" : 6.99,
    "cheese" : 4.00,
    "pepsi" : 7.89,
    "eggs" : 3.50,
    "bread" : 3.00
}
cart = []
#Define the functions

#Display available items
def show_avail_items(dictionary):
    print (f"{'Grocery Item':<25} Price")
    print ('------------------------------')
    for key, value in dictionary.items():
        print (f"{key:<25} ${value:.2f}")
    print ('------------------------------')

#Input from user to accumulate items in cart
def scan():
    item = input("Enter an item to add to the cart, or type 'end' to stop adding items: ")
    while item != "end":
        if item in stock.keys():
            cart.append (item)
        else:
            print (f"{item} is not in stock")
        item = input("Enter an item to add to the cart, or type 'end' to stop adding items: ")

#Print receipt information, including total, tax, and final total
def reciept():
    print ("Grocery Checkout Reciept")
    print ("-------------------------------")
    subtotal = 0
    for item in cart:
        print (f'{item:<25} ${stock[item]:.2f}')
        subtotal += stock[item]
    print ()    
    print (f"{'SUBTOTAL:':<25} ${subtotal:.2f}")
    print ()
    tax_due = subtotal * .02
    print (f"{'TAX:':<25} ${tax_due:.2f}")
    final_total = subtotal + tax_due
    print (f"{'TOTAL:':<25} ${final_total:.2f}")
    print ()
    return final_total

#Gather more input for amount of cash inserted
def collect(final_total):
    print (f"You owe ${final_total:.2f} for the groceries")
    print ()
    cash = float(input ("How much cash will you put in the self-checkout machine? $"))
    print ()
    while cash < final_total:
        print("That is not enough money")
        cash += float(input ("How much more cash will you put in the self-checkout machine? $"))
    change = final_total - cash
    return change
    

        
#Calculate and dispense change
def disperse_change(change):
    change = change * -1
    print(f"The change owed to you is  ${change:.2f}")
    print()
    print ('Dispensing...')
    print ()
    change = round(change * 100)
    if change == 0:
        print("No Change Due")

    #Calculate the amount of each coin needed
    #integer division - //

    num_dollars = change // 100
    change = change - (num_dollars * 100)

    num_quarters = change // 25
    change = change - (num_quarters * 25)

    num_dimes = change // 10
    change = change - (num_dimes * 10)

    num_nickles = change // 5
    change = change - (num_nickles *5)

    num_pennies = change // 1

    #Display coins owed

    if num_dollars > 0:
            print(f'{num_dollars}',  end=" ")
            if num_dollars == 1:
                print("Dollar")
            else:
                print("Dollars")
                
    if num_quarters > 0:
            print(f'{num_quarters}',  end=" ")
            if num_quarters == 1:
                print("Quarter")
            else:
                print("Quarters")

    if num_dimes > 0:
            print(f'{num_dimes}',  end=" ")
            if num_dimes == 1:
                print("Dime")
            else:
                print("Dimes")

    if num_nickles > 0:
            print(f'{num_nickles}',  end=" ")
            if num_nickles == 1:
                print("Nickle")
            else:
                print("Nickles")

    if num_pennies > 0:
            print(f'{num_pennies}',  end=" ")
            if num_pennies == 1:
                print("Penny")
            else:
                print("Pennies")

def main():
    show_avail_items(stock)
    print ("*Welcome to grocery checkout*")
    scan()
    #Print Cart
    print ()
    print ("The items currently in your cart are: ")
    for item in cart:
        print (item)
    print ()
    print ()
    final_total = reciept()
    change = collect(final_total)
    disperse_change(change)


    
#execute
main()






                

