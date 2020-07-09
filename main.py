# import string module
import string
# import random module
import random
# import Flask module
from flask import Flask



app = Flask(__name__)
@app.route('/')
def passGen():
    # set of Uppercase and Lowercase characters
    set1 = string.ascii_letters

    # set of numbers 0-9
    set2 = string.digits

    # set of special characters
    set3 = string.punctuation

    # convert String to list

    ls1 = list(set1)
    ls2 = list(set2)
    ls3 = list(set3)

    pass_glossary = []

    # list1.extend(list2) ===> Similar to appending list but doesnt create list within list

    pass_glossary.extend(ls1)
    pass_glossary.extend(ls2)
    pass_glossary.extend(ls3)

    #pass_len = int(input("Enter Password Length: "))

    o_list = random.sample(pass_glossary, 5)

    o_str = ''.join(o_list)  # ===> join the elements of password list to give a String
    return o_str

if __name__ =='__main__':
    app.run()


