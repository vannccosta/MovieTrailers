class Movie():
    """Encapsula as propriedades dos filmes do Site de trailer de filmes
    """
    def __init__(self, movie_title, poster_image,
                 trailer_youtube, genero_filme, ano_lancamento):
        """Inicializa objetos da classe movie

        Args:
            self: uma instancia do objeto movie
            movie_title: Sequencia de strings que representam
                       o titulo do filme
            poster_image: Sequencia de strings que representam
                        URL da imagem do poster do filme
            trailer_youtube: Sequencia de strinfs que representam
                           a URL do trailer do filme no Youtube
        """
        self.title = movie_title
        self.poster_image_url = poster_image
        self.trailer_youtube_url = trailer_youtube
        self.genero = genero_filme
        self.ano = ano_lancamento
