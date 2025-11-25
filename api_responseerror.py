import requests

# -----------------------------
# Step 2: Custom Exception
# -----------------------------
class APIResponseError(Exception):
    """Raised when API response is invalid or indicates failure."""
    pass


# -----------------------------
# Step 3: Network Function
# -----------------------------
def fetch_data(url):
    try:
        response = requests.get(url, timeout=3)

        # If API does not return 200 OK
        if response.status_code != 200:
            raise APIResponseError(f"Bad status code: {response.status_code}")

        # Try to parse JSON
        try:
            data = response.json()
        except ValueError:
            raise APIResponseError("Response is not valid JSON")

        return data

    except requests.exceptions.Timeout:
        raise APIResponseError("Request Timeout")

    except requests.exceptions.ConnectionError:
        raise APIResponseError("Host Unreachable")


# -----------------------------
# Step 4: Try–Except to use custom exception
# -----------------------------
good_url = "https://jsonplaceholder.typicode.com/todos/1"  # GOOD URL
bad_url = "https://invalid-website-12345.com/data"          # BAD URL

for url in [good_url, bad_url]:
    print(f"\nChecking: {url}")

    try:
        result = fetch_data(url)
        print("SUCCESS:", result)

    except APIResponseError as e:
        print("API ERROR:", e)

    except Exception as e:
        print("UNKNOWN ERROR:", e)
