weight = float(input("Enter the weight of the package (in pounds): "))
distance = float(input("Enter the distance it needs to be shipped (in miles): "))

def shipping_cost(weight, distance):
    if weight <= 2:
        base_cost = 5.00
    elif weight <= 10:
        base_cost = 10.00
    else:
        base_cost = 20.00

    if distance <= 100:
        additional_charge = 0.00
    elif distance <= 500:
        additional_charge = 5.00
    else:
        additional_charge = 10.00

    total_cost = base_cost + additional_charge
    return total_cost

cost = shipping_cost(weight, distance)
print(f"The shipping cost is: ${cost:.2f}")
