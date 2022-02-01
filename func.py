def zoom_toponym(lc: str, uc: str):
    lc = list(map(float, lc.split()))
    uc = list(map(float, uc.split()))
    return ','.join([str(abs(lc[0] - uc[0]) / 2), str(abs(lc[1] - uc[1]) / 2)])
