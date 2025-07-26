def displayData():
    try:
        print("\n-------------------------------------------------------------------------------------------------------------------")
        print("{:<12}{:<18}{:<15}{:<11}{:<15}{:<10}".format("Kitta", "City", "Direction", "Anna", "Price", "Status"))
        print("-------------------------------------------------------------------------------------------------------------------")
        land_data = []
        with open("land_data.txt", "r") as file:
            lines = file.readlines()
            for line in lines:
                kitta, city, direction, anna, price, status = line.lstrip().replace("\n", "").split(", ")
                land_data.append({
                    "kitta" : kitta,
                    "city" : city, 
                    "direction" : direction, 
                    "anna" : anna, 
                    "price" : price, 
                    "status" : status
                })
                print("{:<10}{:<20}{:<15}{:<10}{:<15}{:<10}".format(kitta, city, direction, anna, price, status))
        print("-------------------------------------------------------------------------------------------------------------------\n")
    except FileNotFoundError:
        print("Error: 'land_data.txt' file could not be found.")
    except Exception as e:
        print(f"An error occurred during land data display: {e}")
    return land_data
