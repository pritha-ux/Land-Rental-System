from write import change_available_status_available, print_generate_return_invoice, print_generate_rental_invoice

def rent_land(land_data, customer_name, timestamp, land_ids, rental_months):
    total_prices = []
    a = 0
    for i in range(len(land_ids)):
        for land in land_data:
            if land["kitta"] == land_ids[i]:
                total_price = int(land["price"]) * int(rental_months[i])
                total_prices.append(total_price)
                a += 1
    if a > 0:
        print_generate_rental_invoice(land_data, total_prices, customer_name, timestamp, land_ids, rental_months)

def return_land(land_data, land_id, returner_name, rental_duration, rented_duration, timestamp, land_ids, rental_months, rented_months):
    a = 0
    total_prices = []
    for i in range(len(land_ids)):
        for land in land_data:
            if land["kitta"] == land_ids[i]:
                if rented_months[i] > rental_months[i]:
                    total_price = int(land["price"]) * int(rented_months[i])
                    extra_months_rented = rented_months[i] - rental_months[i]
                    total_price += (0.1 * (int(land["price"] * int(extra_months_rented))))
                    total_prices.append(total_price)
                    a += 1
                else:
                    total_price = int(land["price"]) * int(rental_duration)
                    total_prices.append(total_price)
                    a += 1
                change_available_status_available(land_data, land_ids)

    if a > 0:
        print_generate_return_invoice(land_data, land_id, rental_duration, rented_duration, total_prices, returner_name, timestamp, rental_months, rented_months, land_ids)

def right_choice(land_id, land_data, rent_or_return):
    a = 0
    for i in range(len(land_data)):
        if rent_or_return == 1 and land_data[i]["kitta"] == land_id and land_data[i]["status"] == "Available":
            a += 1
        elif rent_or_return == 2 and land_data[i]["kitta"] == land_id and land_data[i]["status"] == "Not Available":
            a += 1
    if a > 0:
        return True
