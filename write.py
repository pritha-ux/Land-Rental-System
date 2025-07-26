import os

def change_available_status_not_available(land_data, land_ids):
    with open("land_data.txt", "w") as file:
        for land in land_data:
            if land["kitta"] in land_ids and land["status"] == "Available":
                file.write(land["kitta"] + ", " + land["city"] + ", " + land["direction"] + ", " + land["anna"] + ", " + land["price"] + ", " + "Not Available\n")
            else:
                file.write(land["kitta"] + ", " + land["city"] + ", " + land["direction"] + ", " + land["anna"] + ", " + land["price"] + ", " + land["status"] + "\n")

def change_available_status_available(land_data, land_ids):
    with open("land_data.txt", "w") as file:
        for land in land_data:
            if land["kitta"] in land_ids and land["status"] == "Not Available":
                file.write(land["kitta"] + ", " + land["city"] + ", " + land["direction"] + ", " + land["anna"] + ", " + land["price"] + ", " + "Available\n")
            else:
                file.write(land["kitta"] + ", " + land["city"] + ", " + land["direction"] + ", " + land["anna"] + ", " + land["price"] + ", " + land["status"] + "\n")

def print_generate_rental_invoice(land_data, total_prices, customer_name, timestamp, land_ids, rental_months):
    print("\n")
    print("******************************************************************************************Date: " + timestamp)
    print("***********************************Your rental invoice has been generated******************************************")
    print("___________________________________________________________________________________________________________________")
    print("Customer Name: " + str(customer_name))
    print("___________________________________________________________________________________________________________________")
    print("{:<12}{:<18}{:<15}{:<11}{:<15}{:<20}{:<10}".format("Kitta", "City", "Direction", "Anna", "Price", "Rental Duration", "Total Price"))
    for i in range(len(land_ids)):
        for land in land_data:
            if land["kitta"] == land_ids[i]:
                print("{:<10}{:<20}{:<15}{:<11}{:<15}{:<20}{:<10}".format(land["kitta"], land["city"], land["direction"], land["anna"], land["price"], rental_months[i], total_prices[i]))
    print("___________________________________________________________________________________________________________________")
    
    data = f"{customer_name}_invoice.txt"
    mode = 'a' if os.path.exists(data) else 'w'
    with open(data, mode) as file:
        file.write("******************************************************************************************Date: " + timestamp + "\n")
        file.write("***************************************Your invoice has been generated*********************************************" + "\n")
        file.write("___________________________________________________________________________________________________________________" + "\n")
        file.write("Customer Name: " + str(customer_name) + "\n")
        file.write("___________________________________________________________________________________________________________________" + "\n")
        file.write("{:<12}{:<18}{:<15}{:<11}{:<15}{:<20}{:<10}".format("Kitta", "City", "Direction", "Anna", "Price", "Rental Duration", "Total Price") + "\n")
        for i in range(len(land_ids)):
            for land in land_data:
                if land["kitta"] == land_ids[i]:
                    file.write("{:<10}{:<20}{:<15}{:<11}{:<15}{:<20}{:<10}".format(land["kitta"], land["city"], land["direction"], land["anna"], land["price"], rental_months[i], total_prices[i]) + "\n")
        file.write("___________________________________________________________________________________________________________________" + "\n")

def print_generate_return_invoice(land_data, land_id, rental_duration, rented_duration, total_prices, returner_name, timestamp, rental_months, rented_months, land_ids):
    print("\n")
    print("******************************************************************************************Date: " + timestamp)
    print("***********************************Your return invoice has been generated******************************************")
    print("___________________________________________________________________________________________________________________")
    print("Customer Name: " + str(returner_name))
    print("___________________________________________________________________________________________________________________")
    print("{:<12}{:<18}{:<15}{:<11}{:<15}{:<20}{:<20}{:<10}".format("Kitta", "City", "Direction", "Anna", "Price", "Rental Duration", "Rented Duration", "Total Price"))
    for i in range(len(land_ids)):
        for land in land_data:
            if land["kitta"] == land_ids[i]:
                print("{:<10}{:<20}{:<15}{:<11}{:<15}{:<20}{:<20}{:<10}".format(land["kitta"], land["city"], land["direction"], land["anna"], land["price"], rental_months[i], rented_months[i], total_prices[i]))
    print("___________________________________________________________________________________________________________________")
    
    data = f"{returner_name}_invoice.txt"
    mode = 'a' if os.path.exists(data) else 'w'
    with open(data, mode) as file:
        file.write("******************************************************************************************Date: " + timestamp + "\n")
        file.write("***************************************Your invoice has been generated*********************************************" + "\n")
        file.write("___________________________________________________________________________________________________________________" + "\n")
        file.write("Customer Name: " + str(returner_name) + "\n")
        file.write("___________________________________________________________________________________________________________________" + "\n")
        file.write("{:<12}{:<18}{:<15}{:<11}{:<15}{:<20}{:<20}{:<10}".format("Kitta", "City", "Direction", "Anna", "Price", "Rental Duration", "Rented Duration", "Total Price") + "\n")
        for i in range(len(land_ids)):    
            for land in land_data:
                if land["kitta"] == land_ids[i]:
                    file.write("{:<10}{:<20}{:<15}{:<11}{:<15}{:<20}{:<20}{:<10}".format(land["kitta"], land["city"], land["direction"], land["anna"], land["price"], rental_months[i], rented_months[i], total_prices[i]) + "\n")
        file.write("___________________________________________________________________________________________________________________" + "\n")
