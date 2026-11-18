
import sqlite3
from langchain_core import tool


@tool
def create_complaint(
    customer_id: int,
    complaint_description: str,
    order_id: int = None
):
    """Register a customer complaint."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO complaints (
            customer_id,
            order_id,
            complaint_description
        )
        VALUES (?, ?, ?)
    """, (customer_id, order_id, complaint_description))

    conn.commit()
    complaint_id = cursor.lastrowid
    conn.close()

    return f"Complaint registered successfully. Complaint ID: {complaint_id}"


@tool
def get_complaint_details(complaint_id: int):
    """Retrieve complaint details using complaint ID."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM complaints
        WHERE complaint_id = ?
    """, (complaint_id,))

    result = cursor.fetchone()
    conn.close()

    return result


@tool
def get_customer_complaints(customer_id: int):
    """Retrieve all complaints submitted by a customer."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM complaints
        WHERE customer_id = ?
        ORDER BY created_at DESC
    """, (customer_id,))

    result = cursor.fetchall()
    conn.close()

    return result


@tool
def update_complaint_status(
    complaint_id: int,
    complaint_status: str
):
    """Update the status of a complaint."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE complaints
        SET complaint_status = ?
        WHERE complaint_id = ?
    """, (complaint_status, complaint_id))

    conn.commit()
    updated = cursor.rowcount
    conn.close()

    return "Complaint status updated." if updated else "Complaint not found."


@tool
def create_support_ticket(
    customer_id: int,
    subject: str,
    description: str,
    priority: str = "medium"
):
    """Create a support ticket for a customer."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO support_tickets (
            customer_id,
            subject,
            description,
            priority
        )
        VALUES (?, ?, ?, ?)
    """, (customer_id, subject, description, priority))

    conn.commit()
    ticket_id = cursor.lastrowid
    conn.close()

    return f"Support ticket created successfully. Ticket ID: {ticket_id}"


@tool
def get_support_ticket(ticket_id: int):
    """Retrieve support ticket details using ticket ID."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM support_tickets
        WHERE ticket_id = ?
    """, (ticket_id,))

    result = cursor.fetchone()
    conn.close()

    return result


@tool
def get_customer_support_tickets(customer_id: int):
    """Retrieve all support tickets submitted by a customer."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM support_tickets
        WHERE customer_id = ?
        ORDER BY created_at DESC
    """, (customer_id,))

    result = cursor.fetchall()
    conn.close()

    return result


@tool
def update_ticket_status(ticket_id: int, ticket_status: str):
    """Update the status of a support ticket."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE support_tickets
        SET ticket_status = ?
        WHERE ticket_id = ?
    """, (ticket_status, ticket_id))

    conn.commit()
    updated = cursor.rowcount
    conn.close()

    return "Support ticket status updated." if updated else "Support ticket not found."


support_tools = [
    create_complaint,
    get_complaint_details,
    get_customer_complaints,
    update_complaint_status,
    create_support_ticket,
    get_support_ticket,
    get_customer_support_tickets,
    update_ticket_status
]
