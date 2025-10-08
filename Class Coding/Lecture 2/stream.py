def of(ls):
    """
    Initializes a stream given an iterable.
    """
    for i in ls:
        yield i


def generate(f):  # produce an element of the stream
    """
    Creates an infinitely long stream whose elements are produced by
    the function.
    """
    while True:
        yield f()


def iterate(f, init):
    """
    Creates an infinitely long stream whose elements are produced by
    iteratively applying a function on an initial value
    """
    while True:
        yield init
        init = f(init)


def take(n):
    """
    Takes the first n elements of a stream
    """

    def g(ls):
        i = 0
        for e in ls:
            if i >= n:
                break
            yield e
            i += 1
            if i >= n:
                break

    return g


def take_while(f):
    """
    Keep taking elements of a stream until the first element that
    does not meet a predicate
    """

    def g(ls):
        for i in ls:
            if f(i):
                yield i
            else:
                break

    return g


def drop(n):
    """
    Drops the first n elements of the stream
    """

    def g(ls):
        i = 0
        for e in ls:
            if i >= n:
                yield e

    return g


def empty():
    """
    either the empty stream or the empty optional
    """
    return []


def optional(x=None):
    """
    Wraps a potentially null value as an optional.
    """
    return [] if x is None else [x]


_map = map
_filter = filter


# put in a group of different functions into one pipeline to allow a series of operations to be done in one function
def pipe(*ls):
    """
    Creates a pipe using a series of operations
    """

    def g(i):
        for f in ls:
            i = f(i)
        return i

    return g


def map(f):
    """
    Maps elements of the stream/optional using a function
    """

    def g(ls):
        if isinstance(ls, list):
            return list(_map(f, ls))
        return _map(f, ls)

    return g


def flat_map(f):
    def g(ls):
        def h():
            for i in ls:
                for j in f(i):
                    yield j

        x = h()
        if isinstance(ls, list):
            return list(x)
        return x

    return g


def filter(f):
    def g(ls):
        if isinstance(ls, list):
            return list(_filter(f, ls))
        return _filter(f, ls)

    return g


def window(count, skip=1):
    return lambda ls: map(of)(buffer(count, skip)(ls))


def buffer(count, skip=1):
    def g(ls):
        if count < 1 or skip < 1:
            return empty()
        win = []
        s = skip
        for i in ls:
            win.append(i)
            if len(win) == count:
                yield win.copy()
                win = win[s:]

    return g


def concat_right(ls):
    def g(ls2):
        if isinstance(ls, list) and isinstance(ls2, list):
            return ls2 + ls

        def h():
            for i in ls2:
                yield i
            for j in ls:
                yield j

        return h()

    return g


def concat_left(ls):
    def g(ls2):
        if isinstance(ls, list) and isinstance(ls2, list):
            return ls + ls2

        def h():
            for i in ls:
                yield i
            for j in ls2:
                yield j

        return h()

    return g


def reduce(f, init=None):
    def g(ls):
        if init is None:
            r = []
        else:
            r = init
        for i in ls:
            if init is None:
                if not r:
                    r.append(i)
                else:
                    r[0] = f(r[0], i)
            else:
                r = f(r, i)
        return r

    return g


def scan(f, init=None):
    def g(ls):
        j = optional(init)
        if j:
            yield j[0]
        for i in ls:
            if not j:
                j.append(i)
                yield j[0]
            else:
                j[0] = f(j[0], i)
                yield j[0]

    return g


def zip_right(ls):
    def g(ls2):
        if isinstance(ls, list) and isinstance(ls2, list):
            return list(zip(ls2, ls))

        def h():
            for i in zip(ls2, ls):
                yield i

        return h()

    return g


def zip_left(ls):
    def g(ls2):
        if isinstance(ls, list) and isinstance(ls2, list):
            return list(zip(ls, ls2))

        def h():
            for i in zip(ls, ls2):
                yield i

        return h()

    return g


def foreach(f):
    def g(ls):
        for i in ls:
            f(i)

    return g


def get(ls):
    if not ls:
        raise RuntimeError("cannot get from empty value!")
    return ls[0]


def get_or_else(x):
    def f(ls):
        if not ls:
            return x
        return ls[0]

    return f
