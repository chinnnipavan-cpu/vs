import requests
import sys
import json
import urllib.parse

def main():
    if len(sys.argv) != 2:
        print("Usage: python itunes.py <search term>")
        sys.exit(1)

    term = urllib.parse.quote_plus(sys.argv[1])
    r = requests.get(
        "https://itunes.apple.com/search?entity=song&limit=1&term=" + term
    )

    try:
        data = json.dumps(response.json())
    except ValueError:
        print("Error: response is not valid JSON")
        sys.exit(1)

    print(json.dumps(data, indent=2))


if __name__ == "__main__":
    main()