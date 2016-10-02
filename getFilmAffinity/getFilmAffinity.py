__author__ = 'ruben'

# -*- coding: utf-8 -*-
import urllib2, unicodedata
import time
import re
from bs4 import BeautifulSoup

def analisisDescarga(url, run_file, data_file):
    conector = urllib2.urlopen(url, timeout=60)
    html = conector.read()
    soup = BeautifulSoup(html)
    links = soup.findAll("div", {"class": "movie-card movie-card-1"})
    for link in links:
        sPeli = "";
        numPeli = (link['data-movie-id'])
        # Esta url representa una unica pelicula.
        # De la cual vamos a obtener titulo, anno, director, votos y valoracion
        url = "http://www.filmaffinity.com/es/film" + numPeli + ".html"
        conector = urllib2.urlopen(url, timeout=60)
        sPeli += numPeli + "|"
        html = conector.read()
        soup = BeautifulSoup(html)
        # Recogemos el titulo
        titulo = soup.findAll("span", {"itemprop": "name"})[0].text
        sPeli += titulo + "|"
        # Recogemos el director
        director = soup.findAll("span", {"itemprop": "name"})[1].text
        sPeli += director + "|"
        # Recogemos el anno
        anno = soup.findAll("dd", {"itemprop": "datePublished"})[0].text
        sPeli += anno + "|"
        # Recogemos el pais
        pais = soup.findAll("span", {"id": "country-img"})[0].findAll("img")[0]['title']
        sPeli += pais + "|"
        # Recogemos la valoracion
        valoracion = soup.findAll("div", {"itemprop": "ratingValue"})[0].text
        sPeli += valoracion.strip() + "|"
        # Recogemos el numero de votos
        numVotos = soup.findAll("span", {"itemprop": "ratingCount"})[0].text
        sPeli += numVotos + "|"
        # Almacenamos en el fichero
        data_file.write((sPeli.strip()+"\n").encode('utf-8'))
        # Recogemos la imagen de la pelicula
        imagenes = soup.findAll("a", {"class": "lightbox"})
        try:
            run_file.write("wget " + imagenes[0]['href'] + "\n")
        except:
            run_file.write("# error " + url + "\n")

# Programa principal
run_file = open("getPelis.sh", "w")
data_file = open("dataPelis.txt", "w")
# Para cada anno de publicacion de la pelicula
for anno in range(2010, 2016):
    # En FilmAffinity se publican 25 paginas para cada anno
    print ("Tratando el anno: " + str(anno))
    for i in range(1, 26):
        url = "http://www.filmaffinity.com/es/advsearch.php?page=" + str(i) + "&stype[]=title&fromyear=" + str(anno) + "&toyear=" + str(anno + 1)
        print (" - - Analizando pagina: " + str(i))
        print (" - - url: " + url)
        print (" - - time: " + time.strftime('%X %x %Z'))
        analisisDescarga(url, run_file, data_file)
run_file.close()
data_file.close()
