from django.shortcuts import render, render_to_response, redirect, get_object_or_404
from django.template import RequestContext

def index(request):
    data={}
    return render_to_response("trove_app/index.html",data, context_instance=RequestContext(request))

