# 📘 Assignment: Testing FastAPI Endpoints

## 🎯 Objective

Write automated tests for the `/books` endpoint from the FastAPI assignment. Use `pytest` and FastAPI's `TestClient` to check its HTTP response and returned JSON without starting a separate server.

## 📝 Tasks

### 🛠️ Test the Endpoint Status

#### Description
In a new `test_main.py` file, create a `TestClient` for the FastAPI app in `main.py` and write a test that sends a GET request to `/books`.

#### Requirements
Completed tests should:

- Import `app` from `main.py` and create a client with `TestClient(app)`.
- Send a GET request to `/books`.
- Assert that the response status code is `200`.
- Run with `python -m pytest -q` from the folder containing `main.py`.

### 🛠️ Check the Returned Books

#### Description
Add an assertion to check that the endpoint returns the expected books as JSON. Use the sample books already defined in the FastAPI assignment.

#### Requirements
Completed tests should:

- Check that the response JSON contains both sample books, including their IDs, titles, and authors.
- Use a pytest assertion so the test fails if the returned data is incorrect.
- Pass when run against the completed `/books` endpoint from the FastAPI assignment.
