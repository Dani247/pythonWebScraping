from bs4 import BeautifulSoup
import requests

#get request
html_doc = requests.get('http://toscrape.com/', headers = {'Accept-Encoding':'identity'})

#pasar contenido html a la una variable BeautifulSoup
soup = BeautifulSoup(html_doc.content, 'html.parser')


#pruebas

#print(soup.img.get('class')[0])
#print(soup.find_all('img'))

#for imagen in soup.find_all('img'):
#    print ("Ruta de la imagen: " + imagen.get('src'))

#for link in soup.find_all('a'):
#    print(link.get('href'))