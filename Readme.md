# FastAPI Python App

This is a simple FastAPI Python app that demonstrates how to create a RESTful API using FastAPI and run it using Uvicorn.

## Getting Started

Follow these instructions to set up and run the FastAPI app on your local machine.

### Prerequisites

- Python 3.10+
- pip (Python package manager)

### Installation

1. Clone the repository to your local machine:

   ```bash
   git clone https://github.com/your-username/fastapi-app.git

2. Navigate to the project directory:

   ```bash
   cd fastapi-app

3. Create a virtual environment:

   ```bash
   python -m venv venv

4. Activate the virtual environment:

   ```bash
    # Windows
    venv\Scripts\activate.bat

    # Linux/macOS
    source venv/bin/activate

5. Install the dependencies:

   ```bash
   pip install -r requirements.txt

### Running the App
Once you have set up the environment, you can run the FastAPI app using Uvicorn.
    
    ```bash
    uvicorn main:app --reload
