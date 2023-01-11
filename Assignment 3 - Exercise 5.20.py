def display_table(twoD_list, column_width):
    indent = len(str(len(twoD_list)))
    print(f'{"":{indent}}', end='')

    for col in range(len(twoD_list[0])):
        print(f'{col:>{column_width}}', end='')

    print()

    for i, row in enumerate(twoD_list):
        print(f'{i:>{indent}}', end='')

        for value in row:
            print(f'{value:>{column_width}}', end='')

        print()
          
values = [list(range(90, 100)), 
          list(range(100, 110)), 
          list(range(110, 120)), 
          list(range(120, 130)), 
          list(range(130, 140)), 
          list(range(140, 150)), 
          list(range(150, 160)), 
          list(range(160, 170)), 
          list(range(170, 180)), 
          list(range(180, 190)), 
          list(range(190, 200))]

display_table(values, 5)