#!/usr/bin/env python3

# command line args
import argparse
parser = argparse.ArgumentParser()
parser.add_argument('--input_path',required=True)
parser.add_argument('--key',required=True)
parser.add_argument('--percent',action='store_true')
parser.add_argument('--graph_number', type=int, required=True)
args = parser.parse_args()

# imports
import os
import json
from collections import Counter,defaultdict
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# open the input path
with open(args.input_path) as f:
    counts = json.load(f)

# normalize the counts by the total values
if args.percent:
    for k in counts[args.key]:
        counts[args.key][k] /= counts['_all'][k]

# sort the count values and select the top 10 keys
items = sorted(counts[args.key].items(), key=lambda item: (item[1],item[0]), reverse=True)
top_items = items[0:9]
keys, values = zip(*top_items)

# Generate and save the bar graph
plt.figure(figsize=(10, 6))
plt.bar(keys, values)
plt.xlabel('Keys')
plt.ylabel('Values')
plt.title('Top 10 Keys by Value')
plt.xticks(rotation=45)
plt.tight_layout()  

output_file_name = f"reduced_bargraph_{args.graph_number}.png"
output_path = os.path.join(os.path.dirname(args.input_path), output_file_name)

plt.savefig(output_path)
print(f"Bar graph saved to {output_path}")






