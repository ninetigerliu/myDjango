
# -*- coding: utf-8 -*-
 
from django.shortcuts import render
from django.views.decorators import csrf

from MathFinance.blackScholes import BlackScholes
 
# 接收POST请求数据
def calcBS(request):
    ctx ={}
    if request.POST:
        optionType = str(request.POST['optionType'])
        s = float(request.POST['s'])
        k = float(request.POST['k'])
        r = float(request.POST['r'])
        vol = float(request.POST['vol'])
        t = float(request.POST['t'])
        ctx['rlt'] = BlackScholes(optionType,s,k,r,vol,t)
    return render(request, "blackScholeCalculator.html", ctx)
