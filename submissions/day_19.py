import requests

def get_latest_launch_info():
    # API endpoint for latest launch
    url = "https://api.spacexdata.com/v5/launches/latest"

    try:
        # Sending GET request to the API endpoint
        response = requests.get(url)
        response.raise_for_status()  # Raise an exception for 4xx/5xx status codes

        # Printing response content for inspection
        print("Response Content:", response.content)

        # Parsing JSON content
        launch_data = response.json()

        # Extracting relevant information
        mission_name = launch_data.get('name', 'No mission name available')
        launch_date = launch_data.get('date_utc', 'No launch date available')
        rocket_name = launch_data.get('rocket', {}).get('name', 'No rocket name available')
        launch_site = launch_data.get('launchpad', {}).get('name', 'No launch site available')
        details = launch_data.get('details', 'No details available.')

        # Displaying launch information
        print("Latest SpaceX Launch Information:")
        print(f"Mission: {mission_name}")
        print(f"Launch Date (UTC): {launch_date}")
        print(f"Rocket: {rocket_name}")
        print(f"Launch Site: {launch_site}")
        print(f"Details: {details}")
    except requests.exceptions.RequestException as e:
        print("Error occurred:", e)

if __name__ == "__main__":
    get_latest_launch_info()
