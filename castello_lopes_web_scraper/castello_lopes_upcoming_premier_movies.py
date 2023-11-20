import requests
from bs4 import BeautifulSoup
from datetime import datetime
import pandas as pd

def get_movies_data():
    url = 'https://castellolopescinemas.pt/'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.110 Safari/537.36'
    }

    try:
        response = requests.get(url, headers=headers)
        response.raise_for_status()  # Raises an HTTPError for bad requests
    except requests.exceptions.RequestException as e:
        print(f"HTTP request error: {e}")
        return None, None, None, None

    html = response.text
    soup = BeautifulSoup(html, "html.parser")

    ul = soup.find_all('ul')
    moviesList = ul[5].find_all('li')

    today = datetime.now()
    cinemaReleases = []
    movieReleasesDates = []
    cinemaPremieres = []
    moviePremieresDates = []

    for movies in moviesList:
        movieInfo = movies.find_all('div')

        # Check if movieInfo has enough elements
        if len(movieInfo) > 5:
            try:
                movieDate = movieInfo[4].text
                release_date = datetime.strptime(movieDate, "%d.%m.%Y")

                if release_date > today:
                    cinemaReleases.append(movieInfo[5].text)
                    movieReleasesDates.append(movieDate)
                else:
                    cinemaPremieres.append(movieInfo[5].text)
                    moviePremieresDates.append(movieDate)
            except Exception as e:
                print(f"Error processing movie: {e}")

    return cinemaReleases, movieReleasesDates, cinemaPremieres, moviePremieresDates

def save_to_file(option, releases, releases_dates, premieres, premieres_dates):
    if option == '1':
        filename = 'castello_lopes_upcoming_releases.csv'
        df = pd.DataFrame({'Movie': releases, 'Date': pd.to_datetime(releases_dates, format='%d.%m.%Y')})
    elif option == '2':
        filename = 'castello_lopes_past_premieres.csv'
        df = pd.DataFrame({'Movie': premieres, 'Date': pd.to_datetime(premieres_dates, format='%d.%m.%Y')})
    else:
        print("Invalid option selected.")
        return

    df = df.sort_values(by=['Date']).reset_index(drop=True)
    df['Date'] = df['Date'].dt.strftime('%d.%m.%Y')
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
