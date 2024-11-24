from flask import Flask, render_template, request, redirect, url_for, flash, session, jsonify
from flask_sqlalchemy import SQLAlchemy
import os
import requests

# App Configuration
app = Flask(__name__)
app.secret_key = os.urandom(24)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///catering_service.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# Constants
ADMIN_PASSWORD = 'admin'
USER_PASSWORD = 'user'
MESSAGES = {
    'LOGIN_FAILED': "Invalid username or password.",
    'SUCCESS_BOOKING': "Catering service booked successfully!",
    'SUCCESS_DELETION': "Booking deleted successfully.",
    'ERROR_DATE_BOOKED': "Catering services are already booked for this date.",
}

# Models
class CateringBooking(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    full_name = db.Column(db.String(100), nullable=False)
    address = db.Column(db.String(255), nullable=False)
    phone_number = db.Column(db.String(15), nullable=False)
    event_date = db.Column(db.String(10), nullable=False)  # Format: YYYY-MM-D
    event_time = db.Column(db.String(10), nullable=False)
    guest_count = db.Column(db.Integer, nullable=False)
    event_place = db.Column(db.String(255), nullable=False)
    event_type = db.Column(db.String(50), nullable=False)
    service_type = db.Column(db.String(50), nullable=False)
    food_package = db.Column(db.String(100), nullable=False)
    meal_type = db.Column(db.String(50), nullable=False)
    theme_suggestion = db.Column(db.String(255), nullable=True)
    chair_type = db.Column(db.String(50), nullable=False)  # New field for chair type
    table_type = db.Column(db.String(50), nullable=False)  # New field for table type
    additional_suggestion = db.Column(db.String(255), nullable=True)  # New field for additional suggestion

# Database Initialization
def create_database():
    with app.app_context():
        db.create_all()

# Helper Functions
def is_date_booked(event_date):
    return CateringBooking.query.filter_by(event_date=event_date).first() is not None

def get_booking_by_date(event_date):
    return CateringBooking.query.filter_by(event_date=event_date).first()

def send_sms(phone_number, full_name, event_date, event_time, guest_count, event_place, event_type, service_type, food_package, meal_type, chair_type, table_type, theme_suggestion=None, additional_suggestion=None):
    # Construct the detailed message
    default_message = (
        f"Hello {full_name},\n"
        f"Your catering service has been booked successfully!\n\n"
        f"Event Details:\n"
        f"- Event Date: {event_date}\n"
        f"- Event Time: {event_time}\n"
        f"- Guest Count: {guest_count}\n"
        f"- Event Place: {event_place}\n"
        f"- Event Type: {event_type}\n"
        f"- Service Type: {service_type}\n"
        f"- Food Package: {food_package}\n"
        f"- Meal Type: {meal_type}\n"
        f"- Chair Type: {chair_type}\n"
        f"- Table Type: {table_type}\n"
    )
    
    # Add optional suggestions if provided
    if theme_suggestion:
        default_message += f"- Theme Suggestion: {theme_suggestion}\n"
    if additional_suggestion:
        default_message += f"- Additional Suggestions: {additional_suggestion}\n"
    
    # Finalize the message
    default_message += "\nWe look forward to making your event special!"

    try:
        api_url = f'https://api.kenliejugarap.com/freesmslbc/?number={phone_number}&message={default_message}'
        response = requests.get(api_url)
        return response.status_code == 200
    except Exception as error:
        print('Error sending SMS:', error)
        return False

# Routes
@app.route('/')
def login():
    return render_template('login.html')

@app.route('/authenticate', methods=['POST'])
def authenticate():
    username = request.form['username']
    password = request.form['password']
    if username == 'admin' and password == ADMIN_PASSWORD:
        session['role'] = 'admin'
        return redirect(url_for('admin_panel'))
    elif username == 'user' and password == USER_PASSWORD:
        session['role'] = 'user'
        return redirect(url_for('user_contact'))
    else:
        flash(MESSAGES['LOGIN_FAILED'], 'error')
        return redirect(url_for('login'))

@app.route('/user/contact', methods=['GET', 'POST'])
def user_contact():
    if request.method == 'POST':
        full_name = request.form['full_name']
        address = request.form['address']
        phone_number = request.form['phone_number']
        
        # Validate that the phone number contains only digits
        if not phone_number.isdigit():
            return render_template('user_contact.html', 
                                   error="Phone number must contain only digits.",
                                   full_name=full_name,
                                   address=address,
                                   phone_number=phone_number)  # Clear phone number field
        
        session['user_data'] = {
            'full_name': full_name,
            'address': address,
            'phone_number': phone_number,
        }
        return redirect(url_for('event_details'))
    
    return render_template('user_contact.html')

@app.route('/user/event', methods=['GET', 'POST'])
def event_details():
    event_types = [
        'Wedding',
        'Birthday Party',
        'Corporate Event',
        'Anniversary',
        'Baby Shower',
        'Graduation Party',
        'Holiday Party'
    ]

    if request.method == 'POST':
        event_date = request.form['event_date']

        # Check if the event date is already booked
        if is_date_booked(event_date):
            # Retain the other fields in case of an error
            session['event_data'] = {
                'event_date': event_date,
                'event_time': request.form['event_time'],
                'guest_count': request.form['guest_count'],
                'event_place': request.form['event_place'],
                'event_type': request.form['event_type'],
            }
            flash(MESSAGES['ERROR_DATE_BOOKED'], 'error')
            return redirect(url_for('event_details'))

        # Save all data in the session if the date is not booked
        session['event_data'] = {
            'event_date': event_date,
            'event_time': request.form['event_time'],
            'guest_count': request.form['guest_count'],
            'event_place': request.form['event_place'],
            'event_type': request.form['event_type'],
        }
        return redirect(url_for('menu_details'))

    # Populate the form with existing session data if available
    event_data = session.get('event_data', {})
    return render_template('event_details.html', event_data=event_data, event_types=event_types)

@app.route('/user/menu', methods=['GET', 'POST'])
def menu_details():
    service_type = [
        'Buffet Style',
        'Plated Service',
        'Cocktail Reception',
        'Family Style Catering',
        'Boxed Meals',
        'Cafeteria Style',
        'Themed Catering'
    ]

    food_package = [
        'Standard Package',
        'Premium Package',
        'Vegetarian Package',
        'Vegan Package',
        'Gluten-Free Package',
        'Family Feast Package',
        'Gourmet Package',
        'Breakfast Package',
        'Brunch Package'
    ]

    meal_type = [
        'Breakfast',
        'Lunch',
        'Dinner',
        'Snacks',
        'Dessert',
        'Appetizer',
        'Main Course',
        'Buffet',
        'Family-Style',
        'Platters',
        'Sweets and Treats',
        'Barbecue',
        'Barista Bar',
    ]

    if request.method == 'POST':
        # Save the menu data in the session
        session['menu_data'] = {
            'service_type': request.form['service_type'],
            'food_package': request.form['food_package'],
            'meal_type': request.form['meal_type'],
        }
        return redirect(url_for('setup_details'))

    # Check if the session already has menu_data, else pass empty values to avoid undefined error
    menu_data = session.get('menu_data', {})
    return render_template('menu_details.html', menu_data=menu_data, service_type=service_type, food_package=food_package, meal_type=meal_type)

@app.route('/user/setup', methods=['GET', 'POST'])
def setup_details():
    if request.method == 'POST':
        user_data = session.get('user_data')
        event_data = session.get('event_data')
        menu_data = session.get('menu_data')

        # Validate required session data
        if not event_data or not menu_data or not user_data:
            flash("Some booking details are missing. Please go back and complete the process.", 'error')
            return redirect(url_for('event_details'))

        setup_data = {
            'chair_type': request.form['chair_type'],
            'table_type': request.form['table_type'],
            'theme_suggestion': request.form['theme_suggestion'],
            'additional_suggestion': request.form['additional_suggestion'],
        }

        # Check if setup data is present
        if not setup_data.get('chair_type') or not setup_data.get('table_type'):
            flash("Chair type and table type are required. Please provide them.", 'error')
            return redirect(url_for('setup_details'))

        # Proceed with booking
        booking = CateringBooking(
            **user_data, 
            **event_data, 
            **menu_data, 
            **setup_data
        )

        db.session.add(booking)
        db.session.commit()

        # Send SMS after successful booking
        if send_sms(
            user_data['phone_number'], 
            user_data['full_name'], 
            event_data['event_date'],
            event_data['event_time'],
            event_data['guest_count'],
            event_data['event_place'],
            event_data['event_type'],
            menu_data['service_type'],
            menu_data['food_package'],
            menu_data['meal_type'],
            setup_data['chair_type'],
            setup_data['table_type'],
            setup_data.get('theme_suggestion'),  # Optional
            setup_data.get('additional_suggestion')  # Optional
        ):
            flash("SMS notification sent successfully!", 'success')
        else:
            flash("Failed to send SMS notification.", 'error')

        # Clear session data only after a successful booking
        session.pop('event_data', None)
        session.pop('menu_data', None)
        flash(MESSAGES['SUCCESS_BOOKING'], 'success')
        return redirect(url_for('login'))

    # Check if setup_data exists in the session, if not, initialize it as an empty dictionary
    setup_data = session.get('setup_data', {})
    return render_template('setup_details.html', setup_data=setup_data)


@app.route('/admin', methods=['GET', 'POST'])
def admin_panel():
    bookings = CateringBooking.query.all()
    if request.method == 'POST':
        try:
            event_date = request.form['event_date']
            booking = get_booking_by_date(event_date)
            if booking:
                db.session.delete(booking)
                db.session.commit()
                flash(MESSAGES['SUCCESS_DELETION'], 'success')
            else:
                flash(MESSAGES['ERROR_DATE_BOOKED'], 'error')
        except Exception as e:
            flash(f"An error occurred: {e}", 'error')
    return render_template('admin.html', bookings=bookings)

# Main Execution
if __name__ == '__main__':
    create_database()
    app.run(debug=True)