from django.shortcuts import render
from django.views import View
from django.db.models import Q
from django.http import HttpResponse
from ..models import Question

class SearchView(View):
    def searchposts(request):
        quesList = Question.objects.all()
        if request.method == 'GET':
            query = request.GET.get('query')
            submitbutton = request.GET['submit']
            if query is not None:
                lookups= Q(title__icontains=query) | Q(description__icontains=query)
                results= Question.objects.filter(lookups).distinct()
                context={'results': results,
                        'submitbutton': submitbutton,
                        }
                return render(request, 'search.html', context)
            else:
                return HttpResponse("Nothing Found !!!")
        else:
            return render(request, 'search.html')