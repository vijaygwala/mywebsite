from django.shortcuts import render
from django.http import HttpResponse
from dashboard.forms import CityForm
from dashboard.models import City
from dashboard.helper import get_weather_data,get_city_using_publicIp
# Create your views here.

def home(request):
    form = CityForm()

    if request.method == 'POST':
        form = CityForm(request.POST)
        if form.is_valid():
            obj=form.save()
            city_name = form.cleaned_data.get('city_name')
            weather_data = get_weather_data(city_name)
            if weather_data is None:
                obj.delete()
    elif request.method == 'GET':
        try:
            city_name = get_city_using_publicIp()
            weather_data = get_weather_data(city_name)
        except Exception as e:
            weather_data = None

    template_name = 'home.html'
    context = {'form': form, 'weather_data': weather_data}
    return render(request, template_name, context=context)

from dateutil.parser import parse
def history(request):
    template_name = 'history.html'
    date=request.POST.get('date',None)
    if request.method=='POST' and date:
        dt = parse(date)
        print(dt.date())
        cities=City.objects.filter(date_added__date=dt.date())
    else:
        cities = City.objects.all().order_by('-date_added')[:2]

    weather_data_list = []
    for city in cities:
        city_name = city.city_name
        weather_data_list.append(get_weather_data(city_name))

    context = {'weather_data_list': weather_data_list}
    return render(request, template_name, context)