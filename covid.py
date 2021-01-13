from selenium import webdriver
from pyfiglet import Figlet

from selenium.webdriver.firefox.options import Options
#
options = Options()
options.headless = True
#
x = ""
ff = webdriver.Firefox(options=options)
ff.get('https://www.google.com/search?ei=YT__X_-VLuKj5OUPsuGI2Ac&q=covid&oq=covid&gs_lcp=CgZwc3ktYWIQAzIECAAQQzIECAAQQzIICAAQsQMQgwEyCAgAELEDEIMBMggIABCxAxCDATIFCAAQsQMyBQgAELEDMgQIABBDMgUIABCxAzIFCAAQsQM6AggAOgYIABAWEB46CggAELEDEIMBEEM6BQguELEDOgsIABCxAxDHARCjAjoOCAAQsQMQgwEQxwEQowI6AgguUJ4OWL4VYIMcaABwAHgAgAHhAYgB9gaSAQUwLjUuMZgBAKABAaoBB2d3cy13aXrAAQE&sclient=psy-ab&ved=0ahUKEwi_yoWnyJnuAhXiEbkGHbIwAnsQ4dUDCAw&uact=5')
# Total de casos
tudo = ff.find_element_by_class_name("wsV78c").text
def casos():
    print("Essa é toda a informação atualizada hoje!")
    print(tudo) 
    key = input("aperte qualquer tecla para continuar: ")
def sint():
    sintomas = ff.find_element_by_class_name("Z0mB9b").text
    print(sintomas)
    key =input("aperte qualquer tecla para continuar: ")

def menu():
    global x
    while True and x != "3":
        f = Figlet(font='slant')
        print(f.renderText('Covid 19'))
        x = str(input("""O que deseja?\nDados sobre a contaminação: 1\nDesejo saber os sintomas!: 2\nSair: 3\n~>"""))
        if x == "1":
            casos()
        elif x == "2":
            sint()
        elif x == "3":
            break
        else:
            print("Não entendi!")
menu()
