from app import app, db  # Reverted import
from app.models import User

with app.app_context():
    # Check if the user already exists
    existing_user = User.query.filter_by(username='admin').first()
    if existing_user:
        print("⚠️ User 'admin' already exists. Skipping creation.")
    else:
        # Create a new user
        user = User(username='admin', role='admin')
        user.set_password('admin123')  # You can change this password
        db.session.add(user)
        db.session.commit()
        print("✅ Test user created: admin / admin123")