USD = float(input('Enter US Dollars to Convert to Pounds, Euros, and Canadian Dollars: '))

def britishpound(USD): 
    return float((0.82/1) * USD)

def euro(USD):
    return float((0.95/1) * USD)

def candol(USD):
    return float((1.36/1) * USD)
 
print('US Dollars', '\t','British Pounds', '\t', 'Euros', '\t', 'Canadian Dollars')

print (USD, '\t', britishpound(USD), '\t', euro(USD), '\t', candol(USD))