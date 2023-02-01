def capitalise(func):
    def wrapper(request,location):
        cap=location.upper() 
        return func(request,cap)
    return wrapper
