import requests
from datetime import datetime
import pandas as pd

def get_movies_data():
    url = "https://www.cinemas.nos.pt/graphql/execute.json/cinemas/getAllMovies"
    
    try:
        response = requests.get(url)
        response.raise_for_status()  
    except requests.exceptions.RequestException as e:
        print(f"Request failed: {e}")
        return None, None, None, None
    
    try:
        jsonResponse = response.json()
        movies = jsonResponse['data']['movieList']['items']
    except ValueError as e:  # Catches JSON parsing errors
        print(f"JSON parsing error: {e}")
        return None, None, None, None

    today = datetime.now()
    cinemaReleases = []
    movieReleasesDates = []
    cinemaPremieres = []
    moviePremieresDates = []

    for movie in movies:
        movieDate = movie['releasedate'][:10]
        movieTitle = movie['title']
        release_date = datetime.strptime(movieDate, "%Y-%m-%d")

        if release_date > today:
            cinemaReleases.append(movieTitle)
            movieReleasesDates.append(movieDate)
        else: 
            cinemaPremieres.append(movieTitle)
            moviePremieresDates.append(movieDate)

    return cinemaReleases, movieReleasesDates, cinemaPremieres, moviePremieresDates

def save_to_file(option, releases, releases_dates, premieres, premieres_dates):
    if option == '1':
        filename = 'nos_upcoming_releases.csv'
        data = {'Movie': releases, 'Date': releases_dates}
    elif option == '2':
        filename = 'nos_past_premieres.csv'
        data = {'Movie': premieres, 'Date': premieres_dates}
    else:
        print("Invalid option selected.")
        return

    df = pd.DataFrame(data).sort_values(by=['Date']).reset_index(drop=True)
    df.to_csv(filename, index=False)
    print(f"Data saved to {filename}")

def main():
    releases, releases_dates, premieres, premieres_dates = get_movies_data()
    if releases is not None:
        print("Choose an option:\n1. Upcoming Releases\n2. Past Premieres")
        option = input("Enter your choice (1 or 2): ")
        save_to_file(option, releases, releases_dates, premieres, premieres_dates)

if __name__ == "__main__":
    main()
