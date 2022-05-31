from django.db import models


class CategoryModel(models.Model):

    class Meta:
        db_table = "my_category" # 테이블 이름

    category = models.CharField(max_length=256, null=False)
    desc = models.CharField(max_length=256, null=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class ArticleModel(models.Model):

    class Meta:
        db_table = "my_article" # 테이블 이름

    title = models.CharField(max_length=20, null=False)
    category = models.ForeignKey(CategoryModel, on_delete=models.CASCADE)
    content = models.CharField(max_length=256, default='')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


