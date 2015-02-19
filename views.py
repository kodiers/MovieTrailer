import models
import fresh_tomatoes

# Create objects
toy_story = models.Movie("Toy Story",
                        "A story of a boy and his toys that come to life",
                        "http://upload.wikimedia.org/wikipedia/en/1/13/Toy_Story.jpg",
                        "http://www.youtube.com/watch?v=KYz2wyBy3kc", "November 22, 1995")
avatar = models.Movie("Avatar", "A marine on an alien planet",
                     "http://upload.wikimedia.org/wikipedia/en/b/b0/Avatar-Teaser-Poster.jpg",
                     "http://www.youtube.com/watch?v=d1_JBMrrYw8", "December 10, 2009")
iron_man = models.Movie("Iron Man 2", "About Tony Stark :)",
                       "http://photos.imageevent.com/afap/wallpapers/movies/ironman2/iron_man_2_poster.jpg",
                       "http://www.youtube.com/watch?v=FNQowwwwYa0", "April 26, 2010")
avengers = models.Movie("Avengers", "A adventures of the Loki :)",
                       "http://www.theaterhopper.com/wordpress/wp-content/uploads/2012/02/avengers_poster.jpg",
                       "http://www.youtube.com/watch?v=eOrNdBpGMv8", "April 11, 2012")
sherlock = models.Movie("Sherlock", "Some variant about Sherlock Holmes theme",
                       "http://img4.wikia.nocookie.net/__cb20130202212947/bakerstreet/images/d/db/Sherlock_holmes_ritchie.jpg",
                       "http://www.youtube.com/watch?v=I0hXhGt5XPg", "December 25, 2009")
lucy = models.Movie("Lucy", "Another perfect film from L. Besson",
                   "http://mr.comingsoon.it/imgdb/locandine/235x336/50417.jpg",
                   "http://www.youtube.com/watch?v=MVt32qoyhi0", "July 25, 2014")

movies = [toy_story, avatar, iron_man, avengers, sherlock, lucy]     # Create array of object
fresh_tomatoes.open_movies_page(movies)        # Create and render html page
