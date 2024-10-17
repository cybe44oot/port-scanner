from django.shortcuts import render
from django.http import HttpResponse


#from django.shortcuts import render
#from django.http import HttpResponseRedirect
#from django.core.urlresolvers import reverse
from .models import Request,Result
from .forms import RequestForm,ResultForm

import socket
import threading
data_2={}
def scan_port(port,target):
  
  status=''
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.settimeout(0.5)
  result = s.connect_ex((target,port))
  if (not result):
    status='open'
    print(f"port {port} is open ")
   
  else:
    status='close'  

  data_2[port]=status
  s.close()
  
 

def scan(request):
  
  ip =request.POST.get('ip')
  start=request.POST.get('start_port')
  end = request.POST.get('end_port')
  data =RequestForm(request.POST)
  if data.is_valid():
     data.save()
  
  target = socket.gethostbyname(ip)
  
  for port in range(int(start),int(end)):
     thread = threading.Thread(target=scan_port, args=(port,target,))
     thread.daemon=True
     thread.start()
   
  return render(request,'port_scanner.html',{'form':RequestForm,'data':data_2})