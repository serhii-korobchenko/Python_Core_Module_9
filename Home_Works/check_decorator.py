def input_error(func): # decorator
    
    def inner():
        func()
        print (error)
        
    return inner

@input_error
def main():
    try:
        raise KeyError

    except KeyError or  ValueError or IndexError as ex:
         error = type(ex)

    return error
        

    
print (main())






