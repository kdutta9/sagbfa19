def populate():
    lst = []
    columns = input('Separate columns by commas: ')
    columns = columns.split(',')
    while True:
        data = []
        for col in columns:
            col_data = input('Input ' + str(col) + ': ')
            data.append(col_data)
        lst.append(data)
        switch = input("Type 'yes' to continue: ")
        if switch.lower() != 'yes':
            break
    return lst
