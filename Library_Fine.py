def libraryFine(d1, m1, y1, d2, m2, y2):
    fine = 0
    if y1 > y2 :
        fine = 10000
    elif y1 < y2:
        fine = 0
    else:
        if m1 < m2 and y1 == y2:
            fine = 0
        elif m1 == m2 and y1 == y2:
            if d1 <= d2:
                fine = 0
            else:
                fine = 15 * (d1-d2)
        else:
            fine = 500 * (m1-m2)
    
    return fine 