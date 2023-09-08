# PuffinTask Python App

This is Python-based web scraper that collects data from a yahoo finance crypto, stores the data in a database, and exposes the data through a simple API using FastAPI.
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

6. Create .env file for your environment variables in the root directory of the project. The .env file should contain the following variables:

   ```bash
    DATABASE_USER=
    DATABASE_PASSWORD=
    DATABASE_NAME=
    DATABASE_HOST=
   ```

### Running the App
Once you have set up the environment, you can run the FastAPI app using Uvicorn.
    
    ```bash
    uvicorn main:app --host 0.0.0.0 --port 8080


### accessing the API
1. Do a get Request to http://localhost:8080/finance_data/all this will list 100 row of data from the database
2. you can filter the data by adding a query parameter to the url for example http://localhost:8080/finance_data/all?name=Symbol&value=BTC-USD will return all the data for BTC-USD
3. you can also get a single row of data by adding the id of the row to the url for example http://localhost:8080/finance_data/1 will return the first row of data in the database