from .models import MessageType, Message
# Create your views here.

from django.http import HttpResponse
from django.views import generic
import json


class IndexView(generic.ListView):
    template_name = 'secretly/index.html'
    context_object_name = 'message_type_list'

    def get_queryset(self):
        """Return the last five published questions."""
        print("Int he index view")
        return MessageType.objects.all()


def get_message(request, message_type, latest_id=False):
    limit = 20
    typ = MessageType.objects.get(msg_type=message_type)
    msgs=Message.objects.filter(message_type_id=typ.id, pk__gt=latest_id if latest_id
            else False).order_by("id")[:limit]
    msg_dct = dict([(msg.id, msg.message) for msg in msgs])
    msg_json = json.dumps(msg_dct, ensure_ascii=False).encode('utf8')
    return HttpResponse(msg_json)

def get_message_type(request):
    typs = MessageType.objects.all()
    type_dct = dict([(typ.id, typ.msg_type) for typ in typs])
    type_json = json.dumps(type_dct, ensure_ascii=False).encode('utf8')
    return HttpResponse(type_json)

#def ipost_user(request):
    


def detail(request, question_id):
    return HttpResponse("You're looking at question %s." % question_id)


def results(request, question_id):
    response = "You're looking at the results of question %s."
    return HttpResponse(response % question_id)


def vote(request, question_id):
    return HttpResponse("You're voting on question %s." % question_id)
