from lxml import etree
import os

__author__ = ['Kyle P. Johnson <kyle@kyle-p-johnson.com>', 'Stephen Margheim <stephen.margheim@gmail.com>']
__license__ = 'MIT License. See LICENSE.'


def get_tags():
    entire_treebank = 'latin_treebank_perseus/ldt-1.5.xml'
    with open(entire_treebank, 'r') as f:
        xml_string = f.read()
    root = etree.fromstring(xml_string)
    sentences = root.findall('sentence')

    sentences_list = []
    for sentence in sentences:  # note: sentence is Element
        words_list = sentence.findall('word')
        sentence_list = []
        # http://ilk.uvt.nl/conll/
        for x in words_list:  # note: word is class
            word = x.attrib
            #id = word['id']
            form = word['form'].lower()
            #lemma = word['lemma']
            #cpostag = word['relation']  # Coarse-grained part-of-speech tag
            postag = word['postag']
            #feats = '_'  # an underscore if not available
            #head = word['head']
            #deprel = word['head']
            #phead = '_'
            #pderprel = '_'
            word_tag = '/'.join([form, postag])
            sentence_list.append(word_tag)
        sentence_str = ' '.join(sentence_list)
        sentences_list.append(sentence_str)
    treebank_training_set = '\n\n'.join(sentences_list)

    with open('latin_training_set.pos', 'w') as f:
        f.write(treebank_training_set)


def main():
    get_tags()


if __name__ == "__main__":
    main()
