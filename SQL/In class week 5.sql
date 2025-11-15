-- Q1  Insert a new department called seasonal with ID = 22
-- v1
-- INSERT INTO  instacart_db.departments VALUES (22, "seasonal")
-- v2
INSERT INTO  instacart_db.departments (department_id, department_name) VALUES (22, "seasonal");



-- Q2 Insert a new product called Halloween Costume with ID = 50002 into the seasonal department and aisle 6
-- v1
-- INSERT INTO instacart_db.products (product_id, product_name, aisle_id, department_id) VALUES ( 50002, "Halloween Costume",6,22)
-- v2
INSERT INTO instacart_db.products (product_id, product_name, aisle_id, department_id)
VALUES (50002,'Halloween Costume',6,(SELECT department_id FROM instacart_db.departments WHERE department_name = 'seasonal')); 



-- Q3 Insert a new product called Tylenol with ID = 50001 into the department with id 23 and aisle 7. Did it go well? How can you solve the issue?
/*
INSERT INTO instacart_db.products (product_id, product_name, aisle_id, department_id) VALUES ( 50001, "Tylenol",7,23)
We got an error: Error Code: 1452. Cannot add or update a child row: a foreign key constraint fails 
(`instacart_db`.`products`, CONSTRAINT `products_ibfk_2` FOREIGN KEY (`department_id`) REFERENCES `departments` (`department_id`) ON DELETE SET NULL)
this error means that we are try to insert a product into a departments that does not exist (department_id = 23). To solve this we first need to create 
a new departments with ID=23 e.g. pharmacy and then include the new product. We can also do this: 
INSERT INTO instacart_db.products (product_id, product_name, aisle_id) VALUES ( 50001, "Tylenol", 7) but it will insert a new product
with the deparments in null until the department is created

*/
INSERT INTO  instacart_db.departments VALUES (23, "pharmacy");
INSERT INTO instacart_db.products (product_id, product_name, aisle_id, department_id)
VALUES ( 50001, "Tylenol",7,23);



-- Q4 Delete a specific product with id=50002 directly from the products table.
DELETE FROM instacart_db.products WHERE product_id = 50002;



-- Q5 Delete the 'Pharmacy' department that you added above, with id = 23. What happens to products in that department?
DELETE FROM instacart_db.departments WHERE department_id = 23;
/*
If we remove the deparment_id=23 all rows in the table products with deparment_id = 23 will now have deparmet_id = Null because in the definition of our table 
put this: ON DELETE set Null 
we defined 
*/



-- Q6 Delete order with order id 537159 from orders table. What happens to the order_products table?
DELETE FROM instacart_db.Orders WHERE order_id = 537159;
/*
Will DELETE also the row with order_id in the table order_products because we set this configuration: On DELETE CASCADE,
that means if the FOREIGN KEY its eliminate, eliminate all the rows in this table also.
*/



-- Q7. Update the product with id = 50001 and change its department to 3
UPDATE instacart_db.products SET department_id = 3 WHERE product_id = 50001;



-- Q8 Change the table to add a Discounted Price (decimal values with 5 total number of digits and 2 as the number of decimal places) Column to products
ALTER TABLE instacart_db.products ADD COLUMN disconut_price DECIMAL(5,2);



-- Q9. Populate the new column by setting a discount as the discounted_price for all products. If the aisle id is 2 then set a 15% discount. Otherwise set a 10% discount.
UPDATE instacart_db.products 
SET discounted_price =  
	CASE
        WHEN aisle_id = 2 THEN 0.15
        ELSE 0.10
    END;



-- Extras
CREATE TABLE IF NOT EXISTS teams 
(
team_id INT NOT NULL PRIMARY KEY,
team_name VARCHAR(50));

CREATE TABLE IF NOT EXISTS team_members(
member_id  INT NOT NULL PRIMARY KEY,
team_name VARCHAR(50),
team_id INT,
FOREIGN KEY (team_id) REFERENCES teams (team_id) ON DELETE CASCADE
);
DROP TABLE teams;
/*
Error Code: 3730. Cannot drop table 'teams' referenced by a foreign key constraint 'team_members_ibfk_1' on table 'team_members'.
You can't eliminate a parent table that is being reference in another table (child table) We need to Drop the child table first (team_members),
 then the parent table (teams)
*/



-- Q10 Create a View for Frequently Ordered Products. Create a view named popular_products
-- that shows each product's ID and the total number of times it was ordered, sorted by the most
-- ordered products in descending order.
CREATE OR REPLACE VIEW popular_products AS (
SELECT 
	product_id,
	count(*) AS number_of_items
FROM instacart_db.order_products
GROUP BY product_id
ORDER BY number_of_items DESC
);



-- Q11. Create a View for Order Details. Create a view named order_details that displays each
-- order's ID, user ID, product name, and the order in which products were added to the cart
CREATE OR REPLACE VIEW order_details AS(
SELECT 
	O.order_id,
	O.user_id,
	P.product_name,
    OP.add_to_cart_order
FROM
	instacart_db.order_products OP
JOIN
	instacart_db.orders O
ON 
	OP.order_id = O.order_id
JOIN 
	instacart_db.products P
ON OP.product_id = P.product_id
ORDER BY O.order_id, OP.add_to_cart_order

);


