# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth import login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm
from .forms import CustomUserCreationForm

def user_register(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = CustomUserCreationForm()
    return render(request, 'blog/register.html', {'form': form})

def user_login(request):
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = AuthenticationForm()
    return render(request, 'blog/login.html', {'form': form})

def user_logout(request):
    logout(request)
    return redirect('login')

@login_required
def user_profile(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(instance=request.user, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('profile')
    else:
        form = CustomUserCreationForm(instance=request.user)
    return render(request, 'blog/profile.html', {'form': form})

# CRUD OPERATIONS
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Post
from .forms import PostForm

class PostListView(ListView):
    model = Post
    template_name = 'blog/post_list.html'
    context_object_name = 'posts'
    ordering = ['-published_date']  # Show most recent posts first

class PostDetailView(DetailView):
    model = Post
    template_name = 'blog/post_detail.html'
    context_object_name = 'post'

class PostCreateView(LoginRequiredMixin, CreateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

    def form_valid(self, form):
        form.instance.author = self.request.user
        return super().form_valid(form)

class PostUpdateView(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Post
    form_class = PostForm
    template_name = 'blog/post_form.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author

class PostDeleteView(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Post
    template_name = 'blog/post_confirm_delete.html'
    success_url = reverse_lazy('post_list')

    def test_func(self):
        post = self.get_object()
        return self.request.user == post.author
    
                # CRUD operations for comments
from django.views.generic import CreateView, UpdateView, DeleteView
from django.shortcuts import get_object_or_404
from .models import Comment, Post
from .forms import CommentForm

class CommentCreateView(CreateView):
    model = Comment
    form_class = CommentForm

    def form_valid(self, form):
        post = get_object_or_404(Post,
    pk=self.kwargs['post_pk'])
        form.instance.post = post
        form.instance.author = self.request.user
        return super().form_valid(form)

class CommentUpdateView(UpdateView):
    model = Comment
    form_class = CommentForm

    def get_success_url(self):
        return self.object.post.get_absolute_url()

class CommentDeleteView(DeleteView):
    model = Comment

    def get_success_url(self):
        return self.object.post.get_absolute_url()
    
    "SEARCH VIEW"
# blog/views.py
from django.db.models import Q
from django.shortcuts import render
from .models import Post

def search_posts(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(
            Q(title__icontains=query) |
            Q(content__icontains=query) |
            Q(tags__name__icontains=query)
        ).distinct()
    else:
        posts = Post.objects.none()
    return render(request, 'blog/search_results.html', {'posts': posts, 'query': query})


# class PostDetailView(DetailView):
#     model = Post
#     template_name = 'blog/post_detail.html'

#     def get_context_data(self, **kwargs):
#         context = super().get_context_data(**kwargs)
#         context['comment_form'] = CommentForm()
#         context['comments'] = self.object.comments.all()
#         return context
# "CommentCreateView"
# @login_required
# def add_comment(request, post_id):
#     post = get_object_or_404(Post, id=post_id)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.post = post
#             comment.author = request.user
#             comment.save()
#             return redirect(reverse('post_detail', args=[post_id]))
#     return redirect(reverse('post_detail', args=[post_id]))

# "CommentUpdateView"
# @login_required
# def edit_comment(request, comment_id):
#     comment = get_object_or_404(Comment, id=comment_id)
#     if request.user != comment.author:
#         return redirect('post_detail', pk=comment.post.pk)
#     if request.method == 'POST':
#         form = CommentForm(request.POST, instance=comment)
#         if form.is_valid():
#             form.save()
#             return redirect(reverse('post_detail', args=[comment.post.id]))
#     else:
#         form = CommentForm(instance=comment)
#     return render(request, 'blog/edit_comment.html', {'form': form})

# "CommentDeleteView"
# @login_required
# def delete_comment(request, comment_id):
#     comment = get_object_or_404(Comment, id=comment_id)
#     if request.user == comment.author:
#         post_id = comment.post.id
#         comment.delete()
#         return redirect(reverse('post_detail', args=[post_id]))
#     return redirect('post_detail', pk=comment.post.pk)