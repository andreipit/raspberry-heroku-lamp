from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from django.conf import settings
import pickle
import pandas as pd

# Create your views here.
def index2(request):
    # return HttpResponse('Hello from Python!')
    return render(request, "index.html")


def db(request):

    greeting = Greeting()
    greeting.save()

    greetings = Greeting.objects.all()

    return render(request, "db.html", {"greetings": greetings})


# def index3(request):
#     import pickle
#     import pandas as pd

#     imgs_adress = settings.STATIC_ROOT + '\\hello\\hello_imgs\\'
#     context = {'predictions': 'index','df': 'index','pred': 'index','imgs_adress':imgs_adress, 'values':[12,13,14,15,16,17]}
#     filepath = settings.MEDIA_ROOT + '/hello/'+ 'df' + '.csv'
#     df = pd.read_csv(filepath, parse_dates=["date"], index_col="date") #df = pd.read_json('NashDomRyazan-29-03-2019.json', encoding='utf-8')
#     true_values = []; predictions = []; dates = []
#     for i in range(df.shape[0]):
#         true_values.append(df.iloc[i]['activity'])
#         predictions.append(df.iloc[i]['pred6h'])    
#         dates.append(str(df.index[i]))
#     result = (true_values, predictions, dates)
#     context['df'] = result#str(df.head(1000))
#     context['values'] = [df['f0'][-1],df['f1'][-1],df['f2'][-1],df['f3'][-1],df['f4'][-1],df['f5'][-1]]
#     return render(request, "index.html", context)


def index(request):
    col0 = []; col1 = []; col2 = []
    filepath = settings.MEDIA_ROOT + '/hello/df.csv'
    df = pd.read_csv(filepath, parse_dates=["date"], index_col="date")




    for i in range(df.shape[0]):
        col0.append(str(df.index[i])); col1.append(df.iloc[i]['activity']); col2.append(df.iloc[i]['pred6h'])    
    
    df.iloc[0]['activity'] += 1; df.to_csv(filepath)
    return render(request, "index.html", {'df': (col0, col1, col2)})
