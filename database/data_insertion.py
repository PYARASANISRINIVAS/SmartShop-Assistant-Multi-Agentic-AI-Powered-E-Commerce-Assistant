
import sqlite3

conn = sqlite3.connect("smartshop.db")
cursor = conn.cursor()

cursor.execute("PRAGMA foreign_keys = ON")

try:

    # ==========================================
    # 1. CATEGORIES - 10 RECORDS
    # ==========================================

    cursor.executemany("""
    INSERT INTO categories (category_name, description)
    VALUES (?, ?)
    """, [
        ("Traditional Sweets", "Traditional Indian sweets"),
        ("Milk Sweets", "Sweets prepared using milk"),
        ("Dry Fruit Sweets", "Sweets made using nuts and dry fruits"),
        ("Bengali Sweets", "Traditional Bengali sweets"),
        ("Festival Specials", "Special sweets for festivals"),
        ("South Indian Sweets", "Traditional South Indian sweets"),
        ("Sugar Free Sweets", "Sweets with reduced or no added sugar"),
        ("Snacks", "Traditional Indian snacks"),
        ("Gift Boxes", "Assorted sweet gift boxes"),
        ("Seasonal Specials", "Seasonal sweet varieties")
    ])


    # ==========================================
    # 2. PRODUCTS - 20 RECORDS
    # ==========================================

    cursor.executemany("""
    INSERT INTO products
    (category_id, product_name, description, ingredients,
     price, price_unit, stock_quantity, is_available)
    VALUES (?, ?, ?, ?, ?, ?, ?, ?)
    """, [
        (3, "Kaju Katli", "Cashew-based traditional sweet", "Cashews, Sugar, Ghee", 900, "kg", 25, 1),
        (1, "Mysore Pak", "Traditional South Indian sweet", "Gram Flour, Sugar, Ghee", 600, "kg", 20, 1),
        (2, "Gulab Jamun", "Milk-solid dumplings in sugar syrup", "Milk Solids, Sugar, Cardamom", 300, "kg", 30, 1),
        (4, "Rasgulla", "Soft and spongy Bengali sweet", "Chenna, Sugar, Water", 280, "kg", 18, 1),
        (3, "Badam Halwa", "Rich almond-based sweet", "Almonds, Sugar, Ghee", 1000, "kg", 12, 1),
        (1, "Laddu", "Traditional sweet balls", "Gram Flour, Sugar, Ghee", 400, "kg", 35, 1),
        (4, "Cham Cham", "Bengali milk sweet", "Chenna, Sugar, Milk", 350, "kg", 15, 1),
        (6, "Jangri", "Traditional fried Indian sweet", "Urad Dal, Sugar, Oil", 450, "kg", 10, 1),
        (9, "Dry Fruit Box", "Premium assorted dry fruit sweets", "Cashews, Almonds, Pistachios", 1200, "box", 8, 1),
        (2, "Peda", "Traditional milk-based sweet", "Milk Solids, Sugar, Cardamom", 500, "kg", 0, 0),
        (3, "Anjeer Roll", "Fig-based dry fruit sweet", "Figs, Almonds, Cashews", 850, "kg", 14, 1),
        (4, "Rasmalai", "Cheese patties in flavoured milk", "Milk, Chenna, Sugar", 400, "kg", 0, 0),
        (5, "Kaju Roll", "Cashew-based festival sweet", "Cashews, Sugar, Pistachios", 750, "kg", 16, 1),
        (6, "Ariselu", "Traditional rice flour sweet", "Rice Flour, Jaggery, Sesame", 550, "kg", 22, 1),
        (7, "Sugar Free Kaju Katli", "Reduced-sugar cashew sweet", "Cashews, Sugar Substitute", 950, "kg", 9, 1),
        (8, "Mixture", "Traditional spicy snack mixture", "Besan, Peanuts, Spices", 250, "kg", 40, 1),
        (10, "Mango Peda", "Seasonal mango-flavoured sweet", "Milk Solids, Mango, Sugar", 320, "kg", 12, 1),
        (2, "Kalakand", "Soft milk-based sweet", "Milk, Sugar, Cardamom", 420, "kg", 18, 1),
        (5, "Soan Papdi", "Flaky traditional Indian sweet", "Gram Flour, Sugar, Ghee", 350, "kg", 25, 1),
        (9, "Assorted Sweet Box", "Mixed traditional sweet gift box", "Assorted Sweets, Dry Fruits", 800, "box", 10, 1)
    ])


    # ==========================================
    # 3. CUSTOMERS - 15 RECORDS
    # ==========================================

    cursor.executemany("""
    INSERT INTO customers
    (telegram_user_id, customer_name, phone_number, email)
    VALUES (?, ?, ?, ?)
    """, [
        ("TG10001", "Arjun Kumar", "9000000001", "arjun@example.com"),
        ("TG10002", "Priya Sharma", "9000000002", "priya@example.com"),
        ("TG10003", "Rahul Reddy", "9000000003", "rahul@example.com"),
        ("TG10004", "Sneha Rao", "9000000004", "sneha@example.com"),
        ("TG10005", "Kiran Kumar", "9000000005", "kiran@example.com"),
        ("TG10006", "Ananya Das", "9000000006", "ananya@example.com"),
        ("TG10007", "Vikram Singh", "9000000007", "vikram@example.com"),
        ("TG10008", "Meera Patel", "9000000008", "meera@example.com"),
        ("TG10009", "Rohit Verma", "9000000009", "rohit@example.com"),
        ("TG10010", "Divya Reddy", "9000000010", "divya@example.com"),
        ("TG10011", "Sanjay Rao", "9000000011", "sanjay@example.com"),
        ("TG10012", "Neha Sharma", "9000000012", "neha@example.com"),
        ("TG10013", "Manoj Kumar", "9000000013", "manoj@example.com"),
        ("TG10014", "Pooja Patel", "9000000014", "pooja@example.com"),
        ("TG10015", "Ajay Singh", "9000000015", "ajay@example.com")
    ])


    # ==========================================
    # 4. CUSTOMER ADDRESSES - 15 RECORDS
    # ==========================================

    cursor.executemany("""
    INSERT INTO customer_addresses
    (customer_id, address_line, city, state, pincode, is_default)
    VALUES (?, ?, ?, ?, ?, ?)
    """, [
        (1, "KPHB Phase 1", "Hyderabad", "Telangana", "500072", 1),
        (2, "Madhapur Main Road", "Hyderabad", "Telangana", "500081", 1),
        (3, "Kukatpally Housing Board", "Hyderabad", "Telangana", "500072", 1),
        (4, "Ameerpet", "Hyderabad", "Telangana", "500016", 1),
        (5, "Gachibowli", "Hyderabad", "Telangana", "500032", 1),
        (6, "Secunderabad", "Hyderabad", "Telangana", "500003", 1),
        (7, "Kondapur", "Hyderabad", "Telangana", "500084", 1),
        (8, "Manikonda", "Hyderabad", "Telangana", "500089", 1),
        (9, "Miyapur", "Hyderabad", "Telangana", "500049", 1),
        (10, "Begumpet", "Hyderabad", "Telangana", "500016", 1),
        (11, "Jubilee Hills", "Hyderabad", "Telangana", "500033", 1),
        (12, "Banjara Hills", "Hyderabad", "Telangana", "500034", 1),
        (13, "Nizampet", "Hyderabad", "Telangana", "500090", 1),
        (14, "Hitech City", "Hyderabad", "Telangana", "500081", 1),
        (15, "LB Nagar", "Hyderabad", "Telangana", "500074", 1)
    ])


    # ==========================================
    # 5. ORDERS - 15 RECORDS
    # ==========================================

    cursor.executemany("""
    INSERT INTO orders
    (customer_id, order_status, total_amount,
     delivery_address_id, delivery_type)
    VALUES (?, ?, ?, ?, ?)
    """, [
        (1, "delivered", 1150, 1, "delivery"),
        (2, "delivered", 920, 2, "delivery"),
        (3, "confirmed", 1020, 3, "delivery"),
        (4, "preparing", 980, 4, "delivery"),
        (5, "pending", 1800, 5, "pickup"),
        (6, "cancelled", 850, 6, "delivery"),
        (7, "delivered", 1500, 7, "delivery"),
        (8, "confirmed", 700, 8, "pickup"),
        (9, "delivered", 850, 9, "delivery"),
        (10, "preparing", 500, 10, "delivery"),
        (11, "delivered", 850, 11, "pickup"),
        (12, "pending", 400, 12, "delivery"),
        (13, "confirmed", 750, 13, "delivery"),
        (14, "delivered", 550, 14, "pickup"),
        (15, "delivered", 650, 15, "delivery")
    ])


    # ==========================================
    # 6. ORDER ITEMS - 20 RECORDS
    # ==========================================

    cursor.executemany("""
    INSERT INTO order_items
    (order_id, product_id, quantity, unit_price, subtotal)
    VALUES (?, ?, ?, ?, ?)
    """, [
        (1, 1, 1, 900, 900),
        (1, 16, 1, 250, 250),

        (2, 2, 1, 600, 600),
        (2, 18, 1, 320, 320),

        (3, 3, 2, 300, 600),
        (3, 17, 1, 420, 420),

        (4, 4, 1, 280, 280),
        (4, 13, 1, 700, 700),

        (5, 5, 1, 1000, 1000),
        (5, 20, 1, 800, 800),

        (6, 11, 1, 850, 850),
        (7, 9, 1, 1200, 1200),
        (7, 3, 1, 300, 300),
        (8, 8, 1, 450, 450),
        (8, 2, 0.416667, 600, 250),
        (9, 11, 1, 850, 850),
        (10, 10, 1, 500, 500),
        (11, 15, 1, 850, 850),
        (12, 12, 1, 400, 400),
        (13, 13, 1, 750, 750)
    ])

    # Orders 14 and 15 each have one additional order item.
    cursor.executemany("""
    INSERT INTO order_items
    (order_id, product_id, quantity, unit_price, subtotal)
    VALUES (?, ?, ?, ?, ?)
    """, [
        (14, 14, 1, 550, 550),
        (15, 19, 1, 650, 650)
    ])


    # ==========================================
    # 7. PAYMENTS - 15 RECORDS
    # ==========================================

    cursor.executemany("""
    INSERT INTO payments
    (order_id, payment_method, transaction_id,
     payment_amount, payment_status)
    VALUES (?, ?, ?, ?, ?)
    """, [
        (1, "UPI", "TXN20001", 1150, "successful"),
        (2, "Card", "TXN20002", 920, "successful"),
        (3, "UPI", "TXN20003", 1020, "successful"),
        (4, "UPI", "TXN20004", 980, "successful"),
        (5, "Cash", None, 1800, "pending"),
        (6, "UPI", "TXN20006", 850, "refunded"),
        (7, "Card", "TXN20007", 1500, "successful"),
        (8, "UPI", "TXN20008", 700, "successful"),
        (9, "UPI", "TXN20009", 850, "successful"),
        (10, "Cash", None, 500, "pending"),
        (11, "Card", "TXN20011", 850, "successful"),
        (12, "UPI", "TXN20012", 400, "pending"),
        (13, "UPI", "TXN20013", 750, "successful"),
        (14, "Cash", None, 550, "successful"),
        (15, "Card", "TXN20015", 650, "successful")
    ])


    # ==========================================
    # 8. OFFERS - 10 RECORDS
    # ==========================================

    cursor.executemany("""
    INSERT INTO offers
    (offer_name, description, discount_type,
     discount_value, start_date, end_date, is_active)
    VALUES (?, ?, ?, ?, ?, ?, ?)
    """, [
        ("Diwali Special", "Festival discount on selected sweets", "percentage", 10, "2026-10-15", "2026-11-15", 1),
        ("Welcome Offer", "Discount for new customers", "percentage", 5, "2026-11-01", "2026-12-31", 1),
        ("Premium Box Offer", "Discount on dry fruit boxes", "fixed", 100, "2026-11-01", "2026-11-30", 1),
        ("Summer Offer", "Seasonal promotional offer", "percentage", 15, "2026-04-01", "2026-05-31", 0),
        ("Bulk Purchase", "Discount on bulk purchases", "percentage", 12, "2026-11-01", "2026-12-31", 1),
        ("Weekend Special", "Weekend discount on traditional sweets", "percentage", 8, "2026-11-01", "2026-12-31", 1),
        ("Loyalty Reward", "Special discount for returning customers", "fixed", 50, "2026-11-01", "2026-12-31", 1),
        ("Gift Box Discount", "Discount on assorted sweet boxes", "fixed", 75, "2026-11-01", "2026-12-15", 1),
        ("New Year Offer", "New year promotional discount", "percentage", 20, "2026-12-25", "2027-01-10", 0),
        ("Festival Combo", "Discount on festival sweet combos", "percentage", 10, "2026-10-01", "2026-11-30", 1)
    ])


    # ==========================================
    # 9. COMPLAINTS - 10 RECORDS
    # ==========================================

    cursor.executemany("""
    INSERT INTO complaints
    (customer_id, order_id, complaint_description, complaint_status)
    VALUES (?, ?, ?, ?)
    """, [
        (1, 1, "Product packaging was damaged", "resolved"),
        (2, 2, "Delivery was delayed", "open"),
        (3, 3, "Product quantity was incorrect", "investigating"),
        (4, 4, "Received a different product", "open"),
        (5, 5, "Order confirmation was delayed", "open"),
        (6, 6, "Product quality did not meet expectations", "resolved"),
        (7, 7, "Requested an invoice for the order", "resolved"),
        (8, 8, "Pickup instructions were unclear", "open"),
        (9, 9, "Packaging needs improvement", "investigating"),
        (10, 10, "Product availability information was incorrect", "resolved")
    ])


    # ==========================================
    # 10. SUPPORT TICKETS - 10 RECORDS
    # ==========================================

    cursor.executemany("""
    INSERT INTO support_tickets
    (customer_id, subject, description, priority, ticket_status)
    VALUES (?, ?, ?, ?, ?)
    """, [
        (1, "Product availability", "When will Peda be available?", "low", "open"),
        (2, "Order tracking", "Need an update on my order", "medium", "open"),
        (3, "Payment issue", "Need confirmation of payment", "high", "in_progress"),
        (4, "Refund status", "Please provide refund update", "high", "resolved"),
        (5, "Bulk order enquiry", "Need sweets for a family function", "medium", "open"),
        (6, "Product ingredients", "Need ingredient information for Kaju Katli", "low", "resolved"),
        (7, "Delivery enquiry", "Can my order be delivered earlier?", "medium", "in_progress"),
        (8, "Festival order", "Need to place a large festival order", "high", "open"),
        (9, "Price enquiry", "Need pricing for assorted sweet boxes", "low", "resolved"),
        (10, "Order cancellation", "Need help cancelling my order", "medium", "open")
    ])


    # ==========================================
    # 11. COMMIT ALL INSERTIONS
    # ==========================================

    conn.commit()

    print("All sample records inserted successfully!")


except sqlite3.Error as error:

    conn.rollback()

    print("Insertion failed:", error)


# ==========================================
# 12. VERIFY RECORD COUNTS
# ==========================================

tables = [
    "categories",
    "products",
    "customers",
    "customer_addresses",
    "orders",
    "order_items",
    "payments",
    "offers",
    "complaints",
    "support_tickets"
]

print("\nDATABASE RECORD COUNTS")
print("-" * 35)

for table in tables:

    cursor.execute(f"SELECT COUNT(*) FROM {table}")

    count = cursor.fetchone()[0]

    print(f"{table:<25} {count}")


# ==========================================
# 13. CLOSE CONNECTION
# ==========================================

cursor.close()
conn.close()

print("\nDatabase connection closed!")
