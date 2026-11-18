
import sqlite3
from langchain_core import tool


@tool
def create_payment(
    order_id: int,
    payment_method: str,
    payment_amount: float,
    transaction_id: str = None
):
    """Record a payment for an order."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO payments (
            order_id,
            payment_method,
            transaction_id,
            payment_amount
        )
        VALUES (?, ?, ?, ?)
    """, (
        order_id,
        payment_method,
        transaction_id,
        payment_amount
    ))

    conn.commit()
    payment_id = cursor.lastrowid
    conn.close()

    return f"Payment recorded successfully. Payment ID: {payment_id}"


@tool
def get_payment_details(payment_id: int):
    """Retrieve payment details using payment ID."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM payments
        WHERE payment_id = ?
    """, (payment_id,))

    result = cursor.fetchone()
    conn.close()

    return result


@tool
def get_order_payment(order_id: int):
    """Retrieve payment records for a specific order."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM payments
        WHERE order_id = ?
    """, (order_id,))

    result = cursor.fetchall()
    conn.close()

    return result


@tool
def update_payment_status(payment_id: int, payment_status: str):
    """Update the status of a payment."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE payments
        SET payment_status = ?
        WHERE payment_id = ?
    """, (payment_status, payment_id))

    conn.commit()
    updated = cursor.rowcount
    conn.close()

    return "Payment status updated." if updated else "Payment not found."


@tool
def get_payment_status(order_id: int):
    """Check the payment status of an order."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT payment_status
        FROM payments
        WHERE order_id = ?
    """, (order_id,))

    result = cursor.fetchall()
    conn.close()

    return result


payment_tools = [
    create_payment,
    get_payment_details,
    get_order_payment,
    update_payment_status,
    get_payment_status
]
