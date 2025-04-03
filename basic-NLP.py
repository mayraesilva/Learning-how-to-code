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


#recebe um arquivo dic e devolve em outros dois dicionários um para número e emoções
#Outro para palavras (strings) e a lista de emoçoes associadas a elas
#Os dicionários estão armazenados na lista devolvida
def read_liwc(dictionary):
    liwc_dic = transform_the_file(dictionary) #withot space and \n, this is a list of strings

    liw_dic_emotions = [] #list of strings for numbers and its associated emotion
    separation_string = '%'
    separation_string_count = 0
    liw_dic_words = [] #list of strings for words and the numbers emotions associated

    for line in liwc_dic: #separating the first part
        if line == separation_string:
            separation_string_count += 1
        liw_dic_emotions.append(line)
        if separation_string_count >= 2:
            print("emotions are separetaded, breaking...")
            break
            
        else:
            continue
    
    #print("antes de separar em listas de linhas ", liw_dic_emotions)

    new_liwc_dic_emotions = [] #to keep the emotions as lists

    #Now we're creating new lists for each emotion
    for line in liw_dic_emotions:
        if '\t' in line:
            new_emotion = line.split('\t')
            new_liwc_dic_emotions.append(new_emotion)
    
    #print(new_liwc_dic_emotions) #Check if the emotions are separated in lists with its number


    #Time to transform the list of lists into a dictionary
    emotions_dict = dict(new_liwc_dic_emotions)
    #print(emotions_dict) #check if it has become a dictionary



    separation_string_count = 0
    #Time to get the second dict using the list of lists new dict
    for line in liwc_dic: #separating the first part
       if separation_string_count <= 1:
           if line == separation_string:
               separation_string_count += 1
            
       else:
            liw_dic_words.append(line)
    
    print(liw_dic_words[3])



    # for line in liwc_dic: #separating the first part
    #    if separation_string_count <= 1:
    #        if line == separation_string:
    #            separation_string_count += 1
            
    #     else:
    #         liw_dic_words.append(line)
    
    # print(liw_dic_words[3])
    
    # for line in liwc_dic:
    #     if separation_string_count >= 2:
    #         liw_dic_words.append(line)
    
    #Now liw_dic_words is a list of strings where each string is a line
    #print(liw_dic_words)

    new_liwc_dic_words = [] #list of lists, where each element is a list of word 
    #and its associated emotions by their numbers

    #transform the list of strings into a list of lists
    for line in liw_dic_words:
        if '\t' in line:
            new_word = line.split('\t')
            new_liwc_dic_words.append(new_word)
    

    
    #breaking the lists
    #transform the numbers strings into a list of strings where each string is a number
    new_words_as_a_list = []

    for word_list in new_liwc_dic_words:
        word_string, *associated_emotions = word_list #separete the word of its emotions
        new_words_as_a_list.append([word_string, associated_emotions])
    
    #print(new_words_as_a_list)
    words_dict = dict(new_words_as_a_list)
    #print(words_dict)

    final_dictionary = [emotions_dict, words_dict]


    return final_dictionary




# 'LIWC2007_Portugues_win.dic'




#Takes in a word (string) and a dictionary 
# to check in the dictionary and returns a different string with its class
def get_emotion(word, list_that_contains_dicts):
    fictional_dict = {'126': 'posemo'}
    fictional_dict_word = {'felicidade': ['126', '125', '359']}

    #real_dict = read_liwc(dictionary)
    real_dict_emotions = list_that_contains_dicts[0]
    real_dict_words = list_that_contains_dicts[1]





    if word in fictional_dict_word.keys():
        word_class = fictional_dict_word[word]
        for dict_key in word_class:
            if dict_key in fictional_dict.keys():
                return fictional_dict[dict_key]
    



        #emotion_class = fictional_dict_word['word']


  

#recebe uma lista de listas e devolve uma porcentagem para avaliar o tom
def decide_emotion(lines_as_tokens, possible_dict):
    text_length = [] #lista com tamanho de cada linha
    for line in lines_as_tokens:
        text_length.append(len(line))
    
    text_length = sum(text_length) #inteiro representanto o tamanho do texto geral
    print(f"O texto tem {text_length} palavras")

    word_analysis = []
    for line in lines_as_tokens:
        for word in line:
           word_analysis.append(get_emotion(word, possible_dict))

    #Emotions we are searching for:
    positivity = []
    negativity = []
    swear = []
    anxiousness = []


    for word in word_analysis:
        if word == 'posemo':
            positivity.append(word)

        elif word == 'negemo':
            negativity.append(word)
        
        elif word == 'swear':
            swear.append(word)

        elif word == 'anx':
            anxiousness.append(word)
            

    # if get_emotion(word) == 'posemo':
    #     positivity.append(get_emotion(word))

    # elif get_emotion(word) == 'negemo':
    #     negativity.append(get_emotion(word))

    # elif get_emotion(word) == 'swear':
    #     swear.append(get_emotion(word))

    # elif get_emotion(word) == 'anx':
    #     anxiousness.append(get_emotion(word))
    
    

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
    

def basic_NLP(file, dictionary):
    filex = transform_the_file(file)
    #print("file content ", filex)
    new_lines = []
    for line in filex:
        new_lines.append(clean_line(line))
    
    lines_as_tokens = []
    for line in new_lines:
        lines_as_tokens.append(tokenize(line))

    possible_dictionary = read_liwc(dictionary)
    decision = decide_emotion(lines_as_tokens, possible_dictionary)
    print(decision)

    


basic_NLP('felicidade.txt', 'LIWC2007_Portugues_win.dic')




#print("O tipo de arquivo de felicidade é ", type(felicidade))

#angustia = open('angustia.txt', 'r', encoding='utf-8')
#print(angustia.read()) 
#print("O tipo de de arquivo de angustia é ", type(angustia))


###Arquivo usado para analisar emoções
# liwc_dic = open ("LIWC2007_Portugues_win.dic", "r", encoding="utf-8") #importing file
#print(liwc_dic.read(10000)) #reading the first 10000 bytes to make sure it's right
#print("tipo de arquivo do dic ", type(liwc_dic)) #discovering what kind of file it is

### Iniciando a leitura dos arquivos
