from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import UserCreationForm
from .models import Blog, BlogAuthor, BlogComment

def home(request):
    num_posts = Blog.objects.count()
    num_authors = BlogAuthor.objects.count()
    
    context = {
        "num_posts": num_posts,
        "num_authors":num_authors
    }
    
    return render(request, 'blog/home.html', context)

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/blog_list.html'
    paginate_by = 5

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/blog_details.html'

class BlogCommentCreate(LoginRequiredMixin, CreateView): 
    model = BlogComment
    template_name = 'blog/create_comment.html'
    fields = ['description', ]
    
    def get_context_data(self, **kwargs):
        context = super(BlogCommentCreate, self).get_context_data(**kwargs)
        context['blog'] = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return context
    
    def form_valid(self, form):
        form.instance.author = self.request.user
        form.instance.blog = get_object_or_404(Blog, pk=self.kwargs['pk'])
        return super(BlogCommentCreate, self).form_valid(form)
    
    def get_success_url(self):
        return reverse('blog-detail', kwargs={'pk': self.kwargs['pk']})

class BloggersListView(ListView):
    model = BlogAuthor
    paginate_by = 5
    template_name = 'blog/blogger_list.html'

class BloggersDetails(ListView):
    model = Blog
    paginate_by = 5
    template_name = 'blog/blogger_detail.html'

    def get_queryset(self):
        target_author = get_object_or_404(BlogAuthor, pk=self.kwargs['pk'])
        return Blog.objects.filter(author=target_author)
    
    def get_context_data(self, **kwargs):
        context = super(BloggersDetails, self).get_context_data(**kwargs)
        context['blogger'] = get_object_or_404(BlogAuthor, pk=self.kwargs['pk'])
        return context

def signup(request):
    if request.method == "POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form  = UserCreationForm()
    return render(request, 'blog/signup.html', {'form':form})
