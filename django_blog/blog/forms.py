from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user
    # POSTFORM
from django import forms
from .models import Post

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'content']

    # COMMENT FORM
    from django import forms
from .models import Comment

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ['content']
    
    # POST FORM UPDATE TO INCLUDE TAG
from taggit.forms import TagField

class PostForm(forms.ModelForm):
    tags = TagField()

    class Meta:
        model = Post
        fields = ['title', 'content', 'tags']

# from django import forms
# from .models import Post, Tag

# class PostForm(forms.ModelForm):
#     tags = forms.CharField(max_length=255)

#     class Meta:
#         model = Post
#         fields = ['title', 'content', 'tags']

#     def clean_tags(self):
#         tags = self.cleaned_data['tags']
#         tag_list = [Tag.objects.get_or_create(name=tag.strip())[0] for tag in tags.split(',')]
#         return tag_list