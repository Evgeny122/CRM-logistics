from django.shortcuts import render, redirect
from list_trans.models import Carrier, EditCarrier
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.urls import reverse
from .forms import CarrierModelForm, EditCarrierInTaskForm
from tasks.models import Tasks


    
def all_car(request):
    all_list = Carrier.objects.all()
    context = {'all_list' : all_list}
    return render(request, 'list.html', context)

def detail_car(request, pk):
    try:
        obj = Carrier.objects.get(id=pk)
    except Carrier.DoesNotExist:
        raise Http404
    return render(request, 'list_trans/onecar.html', {'single_obj' : obj})

def delete_car(request, pk):
    try:
        obj = Carrier.objects.get(id=pk)
    except Carrier.DoesNotExist:
        raise Http404
    obj.delete()
    return HttpResponseRedirect(reverse('all_car'))

def create_car(request):
    if request.method == 'POST':
        form = CarrierModelForm(request.POST or None)
        if form.is_valid():
            obj = form.save(commit=False)
            obj.save()
            # return render(request, 'forms.html', {'form':form, 'obj':obj})
            # return redirect(reverse('detail_car', args=[obj.pk]))
            return redirect(f'/allcar/car/{obj.pk}')
    form = CarrierModelForm(request.POST or None)
    return render(request, 'forms.html', {'form':form})

def edit_car(request, pk):
    try:
        obj = Carrier.objects.get(id=pk)
    except Carrier.DoesNotExist:
        raise Http404
    
    if request.method == 'POST':
        form = CarrierModelForm(request.POST, instance=obj)

        if form.is_valid():
            edit_obj = form.save(commit=False)
            edit_obj.save()
    else:
        form = CarrierModelForm(instance=obj)
    
    return render(request, 'edit_car_form.html', {'single_obj': obj, 'form':form})


# def create_car_in_task(request, pk):
#     try:
#         task_obj = Tasks.objects.get(id=pk)
#         editcarrier = False
#     except Tasks.DoesNotExist:
#         raise Http404

#     try:
#         editcarrier = EditCarrier.objects.get(tasks=task_obj)
#     except:
#         pass


#     if request.method == 'POST':
#         if not editcarrier:
#             form = EditCarrierInTaskForm(request.POST)
#             if form.is_valid():
#                 edit_carrier_obj = form.save(commit=False)
#                 edit_carrier_obj.tasks = task_obj
#                 edit_carrier_obj.save()
#                 return redirect(reverse('detail_tasks', args={task_obj.pk}))
#         else:
#             form = EditCarrierInTaskForm(request.POST, instance=editcarrier)
#             if form.is_valid():
#                 edit_carrier_obj = form.save(commit=False)
#                 edit_carrier_obj.save()
#                 return redirect(reverse('detail_tasks', args={task_obj.pk}))
#     else:
#         if not editcarrier:
#             form = EditCarrierInTaskForm(request.POST)
#             return render(request, 'list_trans/editcarrier.html', {'form' : form})
#         else:
#             form = EditCarrierInTaskForm(request.POST, instance=editcarrier)
#             return render(request, 'list_trans/editcarrier.html', {'form' : form})

def create_car_in_task(request, pk):
    try:
        task_obj = Tasks.objects.get(id=pk)
        editcarrier = False
    except Tasks.DoesNotExist:
        raise Http404

    try:
        editcarrier = EditCarrier.objects.get(tasks=task_obj)
        if request.method == 'POST':
            form = EditCarrierInTaskForm(request.POST, instance=editcarrier)
            if form.is_valid():
                edit_carrier_obj = form.save(commit=False)
                edit_carrier_obj.save()
                return render(request, 'list_trans/editcarrier.html', {'form' : form, 'single_carrier' : editcarrier, 'task' : task_obj})
        form = EditCarrierInTaskForm(instance=editcarrier)
        return render(request, 'list_trans/editcarrier.html', {'form' : form, 'single_carrier' : editcarrier, 'task' : task_obj})
    
    except:
        if request.method == 'POST':
            form = EditCarrierInTaskForm(request.POST)
            if form.is_valid():
                edit_carrier_obj = form.save(commit=False)
                edit_carrier_obj.tasks = task_obj
                edit_carrier_obj.save()
                return render(request, 'list_trans/editcarrier.html', {'form' : form, 'single_carrier' : editcarrier, 'task' : task_obj})
        form = EditCarrierInTaskForm()
        return render(request, 'list_trans/editcarrier.html', {'form' : form, 'single_carrier' : editcarrier, 'task' : task_obj})


            


    






    




