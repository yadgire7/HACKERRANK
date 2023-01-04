def squares(a, b):
    if a%(a**0.5) ==0:
        return (int(b**0.5)-int(a**0.5))+1
    else:
        return int(b**0.5)-int(a**0.5)