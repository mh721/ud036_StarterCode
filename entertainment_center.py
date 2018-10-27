import media
import fresh_tomatoes

# initializing the movies

riddick = media.Movie("Riddick",
                      "Left for dead on a sun-scorched planet, Riddick " +
                      "finds himself up against an alien race of " +
                      "predators. Activating an emergency beacon alerts " +
                      "two ships: one carrying a new breed of mercenary, " +
                      "the other captained by a man from Riddick's past.",
                      "https://images-na.ssl-images-amazon.com/images/I/71J21ePe%2BsL._SY445_.jpg",  # NOQA
                      "https://www.youtube.com/watch?v=iP3eFIOBU0k"
                      )

deadpool = media.Movie("Deadpool",
                       "A fast-talking mercenary with a morbid sense of " +
                       "humor is subjected to a rogue experiment that " +
                       "leaves him with accelerated healing powers and a " +
                       "quest for revenge.",
                       "https://upload.wikimedia.org/wikipedia/en/2/23/Deadpool_%282016_poster%29.png",  # NOQA
                       "https://www.youtube.com/watch?v=ONHBaC-pfsk"
                       )

forrest_gump = media.Movie("Forrest Gump",
                           "The presidencies of Kennedy and Johnson, " +
                           "Vietnam, Watergate, and other history unfold " +
                           "through the perspective of an Alabama man with " +
                           "an IQ of 75.",
                           "https://m.media-amazon.com/images/M/MV5BNWIwODRlZTUtY2U3ZS00Yzg1LWJhNzYtMmZiYmEyNmU1NjMzXkEyXkFqcGdeQXVyMTQxNzMzNDI@._V1_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=bLvqoHBptjg"
                           )

fight_club = media.Movie("Fight Club",
                         "An insomniac office worker and a devil-may-care " +
                         "soapmaker form an underground fight club that " +
                         "evolves into something much, much more.",
                         "https://m.media-amazon.com/images/M/MV5BMjJmYTNkNmItYjYyZC00MGUxLWJhNWMtZDY4Nzc1MDAwMzU5XkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY1000_CR0,0,676,1000_AL_.jpg",  # NOQA
                         "https://www.youtube.com/watch?v=BdJKm16Co6M"
                         )

pulp_fiction = media.Movie("Pulp Fiction",
                           "The lives of two mob hit-men, a boxer, " +
                           "a gangster's wife, and a pair of diner bandits " +
                           "intertwine in four tales of violence and " +
                           "redemption.",
                           "https://m.media-amazon.com/images/M/MV5BNGNhMDIzZTUtNTBlZi00MTRlLWFjM2ItYzViMjE3YzI5MjljXkEyXkFqcGdeQXVyNzkwMjQ5NzM@._V1_SY1000_CR0,0,686,1000_AL_.jpg",  # NOQA
                           "https://www.youtube.com/watch?v=s7EdQ4FqbhY"
                           )

matrix = media.Movie("The Matrix",
                     "A computer hacker learns from mysterious rebels about " +
                     "the true nature of his reality and his role in the " +
                     "war against its controllers.",
                     "https://m.media-amazon.com/images/M/MV5BNzQzOTk3OTAtNDQ0Zi00ZTVkLWI0MTEtMDllZjNkYzNjNTc4L2ltYWdlXkEyXkFqcGdeQXVyNjU0OTQ0OTY@._V1_SY1000_CR0,0,665,1000_AL_.jpg",  # NOQA
                     "https://www.youtube.com/watch?v=tGgCqGm_6Hs"
                     )

# push movies in the movies list
movies = [riddick, deadpool, forrest_gump, fight_club, pulp_fiction, matrix]

# generate and open html
fresh_tomatoes.open_movies_page(movies)
