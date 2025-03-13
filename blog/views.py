from django.shortcuts import render, redirect
from django.core.mail import EmailMessage
from django.http import HttpResponse, Http404
from django.urls import reverse
from .models import Category, Post, AboutUs
import logging
from django.core.paginator import Paginator
from .forms import ContactForm

def index(request):
    blog_title = "Recent Recipes"
    # Fetching posts
    all_posts = Post.objects.filter(is_published=True).order_by('-created_at')
    print("Total Posts:", all_posts.count())  # Debugging line
    for post in all_posts:
        print(post.title)  # Print post titles to check

    # Pagination
    paginator = Paginator(all_posts, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    print("Total Pages:", paginator.num_pages)  # Debugging line
    print("Current Page:", page_obj.number)  # Debugging line

    return render(request, 'blog/index.html', {'blog_title': blog_title, 'page_obj': page_obj})

def search(request):
    query = request.GET.get('q', '')
    results = Post.objects.filter(title__icontains=query) if query else []  # Use Post instead of BlogPost
    return render(request, 'blog/search_results.html', {'query': query, 'results': results})

def detail(request, slug):
    try:
        # getting data from model by post id
        post = Post.objects.get(slug=slug)
        related_posts  = Post.objects.filter(category = post.category).exclude(pk=post.id)

    except Post.DoesNotExist:
        raise Http404("Post Does not Exist!")

    # logger = logging.getLogger("TESTING")
    # logger.debug(f'post variable is {post}')=
    return render(request,'blog/detail.html', {'post': post, 'related_posts':related_posts})

def about(request):
    about_content = AboutUs.objects.first()
    if about_content is None or not about_content.content:
        about_content = (
            "Welcome to Mona's BakeBook! 🍰✨ "
            "Your go-to place for delightful recipes, baking tips, and sweet inspirations. "
            "Join us on this delicious journey and bake something magical today! 🎂💕"
        )  # Updated default content
    else:
        about_content = about_content.content
        
    return render(request, 'blog/about.html', {'about_content': about_content})


from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.conf import settings
import logging
from .forms import ContactForm  # Assuming you have a ContactForm

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        logger = logging.getLogger("TESTING")
        if form.is_valid():
            # Log the form data
            logger.debug(f'POST Data is {form.cleaned_data["name"]} {form.cleaned_data["email"]} {form.cleaned_data["message"]}')
            
            # Send an email
            subject = f"New Contact Form Submission from {form.cleaned_data['name']}"
            message = f"""
            Name: {form.cleaned_data['name']}
            Email: {form.cleaned_data['email']}
            Message: {form.cleaned_data['message']}
            """
            sender_email = form.cleaned_data['email']
            recipient_email = settings.DEFAULT_FROM_EMAIL  # Use your email or a configured email in settings.py

            try:
                send_mail(
                    subject=subject,
                    message=message,
                    from_email=sender_email,
                    recipient_list=[recipient_email],
                    fail_silently=False,
                )
                logger.debug("Email sent successfully")
            except Exception as e:
                logger.error(f"Failed to send email: {e}")

            # Redirect to the success page
            return redirect('blog:success')  # Use the URL name for the success page
        else:
            logger.debug('Form validation failure')
            return render(request, 'blog/contact.html', {'form': form, 'name': name, 'email': email, 'message': message})
    
    # For GET requests, render the contact form
    return render(request, 'blog/contact.html')

def success(request):
    # Render the success.html template
    return render(request, 'blog/success.html')