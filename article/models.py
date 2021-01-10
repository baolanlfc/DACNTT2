from django.db import models
from ckeditor.fields import RichTextField
# Create your models here.

class Article(models.Model):
    author = models.ForeignKey("auth.User",on_delete = models.CASCADE,verbose_name = "Tac Gia ")
    title = models.CharField(max_length = 500,verbose_name = "Title")
    content = RichTextField()
    created_date = models.DateTimeField(auto_now_add=True,verbose_name="Ngay Tao")
    article_image = models.FileField(blank = True,null = True,verbose_name="Add Photo")
    def __str__(self):
        return self.title

    class Meta:
        ordering = ['-created_date']
class Comment(models.Model):
    article = models.ForeignKey(Article,on_delete = models.CASCADE,verbose_name = "Bai Viet",related_name="comments")
    comment_author = models.CharField(max_length = 100,verbose_name = "Ten")
    comment_content = models.CharField(max_length = 500,verbose_name = "Binh Luan")
    comment_date = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.comment_content
    class Meta:
        ordering = ['-comment_date']
