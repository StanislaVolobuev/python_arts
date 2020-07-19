def f_row():
    # result = beat_folder.beat()
    # print(result)
    title = []
    x = '_X_'
    y = '_Y_'

    for nom in range(8):
        t = "En" + x + 'raw_00' + str(nom + 1)
        tt = "En" + y + 'raw_00' + str(nom + 1)
        if nom % 2 == 0:
            t = t + 'EC'
            tt = tt + 'EC'
        else:
            t = t + 'EO'
            tt = tt + 'EO'
        title.append(t)
        title.append(tt)
    print(title)
    return title
