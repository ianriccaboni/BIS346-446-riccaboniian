# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 10:08:59 2023

@author: ianri
"""

invoices = [(83, 'Electric sander', 7, 57.98), 
            (24, 'Power saw', 18, 99.99),
            (7, 'Sledge hammer', 11, 21.50),
            (77, 'Hammer', 76, 11.99),
            (39, 'Jig saw', 3, 79.50)]

from operator import itemgetter

# sort the tuples by part description
print('Tools by Quantity')
for part, desc, quant, price in sorted(invoices, key=itemgetter(1)):
        print(f'{part:>2} {desc:<16}{quant:>3}{price:7.2f}')
    
print('Tools, Cheapest to Most Expensive')
for part, desc, quant, price in sorted(invoices, key=itemgetter(3)):
    print(f'{part:>2}  {desc:<16}{quant:>3}{price:7.2f}')
    
quantities = [(desc, quant) for part, desc, quant, price in invoices]

print('Tools, Lowest to Highest Volume')
for desc, quant in sorted(quantities, key=itemgetter(1)):
    print(f'{desc:<16}{quant:>3}')
    

prices = [(desc, quant * price) for part, desc, quant, price in invoices]

print('Tools, Lowest to Highest Total Value')
for desc, total in sorted(prices, key=itemgetter(1)):
    print(f'{desc:<16}{total:9.2f}')
    
print('Tools, Tools in Total Value of 200 to 500')
prices = [(desc, quant * price) for part, desc, quant, price in invoices\
          if 200 <= quant * price <= 500]

for desc, total in sorted(prices, key=itemgetter(1)):
    print(f'{desc:<16}{total:9.2f}')
    
# Calculate the total of all the invoices. 
total = sum([(quant * price) for part, desc, quant, price in invoices])

print(f'Total for all invoices is: {total:.2f}')