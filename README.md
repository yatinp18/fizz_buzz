# Fizz-Buzz FastAPI Server

## Overview
This project implements a FastAPI server for the classic Fizz-Buzz algorithm, including a statistics endpoint. The server exposes a REST API endpoint for Fizz-Buzz calculations and provides insights into the most frequently used requests.

## Build and Run Instructions
1. Ensure Python 3.8.10 is installed , visit  https://www.python.org/downloads/release/python-3810/
2. Create and activate a virtual environment:

    ```bash
    python3.10 -m venv venv
    source venv/bin/activate  # On Unix-like systems
    .\venv\Scripts\activate   # On Windows
    ```

3. Install dependencies:

    ```bash
    pip install -r requirements.txt
    ```

4. Run the server:

    ```bash
    uvicorn main:app --reload
    ```

5. Explore the API documentation at http://localhost:8000/docs.

6. Trigger pytests using : pytest -ra

## Third-Party Libraries
- **FastAPI**: A high-performance web framework for building APIs using Python 3.7+. Employed for constructing the REST API.

- **Uvicorn**: A fast ASGI server acting as the interface between FastAPI and the external environment.

- **Pytest**: A testing framework for creating and executing unit tests. Utilized for testing the Fizz-Buzz logic and API endpoints.

- **Requests**: A straightforward HTTP library for making requests. Applied in the test suite for HTTP interactions.

## API Documentation
The API documentation is available [here](http://localhost:8000/docs) when the server is active. It provides comprehensive details about the available endpoints, parameters, and example requests.

For more in-depth information, refer to the [FastAPI documentation](https://fastapi.tiangolo.com/).

---

Feel free to customize this README according to the unique details of your project and include any additional information relevant to your work. Once your code is ready, ensure it is pushed to a public Git repository, and provide the repository's URL for evaluation.
