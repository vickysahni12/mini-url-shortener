import hashlib
import json
import os
import sys

# File where we store our  links
FILE_NAME = "urls.json"


def load_data():
    """Reads data saved links from the JSON file into a Python dictionary."""
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r") as file:
        return json.load(file)


def save_data(data):
    """Saves the dictionary back into the JSON file."""
    with open(FILE_NAME, "w") as file:
        json.dump(data, file, indent=4)


def shorten(url, alias=None):
    """Generates a short code and saves the URL."""
    # check for a valid link
    if not (url.startswith("http://") or url.startswith("https://")):
        print("Error: URL must start with http:// or https://")
        return

    data = load_data()

    # If the user provided a custom alias, use it
    if alias:
        code = alias
        if code in data and data[code]["url"] != url:
            print(f"Error: Alias '{alias}' is already in use!")
            return
    else:
        # Generate a 6-character code from the URL using sha256
        code = hashlib.sha256(url.encode()).hexdigest()[:6]

    # Save mapping and initialize click count to 0
    data[code] = {
        "url": url,
        "clicks": data.get(code, {}).get("clicks", 0)
    }
    save_data(data)
    print(f"Shortened Code: {code}")


def resolve(code):
    """Finds and displays the original URL for a given code."""
    data = load_data()

    if code not in data:
        print(f"Error: Short code '{code}' not found!")
        return

    # Increase click counter by 1
    data[code]["clicks"] += 1
    save_data(data)

    print(f"Original URL: {data[code]['url']}")
    print(f"Clicks: {data[code]['clicks']}")


def list_urls():
    """Prints all stored URLs and their short codes."""
    data = load_data()

    if not data:
        print("No URLs stored yet.")
        return

    print("--------------------------------------------------")
    print(f"Code      | Clicks      | URL     ")
    print("--------------------------------------------------")
    for code, info in data.items():
        print(f"{code}      | {info['clicks']}      | {info['url']}      ")
    print("--------------------------------------------------")


# Main execution reads terminal arguments directly from sys.argv
if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Usage:")
        print("  python main.py shorten <url> [optional_alias]")
        print("  python main.py resolve <code>")
        print("  python main.py list")
        sys.exit()

    command = sys.argv[1].lower()

    if command == "shorten":
        if len(sys.argv) < 3:
            print("Error: Please provide a URL to shorten.")
        else:
            url_to_shorten = sys.argv[2]
            custom_alias = sys.argv[3] if len(sys.argv) >= 4 else None
            shorten(url_to_shorten, custom_alias)

    elif command == "resolve":
        if len(sys.argv) < 3:
            print("Error: Please provide a short code.")
        else:
            resolve(sys.argv[2])

    elif command == "list":
        list_urls()

    else:
        print(f"Unknown command: '{command}'")