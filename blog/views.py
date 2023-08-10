from django.shortcuts import render
from datetime import date

all_posts = [
    {
        "slug": "hike-in-the-mountains",
        "image": "mountains.jpg",
        "author": "Tanvi",
        "date": date(2023,8,10),
        "title":"Mountain Hiking",
        "excerpt":"There's nothing like the views you get when hiking in the mountains! And I wasn't even prepared for what happened whilst I was enjoying the view!",
        "content": """ 
         Lorem ipsum dolor sit amet consectetur adipisicing elit. Sequi nam 
         impedit omnis atque perferendis solutaamet
         ? Hic dolorem a praesentium adipisci autem sit,
         voluptatum perferendis pariatur aperiam eveniet odio illum.
        """


    },
    {
        "slug": "programming-is-fun",
        "image": "coding.jpg",
        "author": "Tanvi",
        "date": date(2023,3,10),
        "title":"Programming is great",
        "excerpt":"Did you ever spend hours searching that one error in code?",
        "content": """ 
         Lorem ipsum dolor sit amet consectetur adipisicing elit. Sequi nam 
         impedit omnis atque perferendis solutaamet
         ? Hic dolorem a praesentium adipisci autem sit,
         voluptatum perferendis pariatur aperiam eveniet odio illum.

         Lorem ipsum dolor sit amet consectetur adipisicing elit. Sequi nam 
         impedit omnis atque perferendis solutaamet
         ? Hic dolorem a praesentium adipisci autem sit,
         voluptatum perferendis pariatur aperiam eveniet odio illum.
        """


    },
    {
        "slug": "into-the-woods",
        "image": "woods.jpg",
        "author": "Tanvi",
        "date": date(2023,10,10),
        "title":"Nature at it's best",
        "excerpt":"Nature is amazing! The amount of inspiration I get when walking into nature",
        "content": """ 
         Lorem ipsum dolor sit amet consectetur adipisicing elit. Sequi nam 
         impedit omnis atque perferendis solutaamet
         ? Hic dolorem a praesentium adipisci autem sit,
         voluptatum perferendis pariatur aperiam eveniet odio illum.
         """
    }
]

# Create your views here.
def get_date(post):
    return post['date']


def starting_page(request):
    sorted_posts = sorted(all_posts, key=get_date)
    latest_posts = sorted_posts[-3:]
    return render(request,"blog/index.html",{
        "posts":latest_posts
    })


def posts(request):
    return render(request,"blog/all-posts.html",{
      "all_posts":all_posts 
    })

def post_detail(request,slug):
    identified_post = next(post for post in all_posts if post['slug'] == slug)
    return render(request,"blog/post-detail.html",{
        "post":identified_post
    })