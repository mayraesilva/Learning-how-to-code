#Iniciando a tarefa de contagem de palavras e detecção de emoções de Mayra Silva


###Arquivos a serem analisados
# felicidade = open('felicidade.txt', 'r', encoding='utf-8')
# felicidade_read = felicidade.readlines() #transforming into lists for each line
# print(felicidade_read)
# felicidade_modified = []


import string


#Acessando o arquivo (file) e devolvendo uma lista de listas que contém strings
def transform_the_file(file):
    open_the_file = open(file, 'r', encoding='utf-8')
    file_read = open_the_file.readlines()
    #print('Este é o arquivo antes de remover os excessos', file_read)
    file_modified = []

    for line in file_read:
        file_modified.append(line.strip()) #remove the space and the \n in the beggining/end of string

    #print('Este é o arquivo após  a remoção ', file_modified)
    
    return file_modified




#Recebendo uma linha e devolvendo sem pontuação; a linha é uma string e devolve uma string
def clean_line(line): 
    result = line
    for char in string.punctuation:
        result = result.replace(char, '')
    result = result.strip().lower()

    return result





#separando a linha (string) em uma lista de  palavras (list of strings)
def tokenize(line):
    separated_line = line.split()
    return separated_line



#Takes in a word (string) to check in the dictionary returns a different string with its class
def get_emotion(word):
    fictional_dict = {'126': 'posemo'}
    fictional_dict_word = {'felicidade': ['126', '125', '359']}

    if word in fictional_dict_word.keys():
        word_class = fictional_dict_word['word']
        for dict_key in word_class:
            if dict_key in fictional_dict.keys():
                return fictional_dict['key']

        #emotion_class = fictional_dict_word['word']


        # for emotion_class in fictional_dict.values():
        #     if emotion_class == 'posemo':
        #         return 'posemo'
        #     elif emotion_class == 'negemo':
        #         return 'negemo'


        

    #pass


#recebe uma lista de listas e devolve uma porcentagem para avaliar o tom
def decide_emotion(lines_as_tokens):
    text_length = [] #lista com tamanho de cada linha
    for line in lines_as_tokens:
        text_length.append(len(line))
    
    text_length = sum(text_length) #inteiro representanto o tamanho do texto geral
    print(f"O texto tem {text_length} palavras")

    #Emotions we are searching for:
    positivity = []
    negativity = []
    swear = []
    anxiousness = []


    if get_emotion(word) == 'posemo':
        positivity.append(get_emotion(word))

    elif get_emotion(word) == 'negemo':
        negativity.append(get_emotion(word))
    

    positive_emotions = len(positivity)
    negative_emotions = len(negativity) + len(swear) + len(anxiousness)

    positive_text = positive_emotions / text_length
    negative_text = negative_emotions / text_length

    if positive_text > negative_text:
       print("O tom geral do texto é positivo")
       return "posemo"
    else:
        print("O tom geral do texto é negativo")
        return "negemo"
    

def basic_NLP(file):
    filex = transform_the_file(file)
    #print("file content ", filex)
    new_lines = []
    for line in filex:
        new_lines.append(clean_line(line))
    
    lines_as_tokens = []
    for line in new_lines:
        lines_as_tokens.append(tokenize(line))
    
    decision = decide_emotion(lines_as_tokens)
    print(decision)
    

basic_NLP('felicidade.txt')




#print("O tipo de arquivo de felicidade é ", type(felicidade))

#angustia = open('angustia.txt', 'r', encoding='utf-8')
#print(angustia.read()) 
#print("O tipo de de arquivo de angustia é ", type(angustia))


###Arquivo usado para analisar emoções
# liwc_dic = open ("LIWC2007_Portugues_win.dic", "r", encoding="utf-8") #importing file
#print(liwc_dic.read(10000)) #reading the first 10000 bytes to make sure it's right
#print("tipo de arquivo do dic ", type(liwc_dic)) #discovering what kind of file it is

### Iniciando a leitura dos arquivos
