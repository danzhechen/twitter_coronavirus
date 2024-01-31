# Twitter Coronavirus Hashtag Analysis

## Project Overview

This project involved analyzing Twitter data related to the coronavirus pandemic.
The goal was to track the usage and trends of various hashtags over time by scanning all geotagged tweets sent in 2020, providing insights into public discourse and sentiment surrounding the pandemic. 

## Methodology

The project was following the MapReduce procedure to analyze these tweets, which consists of three steps: partition, map, and reduce. The analysis was mainly conducted  in several phases:

1. **Data Procession (`map.py`)**:
   - Processed raw Twitter data based on the usage of the hashtags on both a language and country level.

2. **Data Aggregation (`reduce.py`)**: 
   - Aggregated data across multiple files to create a comprehensive dataset.

3. **Data Visualization (`visualize.py` and `alternative_reduce.py`)**:
   - Developed scripts to visualize the aggregated data.
   - Generated bar graphs and line plots showing the frequency of specific hashtags over time and top 10 keys based on language and country.
   - Plots were created for each hashtag, providing a clear visual representation of trends and patterns.

## Results

Five PNG files were generated as a part of this analysis. First four plots represented how language and country will contribute to the usage of certain hashtags. The last plot represented the usage trends of different hashtags related to the coronavirus pandemic. These visualizations offer an intuitive understanding of how discussions evolved on Twitter over specific periods.

*Example Plots:*

### Plot 1
![Plot 1](https://github.com/danzhechen/twitter_coronavirus/blob/master/plots/reduced_bargraph_1.png)

### Plot 2
![Plot 2](https://github.com/danzhechen/twitter_coronavirus/blob/master/plots/reduced_bargraph_2.png)

### Plot 3
![Plot 3](https://github.com/danzhechen/twitter_coronavirus/blob/master/plots/reduced_bargraph_3.png)

### Plot 4
![Plot 4](https://github.com/danzhechen/twitter_coronavirus/blob/master/plots/reduced_bargraph_4.png)

### Plot 5
![Plot 5](https://github.com/danzhechen/twitter_coronavirus/blob/master/plots/hashtag_trends.png)



