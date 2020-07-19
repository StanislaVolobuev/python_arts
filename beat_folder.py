def beat():
    import os
    import test
    import open_text

    d = test.open_weights()

    pach = r'D:\doks\for_stas'
    j = []
    for i in os.listdir(pach):  # где и так же имя испытуемого
        print(i, pach + '\\' + i, )
        if os.path.isdir(pach + '\\' + i):
            j.append(i)
        print(j)
        print(d, type(d))
    r_s = []  # Список участников с информацией о весе
    for i in j:
        if i in d.keys():
            print(i)
            r_s.append(i)
        # print(os.listdir(pach+'\\'+i))
        else:
            print(i, '- нет информации о весе учачтника эксперемента')
    # print('доступна полная информация по:',r_s)
    result = dict()
    for j in r_s:
        user = pach + '\\' + j  # Папака участника с сессиями
        # print(j)

        result[j] = dict()
        for i in os.listdir(user):
            user_session = user + '\\' + i  # где i - номер сессии участника
            res = list(open_text.open_text(user_session))
            it = i[-7:-4]
            u_s_r = [res]
            result[j][it] = u_s_r

        # print(user_session, u_s_r)
    # print(result)
    return result


t = beat()
print(t)
