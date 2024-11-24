# Catering Service Management System

This project is a **Catering Service Management System**, built with **Flask** and **SQLAlchemy**, providing an easy-to-use web interface for managing catering bookings, event details, and administrative tasks. The system is designed for both **admins** and **users**, offering a complete workflow from login to booking confirmation, including SMS notifications.

---

## Features

### User Features
- **Login and Authentication**:
  - Separate roles for *admin* and *user* with distinct functionalities.
- **Contact Information Collection**:
  - Full name, address, and phone number validation.
- **Event Details Submission**:
  - Users can specify event type, date, time, guest count, and more.
  - Validation to check for already booked dates.
- **Menu and Setup Details**:
  - Customizable menu options including service type, food packages, and meal types.
  - Event setup customization (chair type, table type, theme suggestions).
- **SMS Notification**:
  - Automatic SMS notifications upon successful booking.

### Admin Features
- **View All Bookings**:
  - Admin can view all existing bookings.
- **Delete Bookings**:
  - Admin can delete bookings by selecting the event date.

---

## Prerequisites

1. **Python 3.7+**
2. **Flask** and **SQLAlchemy**
3. **SQLite** for the database
4. **Requests** library for SMS API integration

Install dependencies using:
```bash
pip install -r requirements.txt
```

---

## Setup

1. **Clone the Repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>
   ```

2. **Install Dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**:
   - Initialize the database:
     ```bash
     python app.py
     ```
   - Start the Flask development server:
     ```bash
     python app.py
     ```

4. **Access the Application**:
   - Open a browser and go to `http://127.0.0.1:5000`.

---

## Default Login Credentials

### Admin
- **Username**: `admin`
- **Password**: `admin`

### User
- **Username**: `user`
- **Password**: `user`

---

## SMS Integration

The application uses an API to send SMS notifications upon successful booking. Make sure to configure the SMS API endpoint in the `send_sms` function.

---

## Database Structure

The `CateringBooking` model has the following fields:
- `id` (Primary Key)
- `full_name`, `address`, `phone_number`
- `event_date`, `event_time`, `guest_count`, `event_place`, `event_type`
- `service_type`, `food_package`, `meal_type`
- `chair_type`, `table_type`, `theme_suggestion`, `additional_suggestion`

---

## Directory Structure

```
catering_service/
│
├── app.py               # Main application script
├── templates/           # HTML templates for Flask
│   ├── login.html
│   ├── user_contact.html
│   ├── event_details.html
│   ├── menu_details.html
│   ├── setup_details.html
│   └── admin.html
├── static/              # Static assets (CSS, JS, Images)
├── requirements.txt     # Python dependencies
├── catering_service.db  # SQLite database file (created after first run)
└── README.md            # This file
```

---

## Key Endpoints

| Endpoint                  | Method | Description                       |
|---------------------------|--------|-----------------------------------|
| `/`                       | GET    | Login page                       |
| `/authenticate`           | POST   | User authentication              |
| `/user/contact`           | GET/POST | User contact information form    |
| `/user/event`             | GET/POST | Event details submission         |
| `/user/menu`              | GET/POST | Menu selection                   |
| `/user/setup`             | GET/POST | Event setup details              |
| `/admin`                  | GET/POST | Admin panel                      |

---

## Flash Messages

| Message Code           | Description                                   |
|------------------------|-----------------------------------------------|
| `LOGIN_FAILED`         | Invalid username or password.                |
| `SUCCESS_BOOKING`      | Booking successful.                          |
| `SUCCESS_DELETION`     | Booking deleted successfully.                |
| `ERROR_DATE_BOOKED`    | Catering service already booked for this date.|

---

## Future Enhancements

- Add email notification support.
- Implement user registration and profile management.
- Enhance the admin panel with filtering and sorting options.
- Support for payment integration.

---

## License

This project is licensed under the MIT License. See the LICENSE file for details.
