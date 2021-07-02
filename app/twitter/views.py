import django
from django.core.checks import messages
from django.http.response import HttpResponse, HttpResponseRedirect
from django.views.generic import ListView, FormView, CreateView, UpdateView, View
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib import messages

from .models import Tweet
from .forms import TweetForm

class IndexView(LoginRequiredMixin, ListView):

    template_name = 'twitter/index.html'
    context_object_name = 'tweets'
    queryset = Tweet.objects.filter(is_sent=False, is_deleted=False)

index = IndexView.as_view()


class FormViewBase(LoginRequiredMixin, FormView):

    model = Tweet
    template_name = 'twitter/form.html'
    success_url = reverse_lazy('twitter:index')
    form_class = TweetForm
    message = ''

    def form_valid(self, form):
        tweet = form.save(commit=False)
        tweet.user_id = self.request.user.id
        tweet.save()
        messages.success(self.request, self.message)
        return super().form_valid(form)


class TweetCreateView(FormViewBase):

    message = 'ツイートを予約しました'

create = TweetCreateView.as_view()


class TweetUpdateView(FormViewBase, UpdateView):

    message = '予約ツイート内容を変更しました'

update = TweetUpdateView.as_view()


class TweetDeleteView(LoginRequiredMixin, View):

    success_url = reverse_lazy('twitter:index')
    message = '予約ツイートを削除しました'

    def get(self, request, *args, **kwargs):
        tweet_id = kwargs.get('pk')
        tweet = Tweet.objects.get(id=tweet_id)
        tweet.is_deleted = True
        tweet.save()
        messages.success(self.request, self.message)
        return HttpResponseRedirect(self.success_url)

delete = TweetDeleteView.as_view()