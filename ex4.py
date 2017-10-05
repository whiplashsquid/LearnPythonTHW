# assigns number one hundred to variable cars
cars = 100
# assigns floating point number 4.0 to variable space_in_a_car
space_in_a_car = 4.0
# assigns number thirty to variable drivers
drivers = 30
# assigns number ninety to variable passengers
passengers = 90
# assigns result of operation variable cars minus variable drivers to variable cars_not_driven
cars_not_driven = cars - drivers
# assigns variable drivers to variable cars_driven
cars_driven = drivers
# assigns result of operation variable cars_driven multiplied by variable space_in_a_car to variable carpool_capacity
carpool_capacity = cars_driven * space_in_a_car
# assigns result of operation variable passengers divided by variable cars_driven to variable average_passengers_per_car
average_passengers_per_car = passengers / cars_driven

# prints string including the assignment of the variable cars
print("There are", cars, "cars available.")
# prints string including the assignment of the variable drivers
print("There are only", drivers, "drivers available.")
# prints string including the assignment of the variable cars_not_driven
print("There will be", cars_not_driven, "empty cars today.")
# prints string including the assignment of the variable carpool_capacity
print("We can transport", carpool_capacity, "people today.")
# prints string including the assignment of the variable passengers
print("We have", passengers, "to carpool today.")
# prints string including the assignment of the variable average_passengers_per_car
print("We need to put about", average_passengers_per_car, "in each car.")
