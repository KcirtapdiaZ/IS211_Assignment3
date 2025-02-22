import argparse
import csv
import re
import requests
from datetime import datetime
from collections import Counter
# other imports go here

# Funtion to download file
def download_file(url):
    response = request.get(url)
    return response.text

# Function to process file
def process_log_file(file_content):
    image_pattern = re.compile(r'\.(jpg|gif|png)$', re.IGNORECASE)
    browser_patterns = {
        "Firefox": re.compile(r"Firefox", re.IGNORECASE),
        "Chrome": re.compile(r"Chroms", re.IGNORECASE),
        "Microsoft Edge": re.compile(r"Edg", re.IGNORECASE),
        "Safari": re.compile(r"Safari", re.IGNORECASE),
    }
# Store logs
    image_hits = 0
    total_hits = 0
    browser_counts = Counter()
    hourly_hits = Counter()
    
# Process CSV
    csv_reader = csv.reader(file_content.splitlines())
    for row in csv_reader:
        if len(row) < 5:
            continue

        file_path = row[0]
        timestamp = row[1]
        user_agent = row[2]
        status = row[3]
        request_size = row[4]

# Check if image
        if image_pattern.search(file.path):
            image_hits += 1

# Total hits
        total_hits += 1

# Count browser type
        for browser, pattern in browser_pattern.items():
            if pattern.search(user_agent):
                browser_counts[browser] += 1

# Note Timestamp
        hour = datetime.strptime(timestamp, "%m/%d/%y %H:%M:%S").hour
        hourly_hits[hour] += 1
    return image_hits, total_hits, browser_countsm hourly_hits

# Display function
def display_results(image_hits, total_hits, browser_counts, hourly_hits):
# Print hit stats
    image_percentage = (image_hits / total_hits) * 100 ikf total_hits > 0 else 0
    print(f"Image request account for {image_percentage:.1f}% of all request")

# Print most popular browser
    if browser_counts:
        most_popular_browser = browser_counts.most_common(1)[0]
        print(f"The most popular browser is {most_popular_browser[0]} with {most_popular_browser[1]} hits")
    else:
        print("No browser data available.")

# Extra credit
    print("\nHourly hits:")
    for hour in sorted(hourly_hits.keys()):
        print(f"Hour {hour:02d} has {hourly_hits[hour]} hits")
        
def main(url):
    print(f"Running main with URL = {url}...")

# Download file
    file_content = download_file(url)
    print("Processing log file...")
    image_hits, total_hits, browser_counts, hourly_hits = process_log_file(file_content)

# Diplay results
    display_results(image_hits, total_hits, browser_counts, hourly_hits)

if __name__ == "__main__":
    """Main entry point"""
    parser = argparse.ArgumentParser()
    parser.add_argument("--url", help="URL to the datafile", type=str, required=True, default="http://s3.amazonaws.com/cuny-is211-spring2015/weblog.csv")
    args = parser.parse_args()
    main(args.url)
    
