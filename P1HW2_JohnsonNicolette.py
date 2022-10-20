Python 3.10.7 (v3.10.7:6cc6b13308, Sep  5 2022, 14:02:52) [Clang 13.0.0 (clang-1300.0.29.30)] on darwin
Type "help", "copyright", "credits" or "license()" for more information.
>>>    # P1HW2
...    # 9 October 2022 
...    # CTI-110 P1HW2 - Travel Expense
...    # Nicolette Johnson
... 
... #Asking for user input
... print("This program calculates and displays travel expenses.")
... 
... #User input
... budget = int(input("Enter budget: $"))
... destination = input("Enter your travel destination: ")
... gas = int(input("How much do you think you will spend on gas? $"))
... hotel = int(input("Approximately, how much will you need for accomodation/hotel? $"))
... food = int(input("Last, how much do you need for food? $"))
... 
... #Remaining balance equation
... remaining_balance = budget - (gas + hotel + food)
... 
... #Results
... print("----Travel Expenses----")
... print("Location: ",(destination))
... print("Initial Budget: $",(budget))
... print("Fuel: $",(gas))
... print("Accomodation: $",(hotel))
... print("Food: $",(food))
