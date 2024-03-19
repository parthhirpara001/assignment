from django.shortcuts import render

# Create your views here.
def index(requset):
    return render(requset,'index.html')

# Create a new Post object
new_post = index.objects.create(
    title='Sample Post',
    content='This is the content of the post.',
)

# Save the post to the database
new_post.save()