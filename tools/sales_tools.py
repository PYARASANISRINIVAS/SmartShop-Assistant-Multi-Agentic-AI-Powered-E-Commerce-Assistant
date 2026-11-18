
import sqlite3
from langchain_core import tool


@tool
def get_total_sales():
    """Calculate the total revenue from all orders."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(total_amount)
        FROM orders
        WHERE order_status != 'cancelled'
    """)

    result = cursor.fetchone()
    conn.close()

    return result[0] if result[0] is not None else 0


@tool
def get_sales_by_date(date: str):
    """Get total sales for a specific date. Date format: YYYY-MM-DD."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(total_amount)
        FROM orders
        WHERE DATE(order_date) = ?
        AND order_status != 'cancelled'
    """, (date,))

    result = cursor.fetchone()
    conn.close()

    return result[0] if result[0] is not None else 0


@tool
def get_sales_by_month(year: int, month: int):
    """Get total sales for a specific month and year."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT SUM(total_amount)
        FROM orders
        WHERE STRFTIME('%Y', order_date) = ?
        AND STRFTIME('%m', order_date) = ?
        AND order_status != 'cancelled'
    """, (str(year), f"{month:02d}"))

    result = cursor.fetchone()
    conn.close()

    return result[0] if result[0] is not None else 0


@tool
def get_sales_by_product():
    """Get total quantity sold and revenue for each product."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            p.product_name,
            SUM(oi.quantity),
            SUM(oi.subtotal)
        FROM order_items oi
        JOIN products p
            ON oi.product_id = p.product_id
        JOIN orders o
            ON oi.order_id = o.order_id
        WHERE o.order_status != 'cancelled'
        GROUP BY p.product_id, p.product_name
        ORDER BY SUM(oi.subtotal) DESC
    """)

    result = cursor.fetchall()
    conn.close()

    return result


@tool
def get_top_selling_products(limit: int = 5):
    """Get the top-selling products based on quantity sold."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            p.product_name,
            SUM(oi.quantity) AS total_quantity
        FROM order_items oi
        JOIN products p
            ON oi.product_id = p.product_id
        JOIN orders o
            ON oi.order_id = o.order_id
        WHERE o.order_status != 'cancelled'
        GROUP BY p.product_id, p.product_name
        ORDER BY total_quantity DESC
        LIMIT ?
    """, (limit,))

    result = cursor.fetchall()
    conn.close()

    return result


@tool
def get_order_count():
    """Get the total number of non-cancelled orders."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT COUNT(*)
        FROM orders
        WHERE order_status != 'cancelled'
    """)

    result = cursor.fetchone()
    conn.close()

    return result[0]


sales_tools = [
    get_total_sales,
    get_sales_by_date,
    get_sales_by_month,
    get_sales_by_product,
    get_top_selling_products,
    get_order_count
]
