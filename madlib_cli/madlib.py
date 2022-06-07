
import re

#function can return the text in the file
def read_template(file):
    # file=Extension of the file
    text_file=open(file,"r")
    rd=text_file.read()
    print(rd)

    text_file.close()
    return rd


#function extracts the word between {} and puts it in a tuple and makes it empty
def parse_template(text):
    #text = The text you want to edit
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

    #return edited text
    return  text1 , tuple (reslt)

print(parse_template("It was a {Adjective} and {Adjective} {Noun}."))


#Function: Fill in the information you want to enter in the text
def merge(text,args):

#text=The text in which you want to enter the information
#args=The information you want to enter

    text1_merge=text.format(*args)
#The text after placing the information in it
    return text1_merge


print(merge("I the {} and {} {}",("vgff","uguv","rzzrzs")))


def all_game(file,item):

    text=read_template(file)
    x,y=parse_template(text)

    rslt = merge(x,*item)
    return rslt
# if __name__=="__main__":
    # all_game("file.txt")













