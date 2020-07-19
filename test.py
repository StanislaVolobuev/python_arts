import os
def open_weights():

    '''преобразует текстовый документ весов в словарь весов,
    возращая значения в виде словаря w_d'''
    # D:\doks\for_stas
    # pach=r'D:\doks\for_stas'
    #print(os.listdir(pach))
    weights=open(r'D:\doks\for_stas\weights.txt')
    w_d =[]
    for row in weights:
        d=str(row)
        d=d.split()
        d.pop(1)
        d.pop(2)
        w_d.append(d)
        #print(d)
    w_d=dict(w_d)
    #print(w_d)
    return w_d
print(open_weights())