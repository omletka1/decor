def decor(kap):
    def ny(*args, **kwargs):
        print(f"вызывается функция {kap.__name__}")
        kap(*args, **kwargs)
        kap(*args, **kwargs)
    return ny

@decor
def pr():
    print("примерчик")

pr()