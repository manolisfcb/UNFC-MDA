CREATE DATABASE instacart_db;
USE instacart_db;

Create Table departments ( department_id INT PRIMARY key, department_name VARCHAR (50) Not Null); 
-- Drop Table departments
CREATE TABLE aisles (aisle_id Int PRIMARY Key,	aisle_name VARCHAR (50) Not Null);
Create Table products 
( product_id INT PRIMARY Key, 
	product_name VARCHAR (100) Not Null, 
    aisle_id	INT, 
    department_id INT, 
    FOREIGN KEY (aisle_id) REFERENCES aisles (aisle_id) ON DELETE set Null, 
    FOREIGN KEY (department_id) REFERENCES departments (department_id) ON DELETE set Null);
    
    Create Table Orders ( 
    order_id INT Primary key, 
	user_id	INT Not Null, 
    eval_set VARCHAR (10), 
	order_number INT, 
	order_dow INT, 
	order_hour_of_day INT, 
	days_since_prior_order INT NOT Null); 
    
    Create Table order_products (
    order_id	INT , 
    product_id	Int , 
    add_to_cart_order INT, 
	reordered BOOLEAN, 
    PRIMARY Key (order_id, Product_id), 
    FOREIGN KEY( order_id) REFERENCES Orders(order_id) On DELETE CASCADE, 
    FOREIGN KEY (product_id) REFERENCES products(product_id) ON DELETE CASCADE    
    ); 



    
