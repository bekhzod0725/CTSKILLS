import json, pandas as pd
from django.http import Http404, HttpResponse

def get_town_info(town_name):
    town_emp = pd.read_csv('town_emp.csv')
    town_info = town_emp[ town_emp['Town/County']==town_name]
    return town_info[['Industry Name','Value']]

def getdata(request):
    if request.is_ajax() and request.POST:
        town = request.POST.get('town', None)
        if not isinstance(town, type(None)):
            result = get_town_info(town)
            data = {'value': result}
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        raise Http404
