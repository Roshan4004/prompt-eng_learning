from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords

def get_synonyms(word):
    synonyms = []
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            synonyms.append(lemma.name())
    return synonyms

def paraphrase_sentence(sentence):
    tokens = word_tokenize(sentence)
    stop_words = set(stopwords.words('english'))
    paraphrased_tokens = []

    for token in tokens:
        if token.lower() in stop_words or not token.isalnum():
            paraphrased_tokens.append(token)
            continue
        
        synonyms = get_synonyms(token)
        if synonyms:
            semantic_similarity = {}
            for synonym in synonyms:
                if synonym != token:
                    similarity_score = wordnet.synsets(token)[0].wup_similarity(wordnet.synsets(synonym)[0])
                    if similarity_score:
                        semantic_similarity[synonym] = similarity_score
            
            if semantic_similarity:
                sorted_synonyms = sorted(semantic_similarity, key=semantic_similarity.get, reverse=True)
                paraphrased_tokens.append(sorted_synonyms[0])
            else:
                paraphrased_tokens.append(token)
        else:
            paraphrased_tokens.append(token)
    
    paraphrased_sentence = ' '.join(paraphrased_tokens)
    return paraphrased_sentence

