from django.db import models

#ユーザーモデル
class User(models.Model):
    name = models.CharField(max_length=32)
    mail = models.EmailField()

#記事モデル
class Post(models.Model):
    STATUS_DRAFT = "draft"
    STATUS_PUBLIC = "public"
    STATUS_SET = (
            (STATUS_DRAFT, "下書き"),
            (STATUS_PUBLIC, "公開中"),
    )
    title = models.CharField(max_length=128)
    body = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    status = models.CharField(choices=STATUS_SET, default=STATUS_DRAFT, max_length=8)
    #Postを書いた人の情報として、Userを参照する
    #Djangoの場合related_nameを付けるだけで逆参照も行える
    author = models.ForeignKey(User, related_name='Posts', on_delete=models.CASCADE)