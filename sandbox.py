
def mylist(show=True):
    if show:
        print('hello')
    print(show)
    return ['caio', 'mayra']



def main():
    print(mylist(False)[0])


main()

def ftype(v):
    if isinstance(v, list):
        return f"{type(v)}<{type(v[0])}>"
    
    if isinstance(v, dict):
        return f"{type(v)}<{type(list(v.keys())[0]), type(list(v.values())[0])}>"
    
    return type(v)
