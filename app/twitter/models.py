from django.db import models
from django.contrib.auth import get_user_model


class Tweet(models.Model):

    user = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, verbose_name='投稿者')
    text = models.TextField(verbose_name='ツイート本文')
    img = models.ImageField(upload_to='image', null=True, blank=True, verbose_name='ツイート画像')
    is_sent = models.BooleanField(default=False, verbose_name='送信済みフラグ')
    is_deleted = models.BooleanField(default=False, verbose_name='削除フラグ')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='作成日時')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='更新日時')
    tweeted_at = models.DateTimeField(null=True, verbose_name='ツイート予定日時')

    def __str__(self):
        return self.text

    class Meta:
        verbose_name_plural = 'ツイート'
