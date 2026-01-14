from django.shortcuts import render, get_object_or_404
from .models import Posts
from django.views.generic import ListView , DetailView
from django.views import View
from django.http import HttpResponseRedirect
from django.urls import reverse
# Create your views here.
from .forms import CommentForm
  
class starting_pageView(ListView):
  template_name = "blog/index.html"
  model = Posts
  ordering = ["-date"]
  context_object_name = "posts"
  
  def get_queryset(self):
      query_set =  super().get_queryset()
      data = query_set[:3]
      return data
  
  
 
class  postsView(ListView):
  template_name = "blog/all-posts.html"
  model = Posts
  context_object_name = "posts"
  
  

class post_detailView(View):
  template_name = "blog/post-detail.html"
  model = Posts
  
  def get(self, request, slug):
    post = Posts.objects.get(slug = slug)
    context = {
      "post":post,
      "post_tags":post.tag.all(),
      "comment_form" : CommentForm()
    }
    return render(request , "blog/post-detail.html" , context)
  
  def post(self, request, slug):
    post = Posts.objects.get(slug = slug)
    comment_form = CommentForm(request.POST)
    if comment_form.is_valid():
      comment =comment_form.save(commit = False)
      comment.post = post
      comment.save()
      return HttpResponseRedirect(reverse("post-detail-page", args=[slug]))
    else:   
      context = {
        "post":post,
        "post_tags":post.tag.all(),
        "comment_form" : CommentForm()
      }
      return render(request , "blog/post-detail.html" , context)
    
  
  
  
  
  
  
  
  
  
  
  
#   int this only get but we need post request
# class post_detailView(DetailView):
#   template_name = "blog/post-detail.html"
#   model = Posts
#   context_object_name = "post"

#   def get_context_data(self, **kwargs):
#      context = super().get_context_data(**kwargs)
#      context["post_tags"]= self.object.tag.all()
#      context["comment_form"] = CommentForm()
#      return context
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
  
 # function based viewss
# def starting_page(request):
#     latest_posts = Posts.objects.all().order_by("-date")[:3]
#     return render(request, "blog/index.html", {
#         "posts": latest_posts ,
#     })

# def posts(request):
#     all_posts= Posts.objects.all().order_by("-date")
#     return render(request, "blog/all-posts.html", {
#       "posts": all_posts
#     })


# def post_detail(request, slug):
    
#     identified_post = get_object_or_404(Posts, slug = slug)
#     return render(request, "blog/post-detail.html", {
#       "post": identified_post,
#       "post_tags": identified_post.tag.all()
#     })