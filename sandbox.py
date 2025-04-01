
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


# txt = "welcome to the jungle"
# x = txt.split()
# print(x)



thisdict = {"brand": "Ford", "model": "Mustang", "year": 1964}
print(thisdict["brand"])

dict1 = {'126': 'felicidade', 'b': 2}
dict2 = {'felicidade': '126', 'y': 3}

# Check if any value in dict1 is present as a value in dict2
for key, value in dict1.items():
    if key in dict2.values():
        print(f"The value {value} from dict1 is in dict2.")


dict1 = {'126': 'positive', 'location': 'city'}
dict2 = {'amora': ['Alice', '126'], 'age': 23}

# Check if any key in dict2 is present as a value in dict1
for key in dict2:
    if key in dict1.values():
        print(f"The key '{key}' from dict2 is a value in dict1.")