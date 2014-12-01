from django.core.context_processors import csrf
from django.template import RequestContext
from django.shortcuts import render_to_response, render
from django.http import Http404, HttpResponse, HttpResponseRedirect, HttpResponseNotFound
from django.http import *
from django.conf import settings
# import mongoengine
from django.core.mail import send_mail
from django.template.loader import render_to_string, get_template
from django.core.mail import EmailMultiAlternatives
from django.template.loader import get_template
from django.template import Context
import random,string
from pyUrl.models import * 

def home(request):
	random1 = None
	c = {}
	c.update(csrf(request))
	if request.POST:
		c = {}
		c.update(csrf(request))
		url = request.POST['url']
		random1=''.join([random.choice(string.letters + string.digits) for i in range(5)])
		shortUrl = str(random1)
		print shortUrl
		urldata(url = url,shortUrl = shortUrl).save()
		return render_to_response("shorten.html",{"shortUrl" : "http://pyUrl.com/"+str(shortUrl)},
                           context_instance=RequestContext(request))
		# return render_to_response("index.html",{'shortUrl':1},c)
	# request.session.set_test_cookie()
	# if request.session.test_cookie_worked():
	# 	print 'hello'
	#geo=''.join([random.choice(string.letters + string.digits) for i in range(10)])
	return render_to_response("index.html",c)

# def shorten(request):
# 	if request.POST:
# 		url = request.POST['url']
# 		random=''.join([random.choice(string.letters + string.digits) for i in range(10)])
# 		shortUrl = "http://pyUrl.com/"+str(random)
# 		print shortUrl
# 		return render_to_response("index.html",{'shortUrl':shortUrl},context_instance=RequestContext(request))
# 	return render_to_response("shorten.html")
def open(request,url=None):
	# print url
	if request.path=='/':
		return home(request)
	print "check below one "
	print request.path
	print "just above one "
	try:
		out = urldata.objects.get(shortUrl=str(request.path)[1:])
		urlOut = str(out.url)
		print urlOut
		return HttpResponseRedirect(urlOut)
	except:
		return HttpResponse('<h1>The give url link is invalid</h1>')