#  Employee Management System  

##  Overview  
The **Employee Management System (EMS)** is a web application built with **Django** that simplifies employee record management.  
It provides a user-friendly interface to **add, update, view, and delete employee data**, making it an efficient solution for HR departments and small companies.  

---

##  Technologies  
- **Backend**: Python 3.13.5, Django 5+  
- **Database**: SQLite (default, easily replaceable with PostgreSQL or MySQL)  
- **Frontend**: HTML5, DaisyUI, Tailwind CSS / Bootstrap  
  

---

##  Architecture (MVT)  
The project follows the **MVT (Model–View–Template)** design pattern:
  
<img width="5704" height="1895" alt="Image" src="https://github.com/user-attachments/assets/ee42827a-e771-4ac7-a752-617a177ff73a" /> 

- **Model**: Manages the data and business logic. It defines the structure of the database (fields, relationships, validations, constraints, etc.) and provides an interface to interact with the data.

- **View**: Acts as the connector between the model and the template. It receives the user’s request, applies the necessary logic (processing, fetching data, redirection, etc.), and passes the relevant information to the template.

- **Template**: Represents the presentation layer. It is the HTML part that displays the data provided by the view, with Django template tags to dynamically insert content.

How they interact:
A user's request first arrives at the URL dispatcher, which maps the incoming URL to the appropriate View function or class.
The View processes the request and, if necessary, interacts with the Model to retrieve or update data in the database.
Once the required data is prepared, the View passes it to a Template.
Finally, the Template renders the data into an HTML response, which is returned to the user's browser.
---

## 📂 Project Structure  
