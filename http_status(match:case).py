def get_status(code):
    match code:
        case 200:
            return "OK"
        case 404:
            return "Not Found"
        case 500:
            return "Server Error"
        case _:
            return "Unknown"
            
'''
match code:
    case 200 | 201 | 204:
        return "Success"
    case 400 | 404:
        return "Client Error"
'''