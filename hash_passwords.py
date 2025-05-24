from app.models import User
from app.database import db
from werkzeug.security import generate_password_hash

# Update existing passwords to be hashed
def hash_existing_passwords():
    users = User.query.all()
    for user in users:
        if not user.password_hash.startswith('pbkdf2:sha256'):  # Check if already hashed
            user.password_hash = generate_password_hash(user.password_hash)
            print(f"Hashed password for user: {user.username}")
    db.session.commit()

if __name__ == "__main__":
    with db.app.app_context():
        hash_existing_passwords()
