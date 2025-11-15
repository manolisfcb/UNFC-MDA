from grocety_toolkit.discounts import grand_total
from grocety_toolkit.calculations import item_subtotal
def cheapest_basket(baskets, bogof_items=None, category_discounts=None, threshold_amount=0.0, threshold_rate=0.0, tax_rate=0.13) -> str:   
    """
    ○	Input: 
        -   dictionary of baskets, e.g. {"BasketA": basket_a, "BasketB": basket_b, "BasketC": basket_c}
    ○	Rules:
        -	Compute the grand total of each basket.
        -	Keep track of the basket with the lowest grand total.     
    ○	Return 
        -   the name of the basket with the lowest grand total (if totals are equal, return the first basket). 
    """
    cheapest_basket = None
    cheapest_total = float("inf")
    for basket_name, basket in baskets.items():
        total = grand_total(basket, bogof_items=bogof_items,
                            category_discounts=category_discounts,
                            threshold_amount=threshold_amount,
                            threshold_rate=threshold_rate,
                            tax_rate=tax_rate)
        if total < cheapest_total:
            cheapest_basket = basket_name
            cheapest_total = total
    return cheapest_basket

def category_breakdown(basket, bogof_items=None, category_discounts=None) -> dict:
    """
    ○	Input: 
        -   a basket of items, e.g. basket_a, basket_b, basket_c..
        -   a list of names elegible for BOGOF offers, e.g. ["pasta", "bread"]
        -   a dictionary of category discounts, e.g. {"produce": 0.10, "bakery": 0.05}    
    ○   Rules:
        -	Compute the subtotal of each item in the basket.
        -	Keep track of the subtotal of each category. and add it up to the previous subtotal.
        -	Round the subtotal of each category to 2 decimals.
    ○	Return 
        -   a dictionary with the breakdown of the basket by category, e.g. {"produce": 5.27, "dry": 2.58, "bakery": 2.79}
    """
    breakdown = {}
    for item in basket:
        name, quantity, unit_price, category = item
        subtotal = item_subtotal(item, bogof_items=bogof_items, category_discounts=category_discounts)
        if category in breakdown:
            breakdown[category] = breakdown[category] + subtotal
        else:
            breakdown[category] = subtotal
    
    return breakdown