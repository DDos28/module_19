from django.shortcuts import render
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from .models import Post

def post_list(request):
    posts = Post.objects.all()
    per_page = request.GET.get('per_page', 10) # 10 по умолчанию
    try:
        per_page = int(per_page)
        if per_page <=0:
            per_page = 10 # если число не положительное то ставим 10
    except ValueError:
        per_page = 10
    paginator = Paginator(posts, per_page)
    page_number = request.GET.get('page')
    try:
        page_obj = paginator.get_page(page_number)
    except PageNotAnInteger:
        page_obj = paginator.get_page(1)
    except EmptyPage:
        page_obj = paginator.get_page(paginator.num_pages)
    context = {'page_obj': page_obj, 'per_page': per_page}
    return render(request, 'post_list.html', context)