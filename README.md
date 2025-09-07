#  Employee Management System  

##  Overview  
The Employee Management System (EMS) is a web application developed for **Alton**, which is a consulting firm in management and information systems, using **Django**.  
It streamlines the management of employee records by providing a user-friendly interface to add, update, view, and delete employee information.  
This solution enhances efficiency for Alton's HR department, offering a practical and organized way to manage employee data for small to medium-sized teams.
  

---

##  Technologies  
- **Backend**: Python 3.13.5, Django 5+  
- **Database**: SQLite (default, easily replaceable with PostgreSQL or MySQL)  
- **Frontend**: HTML5, DaisyUI, Tailwind CSS  
  
---

##  Architecture (MVT)  
The project follows the **MVT (Model–View–Template)** design pattern:
  
  <img width="5704" height="1895" alt="Image" src="https://github.com/user-attachments/assets/ee42827a-e771-4ac7-a752-617a177ff73a" /> 

- **Model**: Manages the data and business logic. It defines the structure of the database (fields, relationships, validations, constraints, etc.) and provides an interface to interact with the data.

- **View**: Acts as the connector between the model and the template. It receives the user’s request, applies the necessary logic (processing, fetching data, redirection, etc.), and passes the relevant information to the template.

- **Template**: Represents the presentation layer. It is the HTML part that displays the data provided by the view, with Django template tags to dynamically insert content.

- **How It Works**:
A user's request first arrives at the **URL dispatcher**, which maps the incoming URL to the appropriate **View** function or class.  
The **View** processes the request and, if necessary, interacts with the **Model** to retrieve or update data in the database.  
Once the required data is prepared, the **View** passes it to a **Template**.  
Finally, the **Template** renders the data into an **HTML response**, which is returned to the user's browser.

---

##  Project Structure

```plaintext
employee_project/              # Projet principal Django
│
├── employee/                  # Application "employee"
│   ├── migrations/            # Fichiers de migration (base de données)
│   ├── templates/employee/    # Templates HTML
│   │   ├── base.html          # Template de base
│   │   ├── list.html          # Liste des employés
│   │   ├── formulaire.html    # Formulaire (ajout/modif)
│   │   └── confirm_delete.html# Confirmation suppression
│   │
│   ├── __init__.py
│   ├── admin.py               # Configuration Django admin
│   ├── apps.py                # Configuration de l’application
│   ├── forms.py               # Formulaires (ModelForm)
│   ├── models.py              # Modèle Employee
│   ├── tests.py               # Tests unitaires
│   ├── urls.py                # Routes de l’app Employee
│   └── views.py               # Logique (CRUD : Create, Read, Update, Delete)
│
├── employee_project/          # Répertoire principal du projet
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py            # Configuration générale du projet
│   ├── urls.py                # Routes principales
│   └── wsgi.py
│
├── db.sqlite3                 # Base de données SQLite
├── manage.py                  # Script de gestion Django
└── venv/                      # Environnement virtuel
```
---

##  Installation and Execution

### 1. Create and activate a virtual environment
- python -m venv venv 
- venv\Scripts\activate  

### 2. Install dependencies
- pip install django

### 3. Apply migrations (create the database)
- python manage.py makemigrations  
- python manage.py migrate

### 4. Create a superuser
- python manage.py createsuperuser 

### 5. Start the server
- python manage.py runserver

## Screenshots

### Home Page
![Image](https://github.com/user-attachments/assets/c32e17c8-4f5e-42c9-b445-aee374870e90)

### Add Employee
![Image](https://github.com/user-attachments/assets/73d4b71d-aa0b-4d81-b61e-1ffee4ba471d)

### Employee List
![Image](https://github.com/user-attachments/assets/ced1f4b9-56bc-4810-bce3-e66a861baa70)

### Edit Employee
![Image](https://github.com/user-attachments/assets/e41739a1-29cf-4654-9f3e-08fc67abdda5)

### Delete Employee
![Image](https://github.com/user-attachments/assets/f230c37f-fa56-4f9e-a5aa-4ba0e393202c)

### final list
![Image](https://github.com/user-attachments/assets/406833a2-f402-43b5-9865-0ac23282ef16)
