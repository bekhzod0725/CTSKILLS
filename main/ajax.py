import json
from django.http import Http404, HttpResponse

def getdata(request):
    if request.is_ajax() and request.POST:
        value = request.POST.get('value', None)
        data = {'value': int(value) * 2}
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        raise Http404
