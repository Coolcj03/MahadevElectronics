# Mahadeva Electronics Website

A comprehensive e-commerce website for Mahadeva Electronics with both customer-facing frontend and administrative backend.

## Features

- **Customer Frontend**: Product browsing, shopping cart, technician booking, contact form
- **Admin Dashboard**: Product management, parts management, technician management, booking management, feedback management
- **FastAPI Backend**: Modern Python web framework with PostgreSQL database
- **Responsive Design**: Mobile-first design with beautiful gradients and animations

## Tech Stack

- **Frontend**: HTML, CSS, JavaScript
- **Backend**: FastAPI (Python)
- **Database**: PostgreSQL
- **Authentication**: JWT tokens
- **Deployment**: Railway

## Project Structure

```
website/
├── main.py              # FastAPI application entry point
├── database.py          # Database configuration
├── models.py            # SQLAlchemy database models
├── schemas.py           # Pydantic schemas for validation
├── crud.py             # Database CRUD operations
├── init_db.py          # Database initialization script
├── requirements.txt    # Python dependencies
├── Procfile           # Railway deployment configuration
├── env_template.txt   # Environment variables template
├── *.html             # Frontend HTML files
├── style.css          # Global styles
└── images/            # Product images
```

## Local Development

1. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

2. **Set up environment variables**:
   - Copy `env_template.txt` to `.env`
   - Update the values as needed

3. **Initialize database**:
   ```bash
   python init_db.py
   ```

4. **Run the application**:
   ```bash
   python main.py
   ```

5. **Access the API**:
   - API: http://localhost:8000
   - API docs: http://localhost:8000/docs
   - ReDoc: http://localhost:8000/redoc

## Railway Deployment

### Backend Deployment

1. **Create a new Railway service** for your FastAPI backend
2. **Connect your GitHub repository**
3. **Set environment variables** in Railway:
   - `DATABASE_URL`: Your PostgreSQL connection string
   - `SECRET_KEY`: A strong random secret key
   - `ADMIN_EMAIL`: Admin email (default: admin@mahadeva.com)
   - `ADMIN_PASSWORD`: Admin password (default: admin123)
   - `DEBUG`: False
   - `ALLOWED_HOSTS`: Your Railway domain

4. **Deploy**: Railway will automatically detect the Python app and deploy

### Database Setup

1. **Create a PostgreSQL service** in Railway
2. **Link it to your FastAPI service** using Railway's variable referencing:
   - In your FastAPI service → Variables
   - Add `DATABASE_URL` with value `${{ Postgres.DATABASE_URL }}`

3. **Initialize the database**:
   - Go to your FastAPI service → Shell
   - Run: `python init_db.py`

### Frontend Deployment

1. **Create a static site service** in Railway
2. **Upload your HTML/CSS/JS files**
3. **Set the domain** to your preferred URL

## API Endpoints

### Authentication
- `POST /api/auth/token/` - Admin login

### Products
- `GET /api/products/` - List all products
- `POST /api/products/` - Create product
- `GET /api/products/{id}` - Get product details
- `PUT /api/products/{id}` - Update product
- `DELETE /api/products/{id}` - Delete product

### Parts
- `GET /api/parts/` - List all parts
- `POST /api/parts/` - Create part
- `GET /api/parts/{id}` - Get part details
- `PUT /api/parts/{id}` - Update part
- `DELETE /api/parts/{id}` - Delete part

### Technicians
- `GET /api/technicians/` - List all technicians
- `POST /api/technicians/` - Create technician
- `PUT /api/technicians/{id}` - Update technician
- `DELETE /api/technicians/{id}` - Delete technician

### Bookings
- `GET /api/bookings/` - List all bookings
- `POST /api/bookings/` - Create booking
- `PUT /api/bookings/{id}` - Update booking
- `DELETE /api/bookings/{id}` - Delete booking

### Feedback
- `GET /api/feedback/` - List all feedback
- `POST /api/feedback/` - Create feedback
- `PUT /api/feedback/{id}` - Update feedback (admin reply)
- `DELETE /api/feedback/{id}` - Delete feedback

## Admin Access

- **Email**: admin@mahadeva.com (or as set in environment)
- **Password**: admin123 (or as set in environment)

## Features

### Product Management
- Add, edit, delete products
- Multiple image uploads
- Category and stock management

### Parts Management
- Technical parts catalog
- Manufacturer and part number tracking
- Stock management

### Technician Management
- Technician profiles and availability
- Specialization tracking
- Experience management

### Booking System
- Customer service requests
- Technician assignment
- Status tracking

### Feedback System
- Customer feedback collection
- Admin response management
- Issue resolution tracking

## Mobile Responsiveness

The website is fully responsive with:
- Mobile-first design approach
- Hamburger navigation menu
- Optimized layouts for all screen sizes
- Touch-friendly interface elements

## Color Scheme

Features a modern multicolor gradient theme:
- Rainbow gradients for headers and CTAs
- Professional color combinations
- Consistent visual hierarchy
- Accessible color contrasts
