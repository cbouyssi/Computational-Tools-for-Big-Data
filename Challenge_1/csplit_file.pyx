import xml.etree.cElementTree as ET, re, os


def file_iter(tab, iter_line_per_file):
    tab[0]=0
    tab[1]+=1
    if tab[1]>=iter_line_per_file:
        # print("file " + str(tab[2]) + " written")
        tab[1]=0
        tab[2]+=1


def write_file(inputbuffer, file_name):
    wiki_file = open("wiki_inputs/" + str(file_name), "a", encoding='utf-8')
    wiki_file.write(inputbuffer)
    wiki_file.close()


def split_file():
    cdef str source = "enwiki-20170820-pages-meta-current.xml"
    cdef int number_line = 1000
    cdef int iter_line_per_file = 5000
    cdef str inputbuffer = ''
    if not os.path.exists("wiki_inputs/"):                                  #wiki_inputs/
        os.makedirs("wiki_inputs/")
    tab = [0,0,0]                                                           #[lines, iter_lines, name_file]
    with open(source,'r', encoding='utf-8') as inputfile:
        for line in inputfile:
            if tab[0] < number_line:
                tab[0]+=1
                inputbuffer += line
            elif tab[0] >= number_line:
                if '</page>' not in line:
                    inputbuffer += line
                else:
                    inputbuffer += line
                    write_file(inputbuffer, tab[2])
                    file_iter(tab, iter_line_per_file)
                    inputbuffer = ''
        write_file(inputbuffer, tab[2])
