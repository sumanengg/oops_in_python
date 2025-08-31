from abc import ABC, abstractmethod
class ShippingStrategy(ABC):
    @abstractmethod
    def calculate_cost(self, order):
        pass


class FlatShippingCost(ShippingStrategy):
    def __init__(self, rate):
        self.rate = rate

    def calculate_cost(self, order):
        return self.rate
    

class WeightBasedShipping(ShippingStrategy):
    def __init__(self, rate_per_kg):
        self.rate_per_kg = rate_per_kg

    def calculate_cost(self, order):
        return order.get_weight() * self.rate_per_kg
    
''' Defining the context class maintains a reference to ShippingStrategy and 
delegates the calculations to that. '''

class ShippingCostService:
    def __init__(self, strategy):
        self._strategy = strategy

    def set_strategy(self, strategy):
        self._strategy = strategy

    def calculates_total_cost(self, order):
        if self._strategy is None:
            raise ValueError("Shipping strategy is not set.")

        return self._strategy.calculate_cost(order)
    

# Let's set a order class for calculation.
class Order:
    def __init__(self, weight):
        self._weight = weight
    
    def get_weight(self):
        return self._weight
    

def main():
    order1 = Order(5)
    flat_rate = FlatShippingCost(100)
    weight_based = WeightBasedShipping(rate_per_kg=5)

    # Using flat shipping strategy
    service = ShippingCostService(flat_rate)
    print(f"Flat Shipping cost: {service.calculates_total_cost(order1)}")
    
    print("Changing strategy to weight based.")
    service.set_strategy(weight_based)
    print(f"Total cost using weight_based {service.calculates_total_cost(order1)}")


if __name__ == "__main__":
    main()

