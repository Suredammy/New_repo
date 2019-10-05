def string_edit(str_a, str_b, cost = (1, 1, 1)):
    if str_a == str_b:
        return 0
    row = len(str_a) + 1
    col = len(str_b) + 1
    #Make a table of row and col
    table = [[0 for c in range(col)] for r in range(row)]

    #fill the first row and col
    for r in range(row):
        table[r][0] = r
    for c in range(col):
        table[0][c] = c
    
    # fill the rest of the table based on the difference in the string 
    sub, delete, insert = cost

    for r in range(1, row):
        for c in range(1, col):
            
            if str_a[r -1] == str_b[c -1]:
                cost = 0
            else: 
                cost = sub
            
            table[r][c]  = min(table[r][c-1] + insert,        #insertion
                               table[r-1][c] + delete,       #deletion
                               table[r-1][c-1] + cost)  #substitution

    #for r in range(row):
    #     print(table[r])
    return table[row-1][col-1]

print(string_edit("fawn", "crown", cost = (1, 1, 1)))


            