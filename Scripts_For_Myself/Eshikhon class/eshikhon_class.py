###https://pastebin.ubuntu.com/p/WS7Bb9jmNH/

import requests
import re
import sys
import pyperclip
login_url ="https://www.eshikhon.com/wp-login.php"
course_url ="https://www.eshikhon.com/course/complete-interactive-python-course-from-biggener-to-advanced/"
login = {
    "log":"azwad.sidrat@gmail.com",
    "pwd":"019abnek",
    "user-submit":"Log In",
    "user-cookie":"1"
}

def main():
    with requests.session() as s:
        s.post(login_url, data=login)
        r = s.get(course_url)
        text_1 = r.text
        style = re.compile(r'https://www.eshikhon.com/unit/class-\d\d-pyth-batch-n212-2/')
        list_1 = style.findall(text_1)
        
        
        class_number = '+'.join(sys.argv[1:])
        full_link = "https://www.eshikhon.com/unit/class-"+class_number+"-pyth-batch-n212-2/"
        index = list_1.index(full_link)
        
        text_2 = s.get(list_1[index]).text
        style_2 = re.compile(r'\'https://zoo.+?\'')
        class_link = style_2.findall(text_2)
        print(class_link[0][1:-1])
        pyperclip.copy(class_link[0][1:-1])

if __name__ == "__main__":
    sys.argv
    main()

    

        
