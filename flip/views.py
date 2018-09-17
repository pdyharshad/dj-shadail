# Create your views here.

from django.views import generic
from django.shortcuts import redirect

class IndexView(generic.ListView):
    template_name = 'flip/index.html'
#    context_object_name = 'flip_list'

    def get_queryset(self):
        """Return the last five published questions."""
        print("Int he index view")
        return True


def get_image(request,image):
    print(image)
    return redirect('http://localhost:8000/static/flip/lumencanvas-master/img/%s'%image)
