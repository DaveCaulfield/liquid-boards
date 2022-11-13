from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Blog
from .forms import CommentForm


class BlogList(generic.ListView):
    """
    display list of all blog posts
    """
    model = Blog
    queryset = Blog.objects.all().order_by('-created_on')
    template_name = 'blog/blog.html'
    paginate_by = 3


class BlogDetail(View):
    """
    display blog post details 
    """

    def get(self, request, slug, *args, **kwargs):
        """
        get the blog post, check for comments and likes
        """
        queryset = Blog.objects
        blog = get_object_or_404(queryset, slug=slug)
        comments = blog.comments.order_by('created_on')
        liked = False
        if blog.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "blog/blog_detail.html",
            {
                "blog": blog,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()    
            },
        )

    def post(self, request, slug, *args, **kwargs):
        """
        get the blog post, check for comments and likes
        """
        queryset = Blog.objects
        blog = get_object_or_404(queryset, slug=slug)
        comments = blog.comments.order_by('created_on')
        liked = False
        if blog.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)

        if comment_form.is_valid():
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.blog = blog
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "blog/blog_detail.html",
            {
                "blog": blog,
                "comments": comments,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )


class BlogLike(View):
    """
    Blog like feature
    """

    def post(self, request, slug, *args, **kwargs):
        """
        toggle likes on/off. two options.
        if user has liked a blog post then remove like.
        if user has not a blog post the add like.
        """
        blog = get_object_or_404(Blog, slug=slug)

        if blog.likes.filter(id=request.user.id).exists():
            blog.likes.remove(request.user)
            messages.success(request, 'You removed your Like from this blog post')
        else:
            blog.likes.add(request.user)
            messages.success(request, 'You added a Like to this blog post')

        return HttpResponseRedirect(reverse('blog_detail', args=[slug]))