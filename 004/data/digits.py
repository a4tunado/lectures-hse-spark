from sklearn.datasets import load_digits

digits = load_digits()
for y, x in zip(digits.target, digits.data):
    print('%s,%s' % (y, ','.join(map(str, x))))
