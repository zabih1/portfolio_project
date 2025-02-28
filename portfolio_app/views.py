from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Profile, Skill, Technology, Education, Experience, Project
from .models import Message as ContactMessage

def home(request):
    profile = Profile.objects.first()
    return render(request, 'home.html', {'profile': profile})

def about(request):
    profile = Profile.objects.first()
    return render(request, 'about.html', {'profile': profile})

def skills(request):
    technical_skills = Skill.objects.filter(skill_type='technical')
    professional_skills = Skill.objects.filter(skill_type='professional')
    technologies = Technology.objects.all()
    
    context = {
        'technical_skills': technical_skills,
        'professional_skills': professional_skills,
        'technologies': technologies,
    }
    
    return render(request, 'skills.html', context)

def resume(request):
    education_list = Education.objects.all().order_by('order')
    experience_list = Experience.objects.all().order_by('order')
    
    context = {
        'education_list': education_list,
        'experience_list': experience_list,
    }
    
    return render(request, 'resume.html', context)

def projects(request):
    featured_projects = Project.objects.filter(featured=True)
    all_projects = Project.objects.all()
    
    context = {
        'featured_projects': featured_projects,
        'all_projects': all_projects,
    }
    
    return render(request, 'projects.html', context)

def contact(request):
    return render(request, 'contact.html')

def send_message(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        email = request.POST.get('email')
        subject = request.POST.get('subject')
        message_text = request.POST.get('message')
        
        # Create new message
        message = ContactMessage(
            name=name,
            email=email,
            subject=subject,
            message=message_text
        )
        message.save()
        
        # Add success message
        messages.success(request, 'Your message has been sent successfully!')
        return redirect('contact')
    
    return redirect('contact')