from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.db.models import Q
from django.views import generic, View
from django.http import HttpResponseRedirect
from .models import Blog, Comment
from profiles.models import UserProfile, User
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
            messages.success(request, 'Your comment has been added ')

            return HttpResponseRedirect(reverse('blog_detail', args=[slug]))
          
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


@login_required
def edit_comment(request, comment_id):
    """
    Edit a comment
    """
    
    comment = get_object_or_404(Comment, pk=comment_id)
    if request.method == 'POST':
        form = CommentForm(request.POST, instance=comment)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your comment has been \
            successfully updated.')
            return redirect(
                reverse('blog_detail', args=(comment.blog.slug,)))

        else:
            messages.error(request, 'Please try again.')
    else:
        form = CommentForm(instance=comment)

    template = "blog/edit_comment.html"
    context = {
        "form": form,
        "comment": comment,
        "blog": comment.blog,
    }

    return render(request, template, context)


# @login_required
# def delete_comment(request, comment_id):
#     """
#     Delete a blog comment
#     """
#     comment = get_object_or_404(Comment, pk=comment_id)

#     if request.user == comment.commenter or request.user.is_superuser:
#         comment.delete()
#         messages.info(request, "Comment deleted!")
#         return redirect(reverse("blog_detail", args=[comment.blog.slug]))
#     else:
#         messages.error(
#             request,
#             "Only shop owner and comment author can do that.")
#         return redirect(reverse("blog_detail", args=[comment.blog.slug]))


@login_required
def delete_comment(request, comment_id):
    """
    Delete a blog comment
    """
    comment = get_object_or_404(Comment, pk=comment_id)


    comment.delete()
    messages.info(request, "Comment deleted!")
    return redirect(reverse("blog_detail", args=[comment.blog.slug]))
   