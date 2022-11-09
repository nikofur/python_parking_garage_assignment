class ParkingGarage():
    def __init__(self, capacity):
        self.capacity = capacity
        self.currentTicket = {}
        self.tickets = list(range(1, (capacity + 1)))
        self.parkingSpaces = list(range(1, (capacity + 1)))


    def takeTicket(self):
        '''
            .takeTicket()

            method checks if parking garage is full.  If not full, a ticket
            is given to user and a ticket number is displayed.  Does not
            return a value
        '''
        if self.tickets != []:
            ticketNum = self.tickets.pop(0)
            self.currentTicket[ticketNum] = 'unpaid'
            self.parkingSpaces.remove(0)

            print("Your ticket number is: ", ticketNum)

        else:
            print("Huge bummer for you.\nNick's Garage is currently full.")


    def payForParking(self):
        '''
            .payForParking()

            method prompts user for their ticket number.  If unpaid, the method
            prompts user for money until the proper amount has been accepted.  
            Does not return a value
        '''
        amountPaid = 0.00
        amountOwed = 20.00

        ticketNum = int(input("Please enter your ticket number: "))
        if self.currentTicket[ticketNum] == 'unpaid':
            while amountPaid < amountOwed:
                try:
                    print(f"You owe $", round((amountOwed - amountPaid), 2))
                    amountPaid += int(input("Enter amount: $"))
                except:
                    print("Please enter an amount.")
                if amountPaid > amountOwed:
                    print("Returning: $", amountPaid - amountOwed)
            print("Payment complete - You have 15 minutes to exit")
            self.currentTicket[ticketNum] = 'paid'
        else:
            print("Your ticket has already been paid")
        
        
    def leaveGarage(self):
        '''
            .leaveGarage()

            Method checks if the ticket has been paid and if so, allows the user
            to leave garage and adds 1 more available parking space and ticket.  If 
            the ticket is unpaid, it takes the user to the payForParking method.
            Does not return a value
        '''
        ticketNum = int(input("Please enter your ticket number: "))
        if self.currentTicket[ticketNum] == 'paid':
            print("Thank you, have a nice day!")
            self.currentTicket.pop(ticketNum)
            self.tickets.append(ticketNum)
            self.parkingSpaces.append(ticketNum)
        else:
            print("You have to pay before you can leave.")
            self.payForParking()

                


#body
nicksGarage = ParkingGarage(10)

while True:
    print("\n")
    print(nicksGarage.currentTicket)
    print("Tickets: ", nicksGarage.tickets)
    print("parkingSpaces: ", nicksGarage.parkingSpaces)

    print("\nPlease choose an option from the list below:")
    print("1.) Take a ticket")
    print("2.) Pay for parking")
    print("3.) Leave garage")
    menuChoice = 0
    try:
        menuChoice = int(input(": "))
    except:
        if menuChoice.lower() == 'quit':
            break
        else:
            print("Please enter a number (1-3) or type 'quit' to exit")

    if menuChoice == 1:
        nicksGarage.takeTicket()
    elif menuChoice == 2:
        nicksGarage.payForParking()
    elif menuChoice == 3:
        nicksGarage.leaveGarage()

    