def calculate_bill(units):
    # Define tariff rates\
    rate1 = 5
    rate2 = 7
    rate3 = 10

    if units <= 100:
        cost = units * rate1
    elif units <= 200:
        cost = (100 * rate1) + (units - 100) * rate2
    else:
        cost = (100 * rate1) + (200 * rate2) + (units - 200) * rate3
    return cost

units = int(input("Enter units consumed"))
total_cost = calculate_bill(units)
print(f"Total cost for {units} units: {total_cost} FCFA")