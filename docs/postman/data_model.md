# Data Model

## Entities

### Product
- Source: GET /products/{id}
- Fields: id, name, description, price, is_location_offer, co2_rating, in_stock, is_eco_friendly, product_image. category, brand
- Belongs to one category and one brand
- Notes: Price is in floating numbers.

### Category
- Source: GET /categories
- Fields: id, name, slug
- Notes: No sub categories

### Brand
- Source: GET /brands
- Fields: id, name
- One brand has many products

### User
- Source: GET /users/me
- Fields: id, provider, first_name, last_name, phone, email, totp_enabled, created_at, address
- Notes: password should never appear in any response.

### Cart / Cart Item
- Source: {{baseUrl}}/carts/{{cartId}}
- A cart belongs to one user (or is anonymous until login) and holds many cart items
- Cart item = product + quantity

### Invoice (the order)
- Source: {{baseUrl}}/invoices/
- Fields: id, user_id, invoice number, status, total, subtotal, billing_street, billing_city, billing_state, billing_country, billing_postal_code, additional_discount_percentage, additional_discount_amount, invoicelines
- Belongs to one user

### Invoice Item
- Product, id, name, price, co2_rating, in_stock, is_eco_friendly, product_image, quantity, unit price, invoice_id, product_id, discount_percentage, discounted_price
- Belongs to one invoice


## Relationships

User ──< Cart ──< Cart Item >── Product >── Category
 │                                  └──── Brand
 └──< Invoice ──< Invoice Item >── Product
          └── Payment, billing address

(──< means one-to-many)



## Consistency rules (these become my DB checks)
1. Invoice total = sum of (unit price x quantity) of its invoice items.
2. Every invoice item points to a product that exists.
3. Every invoice belongs to a user that exists.
4. Email addresses are unique across users.
5. No API response contains a plain-text password.
6. Cart item quantity is always 1 or more.
7. [FILL: one rule I thought of myself]