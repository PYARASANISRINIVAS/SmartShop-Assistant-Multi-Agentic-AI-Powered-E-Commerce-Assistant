
import sqlite3
from langchain_core import tool


# ==========================================
# 1. REGISTER CUSTOMER
# ==========================================

@tool
def register_customer(
    telegram_user_id: str,
    customer_name: str,
    phone_number: str,
    email: str
):
    """
    Registers a new customer in the database.
    Stores the customer's name, Telegram user ID, phone number, and email.
    Generates a unique customer ID.
    Used when a new customer interacts with the application and wants to register.
    Helps establish a customer profile for future orders and interactions.
    
    """

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO customers
        (telegram_user_id, customer_name, phone_number, email)
        VALUES (?, ?, ?, ?)
    """, (telegram_user_id, customer_name, phone_number, email))

    conn.commit()
    customer_id = cursor.lastrowid

    conn.close()

    return f"Customer registered successfully. Customer ID: {customer_id}"


# ==========================================
# 2. GET CUSTOMER DETAILS
# ==========================================

@tool
def get_customer_details(customer_id: int):
    """Retrieves the complete customer profile using the unique customer ID.
    Returns customer name, Telegram user ID, phone number, and email.
    Used when the customer requests their profile information or when another agent needs customer details."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM customers
        WHERE customer_id = ?
    """, (customer_id,))

    result = cursor.fetchone()

    conn.close()

    return result if result else "Customer not found."


# ==========================================
# 3. CHECK CUSTOMER EXISTS
# ==========================================

@tool
def check_customer_exists(telegram_user_id: str):
    """Checks whether a customer is already registered using their Telegram user ID.
    Helps identify returning customers.
    Used during customer onboarding and before initiating customer-specific operations.
    Avoids creating duplicate customer profiles for the same Telegram account."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT customer_id, customer_name
        FROM customers
        WHERE telegram_user_id = ?
    """, (telegram_user_id,))

    result = cursor.fetchone()

    conn.close()

    return result if result else "Customer does not exist."


# ==========================================
# 4. UPDATE CUSTOMER DETAILS
# ==========================================

@tool
def update_customer_details(
    customer_id: int,
    customer_name: str,
    phone_number: str,
    email: str
):
    """Updates the existing customer's profile information.
    Supports changes to customer name, phone number, and email.
    Identifies the customer using their unique customer ID.
    Used when customers request changes to their registered information."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE customers
        SET customer_name = ?,
            phone_number = ?,
            email = ?
        WHERE customer_id = ?
    """, (customer_name, phone_number, email, customer_id))

    conn.commit()

    updated = cursor.rowcount

    conn.close()

    return "Customer details updated." if updated else "Customer not found."


# ==========================================
# 5. GET CUSTOMER ADDRESS
# ==========================================

@tool
def get_customer_address(customer_id: int):
    """Retrieves all saved delivery addresses associated with a customer.
    Returns address details, including address line, city, state, pincode, and default-address status.
    Used when customers want to view their saved addresses or select an address for delivery."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM customer_addresses
        WHERE customer_id = ?
    """, (customer_id,))

    result = cursor.fetchall()

    conn.close()

    return result if result else "No addresses found."


# ==========================================
# 6. ADD CUSTOMER ADDRESS
# ==========================================

@tool
def add_customer_address(
    customer_id: int,
    address_line: str,
    city: str,
    state: str,
    pincode: str,
    is_default: int
):
    """Adds a new delivery address to an existing customer profile.
    Stores complete address information and whether it is marked as the default address.
    Allows customers to maintain multiple delivery addresses.
    Used during customer onboarding or when adding a new delivery location."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO customer_addresses
        (customer_id, address_line, city, state, pincode, is_default)
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        customer_id,
        address_line,
        city,
        state,
        pincode,
        is_default
    ))

    conn.commit()

    address_id = cursor.lastrowid

    conn.close()

    return f"Address added successfully. Address ID: {address_id}"


# ==========================================
# 7. GET CUSTOMER ORDER HISTORY
# ==========================================

@tool
def get_customer_order_history(customer_id: int):
    """Retrieves the order history associated with a customer.
    Helps customers review their previous purchases.
    Can provide information about order IDs, dates, order status, and total amounts, depending on the SQL query.
    Used when customers ask about their previous orders."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            order_id,
            order_date,
            order_status,
            total_amount,
            delivery_type
        FROM orders
        WHERE customer_id = ?
        ORDER BY order_date DESC
    """, (customer_id,))

    result = cursor.fetchall()

    conn.close()

    return result if result else "No order history found."


# ==========================================
# CUSTOMER TOOL LIST
# ==========================================

customer_tools = [
    register_customer,
    get_customer_details,
    check_customer_exists,
    update_customer_details,
    get_customer_address,
    add_customer_address,
    get_customer_order_history
]
