import requests
from bs4 import BeautifulSoup
import pandas as pd

def main():
    url = 'https://www.imdb.com/calendar/?ref_=rlm&region=PT&type=MOVIE'
    headers = {
        'User-Agent': 'Mozilla/5.0 (your updated user agent string here)'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  
        html = response.text

        soup = BeautifulSoup(html, "html.parser")
        moviesByDate = soup.find_all('article', {'data-testid': 'calendar-section'})

        movie_data = []

        for dates in moviesByDate:
            date = dates.find('h3').text
            moviesList = dates.find_all('a')
            
            for movie in moviesList:
                movie_title = movie.text.strip()  
                # Check if movie title is not empty and possibly contains a year in parentheses
                if movie_title and '(' in movie_title and ')' in movie_title:
                    movie_data.append({'Date': date, 'Movie': movie_title})

        releasesDF = pd.DataFrame(movie_data)

        csv_file_path = 'imdb_upcoming_movies_portugal.csv'  
        releasesDF.to_csv(csv_file_path, index=False)
        print(f"CSV file created: {csv_file_path}")

    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    main()