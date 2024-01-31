#!/usr/bin/env python3

import argparse
import os
import json
import re
from collections import defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from datetime import datetime

# Command line args
parser = argparse.ArgumentParser()
parser.add_argument('--hashtags', nargs='+', required=True)
parser.add_argument('--input_folder', required=True)
args = parser.parse_args()

# Data aggregation
hashtag_counts = defaultdict(lambda: defaultdict(int))  # Nested dictionary to store counts per day per hashtag

for filename in os.listdir(args.input_folder):
    if filename.endswith('.lang'):  # Assuming the files are in JSON format
        match = re.search(r'(\d{2}-\d{2}-\d{2})', filename)
        if match:
            date_str = match.group()
            date_obj = datetime.strptime(date_str, '%y-%m-%d').date()
            
            file_path = os.path.join(args.input_folder,filename)
            with open(file_path, 'r') as f:
                data = json.load(f)
                for hashtag in args.hashtags:
                    count = data.get(hashtag, {}).get(str(date_obj),0) 
                    hashtag_counts[hashtag][date_obj] += count

# Convert string dates to datetime objects and sort
for hashtag in hashtag_counts:
    dates = list(hashtag_counts[hashtag].keys())
    counts = [hashtag_counts[hashtag][date] for date in dates]

    # Sort the dates for plotting
    sorted_dates = sorted(dates)
    sorted_counts = [hashtag_counts[hashtag][date] for date in sorted_dates]

    plt.plot(sorted_dates, sorted_counts, label=hashtag) 

# Plotting
plt.figure(figsize=(10, 6))

# Formatting the plot
plt.xlabel('Day of the Year')
plt.ylabel('Number of Tweets')
plt.title('Tweet Counts per Hashtag Over Time')
plt.legend()
plt.gca().xaxis.set_major_formatter(mdates.DateFormatter('%Y-%m-%d'))
plt.gca().xaxis.set_major_locator(mdates.DayLocator(interval=15))  # Adjust interval as needed
plt.gcf().autofmt_xdate()  # Rotate date labels
plt.tight_layout()

# Save the plot
plt.savefig('hashtag_trends.png')
plt.close()

print("Plot saved as 'hashtag_trends.png'")

