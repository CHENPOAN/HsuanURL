from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.views import View

from analytics.models import ClickEvent

from .forms import SubmitUrlForm
from .models import HsuanURL

# Create your views here.

class HomeView(View):
    def get(self, request, *args, **kwargs):
        the_form = SubmitUrlForm()
        context = {
            "title": "Hsuan URL",
            "form": the_form
        }
        return render(request, "shortener/home.html", context)

    def post(self, request, *args, **kwargs):
        form = SubmitUrlForm(request.POST)
        context = {
            "title": "Hsuan URL",
            "form": form
        }
        template = "shortener/home.html"
        if form.is_valid():
            new_url = form.cleaned_data.get("url333")
            print(new_url)
            obj, created = HsuanURL.objects.get_or_create(url=new_url)
            print(obj, created)
            context = {
                "object": obj,
                "created": created
            }
            if created:
                template = "shortener/success.html"
            else:
                template = "shortener/exists.html"

        return render(request, template, context)


class URLRedirectView(View):  # Class Based View (CBV)
    def get(self, request, shortcode=None, *args, **kwargs):
        qs = HsuanURL.objects.filter(shortcode__iexact=shortcode)
        if qs.count != 1 and not qs.exists():
            raise Http404
        obj = qs.first()
        print(ClickEvent.objects.create_event(obj))
        return HttpResponseRedirect(obj.url)


# def hsuan_redirect_view(request, shortcode=None, *args, **kwargs):  # Function Based View (FBV)
#
#     print(request.method)
#     obj = get_object_or_404(HsuanURL, shortcode=shortcode)
#
#     # try:
#     #     obj = HsuanURL.objects.get(shortcode=shortcode)
#     # except:
#     #     obj = HsuanURL.objects.all().first()
#
#     # obj_url = None
#     # qs = HsuanURL.objects.filter(shortcode__iexact=shortcode.upper())
#     # if qs.exists() and qs.count() == 1:
#     #     obj = qs.first()
#     #     obj_url = obj.url
#
#     return HttpResponse("hello {sc}".format(sc=obj.url))