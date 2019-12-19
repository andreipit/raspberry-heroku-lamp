from django.shortcuts import render
from django.http import HttpResponse

from .models import Greeting
from django.conf import settings
import pickle, datetime
import pandas as pd

# Create your views here.
def index_default(request):
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

def _df_path(): return settings.MEDIA_ROOT + '/hello/df.csv'
def _df(): return pd.read_csv(_df_path(), parse_dates=["date"], index_col="date")
def _df2tuple(): 
    col0 = []; col1 = []; col2 = []
    df = _df()
    for i in range(df.shape[0]):
        # col0.append(str(df.index[i])); col1.append(df.iloc[i]['light_theory']); col2.append(df.iloc[i]['light_practice'])    
        col0.append(df.iloc[i]['last_check_date']); col1.append(df.iloc[i]['light_theory']); col2.append(df.iloc[i]['light_practice'])    
    return (col0, col1, col2)

def light_on(request):
    df = _df(); 
    # df.iloc[0]['light_theory'] = 1; 
    df['light_theory'].iat[0] = 1 # 1=row number, works even if index is dates

    df.to_csv(_df_path())
    return render(request, "index.html", {'df': _df2tuple()})

def light_off(request):
    df = _df(); 
    df['light_theory'].iat[0] = 0 # 1=row number, works even if index is dates

    #df.iloc[0]['light_theory'] = 0; 


    df.to_csv(_df_path())
    return render(request, "index.html", {'df': _df2tuple()})

def light_on_practice(request):
    df = _df(); 
    df['light_practice'].iat[0] = 1
    df['last_check_date'].iat[0] = datetime.datetime.now()
    # df.iloc[0]['light_practice'] = 1; 
    # df.iloc[0]['last_check_date'] = datetime.datetime.now(); 
    df.to_csv(_df_path())
    return render(request, "index.html", {'df': _df2tuple()})

def light_off_practice(request):
    df = _df(); 
    df['light_practice'].iat[0] = 0
    df['last_check_date'].iat[0] = datetime.datetime.now()
    # df.iloc[0]['light_practice'] = 0; 
    # df.iloc[0]['last_check_date'] = str(datetime.datetime.now()); 
    df.to_csv(_df_path())
    return render(request, "index.html", {'df': _df2tuple()})


def index(request): return render(request, "index.html", {'df': _df2tuple()})

def min(request): return render(request, "index_min.html", {'df': _df2tuple()})
