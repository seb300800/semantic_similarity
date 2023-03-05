# Import relevant spacy 

import spacy 
nlp = spacy.load("en_core_web_md")


# Description + nlp of description

planet_hulk_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for Earth, the Illuminati trick Hulk into a shuttle and launch him into a space to a planet where the Hulk can live in peace. Unfortunately Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator"
model_hulk = nlp(planet_hulk_description)


# Reading from file and initializing relevant lists

with open("movies.txt", "r") as file:
    temp = file.readlines()

check_similarity = 0
movie_list = []
similarity_list = []


# Iterates through temp from movie list 
# Splits movie by semicolon to only compare descriptions similarity and not Movie A, Movie B etc
# Compares similarity - for each similarity higher than last append movie and similarity score to relevant lists 
# Also sets the score to compare new similarity score to as the highest similarity score to date
for movie in temp:
    movie = movie.split(":")
    similarity = nlp(movie[1]).similarity(model_hulk)
    if similarity > check_similarity:
        movie_list.append(movie)
        check_similarity = similarity
        similarity_list.append(similarity)

# Formatting 
movie_list[-1] = " ".join(movie_list[-1])

# Outputs the most similar movie and similarity score by taking last item added to each relevant list 
print(f"\nThe movie most similar to Planet Hulk is - {movie_list[-1]} with a similarity score of {similarity_list[-1]}")


