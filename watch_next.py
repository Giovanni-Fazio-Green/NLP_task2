import spacy

# read in the movies description from the text file
with open("movies.txt", 'r') as file:
    movies_descrption = file.read().splitlines() 

# 'The Hulk' description
movie_watched_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# load the 'md' model
nlp = spacy.load('en_core_web_md') 

# --- Function to find most probable movie the user may like --- #

def find_next_movie(movie_watched_description: str) -> str:

    """
    This function takes as input the description of the movie
    watched by the user as a string.
    It returns a string indicating what the best next movie to
    watch might be, given a list of movies' descriptions.
    """

    # dictionary to store the each movie name and its similarity score
    # with 'The Hulk' description
    score_by_movie = {}

    # initialize mlp object with 'The Hulk' description
    movie_watched_description = nlp(movie_watched_description)

    for movie_to_watch in movies_descrption:
        # for each movie in the list of movies to watch, initialize nlp object
        # for that movie
        movie_to_watch = nlp(movie_to_watch)
        # get the similarity score using the 'similarity()' nlp method
        score = movie_to_watch.similarity(movie_watched_description)
        # update the dictionary with the current movie name and its score with 'The Hulk'
        score_by_movie.update({movie_to_watch[:2]: score})

    # return the name of the movie with the maximum score in the dictionary
    return max(score_by_movie, key = score_by_movie.get)

# call the function to get recommendation
most_probable_recommendation = find_next_movie(movie_watched_description=movie_watched_description)

# print message of best recommendation
print(f"\nGiven that you watch 'The Hulk', you might like {most_probable_recommendation}!")
