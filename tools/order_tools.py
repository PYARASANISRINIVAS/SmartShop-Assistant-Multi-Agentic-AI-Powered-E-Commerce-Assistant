
import sqlite3
from langchain_core import tool


@tool
def create_order(
    customer_id: int,
    total_amount: float,
    delivery_address_id: int,
    delivery_type: str
):
    """Create a new order for a customer."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO orders (
            customer_id, total_amount,
            delivery_address_id, delivery_type
        )
        VALUES (?, ?, ?, ?)
    """, (
        customer_id,
        total_amount,
        delivery_address_id,
        delivery_type
    ))

    conn.commit()
    order_id = cursor.lastrowid
    conn.close()

    return f"Order created successfully. Order ID: {order_id}"


@tool
def add_order_item(
    order_id: int,
    product_id: int,
    quantity: float,
    unit_price: float
):
    """Add a product to an existing order."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    subtotal = quantity * unit_price

    cursor.execute("""
        INSERT INTO order_items (
            order_id, product_id, quantity,
            unit_price, subtotal
        )
        VALUES (?, ?, ?, ?, ?)
    """, (
        order_id,
        product_id,
        quantity,
        unit_price,
        subtotal
    ))

    conn.commit()
    conn.close()

    return "Product added to order successfully."


@tool
def get_order_details(order_id: int):
    """Retrieve the details of a specific order."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM orders
        WHERE order_id = ?
    """, (order_id,))

    result = cursor.fetchone()
    conn.close()

    return result


@tool
def get_order_items(order_id: int):
    """Retrieve all products included in an order."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            oi.order_item_id,
            p.product_name,
            oi.quantity,
            oi.unit_price,
            oi.subtotal
        FROM order_items oi
        JOIN products p
            ON oi.product_id = p.product_id
        WHERE oi.order_id = ?
    """, (order_id,))

    result = cursor.fetchall()
    conn.close()

    return result


@tool
def get_customer_orders(customer_id: int):
    """Retrieve all orders placed by a customer."""

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

    return result


@tool
def update_order_status(order_id: int, order_status: str):
    """Update the status of an order."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE orders
        SET order_status = ?
        WHERE order_id = ?
    """, (order_status, order_id))

    conn.commit()
    updated = cursor.rowcount
    conn.close()

    return "Order status updated." if updated else "Order not found."


order_tools = [
    create_order,
    add_order_item,
    get_order_details,
    get_order_items,
    get_customer_orders,
    update_order_status
]