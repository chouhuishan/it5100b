import stream


def f(i):
    print(i)
    return i


# filter and map are lazy iterables

print(stream.of([1, 2, 3, 4, 5]))


def constant_one():
    return 1


s = stream.generate(constant_one)
print(list(stream.take(5)(s)))
print(list(stream.take(10)(s)))
s = stream.generate(input)
print(list(stream.take(5)(s)))

s = stream.of([1, 2, 3, 4, 5])
s = stream.map(lambda x: x + 1)(s)
list(stream.map(lambda x: x + 1)(s))

stream.map(lambda x: x + 1)(s)
list(stream.map(lambda x: x + 1)(s))

s = stream.of([1, 2, 3, 4, 5])
list(stream.filter(lambda x: x % 2)(s))
list(stream.flat_map(lambda x: [x + 1])([1, 2, 3, 4]))

s = [1, 2, 3, 4, 5]
_ = stream.of(s)
_ = stream.map(lambda x: x + 1)(_)
_ = stream.flat_map(lambda x: [x, x + 1])(_)
list(_)

my_pipeline = stream.pipe(
    stream.map(lambda x: x + 1),
    stream.filter(lambda x: x % 2),
    stream.flat_map(lambda x: [x + 1]),
)
s = [1, 2, 3, 4, 5]
list(my_pipeline(s))

s = stream.buffer
