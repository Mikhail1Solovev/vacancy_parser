import csv
from datetime import datetime
import psycopg2

# Исходные данные для заполнения таблиц
with open('customers_data.csv', newline='') as file:
    customers_data = [row for row in csv.reader(file) if 'customer_id' not in row]

with open('employees_data.csv', newline='') as file:
    employees_data = [row for row in csv.reader(file) if 'first_name' not in row]

# Создайте подключение к базе данных
conn = psycopg2.connect(host="sql_db", port=5432, dbname="analysis", user="simple", password="qweasd963")

# Открытие курсора
cur = conn.cursor()

# Не меняйте и не удаляйте эти строки - они нужны для проверки
cur.execute("create schema if not exists itresume2936;")
cur.execute("DROP TABLE IF EXISTS itresume2936.orders")
cur.execute("DROP TABLE IF EXISTS itresume2936.customers")
cur.execute("DROP TABLE IF EXISTS itresume2936.employees")

# Ниже напишите код запросов для создания таблиц
cur.execute("""
CREATE TABLE itresume2936.customers (
    customer_id CHAR(5) PRIMARY KEY,
    company_name VARCHAR(100) NOT NULL,
    contact_name VARCHAR(100) NOT NULL
);
""")

cur.execute("""
CREATE TABLE itresume2936.employees (
    employee_id SERIAL PRIMARY KEY,
    first_name VARCHAR(25) NOT NULL,
    last_name VARCHAR(35) NOT NULL,
    title VARCHAR(100),
    birth_date DATE NOT NULL,
    notes TEXT
);
""")

cur.execute("""
CREATE TABLE itresume2936.orders (
    order_id SERIAL PRIMARY KEY,
    customer_id CHAR(5) REFERENCES itresume2936.customers(customer_id) NOT NULL,
    employee_id INTEGER REFERENCES itresume2936.employees(employee_id) NOT NULL,
    order_date DATE NOT NULL,
    ship_city VARCHAR(100) NOT NULL
);
""")

# Зафиксируйте изменения в базе данных
conn.commit()

# Устанавливаем начальное значение для последовательности order_id перед вставкой данных
cur.execute("ALTER SEQUENCE itresume2936.orders_order_id_seq RESTART WITH 11077;")

# Теперь приступаем к операциям вставок данных
for data in customers_data:
    cur.execute(
        "INSERT INTO itresume2936.customers (customer_id, company_name, contact_name) VALUES (%s, %s, %s) RETURNING *",
        data)
conn.commit()
res_customers = cur.fetchall()

for data in employees_data:
    birth_date = datetime.strptime(data[3], "%Y-%m-%d").date()
    cur.execute(
        "INSERT INTO itresume2936.employees (first_name, last_name, title, birth_date, notes) VALUES (%s, %s, %s, %s, %s) RETURNING *",
        (data[0], data[1], data[2], birth_date, data[4]))
conn.commit()
res_employees = cur.fetchall()

with open('orders_data.csv', newline='') as file:
    orders_data = [row for row in csv.reader(file) if 'order_id' not in row]
    for data in orders_data:
order_date = datetime.strptime(data[3], "%Y-%m-%d").date()
cur.execute(
    "INSERT INTO itresume2936.orders (customer_id, employee_id, order_date, ship_city) VALUES (%s, %s, %s, %s) RETURNING *",
    (data[1], int(data[2]), order_date, data[4]))

conn.commit()
res_orders = cur.fetchall()

# Закрытие курсора
cur.close()

# Закрытие соединения
conn.close()
