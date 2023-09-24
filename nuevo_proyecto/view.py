from django.http import HttpResponse

def saludo(request):
	return HttpResponse("Hola Django - Coder")

def segundaVista(requeste):
      return HttpResponse("<br><br> Ya entendimos esto es muy simple :)")

def diaDeHoy(request):
      dia = datetime.datetime.now()
      

def probandoTemplate(self):
	
    nom = "Nicolas"
    ap = "Apellido"

    diccionario = {"nombre":nom,"Apellido":ap}

    miHtml = open("./nuevo_proyecto/template.1/")

    plantilla = Template(miHtml.read())
    
    miHtml.close()

