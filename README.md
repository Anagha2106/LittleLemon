# Little Lemon – Django REST API Capstone

A restaurant management API developed using **Django REST Framework and MySQL**. The project provides menu management, table booking, user registration, and token-based authentication.

## Features

- View, add, update, and delete menu items.
- Create and manage table bookings.
- User registration and authentication using Djoser.
- Token-based authentication for protected endpoints.
- MySQL database integration.
- Django REST Framework Browsable API.
- Unit testing for models and API views.

## Technologies Used

- Python
- Django
- Django REST Framework
- Djoser
- MySQL
- Token Authentication

## Project Structure

```text
Littlelemon/
├── littlelemon/
│   ├── settings.py
│   └── urls.py
├── restaurant/
│   ├── migrations/
│   ├── tests/
│   │   ├── test_models.py
│   │   └── test_views.py
│   ├── admin.py
│   ├── apps.py
│   ├── forms.py
│   ├── menu_urls.py
│   ├── models.py
│   ├── serializers.py
│   ├── urls.py
│   └── views.py
├── static/
├── templates/
│   └── index.html
├── manage.py
└── requirements.txt
```

## API Endpoints

### 1. Homepage

| Method | Endpoint | Description |
|:---:|---|---|
| GET | `/restaurant/` | View the homepage |

### 2. Menu API

| Method | Endpoint | Description |
|:---:|---|---|
| GET | `/restaurant/menu/items/` | View all menu items |
| POST | `/restaurant/menu/items/` | Add a menu item |
| GET | `/restaurant/menu/items/<id>/` | View a specific menu item |
| PUT | `/restaurant/menu/items/<id>/` | Update a menu item |
| PATCH | `/restaurant/menu/items/<id>/` | Partially update a menu item |
| DELETE | `/restaurant/menu/items/<id>/` | Delete a menu item |

### 3. Table Booking API

| Method | Endpoint | Description |
|:---:|---|---|
| GET | `/restaurant/booking/tables/` | View all bookings |
| POST | `/restaurant/booking/tables/` | Create a booking |
| GET | `/restaurant/booking/tables/<id>/` | View a specific booking |
| PUT | `/restaurant/booking/tables/<id>/` | Update a booking |
| DELETE | `/restaurant/booking/tables/<id>/` | Delete a booking |

**Note:** The Booking API requires authentication.

### 4. User Authentication

| Method | Endpoint | Description |
|:---:|---|---|
| POST | `/auth/users/` | Register a new user |
| POST | `/auth/token/login/` | Obtain an authentication token |
| POST | `/auth/token/logout/` | Log out |

### 5. Token Authentication

| Method | Endpoint | Description |
|:---:|---|---|
| POST | `/restaurant/api-token-auth/` | Obtain an authentication token |

For authenticated requests, include the following header:

```http
Authorization: Token <your_auth_token>
```

## Database Models

The project contains two database models:

### Menu

| Field | Description |
|---|---|
| `title` | Name of the menu item |
| `price` | Price of the menu item |
| `inventory` | Available quantity |

### Booking

| Field | Description |
|---|---|
| `name` | Name of the person making the booking |
| `no_of_guests` | Number of guests |
| `booking_date` | Date of the booking |

Both models are registered in the Django administration panel.

## Testing

The project includes unit tests for database models and API views.

Run the tests using:

```bash
python manage.py test restaurant
```

The test cases cover:

- Menu model representation.
- Booking model representation.
- Retrieving all menu items.
- Creating a menu item.

## API Testing

The API endpoints can be tested using:

- **Django REST Framework Browsable API**
- **Insomnia REST Client**

For protected booking endpoints, obtain an authentication token and include it in the request headers:

```http
Authorization: Token <your_auth_token>
```

## GitHub Repository

[Little Lemon – Django REST API](https://github.com/Anagha2106/LittleLemon)

---

**Developed using Django REST Framework, Python, and MySQL.**
