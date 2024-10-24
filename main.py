import requests
import csv
from datetime import datetime

url = "https://api.tradelink.pro/portfolio/get?portfolioId=c7c86b86-fa37-4bee-8a45-d4b3cbb886ef&extended=1&declaration=1&step=day&endDate=2024-10-23T19:00:00.000Z&lang=en&incViews=0"

response = requests.get(url)
if response.status_code == 200:
    # Parse the JSON response
    data = response.json()
    # Print the retrieved data
    profit = data['data']['extended']['profits']
else:
    print(f"Failed to retrieve data: {response.status_code} - {response.text}")

filename = 'data.csv'

with open(filename, 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Date(UTC)', 'Profit(%)'])

    for entry in profit:
        # Convert timestamp to UTC date and time
        utc_datetime = datetime.fromtimestamp(entry['timestamp'] / 1000).strftime('%Y-%m-%d %H:%M:%S')
        value = entry['value'] * 100
        writer.writerow([utc_datetime, value])

print(f"Data saved to {filename}")
