from abc import ABC, abstractmethod
from dataclasses import dataclass

# Visitor Interface
class TaxVisitor(ABC):
    @abstractmethod
    def visit_book(self, book):
        pass
    
    @abstractmethod
    def visit_food(self, food):
        pass
    
    @abstractmethod
    def visit_electronics(self, electronics):
        pass

# Concrete Visitor - Basic Tax Calculator
class BasicTaxCalculator(TaxVisitor):
    def visit_book(self, book):
        # Books often have reduced or no tax
        return book.price * 0.05  # 5% tax
    
    def visit_food(self, food):
        # Food might have reduced tax
        return food.price * 0.08  # 8% tax
    
    def visit_electronics(self, electronics):
        # Electronics usually have standard tax
        return electronics.price * 0.15  # 15% tax

# Element Interface
class Product(ABC):
    @abstractmethod
    def accept(self, visitor: TaxVisitor):
        pass

# Concrete Elements
@dataclass
class Book(Product):
    name: str
    price: float
    isbn: str
    
    def accept(self, visitor: TaxVisitor):
        return visitor.visit_book(self)

@dataclass
class Food(Product):
    name: str
    price: float
    is_perishable: bool
    
    def accept(self, visitor: TaxVisitor):
        return visitor.visit_food(self)

@dataclass
class Electronics(Product):
    name: str
    price: float
    warranty_years: int
    
    def accept(self, visitor: TaxVisitor):
        return visitor.visit_electronics(self)

# Usage example
if __name__ == "__main__":
    # Create products
    products = [
        Book("Python Programming", 50.00, "123-456789"),
        Food("Organic Apples", 3.99, True),
        Electronics("Smartphone", 599.99, 2)
    ]
    
    # Create tax calculator
    tax_calculator = BasicTaxCalculator()
    
    # Calculate taxes for each product
    for product in products:
        tax = product.accept(tax_calculator)
        total = product.price + tax
        print(f"{product.name}: Price=${product.price:.2f}, Tax=${tax:.2f}, Total=${total:.2f}")
