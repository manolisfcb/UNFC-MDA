"""Demo main script for Grocery Basket Analyzer."""

from grocety_toolkit.calculations import *
from grocety_toolkit.analysis import *
from grocety_toolkit.discounts import *

def main():
    # Sample data
    basket_a = [
        ("banana", 6, 0.39, "produce"),
        ("milk 2%", 1, 3.49, "dairy"),
        ("pasta", 2, 1.29, "dry"),
        ("bread", 1, 2.79, "bakery"),
        ("chicken", 2, 8.99, "meat"),
        ("rice", 1, 2.49, "dry"),
    ]

    basket_b = [
        ("apple", 4, 0.55, "produce"),
        ("cheddar", 1, 4.49, "dairy"),
        ("pasta", 3, 1.19, "dry"),
        ("salmon", 1, 12.99, "meat"),
        ("lettuce", 2, 1.99, "produce"),
    ]

    basket_c = [
        ("orange", 8, 0.45, "produce"),
        ("yogurt", 3, 1.29, "dairy"),
        ("cereal", 2, 4.99, "dry"),
        ("bagels", 4, 0.89, "bakery"),
        ("beef", 1, 15.99, "meat"),
        ("pasta", 1, 1.29, "dry"),
    ]

    baskets = {"BasketA": basket_a, "BasketB": basket_b, "BasketC": basket_c}

    category_discounts = {"produce": 0.10, "bakery": 0.05, "meat": 0.15}  # 10% off produce, 5% off bakery, 15% off meat
    bogof = {"pasta", "bread"}  # buy one pasta/bread, get one free
    
    threshold_amount = 20.00
    threshold_rate = 0.10  # extra 10% off if subtotal >= $20
    
    tax_rate = 0.13

    print("=== GROCERY BASKET ANALYZER DEMO ===\n")

    #Test item_charged_units
    print("1. Testing item_charged_units:")
    print("   Pasta (qty=2) with BOGOF:", item_charged_units(("pasta", 2, 1.29, "dry"), bogof_items=bogof))
    print("   Bread (qty=4) with BOGOF:", item_charged_units(("bread", 4, 2.79, "bakery"), bogof_items=bogof))
    print("   Banana (qty=6) no BOGOF:", item_charged_units(("banana", 6, 0.39, "produce"), bogof_items=bogof))
    print()

    # Test item_subtotal
    print("2. Testing item_subtotal:")
    print("   Pasta (qty=2, price=1.29) with BOGOF:", item_subtotal(("pasta", 2, 1.29, "dry"), bogof_items=bogof))
    print("   Banana (qty=6, price=0.39) with 10% produce discount:", item_subtotal(("banana", 6, 0.39, "produce"), category_discounts=category_discounts))
    print("   Bread (qty=1, price=2.79) with 5% bakery discount:", item_subtotal(("bread", 1, 2.79, "bakery"), category_discounts=category_discounts))
    print()

    # Test basket_subtotal
    print("3. Testing basket_subtotal:")
    print("   BasketA subtotal:", basket_subtotal(basket_a, bogof_items=bogof, category_discounts=category_discounts))
    print("   BasketB subtotal:", basket_subtotal(basket_b, bogof_items=bogof, category_discounts=category_discounts))
    print("   BasketC subtotal:", basket_subtotal(basket_c, bogof_items=bogof, category_discounts=category_discounts))
    print()

    # Test apply_threshold_discount
    print("4. Testing apply_threshold_discount:")
    subtotal_a = basket_subtotal(basket_a, bogof_items=bogof, category_discounts=category_discounts)
    print("   BasketA subtotal:", subtotal_a)
    print("   After threshold discount (20.00 threshold, 10% off):", apply_threshold_discount(subtotal_a, threshold_amount, threshold_rate))
    print()

    # Test compute_tax
    print("5. Testing compute_tax:")
    discounted_subtotal = apply_threshold_discount(subtotal_a, threshold_amount, threshold_rate)
    print("   On discounted subtotal:", discounted_subtotal)
    print("   Tax (13%):", compute_tax(discounted_subtotal, tax_rate))
    print()

    # Test grand_total
    print("6. Testing grand_total:")
    print("   BasketA grand total:", grand_total(basket_a, bogof_items=bogof, category_discounts=category_discounts, threshold_amount=threshold_amount, threshold_rate=threshold_rate, tax_rate=tax_rate))
    print("   BasketB grand total:", grand_total(basket_b, bogof_items=bogof, category_discounts=category_discounts, threshold_amount=threshold_amount, threshold_rate=threshold_rate, tax_rate=tax_rate))
    print("   BasketC grand total:", grand_total(basket_c, bogof_items=bogof, category_discounts=category_discounts, threshold_amount=threshold_amount, threshold_rate=threshold_rate, tax_rate=tax_rate))
    print()

    # Test category_breakdown
    print("7. Testing category_breakdown:")
    print("   BasketA category breakdown:", category_breakdown(basket_a, bogof_items=bogof, category_discounts=category_discounts))
    print("   BasketB category breakdown:", category_breakdown(basket_b, bogof_items=bogof, category_discounts=category_discounts))
    print("   BasketC category breakdown:", category_breakdown(basket_c, bogof_items=bogof, category_discounts=category_discounts))
    print()

    # Test cheapest_basket
    print("8. Testing cheapest_basket:")
    print("   Cheapest basket:", cheapest_basket(baskets, bogof_items=bogof, category_discounts=category_discounts, threshold_amount=threshold_amount, threshold_rate=threshold_rate, tax_rate=tax_rate))
    print()

    print("=== DEMO COMPLETE ===")


if __name__ == "__main__":
    main()