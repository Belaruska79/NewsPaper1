from django.db import models


class Autor(models.Model):
    full_name = models.CharField(max_length = 255)
    rating_user = models.IntegerField(default = 0)
    user = models.OneToOne(User)

class Category(models.Model):
    category_name = models.CharField(max_length = 255, unique = True)

class Post(models.Model):
    CHOISE = [(artikle, 'Статья'), (video, 'Новость')]
    news = models.CharField(max_length = 10, choices = CHOISE, default = artikle)
    post_title = models.CharField(max_length = 255)
    post_text = models.TextField()
    post_rating = models.IntegerField(default = 0)
    post_datetime = models.DateTimeField(auto_now_add)
    author = models.ForegnKey(Author, on_delete = models.CASCADE)
    category = models.ManyToManyField(Category, through = 'PostCategory')

    def like_sum(self):
        post_like = self.post.like



class PostCategory
    post = models.ForegnKey(Post, on_delete = models.CASCADE)
    category = models.ForegnKey(Category, on_delete = models.CASCADE)

class Comment
    comment_text = models.TextField()
    comment_datetime = models.DateTimeField(auto_now_add)
    post = models.ForegnKey(Post, on_delete = models.CASCADE)
    user = models.ForegnKey(User, on_delete = models.CASCADE)
    comment_rating = models.IntegerField(default = 0)

    def like_sum(self):
        comment_like = self.comment.like
        return comment_like * self.amount

    def dislike_sum(selfself):
        comment_dislike = self.comment.dislike
        return comment_dislike * self.amount

    def get_rating(self):
        comment_rating = self.comment.rating
        return comment_like-comment.dislike

# Create your models here.
