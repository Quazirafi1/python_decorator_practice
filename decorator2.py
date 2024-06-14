def debug(func):
    def wrapper(*args, **kwargs):
        args_value = ', '.join(str(arg) for arg in args)
        kwargs_value = ', '.join(f"{key}:{value}" for key, value in kwargs.items())
        
        print(f"calling: {func.__name__} with args {args_value} and kwargs {kwargs}")
        
        return func(*args,**kwargs)
        
    return wrapper


@debug
def greet(name, greeting='hello'):
    print(f"{greeting}, {name}")
    
greet('rafi', greeting='man')