def mess(kap):
    def dfkvmkdf(*args, **kwargs):
        print("выполняется функц", kap.__name__)
        result = kap(*args, **kwargs)
        return result
    return dfkvmkdf

@mess
def nny():
    print("пример")

nny()