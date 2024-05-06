def concatenate(*args, **kwargs):
    result = ''
    for word in args:
        result += word

    for key, value in kwargs.items():
        result = result.replace(key, value)

    return result


print(concatenate("Soft", "UNI", "Is", "Grate", "!", UNI="Uni", Grate="Great"))
