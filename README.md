FastAPI Product Management Application
Overview
This FastAPI application allows users to manage products through a web interface and API endpoints. It includes functionalities for creating, viewing, updating, and deleting products, as well as analyzing product purchases.

Features
Product Management: Company users can create, update, delete, and get all products of their company.
Product Analysis: Company users can view a graph with the number of times each product has been purchased.
Purchase Tracking: Updates product quantity and purchase history upon purchase.
Technology Stack
Backend: FastAPI, Python
Database: MongoDB
Frontend: HTML, JavaScript
Containerization: Docker, Docker Compose

Setup Instructions
Prerequisites
Docker
Docker Compose
git clone <repository-url>
cd <repository-directory>
docker-compose up --build
API Endpoints
Product Management
Create a Product:

Endpoint: POST /api/products/
Request Body: name, description, quantity (Form data)
Response: Created product details
Get All Products:

Endpoint: GET /api/products/
Response: List of all products
Get a Single Product:

Endpoint: GET /api/products/{product_name}
Response: Details of the specified product
Purchase a Product:

Endpoint: PUT /api/products/{product_name}/purchase
Request Body: quantity (JSON)
Response: Updated product details
Get Product Analysis:

Endpoint: GET /api/products/{product_name}/analysis
Response: Analysis of the specified product's purchases
Delete a Product:

Endpoint: DELETE /api/products/{product_name}
Response: Message confirming deletion
