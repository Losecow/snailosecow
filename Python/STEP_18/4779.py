def cantor(A, start, last):
    if last - start > 2:
        
        mid1 = (last - start      ) // 3 - 1
        mid2 = ((last + 1) // 3) * 2 - 1

    else:
        return A