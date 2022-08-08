
phones = [ "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   "]

def format_phone_number(func):
    def inner (*args, **kwargs):
        added_result = ''
        result =  func(*args, **kwargs)
        
        if len(result) == 10:
            added_result = '+38' + result
        elif len(result) == 12:
            added_result = '+' + result
        
        return added_result
        
    return inner
    
        

@format_phone_number
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
            .removeprefix("+")
            .replace("(", "")
            .replace(")", "")
            .replace("-", "")
            .replace(" ", "")
    )
    return new_phone


for i in phones:
    print(sanitize_phone_number(i))
