
import sqlite3

# ==========================================
# 1. CONNECT TO SQLITE DATABASE
# ==========================================

conn = sqlite3.connect("smartshop.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON")


# ==========================================
# 2. CATEGORIES TABLE
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS categories (
    category_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_name TEXT NOT NULL UNIQUE,
    description TEXT,
    is_active INTEGER DEFAULT 1
)
""")


# ==========================================
# 3. PRODUCTS TABLE
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS products (
    product_id INTEGER PRIMARY KEY AUTOINCREMENT,
    category_id INTEGER NOT NULL,
    product_name TEXT NOT NULL UNIQUE,
    description TEXT,
    ingredients TEXT,
    price REAL NOT NULL CHECK(price >= 0),
    price_unit TEXT NOT NULL,
    stock_quantity INTEGER DEFAULT 0 CHECK(stock_quantity >= 0),
    is_available INTEGER DEFAULT 1,

    FOREIGN KEY (category_id)
        REFERENCES categories(category_id)
)
""")


# ==========================================
# 4. CUSTOMERS TABLE
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS customers (
    customer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    telegram_user_id TEXT UNIQUE,
    customer_name TEXT NOT NULL,
    phone_number TEXT UNIQUE,
    email TEXT UNIQUE
)
""")


# ==========================================
# 5. CUSTOMER ADDRESSES TABLE
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS customer_addresses (
    address_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    address_line TEXT NOT NULL,
    city TEXT NOT NULL,
    state TEXT NOT NULL,
    pincode TEXT NOT NULL,
    is_default INTEGER DEFAULT 0,

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
        ON DELETE CASCADE
)
""")


# ==========================================
# 6. ORDERS TABLE
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS orders (
    order_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    order_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    order_status TEXT DEFAULT 'pending',
    total_amount REAL NOT NULL CHECK(total_amount >= 0),
    delivery_address_id INTEGER,
    delivery_type TEXT DEFAULT 'pickup',

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    FOREIGN KEY (delivery_address_id)
        REFERENCES customer_addresses(address_id)
)
""")


# ==========================================
# 7. ORDER ITEMS TABLE
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS order_items (
    order_item_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    product_id INTEGER NOT NULL,
    quantity REAL NOT NULL CHECK(quantity > 0),
    unit_price REAL NOT NULL CHECK(unit_price >= 0),
    subtotal REAL NOT NULL CHECK(subtotal >= 0),

    FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
        ON DELETE CASCADE,

    FOREIGN KEY (product_id)
        REFERENCES products(product_id)
)
""")


# ==========================================
# 8. PAYMENTS TABLE
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS payments (
    payment_id INTEGER PRIMARY KEY AUTOINCREMENT,
    order_id INTEGER NOT NULL,
    payment_method TEXT NOT NULL,
    transaction_id TEXT UNIQUE,
    payment_amount REAL NOT NULL CHECK(payment_amount >= 0),
    payment_status TEXT DEFAULT 'pending',
    payment_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
)
""")


# ==========================================
# 9. OFFERS TABLE
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS offers (
    offer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    offer_name TEXT NOT NULL,
    description TEXT,
    discount_type TEXT NOT NULL,
    discount_value REAL NOT NULL CHECK(discount_value >= 0),
    start_date TIMESTAMP,
    end_date TIMESTAMP,
    is_active INTEGER DEFAULT 1
)
""")


# ==========================================
# 10. COMPLAINTS TABLE
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS complaints (
    complaint_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    order_id INTEGER,
    complaint_description TEXT NOT NULL,
    complaint_status TEXT DEFAULT 'open',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id),

    FOREIGN KEY (order_id)
        REFERENCES orders(order_id)
)
""")


# ==========================================
# 11. SUPPORT TICKETS TABLE
# ==========================================

cursor.execute("""
CREATE TABLE IF NOT EXISTS support_tickets (
    ticket_id INTEGER PRIMARY KEY AUTOINCREMENT,
    customer_id INTEGER NOT NULL,
    subject TEXT NOT NULL,
    description TEXT,
    priority TEXT DEFAULT 'medium',
    ticket_status TEXT DEFAULT 'open',
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    resolved_at TIMESTAMP,

    FOREIGN KEY (customer_id)
        REFERENCES customers(customer_id)
)
""")


# ==========================================
# 12. COMMIT CHANGES
# ==========================================

conn.commit()

print("SmartShop database created successfully!")


# ==========================================
# 13. VERIFY CREATED TABLES
# ==========================================

cursor.execute("""
SELECT name
FROM sqlite_master
WHERE type = 'table'
ORDER BY name
""")

tables = cursor.fetchall()

print("\nCreated Tables:")

for table in tables:
    print(table[0])


# ==========================================
# 14. CLOSE CONNECTION
# ==========================================

cursor.close()
conn.close()

print("\nDatabase connection closed!")
