# URL Shortener
This is a simple URL Shortener application built using FastAPI for the backend, PostgreSQL as the database, and plain JavaScript for the frontend. The application allows users to shorten long URLs, which can then be used to redirect to the original URLs.
## Table of Contents
- [Project Structure](#project-structure)
- [Backend Setup](#backend-setup)
- [Frontend Setup](#frontend-setup)
- [How It Works](#how-it-works)
- [Deployment Notes](#deployment-notes)
- [Additional Information](#additional-information)
- [License](#license)
## Project Structure

```plaintext
url_shortener/
│
├── backend/
│   ├── app/
│   │   ├── __init__.py          # Initializes the app package
│   │   ├── database.py          # Handles database connections and session management
│   │   ├── models.py            # Contains the SQLAlchemy models
│   │   └── routes.py            # Defines the API routes for the application
│   ├── main.py                  # Entry point for the FastAPI application
│   ├── requirements.txt         # Lists the dependencies required for the backend
│   └── .env                     # Environment variables for database connection
│
├── frontend/
│   ├── index.html               # The main HTML file for the frontend
│   ├── script.js                # JavaScript file that interacts with the backend API
│   └── styles.css               # Basic styling for the frontend
│
└── README.md                    # This README file
```
### Prerequisites
- Python 3.8+
- PostgreSQL
- Virtual environment (optional but recommended)
### Setting Up the Backend
1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/url_shortener.git
   cd url_shortener/backend
## Frontend Setup

1. **Navigate to the Frontend Directory:**
   ```bash
   cd ../frontend
## How It Works

### Shorten a URL
- Enter a long URL in the input field on the frontend and click the "Shorten" button.
- The frontend sends a POST request to the FastAPI backend, which generates a short URL, stores it in the PostgreSQL database, and returns it to the frontend.
- The shortened URL is displayed on the frontend for easy access.

### Redirect Using a Shortened URL
- When you visit the shortened URL (e.g., `http://localhost:8000/abc123`), the backend looks up the original URL in the database and redirects you to it.
## Additional Information

### Technologies Used
- **Backend:** FastAPI, SQLAlchemy, PostgreSQL
- **Frontend:** HTML, CSS, JavaScript
- **Environment Management:** Python dotenv
