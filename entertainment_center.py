import media
import fresh_tomatoes

# initializing the movies

riddick = media.Movie("Riddick", 
                      "Left for dead on a sun-scorched planet, Riddick " +
                      "finds himself up against an alien race of " +
                      "predators. Activating an emergency beacon alerts " +
                      "two ships: one carrying a new breed of mercenary, " +
                      "the other captained by a man from Riddick's past.",
                      "https://images-na.ssl-images-amazon.com/images/I/71J21ePe%2BsL._SY445_.jpg",
                      "https://www.youtube.com/watch?v=iP3eFIOBU0k"
                      )

deadpool = media.Movie("Deadpool", 
                       "A fast-talking mercenary with a morbid sense of humor " +
                       "is subjected to a rogue experiment that leaves him " +
                       "with accelerated healing powers and a quest for revenge.",
                       "https://upload.wikimedia.org/wikipedia/en/2/23/Deadpool_%282016_poster%29.png",
                       "https://www.youtube.com/watch?v=ONHBaC-pfsk"
                       )

movies = [riddick, deadpool] 

fresh_tomatoes.open_movies_page(movies)