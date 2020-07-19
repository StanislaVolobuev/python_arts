def open_text(d):
    import test
    # ринимает аргументом адрес текстового документа, возвращает
    #  количество строк в документе и значение энергии
    n = 1
    s_zero = [0, 0, 0]
    v_zero = [0, 0, 0]
    session = open(d)
    Es = [0, 0]  # приращение энергии
    # p=test.open_weights()

    for row in session:
        n += 1

        if 20 < n:
            E = [0, 0]
            s = []  # смещение за период Т
            v = []  # скорость за период Т
            m = list(row.split())
            s.append(float(m[0]) - float(s_zero[0]))
            s.append(float(m[1]) - float(s_zero[1]))
            s.append(float(m[2]) - float(s_zero[2]))
            v.append(s[1] / s[0])
            v.append(s[2] / s[0])
            Es[0] += 48 * abs(v[0] ** 2 - v_zero[0] ** 2) / 2  # М - Аргумент массы из файла весоы
            Es[1] += 48 * abs(v[1] ** 2 - v_zero[1] ** 2) / 2
            s_zero = m
            v_zero = v
        # print(n-20, Es)
    return Es


t = open_text(r'D:\doks\for_stas\Maria\Maria 001.txt')
print(t)
