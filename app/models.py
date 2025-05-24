from app.database import db
from flask_login import UserMixin
from sqlalchemy import ForeignKey
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy.orm import relationship

Jobs = db.Table('jobs',
    db.Column('job_id', db.Integer, db.ForeignKey('job.id'), primary_key=True),
    db.Column('user_id', db.Integer, db.ForeignKey('user.id'), primary_key=True)
)

class Customer(db.Model):
    __tablename__ = 'Customer'
    Customer_ID = db.Column(db.Integer, primary_key=True)
    Name = db.Column(db.VARCHAR(100), nullable=False)
    contact_number = db.Column(db.VARCHAR(12), nullable=False, unique=True)
    reg_number = db.Column(db.VARCHAR(6), nullable=False, unique=True)
    initial_date = db.Column(db.Date, nullable=False)

    def __repr__(self):
        return f'{self.Name.upper()} CUSTOMER'

class Technician(db.Model):
    __tablename__ = 'Technician'
    Technician_ID = db.Column(db.Integer, primary_key=True)
    Technitian_name = db.Column(db.VARCHAR(100), nullable=False)
    category_technician = db.Column(db.TEXT, nullable=False)
    Pay_per_hour = db.Column(db.Numeric(10,2), nullable=True, default=0.00)

    def __repr__(self):
        return f'{self.Technitian_name.upper()} TECHNICIAN'

class Job(db.Model):
    __tablename__ = 'Job'
    Job_ID = db.Column(db.Integer, primary_key=True)
    Customer_ID = db.Column(db.Integer, db.ForeignKey('Customer.Customer_ID'), nullable=False)
    Technician_ID = db.Column(db.Integer, db.ForeignKey('Technician.Technician_ID'), nullable=False)
    Job_description = db.Column(db.TEXT, nullable=False)
    Status = db.Column(db.TEXT, nullable=True, default='Pending')
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=True)
    total_cost = db.Column(db.Numeric(10,2), nullable=True, default=0.00)

    def __repr__(self):
        return f'{self.Job_description.upper()} JOB'


class User(db.Model, UserMixin):
    __tablename__ = 'user'

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(150), unique=True, nullable=False)
    password_hash = db.Column(db.String(255), nullable=False)
    role = db.Column(db.String(50), nullable=False, default='user')  # Added role column

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)