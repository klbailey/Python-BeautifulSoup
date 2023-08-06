import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

#where we are getting the html from and returns object
response = requests.get(URL)
#take html page sends request and text retrieves the html and parses info in html format
soup = BeautifulSoup(response.text, 'html.parser')
#from inspection of site <h3 class="title"
all_movies = soup.find_all(name="h3", class_="title")
#pulls movie titles from html 100-1 order as listed on url
movie_titles = [movie.getText() for movie in all_movies]
#reverse from 100-1 to 1-100 start/stop/step reversal slice
movies = movie_titles[::-1]
#create text file mode "w" to write
#encoding due to windows 11 runs 8 bit character set due to 'open' behavior-will match behavior of Notepad
with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")