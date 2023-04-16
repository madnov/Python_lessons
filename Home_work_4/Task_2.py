def product():

    product_range = {'Сливочное', 'Бурёнка', 'Вафелька', 'Сладкоежка'}
    product_range_2 = {'Сливочное', 'Сладкоежка', 'Вафелька'}
    result = list(product_range - product_range_2)
    print(f'На складе закончилась ',*result)

product()    
   
