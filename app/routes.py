from app import app
from flask import render_template, abort
from flask_sqlalchemy import SQLAlchemy
import os


basedir = os.path.abspath(os.path.dirname(__file__))
db = SQLAlchemy()
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'app.db')
db.init_app(app)


import models as models


@app.route('/')
def root():
    return render_template('home.html', page_title='Home', title='Home', description='Welcome to the home page.')



@app.route('/about')
def about():
    return render_template('about.html', page_title='About', title='About', description='Welcome to the about page.')


@app.route('/contact')
def contact():
    return render_template('contact.html', page_title='Contact', title='Contact', description='Welcome to the contact page.')


@app.route('/customers')
def customers():
    customers = models.Customer.query.all()
    return render_template('customers.html', customers=customers, page_title='Customers', title='Customers', description='Welcome to the customers page.')


@app.route('/technicians')
def technicians():
    technicians = models.Technician.query.all()
    return render_template('technicians.html', technicians=technicians, page_title='Technicians', title='Technicians', description='Welcome to the technicians page.')


@app.route('/jobs')
def jobs():
    jobs = models.Job.query.all()
    return render_template('jobs.html', jobs=jobs, page_title='Jobs', title='Jobs', description='Welcome to the jobs page.')


@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html', page_title='404', title='404', description='Page not found.'), 404




