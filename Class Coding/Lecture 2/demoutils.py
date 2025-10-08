from dataclasses import dataclass
from typing import Literal
from random import randint, uniform
import stream

Food = str

@dataclass
class Order:
    account_id: int
    items: list[Food]

Celsius = Literal['C']
Fahrenheit = Literal['F']

class Temperature:
    def __init__(self, amount: float, units: Celsius | Fahrenheit):
        self.amount = amount
        self.units = units
    @staticmethod
    def celsius(amt: float) -> 'Temperature':
        return Temperature(amt, 'C')
    @staticmethod
    def fahrenheit(amt: float) -> 'Temperature':
        return Temperature(amt, 'F')
    def as_fahrenheit(self) -> 'Temperature':
        if self.units == 'F': return self
        return Temperature.fahrenheit(self.amount * 9 / 5 + 32)
    def as_celsius(self) -> 'Temperature':
        if self.units == 'C': return self
        return Temperature.celsius((self.amount - 32) * 5 / 9)
    def __str__(self):
        return f'{self.amount:.2f}°{self.units}'
    def __eq__(self, other):
        return isinstance(other, Temperature) and self.amount == other.amount and self.units == other.units
    def __hash__(self):
        return hash(f'{self.amount}{self.units}')
    def __repr__(self):
        return f'Temperature({self.amount}, {self.units})'
    
random_food_names = """Tiramisu
Sushi Burrito
Miso Soup
Beef Stroganoff
Peking Duck
Pad Thai
Pho Bo
Gyros
Peking Duck
Chicken Pad See Ew
Falafel Wrap
Pad Thai
Butter Chicken
Croissants
Chocolate Chip Cookies
Beignets
Cinnamon Rolls
Chicken Parmesan
Tacos al Pastor
Philly Cheesesteak
Risotto
Crispy Fried Chicken
Lomo Saltado
Samosas
Chicken Caesar Salad
Miso Soup
Pancakes
Margarita Pizza
Caprese Salad
Mushroom Risotto
Tandoori Chicken
Crispy Fried Chicken
Chicken Shawarma
Chicken Katsu Curry
Mango Sticky Rice
Chicken Tikka Masala
Ceviche
Tandoori Chicken
Fish and Chips
Hamburger
Spanakopita
Cobb Salad
Beef Wellington
Chicken Satay
Churros
Poke Bowl
Falafel
Lomo Saltado
Phapda
Pizza
Sushi
Chicken Satay
Lasagna
Crispy Pork Belly
Chicken Noodle Soup
Gyudon
Tiramisu
Croissant
Falafel
Spanakopita
Macarons
Sushi Platter
Chicken Enchiladas
Crispy Pork Belly
Beef Rendang
Chicken Parmesan
Eggs Benedict
Butter Chicken
Chicken Shawarma
Vegetable Curry
Red Velvet Cake
Pad Thai
Butter Chicken
Chicken Adobo
Shrimp Scampi
Fish and Chips
Beef Bulgogi
Pho Bo
Strawberry Shortcake
Spanakopita
Beef Tacos
Pho Ga
Pulled Pork Sandwich
Beef Pho
Fish and Chips
Caprese Salad
Philly Cheesesteak
Chicken Noodle Soup
Spinach and Feta Stuffed Chicken
Moussaka
Miso Salmon
Mushroom Risotto
Chicken Tikka Masala
Key Lime Pie
Burger
Beef Tendon Noodle Soup
Chicken Shawarma
Pasta Carbonara
Crème Brûlée
Chicken Enchiladas""".split('\n')

random_neighbourhoods = """Pasir Ris
Tampines
Simei
Tanah Merah
Bedok
Kembangan
Eunos
Paya Lebar
Aljunied
Geylang
Kallang
Tanjong Rhu
Lavender
Tiong Bahru
Redhill
Bukit Merah
Queenstown
Bukit Timah
Clementi
Jurong East
Jurong West
Sembawang
Bukit Batok
Bukit Gombak
Yew Tee
Yishun
Khatib
Marsiling
Woodlands
Punggol
Sengkang
Boon Keng
Bendemeer
Harbourfront
Lakeside
Boon Lay""".split('\n')

@dataclass
class Transaction:
    amount: int | Literal['NaN']
    address: str

def _random_food() -> Food:
    return random_food_names[randint(0, len(random_food_names) - 1)]

def _random_order() -> Order:
    return Order(randint(100000,999999), [_random_food() for _ in range(randint(1, 10))])

def random_orders(size: int = -1):
    if size < 0:
        return (_random_order() for _ in range(randint(1, 100)))
    return (_random_order() for _ in range(size))
    
def _random_temperature():
    if randint(0, 1):
        return Temperature.celsius(uniform(20, 40))
    return Temperature.celsius(uniform(20, 40)).as_fahrenheit()

def _random_transaction():
    price = randint(5,15) * 100_000
    unit = randint(1,999)
    addr = f'{unit} {random_neighbourhoods[randint(0, len(random_neighbourhoods) - 1)]} St {randint(10, 99)} #{randint(1, 30)}-{randint(10, 999)} S{randint(100,999)}{unit:03d}'
    if randint(0, 5):
        return Transaction(price, addr)
    return Transaction('NaN', addr)

def random_temperatures(size: int = -1):
    if size < 0:
        return (_random_temperature() for _ in range(randint(1, 100)))
    return (_random_temperature() for _ in range(size))

def random_ints(min: int = 1, max: int = 100, size: int = -1):
    if size < 1:
        return stream.generate(lambda: randint(min, max))
    return (randint(min, max) for _ in range(size))

def random_transactions(size: int = -1):
    if size < 0:
        return (_random_transaction() for _ in range(randint(1, 100)))
    return (_random_transaction() for _ in range(size))

@dataclass
class User:
    id: int
    prev_order: list[Order]

def random_user():
    if not randint(0, 5):
        return stream.optional()
    if not randint(0, 5):
        return stream.optional((User(randint(1000,9999), stream.optional())))
    return stream.optional(User(randint(1000,9999), stream.optional(_random_order())))

def random_temperature():
    if not randint(0, 5):
        return stream.optional()
    return stream.optional(_random_temperature())

def random_transaction():
    if not randint(0, 5):
        return stream.optional()
    return stream.optional(_random_transaction())
