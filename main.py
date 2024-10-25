#
# main.py
#
# Implement five commands to display database statistics
# based on user input.
#
# Original author: Nathen Priyonggo
#
# CS 341 Project 2
# Chicago Lobbyist Database App
#
# Name      : Nathen Priyonggo
# UIN       : 664887330
# NetID     : rpriyo2
# Semester  : Fall 2024
#
import sqlite3
import objecttier


##################################################################  
#
# Helper Functions
#

# Output basic info for all lobbyists given name input
def cmd1(dbConn):

    print()
    # Prompt user input for name to search
    name = input("Enter lobbyist name (first or last, wildcards _ "
                 + "and % supported): ")

    # Retrieve list of lobbyists that match with name
    lobbyistList = objecttier.get_lobbyists(dbConn, name)

    # Print list length
    print()
    print("Number of lobbyists found:", len(lobbyistList))

    # If oversized list, print error message
    if len(lobbyistList) > 100:
        print()
        print("There are too many lobbyists to display, please"
              + " narrow your search and try again...")
        
    # Else if empty list, do nothing for formatting reasons
    elif len(lobbyistList) == 0:
        pass

    # Else print list contents
    else:
        print()
        for lob in lobbyistList:
            print(f"{lob.Lobbyist_ID} : {lob.First_Name}"
                + f" {lob.Last_Name} Phone: {lob.Phone}")


# Output detailed info for lobbyist given id input
def cmd2(dbConn):

    print()
    # Prompt user input for id to search
    id = input("Enter Lobbyist ID: ")

    # Retrieve lobbyists details that match with id
    lobbyistDetails = objecttier.get_lobbyist_details(dbConn, id)

    # If non-existent id, print error message
    if lobbyistDetails == None:
        print()
        print("No lobbyist with that ID was found.")
    
    # Else, print details
    else:
        det = lobbyistDetails
        print()
        print(f"{det.Lobbyist_ID} :")

        # Full Name
        print(f"  Full Name: {det.Salutation} {det.First_Name}"
              + f" {det.Middle_Initial} {det.Last_Name} {det.Suffix}")
        
        # Address
        print(f"  Address: {det.Address_1} {det.Address_2} , "
              + f"{det.City} , {det.State_Initial} {det.Zip_Code} "
              + f"{det.Country}")
        
        # Email
        print(f"  Email: {det.Email}")

        # Phone
        print(f"  Phone: {det.Phone}")

        # Fax
        print(f"  Fax: {det.Fax}")

        # List of Years Registered
        print("  Years Registered: ", end="")
        for year in det.Years_Registered:
            print(f"{year}", end=", ")
        print()

        # List of Employers
        print(f"  Employers: ", end="")
        for employer in det.Employers:
            print(f"{employer}", end=", ")
        print()

        # Total Compensation
        print(f"  Total Compensation: ${det.Total_Compensation:,.2f}")


# Output top N lobbyists given year input
def cmd3(dbConn):

    print()
    # Prompt user input for value of N
    n = int(input("Enter the value of N: "))

    # Check if N's value is not positive
    if n <= 0:
        print("Please enter a positive value for N...")
        return
    
    # Prompt user input for year
    year = input("Enter the year: ")

    # Retrieve top N lobbyists that match with year
    lobClientList = objecttier.get_top_N_lobbyists(dbConn, n, year)

    # If empty list, return for formatting reasons
    if lobClientList == []:
        return
    
    print()
    num = 1
    # Print all details
    for lob in lobClientList:

        print(f"{num} . {lob.First_Name} {lob.Last_Name}\n" +
              f"  Phone: {lob.Phone}\n" + 
              f"  Total Compensation: ${lob.Total_Compensation:,.2f}\n" +
              f"  Clients:", end="")
        
        for client in lob.Clients:
            print(f" {client}", end=",")
        
        print()
        num += 1


# Add new year for existing lobbyist
def cmd4(dbConn):
    
    # Prompt user for year and lobbyist id
    print()
    year = input("Enter year: ")
    lobId = input("Enter the lobbyist ID: ")

    # Add year, return if succesfully added or not
    rowCount = objecttier.add_lobbyist_year(dbConn, lobId, year)

    print()
    # Lobbyist does not exist
    if rowCount <= 0:
        print("No lobbyist with that ID was found.")

    # Lobbyist added
    else:
        print("Lobbyist successfully registered.")
        

    
# Set saluation of given lobbyist id
def cmd5(dbConn):
    
    # Prompt user for lobbyist id and salutation
    print()
    lobId = input("Enter the lobbyist ID: ")
    sal = input("Enter the salutation: ")

    # Set salutation, return if succesfully set or not
    rowCount = objecttier.set_salutation(dbConn, lobId, sal)

    print()
    # Salutation does not exist
    if rowCount <= 0:
        print("No lobbyist with that ID was found.")

    # Salutation set
    else:
        print("Salutation successfully set.")



##################################################################  
#
# main
#

print('** Welcome to the Chicago Lobbyist Database Application **')
print()

# Initiate connection with database
dbConn = sqlite3.connect("Chicago_Lobbyists.db")

# Fetch general statistics from database
lobbyistsNum = objecttier.num_lobbyists(dbConn)
employersNum = objecttier.num_employers(dbConn)
clientsNum = objecttier.num_clients(dbConn)

# Print Stats
print("General Statistics:")
print(f"  Number of Lobbyists: {lobbyistsNum:,}")
print(f"  Number of Employers: {employersNum:,}")
print(f"  Number of Clients: {clientsNum:,}")
print()

cmd = input("Please enter a command (1-5, x to exit): ")

# Execute command while loop
while cmd != "x":

    if cmd == "1":
        cmd1(dbConn)
    elif cmd == "2":
        cmd2(dbConn)
    elif cmd == "3":
        cmd3(dbConn)
    elif cmd == "4":
        cmd4(dbConn)
    elif cmd == "5":
        cmd5(dbConn)
    else:
        print("**Error, unknown command, try again...")
    
    print()
    cmd = input("Please enter a command (1-5, x to exit): ")


#
# done
#