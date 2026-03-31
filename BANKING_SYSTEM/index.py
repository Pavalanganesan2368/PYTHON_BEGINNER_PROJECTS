class Banking :
    def __init__ (self) :
        self.__amountBalance = 0
        self.amountDeposits = 0
        self.amountWithdrawal = 0

    def depositsAmount (self) :
        self.amountDeposits = int(input("ENTER THE AMOUNT TO DEPOSITS : "))

        if (self.amountDeposits > 0) : 
            self.__amountBalance += self.amountDeposits 
            print("AMOUNT IS DEPOSITED SUCCESSFULLY")
        else :
            print("YOU ENTER THE INVALID AMOUNT!")

    def withdrawalAmount (self) :
        self.amountWithdrawal = int(input("ENTER THE AMOUNT TO WITHDRAWAL : "))

        if (self.__amountBalance <= 0) :
            print("YOUR AMOUNT IS EMPTY!")
        elif (self.amountWithdrawal > self.__amountBalance) :
            print("INSUFFICIENT BALANCE!")
        else :
            self.__amountBalance -= self.amountWithdrawal
            print("AMOUNT WITHDRAWAL SUCCESSFULLY")

    def balanceAmount (self) :
        print(f"YOUR BALANCE AMOUNT OF YOUR ACCOUNT IS : {self.__amountBalance}")

    def amountDisplay (self) :
        print(f"YOUR ACCOUNT BALANCE IS : {self.__amountBalance}")
        print(f"YOUR ACCOUNT WITHDRAWAL IS : {self.amountWithdrawal}")

    
class AmountDeposits (Banking) :
    def __init__ (self) :
        super().__init__()

    def accountHolder (self) :
        self.accountNumber = int(input("ENTER THE CUSTOMER ACCOUNT NUMBER : "))
        self.accountName = str(input("ENTER THE CUSTOMER NAME : ").strip().upper())

    def accountDetailDisplay (self) :
        print(f"YOUR ACCOUNT HOLDER NAME : {self.accountName}")
        print(f"YOUR ACCOUNT NUMBER : {self.accountNumber}")

status = True
banking = AmountDeposits ()

while(status) :
    print("-----------------------------")
    print("WELCOME TO OUR BANKING SYSTEM")
    print("1.ACCOUNT DETAILS")
    print("2.ACCOUNT DEPOSITS")
    print("3.ACCOUNT WITHDRAWAL")
    print("4.ACCOUNT BALANCE")
    print("5.ACCOUNT STATUS")
    print("6.EXIT")
    print("-----------------------------")
    choice = int(input('ENTER YOUR CHOICE : '))


    match (choice) :
        case 1 :
            banking.accountHolder()

        case 2 :
            banking.depositsAmount()

        case 3 :
            banking.withdrawalAmount()

        case 4 :
            banking.balanceAmount()

        case 5 :
            banking.accountDetailDisplay()
            banking.amountDisplay()

        case _ :
            print("THANK YOU SO MUCH FOR VISITING OUR BANKING")
            status = False