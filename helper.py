import os
import numpy as np
import nltk
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse


nltk.download('stopwords')


def get_tokenized_list(doc_text):
    tokens = nltk.word_tokenize(doc_text)
    return tokens


def word_stemmer(token_list):
    ps = nltk.stem.PorterStemmer()
    stemmed = []
    for words in token_list:
        stemmed.append(ps.stem(words))
    return stemmed


def remove_stopwords(doc_text):
    stop_words = set(nltk.corpus.stopwords.words('english'))
    cleaned_text = []
    for words in doc_text:
        if words not in stop_words:
            cleaned_text.append(words)
    return cleaned_text


def Clean_Data(input_text):
    input_text = get_tokenized_list(input_text)
    input_text = remove_stopwords(input_text)
    q = []
    for w in word_stemmer(input_text):
        q.append(w)
    q = ' '.join(q)
    return q


def Run_Model(input_text):
    cleaned_input = Clean_Data(input_text)
    tf_idf = pickle.load(open('tf-idf.sav', 'rb'))
    query_vector = tf_idf.transform([cleaned_input])
    doc_vectors = sparse.load_npz("doc_vector.npz")
    cosineSimilarities = cosine_similarity(doc_vectors, query_vector).flatten()
    related_docs_indices = cosineSimilarities.argsort()[:-10:-1]
    return related_docs_indices


def Read_Content(the_input):
    all_content = {}
    indices = Run_Model(the_input)
    for each_index in indices:
        path = os.getcwd()
        path = path + '/data/' + file_names[each_index]
        file = open(path, "r")
        content_in_file = file.read()
        all_content[file_names[each_index]] = content_in_file
    return all_content


file_names = np.load("file_names.npy")
