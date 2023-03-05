import spacy 

nlp = spacy.load("en_core_web_md")

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word1))
print(word3.similarity(word2))

tokens = nlp("yellow flame sleep mango")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

sentence_to_compare = "Why is my cat on the car"

sentences = ["where did my dog go",
"Hello there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]

model_sentence = nlp(sentence_to_compare)

for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ", similarity)


#Note similarities between cat, monkey, banana
# Cat and monkey relatively high level of similarity recognzing both are animals
# Similarity between monkey and banana not there with the cat
# as an example demonstrates en_core_web_md finding similarities and disimilarities between animals and animals relations to different  
# Finds similar similarites between human and sailor - and then with sailor and boat


# Difference between en_core_web_sm and en_core_web_md 
# en_core_web_md broader model including word vectors - en_core_web_sm determines similarity with tagger, parser, NER - not returning equally useful similarity judgments





