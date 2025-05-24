from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_user, logout_user, login_required
from app.models import User, Customer, Technician, Job

# Create a Blueprint
auth = Blueprint('auth', __name__)

# Home page
@auth.route('/')
def home():
    return render_template('home.html', page_title='Home', title='Home', description='Welcome to the home page.')

# About page
@auth.route('/about')
def about():
    return render_template('about.html', page_title='About', title='About', description='Welcome to the about page.')

# Contact page
@auth.route('/contact')
def contact():
    return render_template('contact.html', page_title='Contact', title='Contact', description='Welcome to the contact page.')

# Customers page
@auth.route('/customers')
@login_required
def customers():
    try:
        customers = Customer.query.all()
    except Exception as e:
        customers = []
        print(f"Error fetching customers: {e}")
    return render_template('customers.html', customers=customers, page_title='Customers', title='Customers', description='Welcome to the customers page.')

# Technicians page
@auth.route('/technicians')
@login_required
def technicians():
    try:
        technicians = Technician.query.all()
    except Exception as e:
        technicians = []
        print(f"Error fetching technicians: {e}")
    return render_template('technicians.html', technicians=technicians, page_title='Technicians', title='Technicians', description='Welcome to the technicians page.')

# Jobs page
@auth.route('/jobs')
@login_required
def jobs():
    try:
        jobs = Job.query.all()
    except Exception as e:
        jobs = []
        print(f"Error fetching jobs: {e}")
    return render_template('jobs.html', jobs=jobs, page_title='Jobs', title='Jobs', description='Welcome to the jobs page.')

# Example POST handler (placeholder)
@auth.route('/add', methods=['POST'])
@login_required
def add():
    print(request.args.get("name"))
    return "Done"

# Login route
@auth.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and user.check_password(password):  # Removed user.active check
            login_user(user)
            return redirect(url_for('auth.dashboard'))
        else:
            flash('Invalid username or password')
    return render_template('login.html')

# Logout route
@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

# Dashboard
@auth.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html')

# Test DB route
@auth.route('/test-db')
def test_db():
    try:
        users = User.query.all()
        return f"✅ Database connection successful. Found {len(users)} users."
    except Exception as e:
        return f"❌ Database connection failed: {e}"

# Custom 404 error page
@auth.app_errorhandler(404)
def page_not_found(e):
    return render_template('404.html', page_title='404', title='404', description='Page not found.'), 404
