import csv
from collections import Counter
from IPython import embed
from re import sub

def dot(phrase1, phrase2):
    """
    Defines the similarity between a sample
    and a list of words
    """
    score = 0
    for word in phrase2:
        if word in phrase1:
            score += phrase1[word]
    for word in phrase1:
        if word in phrase2:
            score += phrase2[word]
    return score

def create_sample_vector(sample):
    """
    Creates a vector out of a samples
    """
    word_dict = Counter()
    for el in sample[1].lower().split():
        word_dict[el] += 1
    for el in sample[2].lower().split():
        word_dict[el] += 1
    for el in sample[6].lower().split():
        word_dict[el] += 1

def create_vector(sample):
    word_dict = Counter()
    for word in sample:
        word_dict += 1
    return word_dict


def parse_samples(num_samples):
    """
    Parses the data from the zip file
    """
    answers = []
    vectors = []
    questions = []
    with open("output.csv") as f:
        csvreader = csv.reader(f)
        csvreader.next()
        for __ in range(num_samples):
            cur = csvreader.next()
            answers.append(cur[8])
            vectors.append(create_sample_vector(cur))
            answers.append(cur[8])
            questions.append(cur[2])
    return answers, vectors, questions

while True:
    entered = raw_input("Enter your question: ")
    entered = create_input_vector(entered.lower().split())
    best_answer = ""
    best_score = 0
    best_match = ""
    for i in range(len(vectors)):
        answer = answers[i]
        question = vectors[i]
        score = dot(question, entered)
        if score > best_score:
            best_answer = answer
            best_score = score
            best_match = questions[i]
    print(best_answer + "\n")





