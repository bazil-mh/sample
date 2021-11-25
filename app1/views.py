from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
import math
import random

def sample_data(m,n,s):

    random.seed(s)
    i=0
    out_list = []
    while i < m:
        j=0
        list = []
        while j < n:
            num = random.random()
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

    dat = sample_data(50,5,6)

    out_var = dist(dat[0], dat[1])
    return render(request, 'app1/index.html', {'out_var': out_var})

