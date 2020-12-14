import markdown
from django.utils.safestring import mark_safe
from django import template
from ..models import Post
from django.db.models import Count

register = template.Library()

# use this function as tag name(@register)  -> html {% load %}

#바로 등록 후 사용가능
@register.simple_tag
def total_posts():
    return Post.published.count()

#등록한 html 파일을 포함해서 사용하는 기능 
@register.inclusion_tag('blog/post/latest_posts.html')
def show_latest_posts(count=5):
    latest_posts = Post.published.order_by('-publish')[:count]
    return {'latest_posts': latest_posts}


@register.simple_tag
def get_most_commented_posts(count=5):
    return Post.published.annotate(total_comments=Count('comments')).order_by('-total_comments')[:count]


@register.filter(name='markdown')
def markdown_format(text):
    return mark_safe(markdown.markdown(text))
    