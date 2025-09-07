from django.shortcuts import render, redirect, get_object_or_404
from .models import Employee   # Importation du modèle Employee
from .forms import EmployeeForm  # Importation du formulaire Employee

def list_employees(request):
    """Vue pour afficher la liste de tous les employés"""
    employes = Employee.objects.all()  # Récupère tous les employés de la base de données
    return render(request, "employee/list.html", {"employes": employes})  # Rend le template avec les données

def add_employee(request):
    """Vue pour ajouter un nouvel employé"""
    if request.method == "POST":  # Si le formulaire est soumis
        form = EmployeeForm(request.POST)  # Crée un formulaire avec les données POST
        if form.is_valid():  # Vérifie si les données sont valides
            form.save()  # Sauvegarde l'employé dans la base de données
            return redirect("list_employees")  # Redirige vers la liste des employés
    else:  # Si c'est une requête GET (affichage initial)
        form = EmployeeForm()  # Crée un formulaire vide
    return render(request, "employee/formulaire.html", {"form": form})  # Affiche le formulaire

def edit_employee(request, id):
    """Vue pour modifier un employé existant"""
    employee = get_object_or_404(Employee, id=id)  # Récupère l'employé ou renvoie 404 si non trouvé
    if request.method == "POST":  # Si le formulaire est soumis
        form = EmployeeForm(request.POST, instance=employee)  # Crée un formulaire avec les données et l'instance
        if form.is_valid():  # Vérifie si les données sont valides
            form.save()  # Sauvegarde les modifications
            return redirect("list_employees")  # Redirige vers la liste
    else:  # Si c'est une requête GET
        form = EmployeeForm(instance=employee)  # Crée un formulaire pré-rempli avec les données de l'employé
    return render(request, "employee/formulaire.html", {"form": form})  # Affiche le formulaire de modification

def delete_employee(request, id):   
    employee = get_object_or_404(Employee, id=id)
    if request.method == "POST":
        employee.delete()
        return redirect("list_employees")
    return render(request, "employee/confirm_delete.html", {"employee": employee})