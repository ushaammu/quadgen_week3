import requests
import logging

# ---------------------------------------------------
# Step 1 & 3: Configure Logging + Create Decorator
# ---------------------------------------------------
logging.basicConfig(
    filename="decorator_log.txt",     # Log file auto-created
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def auto_log(func):
    """
    Decorator that logs:
    - Function name
    - Arguments
    - Success / Failure
    """
    def wrapper(*args, **kwargs):
        logging.info(f"Function '{func.__name__}' started")
        logging.info(f"Args: {args} | Kwargs: {kwargs}")

        try:
            result = func(*args, **kwargs)
            logging.info(f"Function '{func.__name__}' completed successfully")
            return result

        except Exception as e:
            logging.error(f"Function '{func.__name__}' failed: {e}")
            raise e
    
    return wrapper


# ---------------------------------------------------
# Step 2: Implement an API Function
# ---------------------------------------------------
@auto_log      # Step 4: Apply Decorator Here
def fetch_api(url):
    response = requests.get(url, timeout=3)

    if response.status_code != 200:
        raise Exception(f"Bad status code: {response.status_code}")

    try:
        return response.json()
    except ValueError:
        raise Exception("Invalid JSON response")


# ---------------------------------------------------
# Step 5: Test It
# ---------------------------------------------------
good_url = "https://jsonplaceholder.typicode.com/todos/1"
bad_url  = "https://invalid-broken-url.com/data"

for url in [good_url, bad_url]:
    print(f"\nChecking: {url}")
    try:
        print("OUTPUT:", fetch_api(url))
    except Exception as e:
        print("FAILED:", e)

