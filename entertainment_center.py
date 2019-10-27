import fresh_tomatoes
import media


# Cria uma instancia da classe Movie para cada filme
toy_story4 = media.Movie("Toy Story 4",
                         "https://m.media-amazon.com/images/M/MV5BMTYzMDM4Nzkx"
                         "OV5BMl5BanBnXkFtZTgwNzM1Mzg2NzM@._V1_SY1000_CR0,0,67"
                         "4,1000_AL_.jpg",
                         "https://www.youtube.com/watch?v=wmiIUN-7qhE",
                         "Animacao, Aventura, Comedia",
                         "2019")


the_lion_king = media.Movie("The Lion King",
                            "https://m.media-amazon.com/images/M/MV5BMjIwMjE1N"
                            "zc4NV5BMl5BanBnXkFtZTgwNDg4OTA1NzM@._V1_SY1000_CR"
                            "0,0,674,1000_AL_.jpg",
                            "https://www.youtube.com/watch?v=7TavVZMewpY",
                            "Animacao,Aventura,Comedia",
                            "2019")


rocketman = media.Movie("Rocketman",
                        "https://m.media-amazon.com/images/M/MV5BMTY0MzUwODc4N"
                        "15BMl5BanBnXkFtZTgwMjMyMjY0NzM@._V1_SY1000_CR0,0,675,"
                        "1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=S3vO8E2e6G0",
                        "Biografia, Drama, Musical",
                        "2019")

star_is_born = media.Movie("A Star Is Born",
                           "https://m.media-amazon.com/images/M/MV5BNmE5ZmE3OG"
                           "ItNTdlNC00YmMxLWEzNjctYzAwOGQ5ODg0OTI0XkEyXkFqcGde"
                           "QXVyMTMxODk2OTU@._V1_SY1000_CR0,0,666,"
                           "1000_AL_.jpg",
                           "https://www.youtube.com/watch?v=nSbzyEJ8X9E",
                           "Drama, Musical, Romance",
                           "2018")

bohemian_rhapsody = media.Movie("Bohemian Rhapsody",
                                "https://m.media-amazon.com/images/M/MV5BMTA2N"
                                "Dc3Njg5NDVeQTJeQWpwZ15BbWU4MDc1NDcxNTUz._V1_S"
                                "Y1000_CR0,0,674,1000_AL_.jpg",
                                "https://www.youtube.com/watch?v=mP0VHJYFOAU",
                                "Biografia, Drama, Musical",
                                "2018")

deadpool = media.Movie("Deadpool",
                       "https://m.media-amazon.com/images/M/MV5BYzE5MjY1ZDgtMT"
                       "kyNC00MTMyLThhMjAtZGI5OTE1NzFlZGJjXkEyXkFqcGdeQXVyNjU0"
                       "OTQ0OTY@._V1_SY1000_CR0,0,666,1000_AL_.jpg",
                       "https://www.youtube.com/watch?v=Xithigfg7dA",
                       "Acao, Aventura, Comedia",
                       "2016")

click = media.Movie("Click",
                    "https://m.media-amazon.com/images/M/MV5BMTA1MTUxNDY4NzReQ"
                    "TJeQWpwZ15BbWU2MDE3ODAxNw@@._V1_.jpg",
                    "https://www.youtube.com/watch?v=iEIbN37hYNU",
                    "Comedia, Drama, Fantasia",
                    "2006")

the_hangover = media.Movie("The Hangover",
                           "https://m.media-amazon.com/images/M/MV5BNGQwZjg5Ym"
                           "YtY2VkNC00NzliLTljYTctNzI5NmU3MjE2ODQzXkEyXkFqcGde"
                           "QXVyNzkwMjQ5NzM@._V1_SX675_CR0,0,675,999_AL_.jpg",
                           "https://www.youtube.com/watch?v=tcdUhdOlz9M",
                           "Comedia",
                           "2009")


inception = media.Movie("Inception",
                        "https://m.media-amazon.com/images/M/MV5BMjAxMzY3NjcxN"
                        "F5BMl5BanBnXkFtZTcwNTI5OTM0Mw@@._V1_SY1000_CR0,0,675,"
                        "1000_AL_.jpg",
                        "https://www.youtube.com/watch?v=YoHD9XEInc0",
                        "Acao, Aventura, Sci-Fi",
                        "2010")

# Cria uma lista das instancias da classe Movie
movies = [toy_story4, the_lion_king, rocketman, star_is_born,
          bohemian_rhapsody, deadpool, inception, the_hangover, click]

# Monta a pagina de filmes baseada na lista de instancias da classe Movie
fresh_tomatoes.open_movies_page(movies)
