#Iniciando a tarefa de contagem de palavras e detecção de emoções de Mayra Silva


###Arquivos a serem analisados
# felicidade = open('felicidade.txt', 'r', encoding='utf-8')
# felicidade_read = felicidade.readlines() #transforming into lists for each line
# print(felicidade_read)
# felicidade_modified = []

def transform_the_file(file):
    open_the_file = open(file, 'r', encoding='utf-8')
    file_read = open_the_file.readlines()
    print('Este é o arquivo antes de remover os excessos', file_read)
    file_modified = []

    for line in file_read:
        file_modified.append(line.strip()) #remove the space and the \n in the beggining/end of string

    file_lines = print('Este é o arquivo após  a remoção ', file_modified)
    
    return file_modified

def parse_line(line):
    new_lines = []
    for char in line:
        new_lines.append(line.strip(',.'))
        print(new_lines)
    
    return new_lines




def basic_NLP(file):
    
    for line in transform_the_file(file):
        parse_line(line)
   

    return parse_line(line)

basic_NLP('felicidade.txt')

#print("O tipo de arquivo de felicidade é ", type(felicidade))

#angustia = open('angustia.txt', 'r', encoding='utf-8')
#print(angustia.read()) 
#print("O tipo de de arquivo de angustia é ", type(angustia))


###Arquivo usado para analisar emoções
liwc_dic = open ("LIWC2007_Portugues_win.dic", "r", encoding="utf-8") #importing file
#print(liwc_dic.read(10000)) #reading the first 10000 bytes to make sure it's right
#print("tipo de arquivo do dic ", type(liwc_dic)) #discovering what kind of file it is

### Iniciando a leitura dos arquivos
