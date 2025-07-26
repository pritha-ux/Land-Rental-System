from datetime import datetime
from read import displayData
from operations import rent_land, return_land, right_choice
from write import change_available_status_not_available

print("*******************************************************************************************************************")
print("********************************** Welcome to the Land Rental Management System ***********************************")
print("___________________________________________________________________________________________________________________")
print("\n")
timestamp = datetime.now().strftime("%Y-%m-%d %H-%M-%S")
continue_running = True

while continue_running:
    print("1. Rent a Land")
    print("2. Return a Land")
    print("3. Exit")
    print("\n")
    land_data = displayData()
    
    user_choice_valid = False
    while not user_choice_valid:
        try:
            choice = int(input("Please choose an option (1, 2, or 3): "))
            user_choice_valid = True
        except ValueError:
            print("Invalid input. Please select option 1, 2, or 3.")

    print("\n")

    if choice == 1:
        continue_rent_process = True
        land_ids = []
        rental_months = []
        while continue_rent_process:
            land_id_valid = False
            while not land_id_valid:
                try:
                    land_id = input("Please enter the ID of the land you wish to rent: ")
                    if right_choice(land_id, land_data, 1):
                        land_id_valid = True
                        land_ids.append(land_id)
                    else:
                        print("Invalid land ID. Please enter a valid integer ID.")
                except ValueError:
                    print("Invalid land ID. Please enter a valid integer ID.")

            while True:
                rental_duration = input("How many months would you like to rent the land for? ")
                if rental_duration.isdigit():
                    rental_duration = int(rental_duration)
                    if rental_duration > 60:
                        print("You cannot rent land for more than 60 months. Please enter a valid number.")
                    else:
                        rental_months.append(rental_duration)
                        break
                else:
                    print("Invalid input. Please enter a valid number.")

            while True:
                continue_rent_ask = input("Do you wish to continue renting (yes/no): ").strip().lower()
                if continue_rent_ask in ["yes", "no"]:
                    continue_rent_process = continue_rent_ask == "yes"
                    break
                else:
                    print("Please enter 'yes' or 'no' only.")
        
        change_available_status_not_available(land_data, land_ids)
        customer_name = input("Please enter your name: ")
        rent_land(land_data, customer_name, timestamp, land_ids, rental_months)

    elif choice == 2:
        land_ids = []
        rental_months = []
        rented_months = []
        continue_return_process = True
        while continue_return_process:
            land_id_valid = False
            while not land_id_valid:
                try:
                    land_id = input("Please enter the ID of the land you wish to return: ")
                    if right_choice(land_id, land_data, 2):
                        land_id_valid = True
                        land_ids.append(land_id)
                    else:
                        print("Invalid land ID. Please enter a valid integer ID.")
                except ValueError:
                    print("Invalid land ID. Please enter a valid integer ID.")

            while True:
                rental_duration_return = input("Enter the rental months that is in contract: ")
                if rental_duration_return.isdigit():
                    rental_duration_return = int(rental_duration_return)
                    if rental_duration_return <= 60:
                        rental_months.append(rental_duration_return)
                        break
                    else:
                        print("You cannot rent land for more than 60 months. Please enter a valid number.")
                else:
                    print("Invalid input. Please enter a valid number.")

            while True:
                rented_duration = input("Enter the months you rented this land: ")
                if rented_duration.isdigit():
                    rented_duration = int(rented_duration)
                    if rented_duration <= 60:
                        rented_months.append(rented_duration)
                        break
                    else:
                        print("You cannot rent land for more than 60 months. Please enter a valid number.")
                else:
                    print("Invalid input. Please enter a valid number.")

            while True:
                continue_return_ask = input("Do you wish to continue returning (yes/no): ").strip().lower()
                if continue_return_ask in ["yes", "no"]:
                    continue_return_process = continue_return_ask == "yes"
                    break
                else:
                    print("Please enter 'yes' or 'no' only.")

        returner_name = input("Please enter your name: ")
        return_land(land_data, land_id, returner_name, rental_duration_return, rented_duration, timestamp, land_ids, rental_months, rented_months)

    elif choice == 3:
        continue_running = False
        print("/*_____________________________________________________________*/")
        print("Thank you for using the Land Rental Management System!")
        print("_________________________________________________________________")
        print("\n")

    else:
        print("Invalid option selected. Please choose 1, 2, or 3.")
        print("\n")
