from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import math
import random
import matplotlib.pyplot as plt
from .forms import NameForm

def sample_data(m,n,s):

    random.seed(s)
    i=0
    out_list = []
    while i < m:
        j=0
        list = []
        while j < n:
            num = random.random()*10
            list.append(num)
            j+=1
        out_list.append(list)
        i+=1

    return out_list


def dist(n1,n2):
    dim_no = len(n1)
    sum = 0
    i=0
    while i < dim_no:
        sum += pow(n2[i] - n1[i],2)
        i+=1

    distance = math.sqrt(sum)
    return distance


def index(request):

    list1 = [3, 4, 5, 6]
    list2 = [3, 4, 4, 4]

    #list2[2] = 5


    dat = sample_data(50,2,8)
    out_var = dat
    #out_var = dist(dat[0], dat[1])
    x_coor = []
    y_coor = []

    i=0
    while i < len(out_var):
        x_coor.append(out_var[i][0])
        y_coor.append(out_var[i][1])
        i+=1

    plt.scatter(x_coor,y_coor)
    plt.show()
    return render(request, 'app1/index.html', {'out_var': out_var})


def get_name(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = NameForm(request.POST)
        # check whether it's valid:
        if form.is_valid():
            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            return HttpResponse(str(form.cleaned_data['your_name'])+' form filled')

    # if a GET (or any other method) we'll create a blank form
    else:
        form = NameForm()

    return render(request, 'formtest.html', {'form': form})
