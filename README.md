# Little Lemon – Django REST API Capstone

This project is a restaurant management API developed using Django REST Framework and MySQL.

## API Endpoints

### Menu API

- `GET /restaurant/menu/` – View all menu items.
- `GET /restaurant/menu/<id>/` – View a specific menu item.
- `POST /restaurant/menu/` – Add a menu item.
- `PUT /restaurant/menu/<id>/` – Update a menu item.
- `DELETE /restaurant/menu/<id>/` – Delete a menu item.

### Table Booking API

- `GET /restaurant/booking/tables/` – View all bookings.
- `POST /restaurant/booking/tables/` – Create a booking.
- `PUT /restaurant/booking/tables/<id>/` – Update a booking.
- `DELETE /restaurant/booking/tables/<id>/` – Delete a booking.

### User Authentication

- `POST /auth/users/` – Register a new user.
- `POST /auth/token/login/` – Obtain an authentication token.
- `POST /auth/token/logout/` – Log out.

## Testing

Use **Insomnia REST Client** to test the API endpoints.

For authenticated requests, include:

`Authorization: Token <your_auth_token>`
