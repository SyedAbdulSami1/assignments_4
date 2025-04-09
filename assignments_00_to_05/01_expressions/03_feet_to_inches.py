"""Converts feet to inches. Feet is an American unit of measurement. There are 12 inches per foot. Foot is the singular, and feet is the plural."""
INCHES_IN_FOOT:int = 12 # Conversion factor for feet to inches. There are 12 inches in a foot.

def converter ():
    feet : float= float(input("Enter number of feet: "))
    inches : float = feet * INCHES_IN_FOOT # Convert feet to inches
    print("That is" + str(inches) + " inches!") # Print the result

if __name__ == "__main__":
    converter() 