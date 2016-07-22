from media import Movie
import fresh_tomatoes


#All movie descriptions, genre information and ratings are acquired from http://www.imdb.com

#Movie Instances
toy_story = Movie("Toy Story",
					"A cowboy doll is profoundly threatened and jealous when a new spaceman figure supplants him as top toy in a boy's room.",
					"https://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
					"https://youtu.be/KYz2wyBy3kc",
					"8.3",
					"Animation, Adventure, Comedy")

kungfu_panda = Movie("Kung Fu Panda",
				"In the Valley of Peace, Po the Panda finds himself chosen as the Dragon Warrior despite the fact that he is obese and a complete novice at martial arts.",
				"https://upload.wikimedia.org/wikipedia/en/7/76/Kungfupanda.jpg",
				"https://www.youtube.com/watch?v=PXi3Mv6KMzY",
				"7.6",
				"Animation, Action, Adventure")

les_mis = Movie("Les Miserables",
				"In 19th-century France, Jean Valjean, who for decades has been hunted by the ruthless policeman Javert after breaking parole, agrees to care for a factory worker's daughter. The decision changes their lives forever.",
				"https://upload.wikimedia.org/wikipedia/en/b/b0/Les-miserables-movie-poster1.jpg",
				"https://www.youtube.com/watch?v=IuEFm84s4oI",
				"7.6",
				"Drama, Musical, Romance")

interstellar = Movie("Interstellar",
					"A team of explorers travel through a wormhole in space in an attempt to ensure humanity's survival.",
					"https://upload.wikimedia.org/wikipedia/en/b/bc/Interstellar_film_poster.jpg",
					"https://www.youtube.com/watch?v=0vxOhd4qlnA",
					"8.6",
					"Adventure, Drama, Sci-Fi")

lotr = Movie("Lord of the Rings: The Fellowship of the Ring",
			"A meek Hobbit and eight companions set out on a journey to destroy the One Ring and the Dark Lord Sauron.",
			"https://upload.wikimedia.org/wikipedia/en/0/0c/The_Fellowship_Of_The_Ring.jpg",
			"https://www.youtube.com/watch?v=Pki6jbSbXIY",
			"8.8",
			"Action, Adventure, Drama")

#Creating a list and the website page
movies = [toy_story,lotr,interstellar]
fresh_tomatoes.open_movies_page(movies)