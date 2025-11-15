USE sakila;

-- Total Customers per Store List each store_id and the number of customers registered in that store.
SELECT 
	COUNT(customer_id), 
    store_id
FROM customer
group by store_id;

-- Total Revenue per Staff Member Show each staff member and the total payment amount they collected
SELECT 
	S.staff_id,
	CONCAT(S.first_name, " ", S.last_name) AS Staff,
    SUM(amount) AS Revenue
FROM 
	payment P
JOIN
	staff S
ON P.staff_id = S.staff_id
GROUP BY staff_id;

-- Top 10 Most Rented Films Display film title and the number of rentals, sorted from most rented to least, limit to 10 results.
SELECT 
	F.title, 
	COUNT(R.rental_id) AS FILMS_RENTED_COUNT
FROM
	Rental R
JOIN
	Inventory I 
ON R.inventory_id = I.inventory_id
JOIN film F
ON I.film_id = F.film_id
GROUP BY I.film_id
order by COUNT(*) DESC
LIMIT 10;

-- Average Rental Rate by Film Category Show each category name and the average 
-- rental_rate of films in that category.

SELECT 
	C.name,
	AVG(F.rental_rate) AS AVERAGE,
    MAX(F.rental_rate) AS MAXIMUM,
    MIN(F.rental_rate) AS MINUMUN
FROM
	Film F
JOIN
	film_category FC
ON 
	F.film_id = FC.film_id
JOIN category C
ON	C.category_id = FC.category_id
GROUP BY C.category_id;

-- Cities with More than 1 Customers List city name and customer count,
-- but only show cities that have more than 1 customers. (Use HAVING.)

SELECT 
	CT.city
    -- COUNT(CU.customer_id) AS AMOUNT
FROM 
	customer CU
JOIN 
	address AD ON CU.address_id = AD.address_id
JOIN
	city CT ON CT.city_id = AD.city_id
GROUP BY CT.city
HAVING COUNT(CU.customer_id) > 1;

-- Categorize Films by Length Display each film title and a label using
-- CASE: 
-- • 'Short' if length < 60 
-- • 'Standard' if length between 60 and 120 
-- • 'Extended' otherwise

SELECT 
	CASE
		WHEN length < 60 THEN 'Short'
        WHEN length < 121 THEN 'Standard'
	ELSE 'Extended' 
    END AS "CLength"
FROM 
	film;

-- Revenue by Customer (With Ranking) Show each customer’s full name 
-- and the total amount they have spent. Sort by total amount from highest to lowest.

SELECT
	CONCAT(C.first_name, " ", C.last_name) AS FULL_NAME,
    SUM(amount) AS TOTAL_REVENUE
FROM customer C
JOIN payment P ON P.customer_id = C.customer_id
group by C.Customer_id
Order by TOTAL_REVENUE DESC;

-- Count Actors per Film Display film title and the number of actors who acted in that film.

SELECT 
	F.film_id,
    F.title,
	COUNT(FA.actor_id) as AMOUNT_ACTORS
FROM film_actor FA
JOIN film F ON F.film_id = FA.film_id
GROUP BY F.film_id;



-- Active vs Inactive Customers Count
-- Count how many customers are Active and how many are Inactive, grouped by the active column.

SELECT
	COUNT(customer_id) AS AMOUNT,
    active as STATUS_
FROM 
	customer
GROUP BY STATUS_;


-- Frequent vs Moderate vs Rare Renters
-- For each customer, count how many rentals they have made and assign a label using CASE:
-- • 'Frequent' if rentals > 20
-- • 'Moderate' if rentals between 10 and 20
-- • 'Rare' if rentals < 10

SELECT 
	customer_id,
    COUNT(rental_id) AS RENTALS,
	CASE 
		WHEN COUNT(rental_id) < 10  THEN 'Rare'
		WHEN COUNT(rental_id) < 20 THEN 'Moderate'
        ELSE 'Frequent'
	END AS FRECUENCY
FROM rental
GROUP BY customer_id



