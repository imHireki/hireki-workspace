from django_hosts.resolvers import reverse
from django.shortcuts import render
from django.views.generic import View


class About(View):

    def setup(self, *args, **kwargs):
        super().setup(*args, **kwargs)
        
        current_url = reverse('about')

        if '//en.' in current_url:
            self.template_name = 'about/en_about.html'
        elif '//pt.' in current_url:
            self.template_name = 'about/pt_about.html'
        elif '//es.' in current_url:
            self.template_name = 'about/es_about.html'
                
    def get(self, *args, **kwargs):
        return render(self.request, self.template_name)
