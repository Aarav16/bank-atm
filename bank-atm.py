class Atm:
    def __init__(self,cardnumber,pin):
        self.cardnumber=cardnumber
        self.pin=pin
        
    def check_balance(self):
        print("your balance is $50,000")
        
    def withdrawl(self,amount):
        new_amount=50000-amount
        print("You have withdrawen amount "+str(amount)+".Your remaining balance is "+str(new_amount))
        
def main():
    card_number=input("Insert your card number:- ")
    pin_number=input("Insert your pin number:- ")
    new_user=Atm(card_number,pin_number)
    
    print("Choose your activity ")
    print("1. Balance Enquiry  2.Withdrawl")
    activity=int(input("Enter acivity number:- "))
    if activity==1:
        new_user.check_balance()
    elif (activity==2):
        amount=int(input("Enter the amount:- "))
        new_user.withdrawl(amount)
    else:
        print("Enter a valid number")
if __name__=="__main__":
    main()
 
    