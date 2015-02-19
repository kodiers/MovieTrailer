class Movie():
    """
    This class provides a way to store movie related information
    """

    def __init__(self, movie_title, movie_storyline, poster_image, trailer_youtube, release_date):
        """
        Class constructor

        Initialize:
         title - Title of movie
         storyline - Description of movie
         poster_image_url - Link to poster image
         trailer_youtube_url - Link to movie trailer
         release_date - Movie's release date

        """
        self.title = movie_title        # Title of movie
        self.storyline = movie_storyline        # Description of movie
        self.poster_image_url = poster_image         # Link to poster image
        self.trailer_youtube_url = trailer_youtube        # Link to movie trailer
        self.release_date = release_date         # Movie's release date