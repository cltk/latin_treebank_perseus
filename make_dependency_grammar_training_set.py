from lxml import etree
import os

__author__ = ['Kyle P. Johnson <kyle@kyle-p-johnson.com>', 'Stephen Margheim <stephen.margheim@gmail.com>']
__license__ = 'MIT License. See LICENSE.'




def get_files():
    """Return a Generator of the Perseus Latin Treebank XML files
    
    """
    '''
    files = os.listdir('treebank_perseus_latin')
    for file in files:
        if file.endswith('.xml'):
            yield file
    '''


def get_tags():
    treebank_training_set = []
    entire_treebank = 'latin_treebank_perseus/ldt-1.5.xml'
    with open(entire_treebank, 'r') as f:
        xml_string = f.read()
    root = etree.fromstring(xml_string)
    sentences = root.findall('sentence')

    sentences_list = []
    for sentence in sentences:  # note: sentence is Element
        words_list = sentence.findall('word')
        sentence_list = []
        for x in words_list:  #note: word is class
            word = x.attrib
            form = word['form']
            #lemma = word['lemma']
            postag = word['postag']
            head = word['head']
            relation = word['relation']
            word_grammar = '\t'.join([form, postag, head, relation])
            sentence_list.append(word_grammar)
        joined_sentence = '\n'.join(sentence_list)
        sentences_list.append(joined_sentence)

    joined_sentences = '\n\n'.join(sentences_list)

    with open('dg_training_set.txt', 'w') as f:
        f.write(joined_sentences)


def main():
    get_tags()


if __name__ == "__main__":
    main()
