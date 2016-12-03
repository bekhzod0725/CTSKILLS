import json, pandas as pd
from django.http import Http404, HttpResponse

def get_town_info(town_name):
    town_emp = pd.read_csv('town_emp.csv')
    town_info = town_emp[ town_emp['Town/County']==town_name]
    return town_info[['Industry Name','Value']]

def getdata(request):
    if request.is_ajax() and request.POST:
        town = request.POST.get('town', None)
        result = get_town_info(town)
        data = {'value': [ (e[0],e[1]) for e in result.values]}
        return HttpResponse(json.dumps(data), content_type="application/json")
    else:
        raise Http404
 
def get_percapita(request):
    if request.is_ajax() and request.POST:
        town_pc = pd.read_csv('percapit.csv')
        f = lambda x: x.lower()
        vf = pd.np.vectorize(f)
        town_pc['Municipality'] = vf(town_pc['Municipality'])

        town = request.POST.get('town', None)
        town_info = town_pc[town_pc['Municipality'] == town.lower()]
        info = {'2011':town_info['TPC_2011'].values[0],
                '2012':town_info['TPC_2012'].values[0],
                '2013':town_info['TPC_2013'].values[0],
                '2014':town_info['TPC_2014'].values[0],}
        data = {'value':data}
        return HttpResponse(json.dumps(data),content_type="application/json")
    else:
        raise Http404
        
