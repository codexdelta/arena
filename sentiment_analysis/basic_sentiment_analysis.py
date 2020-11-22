import codecs
from pprint import pprint
import nltk
import yaml
import sys
import os
import re

class Splitter(object):

    def __init__(self):
        self.nltk_splitter = nltk.data.load('tokenizers/punkt/english.pickle')
        self.nltk_tokenizer = nltk.tokenize.TreebankWordTokenizer()

    def split(self, text):
        """
        input format: a paragraph of text
        output format: a list of lists of words.
            e.g.: [['this', 'is', 'a', 'sentence'], ['this', 'is', 'another', 'one']]
        """
        sentences = self.nltk_splitter.tokenize(text)
        tokenized_sentences = [self.nltk_tokenizer.tokenize(sent) for sent in sentences]
        return tokenized_sentences


class POSTagger(object):

    def __init__(self):
        pass
        
    def pos_tag(self, sentences):
        pos = [nltk.pos_tag(sentence) for sentence in sentences]
        #adapt format
        pos = [[(word, word, [postag]) for (word, postag) in sentence] for sentence in pos]
        return pos

class DictionaryTagger(object):

    def __init__(self, dictionary_paths):
        files = [open(path, 'r') for path in dictionary_paths]
        dictionaries = [yaml.load(dict_file) for dict_file in files]
        map(lambda x: x.close(), files)
        self.dictionary = {}
        self.max_key_size = 0
        for curr_dict in dictionaries:
            for key in curr_dict:
                if key in self.dictionary:
                    self.dictionary[key].extend(curr_dict[key])
                else:
                    self.dictionary[key] = curr_dict[key]
                    self.max_key_size = max(self.max_key_size, len(key))

    def tag(self, postagged_sentences):
        return [self.tag_sentence(sentence) for sentence in postagged_sentences]

    def tag_sentence(self, sentence, tag_with_lemmas=False):
        tag_sentence = []
        N = len(sentence)
        if self.max_key_size == 0:
            self.max_key_size = N
        i = 0
        while (i < N):
            j = min(i + self.max_key_size, N) #avoid overflow
            tagged = False
            while (j > i):
                expression_form = ' '.join([word[0] for word in sentence[i:j]]).lower()
                expression_lemma = ' '.join([word[1] for word in sentence[i:j]]).lower()
                if tag_with_lemmas:
                    literal = expression_lemma
                else:
                    literal = expression_form
                if literal in self.dictionary:
                    #self.logger.debug("found: %s" % literal)
                    is_single_token = j - i == 1
                    original_position = i
                    i = j
                    taggings = [tag for tag in self.dictionary[literal]]
                    tagged_expression = (expression_form, expression_lemma, taggings)
                    if is_single_token: #if the tagged literal is a single token, conserve its previous taggings:
                        original_token_tagging = sentence[original_position][2]
                        tagged_expression[2].extend(original_token_tagging)
                    tag_sentence.append(tagged_expression)
                    tagged = True
                else:
                    j = j - 1
            if not tagged:
                tag_sentence.append(sentence[i])
                i += 1
        return tag_sentence

def value_of(sentiment):
    if sentiment == 'positive': return 1
    if sentiment == 'negative': return -1
    return 0

def sentence_score(sentence_tokens, previous_token, acum_score):    
    if not sentence_tokens:
        return acum_score
    else:
        current_token = sentence_tokens[0]
        tags = current_token[2]
        token_score = sum([value_of(tag) for tag in tags])
        if previous_token is not None:
            previous_tags = previous_token[2]
            if 'inc' in previous_tags:
                token_score *= 2.0
            elif 'dec' in previous_tags:
                token_score /= 2.0
            elif 'inv' in previous_tags:
                token_score *= -1.0
        return sentence_score(sentence_tokens[1:], current_token, acum_score + token_score)

def sentiment_score(review):
    return sum([sentence_score(sentence, None, 0.0) for sentence in review])

if __name__ == "__main__":
    # text = """What can I say about this place. The staff of the restaurant is 
    # nice and the eggplant is not bad. Apart from that, very uninspired food, 
    # lack of atmosphere and too expensive. I am a staunch vegetarian and was 
    # sorely dissapointed with the veggie options on the menu. Will be the last 
    # time I visit, I recommend others to avoid."""
    # text = """the road near to my home is in bad state. please make sure that you can go through the rebuild process. 
    # it would be a great way of making people's problem get resolved. I would appreciate it more if you can make sure that the 
    # garbage near to my house also gets clean bill.      
    # """
    splitter = Splitter()
    postagger = POSTagger()
    dicttagger = DictionaryTagger([ 'dicts/positive.yml', 'dicts/negative.yml', 
                                    'dicts/inc.yml', 'dicts/dec.yml', 'dicts/inv.yml'])
    answer = []
    # f = open('movies.txt', 'rt')
    # f = codecs.open('unicode.rst', encoding='utf-8')
    f = codecs.open('movies.txt', encoding='utf-8', mode='rt')
    for line in f:
        if line.startswith("review/text:"):
            # print line

            # line = line.decode('utf-8')
            # line = line.decode('latin-1')
            splitted_sentences = splitter.split(line)
            pprint(splitted_sentences)

            pos_tagged_sentences = postagger.pos_tag(splitted_sentences)
            pprint(pos_tagged_sentences)

            dict_tagged_sentences = dicttagger.tag(pos_tagged_sentences)
            pprint(dict_tagged_sentences)

            print("analyzing sentiment...")
            score = sentiment_score(dict_tagged_sentences)
            # print(score)
            answer.append(score)
            if len(answer) == 50:
                answer_file = open('answer_file.txt', 'a')
                answer_file.write(str(answer)+'\n')
                answer_file.close()
                answer[:] = []

    print answer
    # text = """ I own both the VHS and DVD versions of this program, and I second everything the other reviewer wrote.  I used most of these songs in my after school music class with 5th and 6th graders and they love it.  We first sang the songs off lyric sheets and from CD's and then watched the DVD.  They enjoyed it so much I ordered a DVD copy for each of my students as a present for joining the class.  I would suggest ordering the DVD version since it has about eight interviews with artists from the program in addition to six extra songs that aren't available on the VHS version.  The DVD version is now available only from PBS.  The singers may be older than when they first made these songs hits, but they can still sing them as well as ever.  My only complaint with it is it has five songs by Little Anthony and the Imperials.  Two would have been enough with maybe a second song from some of the other singers in their place.  Nevertheless, you can't go wrong with either the VHS or DVD version.  I prefer the DVD since it includes extra songs and interviews that the VHS version doesn't have.

    # """
    
    