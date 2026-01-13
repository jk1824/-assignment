How to Execute the Application
1) Clone the repository
git clone https://github.com/<your-username>/address-book-fastapi.git
cd address-book-fastapi

2) Create and activate a virtual environment
      python -m venv venv
      venv\Scripts\activate

3) Install dependencies
pip install -r requirements.txt

4) Start the FastAPI server
python -m uvicorn app.main:app --reload