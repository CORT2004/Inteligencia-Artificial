#Es igual a
var = 0  # Assigning 0 to var
print(var == 0)

var = 1  # Assigning 1 to var
print(var == 0)

#Es diferente a
var = 0  # Assigning 0 to var
print(var != 0)
 
var = 1  # Assigning 1 to var
print(var != 0)

#Condicionales
#if the_weather_is_good:
#    go_for_a_walk()
#have_lunch()

#if sheep_counter >= 120: # Evaluate a test expression
#    sleep_and_dream() # Execute if test expression is True

#if sheep_counter >= 120:
#    make_a_bed()
#    take_a_shower()
#    sleep_and_dream()
#feed_the_sheepdogs()

#Condicional o segunda opcion
#if true_or_false_condition:
#    perform_if_condition_true
#else:
#    perform_if_condition_false

#if the_weather_is_good:
#    go_for_a_walk()
#else:
#    go_to_a_theater()
#have_lunch()

#if the_weather_is_good:
#    go_for_a_walk()
#    have_fun()
#else:
#    go_to_a_theater()
#    enjoy_the_movie()
#have_lunch()

#If anidado
#if the_weather_is_good:
#    if nice_restaurant_is_found:
#        have_lunch()
#    else:
#        eat_a_sandwich()
#else:
#    if tickets_are_available:
#        go_to_the_theater()
#    else:
#        go_shopping()

#Diversos if en la misma funcion (No anidados)
#if the_weather_is_good:
#    go_for_a_walk()
#elif tickets_are_available:
#    go_to_the_theater()
#elif table_is_available:
#    go_for_lunch()
#else:
#    play_chess_at_home()

# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2:
    larger_number = number1
else:
    larger_number = number2

# Print the result
print("The larger number is:", larger_number)

# Read two numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))

# Choose the larger number
if number1 > number2: larger_number = number1
else: larger_number = number2

# Print the result
print("The larger number is:", larger_number)

# Read three numbers
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# We temporarily assume that the first number
# is the largest one.
# We will verify this soon.
largest_number = number1

# We check if the second number is larger than the current largest_number
# and update the largest_number if needed.
if number2 > largest_number:
    largest_number = number2

# We check if the third number is larger than the current largest_number
# and update the largest_number if needed.
if number3 > largest_number:
    largest_number = number3

# Print the result
print("The largest number is:", largest_number)

#largest_number = -999999999
#number = int(input())
#if number == -1:
#    print(largest_number)
#    exit()
#if number > largest_number:
#    largest_number = number
# Go to line 02

# Read three numbers.
number1 = int(input("Enter the first number: "))
number2 = int(input("Enter the second number: "))
number3 = int(input("Enter the third number: "))

# Check which one of the numbers is the greatest
# and pass it to the largest_number variable.

largest_number = max(number1, number2, number3)

# Print the result.
print("The largest number is:", largest_number)

