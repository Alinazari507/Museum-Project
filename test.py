# Step 1: define our magic mini-function (Lambda)
# add_five gets a number (x) and gives back (x + 5)
add_five = lambda x: x + 5

# Step 2: let's test it with number 10
result = add_five(10)

# Step 3: see the result
print("The result is:", result)
# 1. Our data (The boxes on the conveyor belt)
prices = [100, 200, 300, 400]

# 2. Our machine (The Lambda function: take x and add 10)
# This is our rule: lambda x: x + 10

# 3. Putting them together on the conveyor belt (map)
# map(rule, data)
conveyor_belt = map(lambda x: x + 10, prices)

# 4. Collecting the new boxes into a new list
new_prices = list(conveyor_belt)

print("Original Prices:", prices)
print("New Prices (after adding 10):", new_prices)

# 1. Raw Data
prices = [50, 120, 80, 200, 150]

# 2. Step One: Filter (Only prices > 100)
filtered_data = filter(lambda x: x > 100, prices)

# 3. Step Two: Map (Add 10 to the winners)
final_results = map(lambda x: x + 10, filtered_data)

# 4. Show the final list
print("Final processed prices:", list(final_results))