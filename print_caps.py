def allcaps(func):
    def wrapper():
        result = func()
        print(result.upper())
        return result.upper()

    return wrapper
'''
@allcaps
def greet():
    return "Hello World!"

def main():
    greet()
    
main()
'''