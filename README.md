# Storage security pult
This project written to monitor all entrance and leaves from storage.

## How to run
1. You may want to isolate your environment with [venv](https://docs.python.org/3/library/venv.html).
2. Install all dependencies with `pip` or `pip3`:
```
pip install -r requirements.txt
```
3. Create a `.env` file:
```
SECRET_KEY=<YOUR DJANGO SECRET KEY>
DB_URL=<YOUR DB URL>
DEBUG=<True or False>
ALLOWED_HOSTS=<localhost, 127.0.0.1, etc>
```
4. Run the script with `python` or `python3`:
```
python main.py
```