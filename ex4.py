#declaring number of cars equal to 100
cars = 100

#declaring the space_in_a_car
space_in_a_car = 4

#sdeclaring the number of drivers
drivers = 30

#declaring the number of passengers
passengers = 90

#total number of cars not driven is equal to the amount of cars minus drivers
cars_not_driven = cars - drivers

#cars driven is equal to the number of drivers
cars_driven = drivers

#amount of carpool room is equal to the amount of cars minus passengers
carpool_capacity = cars_driven * space_in_a_car

#avergae equals passengers divided by amount of cars driven
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available")
print("There are only", drivers, "drivers available")
print("There will be", cars_not_driven, "empty cars today")
print("We can transport", carpool_capacity, "to carpool today")
print("We have", passengers, "to carpool today")
print("We need to put about", average_passengers_per_car, "in each car.")
