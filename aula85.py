import urllib.request

pagina= urllib.request.urlopen('tabela.html')
texto=pagina.read().decode('utf-8')

print(texto)