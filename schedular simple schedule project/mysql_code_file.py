"""
import mysql
from pymysql.constants.FLAG import AUTO_INCREMENT
from sqlalchemy import VARCHAR
from sqlparse.sql import Values

CREATE DATABASE IF NOT EXISTS etl_example;
USE etl_example;

CREATE TABLE IF NOT EXISTS sample_data (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name  VARCHAR(255),
    age INT,
    city VARCHAR(255),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

INSERT INTO sample_data(name,age,city)VALUES
("jerry",23,"Tamilnadu"),
("kalvin",25,"Bangalore"),
("Edison",30,'Italy'),
("Johnson",55,"India");
"""

