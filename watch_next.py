# Import relevant spacy 

import spacy 
nlp = spacy.load("en_core_web_md")

with open("movies.txt", "r") as file:
        temp = file.readlines()

def next_movie():

    # Description + nlp of description
    planet_hulk_description = "Will he save their world or destroy it? When the Hulk becomes too dangerous for Earth, the Illuminati trick Hulk into a shuttle and launch him into a space to a planet where the Hulk can live in peace. Unfortunately Hulk lands on the planet Sakaar where he is sold into slavery and trained as a gladiator"
    model_hulk = nlp(planet_hulk_description)

    # Iterates through temp from movie list 
    # Splits movie by semicolon to only compare descriptions similarity and not Movie A, Movie B etc
    # Compares similarity - for each similarity higher than last append movie and similarity score to relevant lists 
    # Also sets the score to compare new similarity score to as the highest similarity score to date

    check_similarity = 0
    for movie in temp:
        movie = movie.split(":")
        similarity = nlp(movie[1]).similarity(model_hulk)
        if similarity > check_similarity:
            #assigning movie and similarity and check similarity by string allocation and replacement
            check_similarity = similarity
            movie_reccomendation = movie
            similarity_score = similarity
    
    # Formatting 
    movie_reccomendation = " ".join(movie_reccomendation)


    # Outputs the most similar movie and similarity score by taking last item added to each relevant list 
    print(f"\nThe movie most similar to Planet Hulk is - {movie_reccomendation} It has a similarity score of {similarity_score}")


#Calls function as needed
next_movie()





