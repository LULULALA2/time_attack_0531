from django.shortcuts import render,redirect
from .models import ArticleModel,CategoryModel


def article_view(request):
    if request.method == 'GET':  # 요청하는 방식이 GET 방식인지 확인하기
            all_category = CategoryModel.objects.all().order_by('-created_at')
            return render(request, 'detail.html', {'category': all_category})

    elif request.method == 'POST':  # 요청 방식이 POST 일때
        my_article = ArticleModel()  # 글쓰기 모델 가져오기
        my_article.title = request.POST.get('my-content', '')
        my_article.category = CategoryModel.category
        my_article.content = request.POST.get('my-content', '')
        my_article.save()
        return redirect('/category')


def category_view(request):
    if request.method == 'GET':  # 요청하는 방식이 GET 방식인지 확인하기
        all_category = CategoryModel.objects.all().order_by('created_at')
        return render(request, 'category.html', {'category': all_category})

