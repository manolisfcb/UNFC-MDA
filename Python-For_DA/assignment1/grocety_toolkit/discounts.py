from grocety_toolkit.calculations import basket_subtotal

def apply_threshold_discount(subtotal: float, threshold_amount: float, threshold_rate: float) -> float:
    """
    ○	Input:
        - subtotal: the subtotal of the basket, 
        - threshold_amount: the threshold amount to apply the discount, 
        - threshold_rate: the discount rate as a decimal (e.g. 0.10 for 10% discount)     
    ○   Rules:
        -	If the subtotal is greater than or equal to the threshold amount, apply the discount.
        -	Otherwise, do not apply the discount.
    ○	Return 
        -   the subtotal after applying the discount (if applicable).
    """
    if subtotal >= threshold_amount:
        discount = subtotal * threshold_rate
        return subtotal - discount
    else:
        return subtotal
    
def compute_tax(discounted_subtotal: float, tax_rate: float) -> float:
    """
    ○	Input:    
        - discounted_subtotal: subtotal after applying discounts to the basket, 
        - tax_rate: tax rate as a decimal (e.g. 0.13 for 13% tax) 
    ○   Rules:
        -	Compute tax on the given subtotal.
        -	Return tax amount (rounded to 2 decimals).
    ○	Return 
        -   tax amount
    """
    tax = discounted_subtotal * tax_rate
    return tax

def grand_total(basket, 
                bogof_items=None,
                category_discounts=None,
                threshold_amount=0.0,
                threshold_rate=0.0, tax_rate=0.13) -> float:
    
    """
    ○	Input: 
        - a basket of items, e.g. basket_a = [("banana", 6, 0.39, "produce"), ...]
        - a list of names elegible for BOGOF offers, e.g. ["pasta", "bread"]
        - a dictionary of category discounts, e.g. {"produce": 0.10,
        - a threshold amount, e.g. 20.00
        - a threshold rate, e.g. 0.10
        - a tax rate, e.g. 0.13 (Depends on the country, province, or state)   
    ○   Rules:
        Full pricing pipeline:
            1.	Compute subtotal of the basket.
            2.	Apply threshold discount.
            3.	Compute and add tax.
    ○	Return 
        - the basket’s grand total rounded to 2 decimals.
    """
    subtotal = basket_subtotal(basket, bogof_items=bogof_items, category_discounts=category_discounts)
    discounted_subtotal = apply_threshold_discount(subtotal, threshold_amount, threshold_rate)
    tax = compute_tax(discounted_subtotal, tax_rate)
    total = discounted_subtotal  + tax
    return total