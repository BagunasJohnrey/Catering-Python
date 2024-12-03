# Catering Service Management System

This project is a **Catering Service Management System**, built with **Flask** and **SQLAlchemy**, providing an easy-to-use web interface for managing catering bookings, event details, and administrative tasks. The system is designed for both **admins** and **users**, offering a complete workflow from login to booking confirmation, including SMS notifications.

---


## Python Concepts and Libraries Used in the Catering Booking System

### 1. **Flask Framework**
- **Web Framework**: Flask is a lightweight web framework that simplifies web application development. It is used to handle HTTP routing, request processing, and rendering HTML templates.
- **Routing**: Routes are defined using the `@app.route` decorator in Flask. These routes handle user requests and return responses. Common routes include `/`, `/user/contact`, and `/admin`, each corresponding to different application functionalities.

### 2. **SQLAlchemy**
- **ORM (Object-Relational Mapping)**: SQLAlchemy is utilized to interact with the SQLite database. It allows defining Python models (like `CateringBooking`) that are mapped to database tables. SQLAlchemy abstracts SQL queries and allows data manipulation using Python objects.
- **Database Operations**: SQLAlchemy handles session management and database transactions, like `db.session.add(booking)` and `db.session.commit()`, to add and commit records to the database.

### 3. **Session Management**
- **User Sessions**: Flask provides session management, enabling the storage of user-specific data temporarily across requests. Data such as user contact info, event details, and menu selections are stored in the session and retrieved as needed.
- **Security**: The session is cleared after the user logs out to ensure no sensitive information remains accessible.

### 4. **Form Handling and Validation**
- **HTML Forms**: HTML forms are used to collect user input for various steps in the booking process. Flask’s `request` object captures form data sent by the user.
- **Validation**: Basic form validation is applied to ensure that fields like phone numbers contain only digits, and that mandatory fields are filled before the form can be submitted.

### 5. **Flash Messages**
- **User Feedback**: The `flash()` function in Flask is used to display real-time feedback to the user, such as confirmation messages after a booking or error alerts. This enhances the user experience by giving clear feedback on their actions.

### 6. **External API Integration**
- **SMS Notifications**: The `requests` library is used to interact with an external SMS API (e.g., Twilio) to send SMS notifications when a user successfully completes a booking. This showcases how the application can communicate with third-party services.

### 7. **HTML Templating**
- **Jinja2 Templating Engine**: Flask uses Jinja2 for rendering dynamic HTML templates. Templates are populated with data (like user input or session data) and used to generate personalized user interfaces for login, booking, and admin views.

### 8. **Error Handling**
- **Exception Handling**: The application includes basic exception handling to catch errors, such as issues during database operations or API requests. This ensures that the application gracefully handles issues and provides meaningful feedback to users when errors occur.

### 9. **Environment Configuration**
- **Environment Variables**: The application uses `os.urandom(24)` to generate a secret key for session management, which is crucial for securing the application and preventing session hijacking.

### 10. **Database Initialization**
- **Database Creation**: The `create_database()` function initializes the SQLite database and creates necessary tables based on the defined models (like `CateringBooking`). This setup is executed when the application starts, ensuring the database is ready for use.

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

---

## Sustainable Development Goals (SDGs) Integration

This **Catering Service Management System** integrates multiple Sustainable Development Goals (SDGs) into its design and functionality. The selected goals focus on promoting health, sustainability, and climate action in the catering industry. Below is an explanation of the chosen SDGs and their integration into the project:

### **SDG 3: Good Health and Well-being**
**Objective:** Ensure healthy lives and promote well-being for all at all ages.  
**Implementation in the Project:**
- The system promotes healthy eating habits by providing **vegetarian**, **vegan**, and **gluten-free food packages** as part of the menu options.
- These options are highlighted as healthier alternatives for users, encouraging better nutritional choices for their events.
- This feature directly aligns with improving well-being through better dietary practices.

### **SDG 12: Responsible Consumption and Production**
**Objective:** Ensure sustainable consumption and production patterns.  
**Implementation in the Project:**
- The system encourages **eco-friendly practices**, such as using **biodegradable tableware** and sourcing ingredients from **sustainable farms**.
- Event details include options for users to suggest themes or setups that prioritize minimal waste and sustainable materials.
- By emphasizing efficient resource use, the project aligns with SDG 12 to reduce the environmental impact of catering events.

### **SDG 13: Climate Action**
**Objective:** Take urgent action to combat climate change and its impacts.  
**Implementation in the Project:**
- The catering service prioritizes **locally sourced ingredients**, reducing the carbon emissions associated with long-distance transportation.
- The inclusion of **plant-based meal options** helps lower the environmental impact of livestock farming, which contributes significantly to greenhouse gas emissions.
- The system minimizes the carbon footprint by incorporating sustainable catering methods into its service offerings.

---

### Admin Features
- **View All Bookings**:
  - Admin can view all existing bookings.
- **Delete Bookings**:
  - Admin can delete, sort, and update bookings by selecting the event date.

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
     python main.py
     ```
   - Start the Flask development server:
     ```bash
     python main.py
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
├── static/              # Static assets (CSS, JS, Images, Videos)
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

## License

This project is licensed under the MIT License. See the LICENSE file for details.
