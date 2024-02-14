def decor(kap):
    def ny(*args, **kwargs):
        try:
            return kap(*args, **kwargs)
        except Exception as e:
            print(f"искл {e}")
    return ny
@decor
def pl():
    x/y

pl()