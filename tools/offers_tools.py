
import sqlite3
from langchain_core import tool


@tool
def get_all_offers():
    """Retrieve all available offers."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM offers
    """)

    result = cursor.fetchall()
    conn.close()

    return result


@tool
def get_active_offers():
    """Retrieve currently active offers."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM offers
        WHERE is_active = 1
        AND (start_date IS NULL OR start_date <= CURRENT_TIMESTAMP)
        AND (end_date IS NULL OR end_date >= CURRENT_TIMESTAMP)
    """)

    result = cursor.fetchall()
    conn.close()

    return result


@tool
def get_offer_by_id(offer_id: int):
    """Retrieve offer details using offer ID."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        SELECT *
        FROM offers
        WHERE offer_id = ?
    """, (offer_id,))

    result = cursor.fetchone()
    conn.close()

    return result


@tool
def add_offer(
    offer_name: str,
    description: str,
    discount_type: str,
    discount_value: float,
    start_date: str,
    end_date: str
):
    """Create a new offer."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        INSERT INTO offers (
            offer_name,
            description,
            discount_type,
            discount_value,
            start_date,
            end_date
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, (
        offer_name,
        description,
        discount_type,
        discount_value,
        start_date,
        end_date
    ))

    conn.commit()
    offer_id = cursor.lastrowid
    conn.close()

    return f"Offer created successfully. Offer ID: {offer_id}"


@tool
def update_offer_status(offer_id: int, is_active: int):
    """Activate or deactivate an offer. Use 1 for active and 0 for inactive."""

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE offers
        SET is_active = ?
        WHERE offer_id = ?
    """, (is_active, offer_id))

    conn.commit()
    updated = cursor.rowcount
    conn.close()

    return "Offer status updated." if updated else "Offer not found."


offer_tools = [
    get_all_offers,
    get_active_offers,
    get_offer_by_id,
    add_offer,
    update_offer_status
]
