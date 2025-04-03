
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


txt = "welcome to the jungle"
x = txt.split()
print(x)



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


def get_emotion(word):
    fictional_dict = {'126': 'posemo'}
    fictional_dict_word = {'felicidade': ['126', '125', '359']}

    if word in fictional_dict_word.keys():
        word_class = fictional_dict_word[word]
        for dict_key in word_class:
            if dict_key in fictional_dict.keys():
                return fictional_dict[dict_key]
    

teste_da_func = get_emotion('felicidade')
print(teste_da_func)


my_list = ["apple", "%", "orange", "%", "grape"]

target = "%"
count = 0

for item in my_list:
    if item == target:
        count += 1
        if count == 2:
            print("Second appearance, breaking...")
            break
        else:
            print("First appearance, ignoring...")
            continue
    print("Processing:", item)


txt = ["apple/banana#cherry#orange", 'amor/odio']
keep_separeted = []

for item in txt:
    x = item.split("/")
    keep_separeted.append(x)

print(keep_separeted)


# Initialize a dictionary
my_dict = {'name': 'Alice', 'age': 25}

# Create a new dictionary with additional key-value pairs
#new_dict = dict(my_dict, city='New York', email='alice@example.com')

new_dict_2 = [['name', 'aline'], ['age', '25'], ['face', ['1', '2', '3']]]

new_real_dict_2 = dict(new_dict_2)

# Print the new dictionary
print(new_real_dict_2)
# Output: {'name': 'Alice', 'age': 25, 'city': 'New York', 'email': 'alice@example.com'}

lista = ['amor', '123', '456', '789']
palavra, *emocoes = lista

palavra_sentimentos = []
palavra_sentimentos.append([palavra, emocoes])

print(palavra_sentimentos)


# Assume separation_string_count is initialized to 0
# for line in liwc_dic:
#     if separation_string_count <= 1:
#         if line == separation_string:
#             separation_string_count += 1
#         # Skip the rest of the loop until we see the second occurrence
#         continue
#     # Once we've seen the separation string twice, start appending lines
#     liw_dic_words.append(line)

# print(liw_dic_words[3])



lista = [{'amora':['1', '2', '3']}, {'banana': ['5', '6', '7']}]

roxo = lista[0]
amarelo = lista[1]

print(roxo)