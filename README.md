# Movies Release Data Scraper

## Introduction
This repository contains Python scripts for scraping movie release data from three different websites: IMDb (for movies releasing in Portugal), Cinemas NOS, and Castello Lopes Cinemas. 

## Scripts Overview

### 1. IMDb - Upcoming Movies in Portugal
The `imdb_upcoming_movies_portugal.py` script scrapes data about upcoming movie releases in Portugal from IMDb. It organizes the data and saves it as a CSV file.

### 2. Cinemas NOS - Upcoming Movies
The `nos_upcoming_premier_movies.py` script extracts data from the Cinemas NOS website. It categorizes movies into upcoming releases and past premieres, based on the user's choice, and saves the information to a CSV file.

### 3. Castello Lopes Cinemas - Upcoming Movies
The `castello_lopes_upcoming_premier_movies.py` script extracts data from the Castello Lopes Cinemas website. It categorizes movies into upcoming releases and past premieres, based on the user's choice, and saves the information to a CSV file.

## Requirements
- Python 3
- Libraries: `requests`, `beautifulsoup4`, `pandas`

## How to Run
1. Clone the repository or download the scripts.
   ```bash
   git clone git@github.com:Fredd124/Cinema-Web-Scrapper.git
   cd Cinema-Web-Scrapper
2. Install the required Python libraries:
   ```bash
   pip install requests beautifulsoup4 pandas
   ````
3. Run the script of your choice:
   ```bash
   python3 imdb_upcoming_movies_portugal.py
   ```
   ```bash
   python3 nos_upcoming_premier_movies.py
   ```
   ```bash
   python3 castello_lopes_upcoming_premier_movies.py
   ```

## Observations
When testing both the NOS and Castello Lopes web scrappers, it was observed that for movies with long titles, parts of these titles are sometimes truncated in our data. This issue arises due to limitations in the website responses we are scraping from. Since the data extraction is dependent on how information is presented on these websites, long movie titles may not be fully captured if the website itself abbreviates them in its listings.
