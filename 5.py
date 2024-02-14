def decor(kap):
    def decorat(op):
        def fpf(*args, **kwargs):
            result = op(*args, **kwargs)
            return kap
        return fpf
    return decorat

@decor("замена")
def es():
    return "ориг"

result = es()
print(f"результат {result}")