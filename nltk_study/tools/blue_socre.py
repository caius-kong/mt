# coding=utf-8
import nltk
from nltk.tokenize import word_tokenize
from nltk.translate.bleu_score import corpus_bleu

nltk.download('punkt')


class BleuScore(object):
    @staticmethod
    def calculate(reference_sentences, candidate_sentences):
        references = [[word_tokenize(sentence)] for sentence in reference_sentences]
        candidates = [word_tokenize(sentence) for sentence in candidate_sentences]
        return corpus_bleu(references, candidates)


if __name__ == '__main__':
    # reference_sentences = ['this is a test', 'how old are you']
    # candidate_sentences = ['this is a test.', 'how old are you?']

    reference_file = '../input/reference.align'
    candidate_file = '../input/candidate.align'
    with open(reference_file, 'r', encoding='utf-8') as f:
        reference_sentences = [line.strip('\n') for line in f.readlines()]
    with open(candidate_file, 'r', encoding='utf-8') as f:
        candidate_sentences = [line.strip('\n') for line in f.readlines()]

    print(BleuScore.calculate(reference_sentences, candidate_sentences))
