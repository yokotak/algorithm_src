from janome.tokenizer import Tokenizer
s = '多くの富よりも良い名を選べ'
for tok in Tokenizer().tokenize(s):
    print(f'- {tok.surface} ({tok.part_of_speech})')
