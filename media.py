import webbrowser

class Movie:
    """ Movie class can initialize movie object and play trailer """

    def __init__(self, movie_title, movie_storyline, poster_image,
                 trailer_youtube):
        """ Constructor
        
        Arguments:
            movie_title {str} -- Movie title
            movie_storyline {str} -- Movie storyline
            poster_image {str} -- URL to poster (box art) image
            trailer_youtube {str} -- URL to youtube trailer
        """
        self.title = movie_title
        self.storyline = movie_storyline
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube

    def show_trailer(self):
        """ Opens trailer in browser """
        webbrowser.open(self.trailer_youtube_url)