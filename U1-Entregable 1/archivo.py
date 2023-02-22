# pip install requests
import requests

# Torrente, el brazo tonto de la ley
r = requests.get('https://www.filmaffinity.com/es/film334167.html')

t = r.text

# print(t)   # Esto es para imprimirme el HTML de la peli

espacio = '&nbsp;'
dd = '<dd>'
dd_c = '</dd>'
span = '<span>'
span_c = '</span>'
div_c = '</div>'
dt = '<dt>'
dt_c = '</dt>'
a = '<a>'
a_c = '</a>'
style = '<style>'
style_c = '</style>'


def titulo_original(t):
    label = t[t.find('<dt>Título original</dt>'):t.find(dd_c)]
    titulo_original = label[label.find(dd):].splitlines()[1]
    titulo_original = titulo_original.lstrip().rstrip()
    # Este paso será necesario sólo para las películas que tienen
    #  'aka', pero no hace daño dejarlo para las demás.
    find_aka = titulo_original.find('<span')
    if (find_aka != -1):
        titulo_original = titulo_original[:find_aka]
    return titulo_original

def anio(t):
    cadena = '<dd itemprop="datePublished">'
    longitud = len(cadena)
    anio = t[t.find('<dd itemprop="datePublished">')+longitud:t.find('<dd itemprop="datePublished">')+longitud+4]

    return anio

def duracion(t):
    cadena = '<dd itemprop="duration">'
    longitud = len(cadena)
    duracion = t[t.find('<dd itemprop="duration">')+longitud:t.find('<dd itemprop="duration">')+longitud+7]

    return duracion

def pais(t):
    longitudEspacio = len(espacio)
    label = t[t.find('<span id="country-img">'):]
    pais = label[label.find(espacio)+longitudEspacio:label.find(dd_c)]

    return pais

def direccion(t):
    cadena = '<span itemprop="name">'
    longitud = len(cadena)
    label = t[t.find('<dd class="directors">'):]
    direccion = label[label.find('<span itemprop="name">')+longitud:label.find(span_c)]

    return direccion

def guion(t):
    cadena = '<span>'
    longitud = len(cadena)
    label = t[t.find('<dt>Guion</dt>'):]
    guion = label[label.find('<span>')+longitud:label.find(span_c)]

    return guion

def musica(t):
    cadena = '<span>'
    longitud = len(cadena)
    label = t[t.find('<dt>Música</dt>'):]
    musica = label[label.find('<span>')+longitud:label.find(span_c)]

    return musica

def fotografia(t):
    cadena = '<span>'
    longitud = len(cadena)
    label = t[t.find('<dt>Fotografía</dt>'):]
    fotografia = label[label.find('<span>')+longitud:label.find(span_c)]

    return fotografia

def reparto(t):
    cadena = '<span itemprop="name">'
    longitud = len(cadena)
    label = t[t.find('<dt>Reparto</dt>'):]
    label = label[label.find('<span itemprop="name">'):label.find(style_c)]

    array = label.split("name")
    array.pop(0)

    reparto = ""

    for i in array:
        reparto += i[2:i.find(span_c)]+", "

    return reparto

def productora(t):
    cadena = '<span>'
    longitud = len(cadena)
    label = t[t.find('<dt>Compañías</dt>'):]
    productora = label[label.find('<span>')+longitud:label.find(span_c)]

    return productora

def genero(t):
    cadena = '<a href="https://www.filmaffinity.com/es/moviegenre.php?genre=CO&attr=rat_count&nodoc">'
    longitud = len(cadena)
    label = t[t.find('<dt>Género</dt>'):]
    label = label[label.find('<a href="https://www.filmaffinity.com/es/moviegenre.php?genre=CO&attr=rat_count&nodoc">')+longitud:label.find(dd_c)]

    array = label.split("<a")


    generos = ""

    generos += label[:label.find(a_c)]+", "

    array.pop(0)

    for i in array:
        cadena = 'count&nodoc">'
        longitud = len(cadena)
        generos += i[i.find('count&nodoc">')+longitud:i.find(a_c)]+", "

    return generos

def sinopsis(t):
    cadena = '<dd class="" itemprop="description">'
    longitud = len(cadena)
    label = t[t.find('<dt>Sinopsis</dt>'):]
    sinopsis = label[label.find('<dd class="" itemprop="description">')+longitud:label.find(dd_c)]

    return sinopsis

direccion = {
    "titulo_original":titulo_original(t),
    "anio":anio(t),
    "duracion":duracion(t),
    "pais":pais(t),
    "direccion":direccion(t),
    "guion":guion(t),
    "musica":musica(t),
    "fotografia":fotografia(t),
    "reparto":reparto(t),
    "productora":productora(t),
    "genero":genero(t),
    "sinopsis":sinopsis(t)
}

print(direccion)