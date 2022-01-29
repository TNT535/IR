import os
import numpy as np
import nltk
import pickle
from sklearn.metrics.pairwise import cosine_similarity
from scipy import sparse
from underthesea import word_tokenize


nltk.download('punkt')
nltk.download('stopwords')

with open('vietnamese-stopwords-dash.txt', mode='r', encoding='utf-8') as f:
    stop_words = set(f.read().split())


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
    stop_words_en = set(nltk.corpus.stopwords.words('english'))
    cleaned_text = []
    for words in doc_text:
        if words not in stop_words_en:
            cleaned_text.append(words)
    return cleaned_text


def token_corpus(text):
    tokens = word_tokenize(text)
    return tokens


def get_tokenized_list_vi(doc_text):
    tokens = word_tokenize(doc_text, format="text")
    tokens = nltk.word_tokenize(tokens)
    return tokens


def remove_stopwords_vi(doc_text):
    cleaned_text = []
    for words in doc_text:
        if words not in stop_words:
            cleaned_text.append(words)
    return cleaned_text


def Clean_Data(input_text):
    input_text = get_tokenized_list_vi(input_text)
    input_text = remove_stopwords_vi(input_text)
    q = ' '.join(input_text)
    return q


def Run_Model(input_text):
    cleaned_input = Clean_Data(input_text)
    tf_idf = pickle.load(open('tf-idf-vietnamese.sav', 'rb'))
    query_vector = tf_idf.transform([cleaned_input])
    doc_vectors = sparse.load_npz("doc_vector_vietnamese.npz")
    cosineSimilarities = cosine_similarity(doc_vectors, query_vector).flatten()
    related_docs_indices = cosineSimilarities.argsort()[:-21:-1]
    return related_docs_indices


def Read_Content(the_input):
    all_content = {}
    indices = Run_Model(the_input)
    for each_index in indices:
        path = os.getcwd()
        path = path + '/mini_news_dataset/news_dataset/' + file_names[each_index]
        file = open(path, "rb")
        content_in_file = file.read()
        all_content[file_names[each_index]] = content_in_file
    return all_content


def Evaluate_System(queries):
    count = 0
    average_precisions = 0
    for each_query in queries:
        relevant_indices = Run_Model(each_query)
        path_of_ground_truth = os.getcwd() + '/ground_truth/' + 'gt_' + str(count) + '.txt'
        ground_truth_files = open(path_of_ground_truth, "r")
        ground_truth_content = ground_truth_files.read()
        relevant_files = ground_truth_content.split('\n')
        predicted_files = [file_names[index] for index in relevant_indices]
        cur = 1
        true_relevant = 0
        precisions = 0
        for each_predicted in predicted_files:
            if each_predicted in relevant_files:
                true_relevant += 1
                precisions += true_relevant / cur
            cur += 1
        average_precisions += precisions / 20  # Because each query was labeled has 20 relevant files
        count += 1
    MAP = average_precisions / 10  # queries were labeled
    return MAP


file_names = np.load("file_names_vietnamese.npy")

