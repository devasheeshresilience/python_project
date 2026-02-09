from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .models import Task
from django.views.decorators.http import require_POST

@login_required(login_url='login')
def dashboard_view(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        if title and description:
            Task.objects.create(user=request.user, title=title, description=description)
            return redirect('dashboard')
            
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'dashboard/dashboard.html', {'tasks': tasks})

@login_required(login_url='login')
@require_POST
def delete_task(request, task_id):
    task = get_object_or_404(Task, id=task_id, user=request.user)
    task.delete()
    return redirect('dashboard')

@login_required(login_url='login')
def edit_task(request, task_id):
    task = Task.objects.filter(id=task_id, user=request.user).first()
    if not task:
        return redirect('dashboard')
    
    if request.method == 'POST':
        title = request.POST.get('title')
        description = request.POST.get('description')
        
        if title and description:
            task.title = title
            task.description = description
            task.save()
            return redirect('dashboard')
    
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'dashboard/dashboard.html', {'tasks': tasks, 'edit_task': task})