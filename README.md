<div align="center">
  <img height="60" src="https://user-images.githubusercontent.com/85709371/156916372-d8c1bbdd-5fe9-40d1-a250-5a1d4d454832.png">
</div>

<h1 align="center">Gramformer</h1>

### Python tip:
- Do you know that we can correct grammar errors in text using Python?
we can use an open source framework, gramformer. Gramformer (created by Prithiviraj Damodaran) is a framework for highlighting, and correcting grammar errors on natural language text.
Here is a simple code that demonstrates how you can use gramformer. to correct errors in a text.

### Prerequisites
`Python 3`

### Source Code
```python3
from gramformer import Gramformer

# instantiate the model
gf = Gramformer(models=1, use_gpu=False)  # model 1 is a corrector

sentences = ['My name was Vikrant', 'I hates walking night',
             'The city is were I work', 'I has no children']

for sentence in sentences:
    correct_sentences = gf.correct(sentence)
    print('[Orignal Sentence]', sentence)
    for correct_sentences in correct_sentences:
        print('[Correct sentence]', correct_sentences)
```

## *Author Name*
[Vikrant](https://github.com/vikrant-v28)
