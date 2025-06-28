from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from .models import Disease
from .forms import DiseaseForm

# Home Page View
def home_view(request):
    return render(request, 'home.html')

# About Page View
def about(request):
    return render(request, 'about.html')

# Disease List View
def disease_list_view(request):
    diseases = Disease.objects.all()
    return render(request, 'disease_list.html', {'diseases': diseases})

# Create a new disease
def disease_create_view(request):
    if request.method == "POST":
        form = DiseaseForm(request.POST)
        if form.is_valid():
            disease = form.save(commit=False)
            # Get symptoms list from POST data
            symptoms = request.POST.getlist('symptoms')
            # Remove empty symptoms
            symptoms = [s for s in symptoms if s.strip()]
            disease.symptoms = symptoms
            disease.save()
            return redirect(reverse('disease_list'))
    else:
        form = DiseaseForm()
    return render(request, 'disease_form.html', {'form': form, 'title': 'Add New Disease', 'disease': None})

# Update an existing disease
def disease_update_view(request, id):
    disease = get_object_or_404(Disease, id=id)
    if request.method == "POST":
        form = DiseaseForm(request.POST, instance=disease)
        if form.is_valid():
            disease = form.save(commit=False)
            symptoms = request.POST.getlist('symptoms')
            symptoms = [s for s in symptoms if s.strip()]
            disease.symptoms = symptoms
            disease.save()
            return redirect(reverse('disease_details', kwargs={'id': disease.id}))
    else:
        form = DiseaseForm(instance=disease)
    return render(request, 'disease_form.html', {'form': form, 'title': f'Update {disease.name}', 'disease': disease})

# Delete a disease
def disease_delete_view(request, id):
    disease = get_object_or_404(Disease, id=id)
    if request.method == "POST":
        disease.delete()
        return redirect(reverse('disease_list'))
    return render(request, 'disease_confirm_delete.html', {'disease': disease})

# Disease Detail View (optional but useful)
def disease_detail_view(request, id):  # add id parameter here
    # Fetch the disease by id
    disease = get_object_or_404(Disease, id=id)
    return render(request, 'disease_details.html', {'disease': disease})


