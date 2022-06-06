
import re


def read_template(file):
    text_file=open(file,"r")
    rd=text_file.read()
    print(rd)
    text_file.close()
    return rd

read_template("file.txt")

def parse_template(text):
    cont_str = 0
    cont_end = 0
    reslt=[]


    for i in text:


        if cont_str < len(text)-1 and cont_end <= len(text)-1 :
            try:
                strt = text.index("{", cont_str,)
                end = text.index("}", cont_end,)
                cont_str = strt + 1
                cont_end = end + 1
                reslt.append(text[cont_str :cont_end -1])



            except:
                break

    text1=text

    for i in reslt:

            text1 = text1.replace(i, "")






    return  tuple (reslt),text1

print(parse_template("It was a {Adjective} and {Adjective} {Noun}."))

def merge(text,args):


    text1_merge=text.format(*args)
    return text1_merge


print(merge("I the {} and {} {}",("vgff","uguv","rzzrzs")))









