from gramformer import Gramformer

# instantiate the model
gf = Gramformer(models=1, use_gpu=False)  # model 1 is a corrector

sentences = ['My name was Vikrant', 'He are moving here.',
             'How is they?', 'I loves walking night.']

for sentence in sentences:
    correct_sentences = gf.correct(sentence)
    print('[Orignal Sentence]', sentence)
    for correct_sentences in correct_sentences:
        print('[Correct sentence]', correct_sentences)
