from app import create_app  # Reverted import

app = create_app()

with app.app_context():  # Ensure app context is active
    print("✅ App context pushed successfully.")

if __name__ == '__main__':
    app.run(debug=True)

