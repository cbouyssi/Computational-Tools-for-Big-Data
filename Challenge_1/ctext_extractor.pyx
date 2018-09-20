import xml.etree.cElementTree as ET
import re, sys, os


def find_len(query):
    cdef long length = 0
    cdef int curs = 0
    while(curs < len(query)-1):
        length += int(query[curs+2]) + len(query[curs+3])
        curs += 3
    return length


def search_word(query, text_found, index, matches):
    for word in re.finditer(query[3], text_found):
        if word.start() <= int(query[2]) - int(query[1]):
            if(len(query)==4):
                matches.append(index + word.end())
            else:
                search_word(query[3:], text_found[word.end()+int(query[4]):], index + word.end() + int(query[4]), matches)
    return matches


def create_query(args):
    query = []
    for k in range(1, len(args)):
        elem_query = re.split('\[|,|\]', args[k])
        for elem in elem_query:
            if elem != '':
                query.append(elem)
    return query


def main(input_query, num):
    cdef long size
    cdef long valid_answer = 0
    cdef str path, find_text, text_input, fullpath, source
    cdef int append
    query = create_query(input_query)
    size = find_len(query)

    if num == 1:                                                            #Section to query the 'cat' article
        fullpath = "wiki_text_file/c/a/ca"
        append = 0
        with open(fullpath, "r") as text:
            lines = text.readlines()
            for line in lines:
                if append == 1:
                    for word in re.finditer(query[0], line):
                        result = search_word(query, line[word.end()+int(query[1]):word.end()+size], word.end() + int(query[1]), [])
                        if result:                                          #Matches array is not empty
                            for it in result:
                                if "\n" not in line[word.start():it]:       #The match should be in a single article
                                    print(line[word.start():it])            #Print the pattern from the first character of S1
                                    valid_answer += 1                       #until the last index of the matching pattern
                                    append = 2
                elif append == 2:
                    break
                if "<TITLE>Cat\n" == line:
                    append = 1
        text.close()

    elif num == 2:                                                          #section to query 'A' article
        source = "wiki_text_file/a/"
        for root, dirs, filenames in os.walk(source):
            for f in filenames:
                fullpath = source + f[1] + '/' + f
                with open(fullpath, "r") as text:
                    lines = text.readlines()
                    for line in lines:
                        for word in re.finditer(query[0], line):
                            result = search_word(query, line[word.end()+int(query[1]):word.end()+size], word.end() + int(query[1]), [])
                            if result:                                       #Matches array is not empty
                                for it in result:
                                    if "\n" not in line[word.start():it]:    #The match should be in a single article
                                        print(line[word.start():it])         #Print the pattern from the first character of S1
                                        valid_answer += 1                    #until the last index of the matching pattern
                text.close()

    elif num == 3:                                                          #Section to query the entire Wikipedia
        source = "wiki_text_file/"
        for root, dirs, filenames in os.walk(source):
            for f in filenames:
                fullpath = source + f[0] + '/' + f[1] + '/' + f
                with open(fullpath, "r") as text:
                    lines = text.readlines()
                    for line in lines:
                        for word in re.finditer(query[0], line):
                            result = search_word(query, line[word.end()+int(query[1]):word.end()+size], word.end() + int(query[1]), [])
                            if result:                                      #Matches array is not empty
                                for it in result:
                                    if "\n" not in line[word.start():it]:   #The match should be in a single article
                                        print(line[word.start():it])        #Print the pattern from the first character of S1
                                        valid_answer += 1                   #until the last index of the matching pattern
                text.close()

    else:
        print("error : wrong param")

    print(valid_answer)                                                     #Print the nb of results
