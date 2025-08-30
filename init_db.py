from database import engine, SessionLocal
from models import Base, AdminUser
from crud import create_admin_user, get_password_hash
from schemas import AdminUserCreate
import os
from dotenv import load_dotenv

load_dotenv()

def init_db():
    # Create tables
    Base.metadata.create_all(bind=engine)
    
    # Create admin user if it doesn't exist
    db = SessionLocal()
    try:
        admin_email = os.getenv("ADMIN_EMAIL", "admin@mahadeva.com")
        admin_password = os.getenv("ADMIN_PASSWORD", "admin123")
        
        existing_admin = db.query(AdminUser).filter(AdminUser.email == admin_email).first()
        if not existing_admin:
            admin_user = AdminUserCreate(
                email=admin_email,
                password=admin_password,
                is_active=True
            )
            create_admin_user(db, admin_user)
            print(f"Admin user created: {admin_email}")
        else:
            print(f"Admin user already exists: {admin_email}")
            
    except Exception as e:
        print(f"Error creating admin user: {e}")
    finally:
        db.close()

if __name__ == "__main__":
    print("Initializing database...")
    init_db()
    print("Database initialization completed!")
