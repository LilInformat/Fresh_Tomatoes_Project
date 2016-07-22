import webbrowser

class Movie():
    #Constructor for Movie Class
    def __init__(self, title, storyline, poster_url, youtube_url, rating, genre):
        self.title = title
        self.storyline = storyline
        self.poster_image_url = poster_url
        self.trailer_youtube_url = youtube_url
        self.rating = rating
        self.genre = genre

    #Opens a browser window with the youtube_url
    def show_trailer(self):
        webbrowser.open(self.youtube_url)