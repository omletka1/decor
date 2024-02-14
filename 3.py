def decor(kap):
    def ny(*args, **kwargs):
        result = kap(*args, **kwargs)
        return str(result)
    return ny

@decor
def rez():
    return 42

result = rez()
print(f"результат {result}")