from collections import Counter
from pathlib import Path

MIN_COUNT = 1

if __name__ == '__main__':
    def words(name):
        return '{}.words.txt'.format(name)


    print('Build vocab words')
    counter_words = Counter()
   
   
    '''
       for n in ['train', 'eval']:
        with Path(words(n)).open() as f:
            for line in f:
                counter_words.update(line.strip().split())
    '''
    print(words('test'))
    with open(words('test'),'r',encoding='utf-8')as f:
        for line in f:
            counter_words.update(line.strip().split())



    vocab_words = {w for w, c in counter_words.items() if c >= MIN_COUNT}

    with open('vo.words.txt','w',encoding='utf-8') as f:
        for w in sorted(list(vocab_words)):
            f.write('{}\n'.format(w))
    print('Done. Kept {} out of {}'.format(
        len(vocab_words), len(counter_words)))



    print('Build labels')
    doc_tags = set()
    with open(words('test'),'r',encoding='utf-8')as f:
        for line in f:
            doc_tags.add(line.strip())

    with open('vo.labels.txt','w',encoding='utf-8') as f:
        for t in sorted(list(doc_tags)):
            f.write('{}\n'.format(t))
    print('- done. Found {} labels.'.format(len(doc_tags)))

    
