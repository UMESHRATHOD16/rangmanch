
# Rangmanch Review API 🎭

A REST API built with **FastAPI, SQLModel, and SQLite** to manage reviews and ratings for plays.

## 🚀 Features

- Create, view, update, and delete reviews (CRUD).
- Filter reviews by play name.
- Support pagination using `skip` and `limit`.
- Calculate average ratings and total reviews for a play.
- Validate ratings between 1 and 5.
- Interactive API documentation with Swagger UI.

## 🛠️ Tech Stack

- **Python**
- **FastAPI** – API development
- **SQLModel** – Database models and queries
- **SQLite** – Database
- **Uvicorn** – Development server

## 📁 Project Structure

```text
rangmanch/
├── main.py
├── database.py
├── models.py
├── requirements.txt
└── routes/
    └── reviews.py
```

## ⚙️ Installation & Setup

**1. Clone the repository**

```bash
git clone <your-repository-url>
cd rangmanch
```

**2. Create and activate a virtual environment**

```bash
python3 -m venv venv
source venv/bin/activate
```

**3. Install dependencies**

```bash
pip install -r requirements.txt
```

**4. Start the server**

```bash
uvicorn main:app --reload
```

The API runs at `http://127.0.0.1:8000`.

## 📚 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| POST | `/review/` | Create a review |
| GET | `/review/` | Get all reviews |
| GET | `/review/{review_id}` | Get a review by ID |
| PATCH | `/review/{review_id}` | Update a review |
| DELETE | `/review/{review_id}` | Delete a review |
| GET | `/review/average/{play_name}` | Get average rating and review count |

The reviews endpoint also supports filtering by play name and pagination using `skip` and `limit`.

## 📖 API Documentation

After starting the server, visit:

- **Swagger UI:** http://127.0.0.1:8000/docs
- **ReDoc:** http://127.0.0.1:8000/redoc

Use Swagger UI to test the endpoints directly from your browser.

## 🎯 Learning Outcomes

This project demonstrates REST API development, CRUD operations, request validation, database integration, and SQL queries using FastAPI and SQLModel.

---

Built to practise backend development with Python and FastAPI.
