import datetime

class Rule:

    def __init__(self, conditions, discounts):
        self.conditions = conditions
        self.discounts = discounts

    def evaluate(self, tab):
        if self.conditions.evaluate(tab):
            return self.discounts.calculate(tab)
        return 0


class Conditions:

    def __init__(self, expression):
        self.expression = expression

    def evaluate(self, tab):
        return self.expression.evaluate(tab)

class And:

    def __init__(self, expression1, expression2):
        self.expresssion1 = expression1
        self.expresssion2 = expression2

    def evaluate(self, tab):
        return self.expresssion1.evaluate(tab) and self.expresssion2.evaluate(tab)


class Or:

    def __init__(self, expression1, expression2):
        self.expression1 = expression1
        self.expression2 = expression2

    def evaluate(self, tab):
        return self.expression1.evaluate(tab) or  self.expression2.evaluate(tab)


class PercentageDiscount:

    def __init__(self, item_type, percentage):
        self.item_type = item_type
        self.percentage = percentage

    def calculate(self, tab):
        return [sum([x.cost for x in tab.items if x.item_type == self.item_type]) * self.percentage] / 100

class CheapestFree:

    def __init__(self, item_type):
        self.item_type = item_type

    def calculate(self, tab):
        try:
            return min([x.cost for x in tab.items if x.item_type == self.item_type])
        except:
            return 0

class TodayIs:

    def __init__(self, day_of_week):
        self.day_of_week = day_of_week

    def evaluate(self, tab):
        return datetime.datetime.today().weekday() == self.day_of_week.name

class TimeIsBetween:

    def __init__(self, from_time, to_time):
        self.from_time = from_time
        self.to_time = to_time

    def evaluate(self, tab):
        hour_now = datetime.datetime.today().hour
        minute_now = datetime.datetime.today().minute
        from_hour, from_minute = [int(x) for x in self.from_time.split(":")]
        to_hour, to_minute = [int(x) for x in self.to_time.split(":")]
        hour_in_range = from_hour <= hour_now <= to_hour
        begin_edge = hour_now == from_hour and minute_now > from_minute
        end_edge = hour_now == to_hour and minute_now < to_minute
        return any(hour_in_range, begin_edge, end_edge)

class Tab:

    def __init__(self, customer):
        self.items = []
        self.discounts = []
        self.customer = customer

    def calculate_cost(self):
        return sum(x.cost for x in self.items)

    def calculate_discount(self):
        return sum(x for x in self.discounts)

class Item:

    def __init__(self, name, item_type, cost):
        self.name = name
        self.item_type = item_type
        self.cost = cost

class ItemType:

    def __init__(self, name):
        self.name = name


class Customer:

    def __init__(self, customer_type, name):
        self.customer_type = customer_type
        self.name = name

class CustomerType:

    def __init__(self, customer_type):
        self.customer_type = customer_type

