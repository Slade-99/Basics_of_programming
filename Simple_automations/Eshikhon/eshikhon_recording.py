import requests
from bs4 import BeautifulSoup
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
        content_1 = BeautifulSoup(r.content, 'html.parser')
        all_class = []
        x=content_1.find_all('table' , attrs={'class' : 'table'})
        for full in x:
            for class_link in full.find_all('a'):
                if 'Quiz' not in class_link.text:
                    all_class.append(class_link.text)


        
        y='+'.join(sys.argv[1:])
        url_2 = f'https://www.eshikhon.com/unit/class-{y}-pyth-batch-n212-2/'
        r_2 = s.get(url_2)
        soup = BeautifulSoup(r_2.content , 'html.parser')
        for p in soup.find_all('a', href=True):
            if 'drive' in p['href'] and 'Video' in p.text:
                x=p['href']
                print(x)
                pyperclip.copy(x)
        
# 
# list_1 = style.findall(text_1)
        
        
#         class_number = '+'.join(sys.argv[1:])
#         full_link = "https://www.eshikhon.com/unit/class-"+class_number+"-pyth-batch-n212-2/"
#         index = list_1.index(full_link)
        
#         text_2 = s.get(list_1[index]).text
#         style_2 = re.compile(r'\'https://zoo.+?\'')
#         class_link = style_2.findall(text_2)
#         print(class_link[0][1:-1])
#         pyperclip.copy(class_link[0][1:-1])

if __name__ == "__main__":
    sys.argv
    main()

