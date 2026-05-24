CREATE TABLE orders (
    order_id TEXT,
    order_date DATE,
    ship_date DATE,
    customer_id TEXT,
    product_id TEXT,
    region TEXT,
    revenue REAL
);

CREATE TABLE customers (
    customer_id TEXT,
    customer_name TEXT,
    segment TEXT,
    region TEXT
);

CREATE TABLE products (
    product_id TEXT,
    category TEXT,
    sub_category TEXT,
    product_name TEXT
);

CREATE TABLE regions (
    region TEXT,
    state TEXT,
    city TEXT
);