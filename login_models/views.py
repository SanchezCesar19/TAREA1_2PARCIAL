from django.shortcuts import render
from login_models.models import Usuario, Trabajador

# Create your views here.
def login(request):
    return render(request,'login.html',{})
def loginsesiondef(request):
    if request.method == 'GET':
        return request(request,"login.html",{})
    else:
        usuariostr = request.POST.get('usu')
        passwordstr = request.POST.get('pass')
        try:
            print(usuariostr, passwordstr)
            usuario = Usuario.objects.get(usuario=usuariostr, password=passwordstr)
            print(usuariostr, passwordstr)
            trabajadorlist = Trabajador.objects.values()
            return render(request, "menu.html", {"list": trabajadorlist, 'usuariostr': usuario.usuario})
        except Usuario.DoesNotExist:
            return render(request, "login.html",{"err":"-Usuario y contraseña incorrectos-"})
