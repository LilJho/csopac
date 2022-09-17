from django.views.generic.base import TemplateView
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView

from thesis.models import Thesis, PublishedManager, Comment
from django.db.models import Q
from django.shortcuts import render, redirect

# @method_decorator(login_required, name='dispatch')
class HomePageView(ListView):
    model = Thesis
    context_object_name = 'thesis'
    template_name = "landingpage/home.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['thesis_count'] = Thesis.objects.count()

        return context

class ThesisList(ListView):
    model = Thesis
    context_object_name = 'thesis'
    template_name = 'thesis_list.html'
    paginate_by = 10

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context

    def get_queryset(self, *args, **kwargs):
        qs = super(ThesisList, self).get_queryset(*args, **kwargs)
        qs = qs.order_by("-publish")
        if self.request.GET.get("q") != None:
            query = self.request.GET.get('q')
            qs = qs.order_by("-publish").filter(Q(title__icontains=query) | Q(authors__icontains=query))
        return qs


def thesis_detail(request, id):
    thesis = Thesis.objects.get(id=id)
    return render(request,
          'thesis_details.html',
         {'thesis': thesis})



                 