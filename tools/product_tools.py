
import sqlite3
from langchain_core.tools import tool


# ==========================================
# 1. GET ALL PRODUCTS
# ==========================================


@tool
def get_all_products():
    """
    Retrieve the complete list of products available in the shop.

    Use this tool when the customer wants to:
    - View all products available in the shop.
    - Browse the complete product catalogue.
    - Know what products the shop sells.
    - Explore available sweets and other product categories.

    """
    print(" Tools working : get_all_products ")
    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM products")

    result = cursor.fetchall()
    conn.close()

    if not result:
        return "No matching products found."
    return result



# ==========================================
# 2. GET PRODUCT BY ID
# ==========================================

@tool
def get_product_by_id(product_id: int):
    """
    Retrieve complete product information using its unique product ID.

    Use this tool when:
    - A product ID is already available.
    - An internal operation requires retrieving a product by ID.
    - The customer explicitly provides a product ID and requests its details.

    """

    print(" Tools working : get_product_by_id ")

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM products WHERE product_id = ?",
        (product_id,)
    )

    result = cursor.fetchone()

    conn.close()

    if not result:
        return "No matching products found."

    return result


# ==========================================
# 3. GET PRODUCT BY NAME
# ==========================================

@tool
def get_product_by_name(product_name: str):
    """
    Retrieve complete product information using its exact product name.

    Use this tool when the customer wants:
    - Complete details about a specific product.
    - General information about a particular sweet.
    - Product details including price, ingredients, description,
      stock quantity and availability.
    """
    print(" Tools working : get_product_by_name ")

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM products WHERE product_name = ?",
        (product_name,)
    )

    result = cursor.fetchone()

    conn.close()

    if result is None:
        return f"No product found with name: {product_name}"
    
    return result 


# ==========================================
# 4. GET PRODUCTS BY CATEGORY
# ==========================================

@tool
def get_products_by_category(category_id: int):
    """Retrieve all products belonging to a particular product category.

    Use this tool when the customer wants to:
    - View products from a specific category.
    - Browse all sweets belonging to a particular category.
    - Explore products associated with a known category ID.

    """
    print(" Tools working : get_product_by_category")

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM products WHERE category_id = ?",
        (category_id,)
    )

    result = cursor.fetchall()

    conn.close()

    if not result:
        return "No matching products found."

    return result





# ==========================================
# 5. CHECK PRODUCT AVAILABILITY
# ==========================================

@tool
def check_product_availability(product_name: str):
    """
    Check whether a specific product is available for purchase and
    retrieve its current stock quantity.

    Use this tool whenever the customer asks:
    - Is this product available?
    - Do you have this sweet in stock?
    - Is this item currently in stock?
    - How much stock is available?
    - Can I purchase this particular product?



    If the product does not exist under the provided exact name,
    no record is returned.

    Interpret is_available = 1 as available and is_available = 0
    as unavailable.

    Never claim that a product is available without checking this tool.
    Do not use this tool for price-related queries.
    """
    print(" Tools working : check_product_availability ")

    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT is_available, stock_quantity FROM products WHERE product_name = ?",
        (product_name,)
    )

    result = cursor.fetchone()

    conn.close()
    if not result:
        return "No matching products found."

    return result


# ==========================================
# 7. SEARCH PRODUCTS
# ==========================================

@tool
def search_product(keyword: str):
    """
    Search the product catalogue using a partial product name or keyword.

    Use this tool when the customer wants to:
    - Search for a product by its name.
    - Find products using only part of a product name.
    - Search for products when the exact product name is unknown.
    - Find products matching a keyword.
    - Search for a product when the customer misspells its name.

    If no matching products are found, an empty list is returned.

    For example:
        keyword = "Kaju"
        This can match products such as "Kaju Katli".

    Use this tool when the exact product name is unknown or when
    searching for partial names.

    """
    print("Tool working : search_product ")
    conn = sqlite3.connect("database/smartshop.db")
    cursor = conn.cursor()

    cursor.execute(
        "SELECT * FROM products WHERE product_name LIKE ?",
        (f"%{keyword}%",)
    )

    result = cursor.fetchall()

    conn.close()
    if not result:
        return "No matching products found."

    return result


product_tools = [
    get_all_products,
    get_product_by_id,
    get_product_by_name,
    get_products_by_category,
    check_product_availability,
    search_product]

