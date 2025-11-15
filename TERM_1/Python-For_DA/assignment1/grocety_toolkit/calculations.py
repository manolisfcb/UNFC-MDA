def item_charged_units(item, bogof_items=None) -> int:
    """
    Returns the number of units of an item that will be charged for, taking into account any BOGOF offers.
    ○	Input: 
        - one tuple like ("banana", 6, 0.39, "produce") 
        - a list of names elegible for BOGOF offers, e.g. ["pasta", "bread"]
    ○   Rules:
        - If the item is in bogof_items, charge only half (round down).
        - Otherwise, charge full quantity.     
    ○	Return:
        - the number of charged units as an integer.
    """
    name, quantity, unit_price, category = item
    if type(quantity) != int or quantity < 0:
        quantity = 0
    
    charged_units = quantity
    if bogof_items is not None and name in bogof_items:
        items_with_2_by_1 = quantity // 2 
        rest_of_items = quantity % 2 
        charged_units = items_with_2_by_1 + rest_of_items
    return charged_units

def item_subtotal(item, bogof_items=None, category_discounts=None) -> float:
    """ 
    Compute the item’s total cost (subtotal) after:
    ○	Input: 
        - one item like ("banana", 6, 0.39, "produce") 
        - a list of names elegible for BOGOF offers, e.g. ["pasta", "bread"]
        - a dictionary of category discounts, e.g. {"produce": 0.10, "bakery": 0.05}
    ○   Rules:
        -	Applying BOGOF discount (if eligible).
        -	Applying category discount (if category in category_discounts dict).
    ○	Return 
        - the item’s total rounded to 2 decimals.
    """
    name, quantity, unit_price, category = item
    charged_units = item_charged_units(item, bogof_items)
    subtotal = charged_units * unit_price
    if category_discounts is not None and category in category_discounts:
        subtotal *= 1 - category_discounts[category] # this is the same as subtotal = subtotal * (1 - category_discounts[category])

    return round(subtotal, 2)

def basket_subtotal(basket, bogof_items=None, category_discounts=None) -> float:
    """
    ○	Input: 
        - a basket of items, e.g. basket_a = [("banana", 6, 0.39, "produce"), ...]
        - a list of names elegible for BOGOF offers, e.g. ["pasta", "bread"]
        - a dictionary of category discounts, e.g. {"produce": 0.10, "bakery": 0.05}    
    ○   Rules:
        - Compute the sum of all item_subtotal() values.
        - Return rounded to 2 decimals.
    ○	Return 
        - the basket’s subtotal rounded to 2 decimals.
    """
    subtotal = 0
    for item in basket:
        subtotal += item_subtotal(item, bogof_items, category_discounts)
    return round(subtotal, 2)