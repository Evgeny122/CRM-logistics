from django.shortcuts import render, redirect
from tasks.models import Tasks, Comments, Likes, Dnot_likes
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from tasks.forms import AddTasksForm, CommentsForm
from datetime import datetime
from list_trans.models import EditCarrier


def index(request):
    current_date = datetime.now().strftime('%H:%M:%S')
    all_list = Tasks.objects.all() 
    return render(request, 'index.html', {"all_list" : all_list, 'current_date' : current_date})

def all_tasks(request):
    all_list = Tasks.objects.all()
    context = {'all_list' : all_list}
    return render(request, 'list_tasks.html', context)

def detail_tasks(request, pk):
    try:
        obj = Tasks.objects.get(id=pk)
    except Tasks.DoesNotExist:
        raise Http404
    
    try:
        editcarrier = EditCarrier.objects.get(tasks=obj)

        profit = obj.price_client - editcarrier.price_carrier
        return render(request, 'detail_task.html', {'single_obj':obj, 'single_carrier':editcarrier, 'profit' : profit})
    except:
        profit = 0
        return render(request, 'detail_task.html', {'single_obj':obj, 'profit' : profit})

def delete_task(request, pk):
    try:
        obj = Tasks.objects.get(id=pk)
        all_commentary = obj.commentary.all()
        all_like = obj.likes.all()
        all_dnot_like = obj.dnot_likes.all()
    except Tasks.DoesNotExist:
        raise Http404
    all_dnot_like.delete()
    all_like.delete()
    all_commentary.delete()
    obj.delete()
    return HttpResponseRedirect(reverse('all_tasks'))

def create_task(request):
    if request.method == 'POST':
        form = AddTasksForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.author = request.user
            obj.save()
            return redirect(reverse('detail_tasks', args={obj.pk}))
    form = AddTasksForm(request.POST or None)
    return render(request, 'forms.html', {'form' : form})
    
def edit_task(request, pk):
    try:
        obj = Tasks.objects.get(id=pk)
    except Tasks.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        form = AddTasksForm(request.POST, instance=obj)
        if form.is_valid():
            edit_obj = form.save(commit=False)
            edit_obj.save()
            return redirect(reverse('detail_tasks', args={obj.pk}))
    else:
        form = AddTasksForm(instance=obj)
    return render(request ,'edit_task.html', {'single_obj':obj, 'form':form})

def comments_view(request, pk):
    form = CommentsForm(request.POST or None)
    try:
        task_obj = Tasks.objects.get(id=pk)
    except Tasks.DoesNotExist:
        raise Http404
    if form.is_valid():
        text = form.cleaned_data.get('text')
        user = request.user
        comments_obj = Comments(user=user, text=text)
        comments_obj.save()
        task_obj.commentary.add(comments_obj)
        task_obj.save()
        return redirect(reverse('comments_view', args={task_obj.pk}))
    return render (request, 'comments.html', {'single_object' : task_obj, 'form': form})

def comments_edit(request, pk, pk1):
    try:
        task_obj = Tasks.objects.get(id=pk)
        comments_obj = Comments.objects.get(id=pk1)
    except Comments.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        form = CommentsForm(request.POST, instance=comments_obj)
        if form.is_valid():
            edit_com = form.save(commit=False)
            edit_com.save()
            return redirect(reverse('comments_view', args={task_obj.pk}))
    else:
        form = CommentsForm(instance=comments_obj)  
    return render (request, 'edit_comments.html', {'single_object' : comments_obj, 'form': form})

def comments_delete(request, pk):
    try:
        comments_obj = Comments.objects.get(id=pk)
    except Comments.DoesNotExist:
        raise Http404
    comments_obj.delete()
    return redirect(('/'))

def likes_view(request, pk):
    try:
        obj = Tasks.objects.get(id=pk)
    except Tasks.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        user = request.user
        if not obj.likes.filter(user=user):
            like_obj = Likes(user=user, like=True)
            like_obj.save()
            obj.likes.add(like_obj)
            obj.save()
            if obj.dnot_likes.filter(user=user):
                obj.dnot_likes.filter(user=user).delete()
        else:
            pass      
    return redirect(('/'))

def dnot_likes_view(request, pk):
    try:
        obj = Tasks.objects.get(id=pk)
    except Tasks.DoesNotExist:
        raise Http404
    if request.method == 'POST':
        user = request.user
        if not obj.dnot_likes.filter(user=user):
            dnot_like_obj = Dnot_likes(user=user, dnot_like=True)
            dnot_like_obj.save()
            obj.dnot_likes.add(dnot_like_obj)
            obj.save()
            if obj.likes.filter(user=user):
                obj.likes.filter(user=user).delete()
        else:
            pass
    return redirect(('/'))


