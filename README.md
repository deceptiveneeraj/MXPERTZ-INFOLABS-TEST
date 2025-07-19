Employee Database Management System
A simple Python-based CRUD (Create, Read, Update, Delete) application for managing employee records using MySQL database.

Insert Data: Add new employee records with name, email, position, salary, and city
Update Data: Modify existing employee records with selective field updates
Show Data: Display all employee records in the database
Delete Data: Remove employee records by ID
Interactive Menu: Easy-to-use command-line interface

Prerequists
Python 3.0
MySql

Required package
pip install mysql-connector-python

Set Up Database:

CREATE DATABASE test_db1;

USE test_db1;

CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    position VARCHAR(100) NOT NULL,
    salary INT NOT NULL,
    city VARCHAR(100) NOT NULL
);