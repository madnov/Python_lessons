def truth_table():
    for i in range(2):
        for j in range(2):
            for k in range(2):
                print(f"{i}\t{j}\t{k}\t{int(not(i and j) or k) }")


truth_table()
