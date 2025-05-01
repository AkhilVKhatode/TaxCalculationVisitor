# Tax Calculation System using Visitor Pattern

A Python implementation of a tax calculation system using the Visitor design pattern, demonstrating how to apply different tax rules to different product types.

## Features

- Implements the Visitor pattern for clean separation of concerns
- Supports different tax rules for different product types (books, food, electronics)
- Easy to extend with new product types or tax rules
- Type hints and abstract base classes for clear interfaces
- Uses Python dataclasses for clean product definitions

## Design Overview

The system consists of:

1. **Visitors** (Tax Calculators):
   - `TaxVisitor`: Abstract base class defining the visitor interface
   - `BasicTaxCalculator`: Concrete implementation with basic tax rules

2. **Elements** (Products):
   - `Product`: Abstract base class for all products
   - `Book`, `Food`, `Electronics`: Concrete product implementations

## How It Works

Each product type accepts a tax visitor, which then calculates the appropriate tax based on the product's type:

```python
# Create products
products = [
    Book("Python Programming", 50.00, "123-456789"),
    Food("Organic Apples", 3.99, True),
    Electronics("Smartphone", 599.99, 2)
]

# Create tax calculator
tax_calculator = BasicTaxCalculator()

# Calculate taxes
for product in products:
    tax = product.accept(tax_calculator)
    total = product.price + tax
    print(f"{product.name}: Price=${product.price:.2f}, Tax=${tax:.2f}, Total=${total:.2f}")
```

Default Tax Rates
- Books: 5% tax (often reduced or exempt)
- Food: 8% tax (reduced rate for essentials)
- Electronics: 15% tax (standard rate)
