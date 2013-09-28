from django.http import HttpResponseRedirect, Http404
from django.shortcuts import render
from django.views.generic.base import View

import re

from models import DomainName, Navigation, CustomPage, Slide

class HomeView(View):
    template_name = 'home.html'

    def get_domain_name(self, request):
        """Gets the domain name from current url
        """
        return re.search('http://(.*):8000', request.build_absolute_uri()).group(1)

    def get(self, request, *args, **kwargs):
        """Handles GET requests
        """
        response = {}
        if 'school' not in request.session:
            try:
                request.session['school'] = response['school'] = \
                DomainName.objects.select_related().get(url=self.get_domain_name(request)).school
            except:
                raise Http404
        else:
            response['school'] = request.session['school']

        if 'navigation' not in request.session:
            request.session['navigation'] = response['navigation'] = \
                Navigation.objects.filter(school__id=response['school'].id)
        else:
            response['navigation'] = request.session['navigation']

        response['slides'] = Slide.objects.filter(school__id=response['school'].id).order_by('order')

        return render(request, self.template_name, response)

    def post(self, request, *args, **kwargs):
        """Handles POST requests
        """
        '''form = self.form_class(request.POST)
        if form.is_valid():
            # <process form cleaned data>
            return HttpResponseRedirect('/success/')'''
        pass

        return render(request, self.template_name, {})

class PageView(View):
    template_name = 'page.html'

    def get(self, request, *args, **kwargs):
        """Handles GET requests
        """
        response = {}
        page_name = kwargs.get('page_name')

        if page_name:
            try:
                response['page'] = CustomPage.objects.get(school__id=request.session['school'].id, page_url=page_name)
            except:
                raise Http404

        return render(request, self.template_name, response)