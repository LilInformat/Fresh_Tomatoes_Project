import webbrowser

#Video Class
class Video():
	def __init__(self,title, genre, rating, description):
		self.title = title
		self.genre = genre
		self.rating = rating
		self.description = description

#Movie Class
class Movie(Video):
	def __init__(self, title, genre, rating, description, poster_url, youtube_url):
		Video.__init__(self,title,genre,rating,description)
		self.poster_image_url = poster_url
		self.trailer_youtube_url = youtube_url
		
	def show_trailer(self):
		webbrowser.open(self.trailer_youtube_url)