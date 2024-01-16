from janome.tokenizer import Tokenizer

# Janomeを使うためにオブジェクトを作成 --- (*1)
tokenizer = Tokenizer()
# 文章を形態素に分割する --- (*2)
s = '多くの富よりも良い名を選べ'
words = [tok.surface for tok in tokenizer.tokenize(s)]
print(words)
