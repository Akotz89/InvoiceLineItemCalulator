# Aaron Kotz, CIS261, Invoice Line Item Calulator

def display_heading():
    print("The Invoice Line Item Calculator")
    print("===============================")

def get_price():
    while True:
        try:
            price = float(input("Enter price: "))
            return price
        except ValueError:
            print("Invalid decimal number. Please try again.")

def get_quantity():
    while True:
        try:
            quantity = int(input("Enter quantity: "))
            return quantity
        except ValueError:
            print("Invalid integer. Please try again.")

def main():
    display_heading()
    
    while True:
        price = get_price()
        quantity = get_quantity()
        total = price * quantity
        
        print(f"\nPRICE:      {price:.2f}")
        print(f"QUANTITY:   {quantity}")
        print(f"TOTAL:      {total:.2f}\n")
        
        continue_prompt = input("Enter another line item? (y/n): ").lower()
        if continue_prompt == 'n':
            print("\nBye!")
            break

if __name__ == "__main__":
    main()

