a=[1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]

def finde_el(a):
    new_ar=[]
    for i in a:
        if i<5:
            new_ar.append(i)

    return new_ar

print(finde_el(a))

a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

def together_element(a,b):
    return set(a)&set(b)

print(together_element(a,b))
