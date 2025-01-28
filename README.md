# My FastAPI Application

This is a simple FastAPI application that handles CORS and returns JSON output with the registered email address, current datetime, and GitHub URL.

## Project Structure

```
my-fastapi-app
├── app
│   ├── main.py          # Entry point of the FastAPI application
│ 
├── requirements.txt     # Project dependencies
└── README.md            # Project documentation
```

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/your-repo.git
    cd your-repo
    ```

2. Create a virtual environment and activate it:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. Install the dependencies:
    ```bash
    pip install -r requirements.txt
    ```

## Running the application

1. Start the FastAPI application:
    ```bash
    uvicorn app.main:app --reload
    ```

2. Open your browser and navigate to `http://127.0.0.1:8000/docs` to see the JSON output.

## API Endpoints

### GET /info

Returns a JSON object with the following information:
- `email`: Your registered email address.
- `timestamp`: The current datetime as an ISO 8601 formatted timestamp.
- `github_url`: The GitHub URL of the project's codebase.

Example response:
```json
{
    "email": "dubemnwabuisi@gmail.com",
    "timestamp": "2023-10-05T12:34:56.789Z",
    "github_url": "https://github.com/yourusername/your-repo"
}
```