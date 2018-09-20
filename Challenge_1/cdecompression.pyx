import xml.etree.cElementTree as ET, re, os


def create_article(buf):
    cdef str name =  re.sub(r' *</*title> *\n*','', buf)                    #remove ' <title>  ' or '  </title>  \n'
    cdef str article_name =  re.sub('[\W]+','_', name)                      #transform non letters/numbers into "_"
    return article_name


def write_file(buf, article_name):
    cdef str content =  re.sub(r' *</*text.*> *\n*','', buf)                #remove ' <text>  ' or '  </text>  \n'
    cdef str content_clean                                                  #remove redirect articles
    if not(re.match(r'#REDIRECT(.|\n)*',content)):
        content_clean= re.sub('\n',' ', content.lower())
        wiki_file = open(which_file(article_name), "a", encoding='utf-8')
        wiki_file.write("<TITLE>" + article_name + "\n")
        wiki_file.write("<TEXT>" + content_clean + "\n")
        wiki_file.close()


def which_file(name):
    cdef str path = "wiki_text_file/"
    if(re.match(r'[^A-Za-z]', name[0])):
        if(len(name)>1):
            if(re.match(r'[^A-Za-z]', name[1])):
                return path + "#/#/##"
            else:
                return path + "#/" + name[1].lower() + "/#" + name[1].lower()
        else:
            return path + "#/#/##"
    else:
        if(len(name)>1):
            if(re.match(r'[^A-Za-z]', name[1])):
                return path + name[0].lower() + "/#/" + name[0].lower() + "#"
            else:
                return path + name[0].lower() + "/" + name[1].lower() + "/" + name[0].lower() + name[1].lower()
        else:
            return path + name[0].lower() + "/" + name[0].lower() + "/"  + name[0].lower() + name[0].lower()


def text_parse(source):
    cdef str inputbuffer = ''
    cdef str article_name
    create_directories()
    with open(source,'r', encoding='utf-8') as inputfile:
        append = False
        for line in inputfile:
            if '<title>' in line:
                inputbuffer = line
                append = True
            if '</title>' in line:
                append = False
                article_name = create_article(inputbuffer)
                inputbuffer = None
            if '<text' in line:
                inputbuffer = line
                append = True
            elif '</text' in line:
                inputbuffer += line
                append = False
                write_file(inputbuffer, article_name)
                inputbuffer = None
            elif append:
                inputbuffer += line
    inputfile.close()


def create_directories():
    if not os.path.exists("wiki_text_file/"):                               #wiki_text_file/
        os.makedirs("wiki_text_file/")
    from string import ascii_lowercase
    for dir1 in ascii_lowercase:                                            #wiki_text_file/letters
        if not os.path.exists("wiki_text_file/" + dir1):
            os.makedirs("wiki_text_file/" + dir1)
        for dir2 in ascii_lowercase:                                        #wiki_text_file/letters/letters
            if not os.path.exists("wiki_text_file/" + dir1 + "/" + dir2):
                os.makedirs("wiki_text_file/" + dir1 + "/" + dir2)
        if not os.path.exists("wiki_text_file/" + dir1 + "/#"):             #wiki_text_file/letters/#
            os.makedirs("wiki_text_file/" + dir1 + "/#")
    if not os.path.exists("wiki_text_file/#"):                              #wiki_text_file/#
        os.makedirs("wiki_text_file/#")
    for dir3 in ascii_lowercase:                                            #wiki_text_file/#/letters
        if not os.path.exists("wiki_text_file/#/" + dir3):
            os.makedirs("wiki_text_file/#/" + dir3)
    if not os.path.exists("wiki_text_file/#/#"):                            #wiki_text_file/#/#
        os.makedirs("wiki_text_file/#/#")
