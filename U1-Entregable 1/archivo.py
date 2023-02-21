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


print(titulo_original(t))

def anio(t):
    cadena = '<dd itemprop="datePublished">'
    longitud = len(cadena)
    anio = t[t.find('<dd itemprop="datePublished">')+longitud:t.find('<dd itemprop="datePublished">')+longitud+4]

    return anio

print(anio(t))

def duracion(t):
    cadena = '<dd itemprop="duration">'
    longitud = len(cadena)
    duracion = t[t.find('<dd itemprop="duration">')+longitud:t.find('<dd itemprop="duration">')+longitud+7]

    return duracion

print(duracion(t))

def pais(t):
    longitudEspacio = len(espacio)
    label = t[t.find('<span id="country-img">'):]
    pais = label[label.find(espacio)+longitudEspacio:label.find(dd_c)]

    return pais

print(pais(t))

def direccion(t):
    cadena = '<span itemprop="name">'
    longitud = len(cadena)
    label = t[t.find('<dd class="directors">'):]
    direccion = label[label.find('<span itemprop="name">')+longitud:label.find(span_c)]

    return direccion

print(direccion(t))

def guion(t):
    cadena = '<span>'
    longitud = len(cadena)
    label = t[t.find('<dt>Guion</dt>'):]
    direccion = label[label.find('<span>')+longitud:label.find(span_c)]

    return direccion

print(guion(t))

def musica(t):
    cadena = '<span>'
    longitud = len(cadena)
    label = t[t.find('<dt>Música</dt>'):]
    direccion = label[label.find('<span>')+longitud:label.find(span_c)]

    return direccion

print(musica(t))

def fotografia(t):
    cadena = '<span>'
    longitud = len(cadena)
    label = t[t.find('<dt>Fotografía</dt>'):]
    direccion = label[label.find('<span>')+longitud:label.find(span_c)]

    return direccion

print(fotografia(t))

def reparto(t):
    cadena = '<span itemprop="name">'
    longitud = len(cadena)
    label = t[t.find('<dt>Reparto</dt>'):]
    direccion = label[label.find('<span itemprop="name">')+longitud:label.find(span_c)]

    return direccion

print(reparto(t))

def productora(t):
    cadena = '<span>'
    longitud = len(cadena)
    label = t[t.find('<dt>Compañías</dt>'):]
    direccion = label[label.find('<span>')+longitud:label.find(span_c)]

    return direccion

print(productora(t))

def genero(t):
    cadena = '<a href="https://www.filmaffinity.com/es/moviegenre.php?genre=CO&amp;attr=rat_count&amp;nodoc">'
    longitud = len(cadena)
    label = t[t.find('<dt>Género</dt>'):]
    print(label)
    genero = label[label.find('<a href="https://www.filmaffinity.com/es/moviegenre.php?genre=CO&amp;attr=rat_count&amp;nodoc">')+longitud:label.find(a_c)]

    return genero

print(genero(t))