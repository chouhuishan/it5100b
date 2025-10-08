from demoutils import *
import stream
# Task 1: Order-to-food stream
"""
The `random_orders` stream produces a stream of orders. Convert
this stream into a stream of foods
"""
order_to_food = stream.flat_map(lambda x: x.items)(random_orders(3))

# Task 2
"""
The `random_temperatures` stream produces a stream of temperature
readings. Convert this stream into a stream of temperatures in degrees fahrenheit.
"""
celsius_temperatures = stream.map(Temperature.as_celsius)(random_temperatures())

# Task 3
"""
The `random_ints` stream produces a stream of random integers. Assume each int is a total watch hour for each day. 
Convert this stream to one that gets the total watch hours for
the week.
"""
weekly_hours = stream.pipe(stream.window(7,7), stream.map(sum))(random_ints(size=100))

# Task 4
"""
The `random_transactions` stream produces a stream of random
transactions. Some of the transactions are NaN values, indicating
some data corruption or something else. Remove the transactions
with NaN values.
"""
non_nan_transactions = stream.filter(lambda x: x.amount != 'NaN')(random_transactions())

# Task 5
"""
Obtain the sum of a random stream of integers
"""
sum_of_stream = stream.reduce(lambda x, y: x + y, 0)(random_ints(size=100))

# Task 6
"""
Obtain the size of a stream
"""
size_of_stream = stream.reduce(lambda x, y: x + 1, 0)(random_transactions())

# Task 7
"""
Find the set of all unique elements in a stream (assume the elements are hashable)
"""
unique_temperatures = stream.reduce(lambda x, y: x | {y}, set())(random_temperatures())

# Task 8
"""
Same as Task 5, except that our stream is infinitely large
"""
partial_sums = stream.scan(lambda x, y: x + y)(random_ints())

# Task 9
"""
Same as Task 6, except that our stream is infinitely large
"""
size_of_stream = stream.pipe(stream.map(lambda x: 1), stream.scan(lambda x, y: x + y))(random_ints())

# Task 10
"""
Same as Task 7, except that our stream is infinitely large
"""
unique_temperatures = stream.scan(lambda x, y: x | {y}, set())(random_temperatures())

# Task 11
"""
The `random_user` function gives a potentially nonexistent user. Obtain the user's order history.
"""
order_history = stream.flat_map(lambda x: x.prev_order)(random_user())

# Task 12
"""
The `random_temperature` gives a potentially nonexistent temperature reading. Convert it to Fahrenheit
"""
temp = stream.map(Temperature.as_fahrenheit)(random_temperature())

# Task 13
"""
Same as Task 4 but for Options
"""
non_nan_transaction = stream.filter(lambda x: x.amount)(random_transaction())
