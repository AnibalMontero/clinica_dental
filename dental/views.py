from django.shortcuts import render
from django.core.mail import send_mail

def home(request):
	return render(request,'home.html',{})

def contacto(request):
	if request.method == "POST":
		nombre_contacto = request.POST['nombre_contacto']
		email_contacto = request.POST['email_contacto']
		mensaje = request.POST['mensaje']

		#Enviar email
		send_mail(
			'Mensaje por la web de '+ nombre_contacto , # subject
			mensaje, # message
			email_contacto, # from email
			['anibal.montero.p@gmail.com'], # to email
			fail_silently=False,
			)

		return render(request,'contacto.html',{
			'nombre_contacto':nombre_contacto,
			'email_contacto':email_contacto,
			'mensaje':mensaje,
			})
	else:

		return render(request,'contacto.html',{})