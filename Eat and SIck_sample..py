

# numbers = [1,2,3,4,5,6,7,8,9,10]
# for number in range(1,10,2):
#  number += 1
#  print(number)
# print("we have 4 even numbers")

access = "Rita"
# def enter_name():
#     return enter_name()
name = input("enter password ")
if name == access:
 print('access successful!')
else:
 print("access denied!")

meaty_menus = ("chicken, turkey, suya, stake, pork")
veggie_menu = ("salad, sunny eggs, rice, pickle, abacha")
nonveggie_menu = ("pizza, salad, ice cream, barbeque, nkwobi")

meaty = input("Are you a meaty? enter yes/no ")
if meaty == "yes":
 print(f"Here is the menu: {meaty_menus}")
else:
    print("Move on to the other options")

veggie = input("Are you a veggie? enter yes/no ")
if veggie == "yes":
    print(f"Here is the menu: {veggie_menu}")
else:
    print("Try another food class,maybe non-veg?")

non_veggie = input("How about non veg, are you one? enter yes/no ")
if non_veggie == "yes":
    print(f"Here is the non veggie menu: {nonveggie_menu}")
else:
        print("Why don't you become a chef yourself and see how difficult it is to make food!")


# account = 100
# interest_rate = 10
# years = 3

# print(f"initial amount: {account}")
# counter = 1
# while counter <= years:
#     accrued_interest = account * interest_rate
#     account += accrued_interest
#     print(f"year {counter}: {account}")
#     counter += 1






class global_health():

    def __init__(self):
        self.name = input('enter patient name: ')
        self.age = input('enter patient age: ')
        self.illness = input('enter illness patient is suffering from: ')
        #self.illness_status = input('is the illness dire, enter yes/no: ')
        self.insurance = input('do you have health insurance? yes/no: ')

patient = global_health()
print(f'hello {patient.name}')

illness_status = input('is the illness dire, enter yes/no: ')
if illness_status == "no":
    print('we are wishing you a quick recovery!')
else:
    print(f'this is what you answered about the insurance:{patient.insurance}')
    if patient.insurance == 'yes':
     print('You will get a 15% increase on your annual insurance fee so as to get proper treatment. Drop the of your insurance detail below!')


