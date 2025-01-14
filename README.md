# Simple Movie App

A web-based application built with Python (backend) and React (frontend) for browsing and managing movie information.

## Features

- Search for movies by title.
- View detailed information about movies.
- Simple and interactive user interface.

## Installation

### Backend Setup

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Topher05/simple-movie-app-Topher05.git
   cd simple-movie-app-Topher05/backend
   ```

2. **Create a virtual environment**:
   ```bash
   python3 -m venv .venv
   ```

3. **Activate the virtual environment**:
   - On macOS/Linux:
     ```bash
     source .venv/bin/activate
     ```
   - On Windows:
     ```bash
     .venv\Scripts\activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Start the backend server**:
   ```bash
   uvicorn main:app --reload
   ```

### Frontend Setup

1. **Navigate to the frontend directory**:
   ```bash
   cd ../frontend
   ```

2. **Install dependencies**:
   ```bash
   npm install
   ```

3. **Start the frontend server**:
   ```bash
   npm start
   ```

## Usage

- Access the application by navigating to `http://localhost:3000` in your browser.
- Use the search bar to find movies.

## Requirements

- Python 3.6 or higher
- Node.js and npm
- See `requirements.txt` (backend) and `package.json` (frontend) for additional dependencies.

## Running Tests

- **Backend tests**:
  ```bash
  pytest
  ```
- **Frontend tests**:
  ```bash
  npm test
  ```
