# Django Auth System

A Django application enabling signup and login for two types of users—**Doctor** and **Patient**. After login, each user is redirected to their respective dashboard displaying the signup details.

---

## Features

### 🔑 Authentication System (Task 1)
- User Registration with role selection (**Patient** or **Doctor**)  
- Secure Login and Logout functionality  
- Upload profile picture during registration  
- Password & Confirm Password match validation  
- Dashboard shows all details filled in the signup form  
- Role-based redirection after login (**Patient Dashboard** / **Doctor Dashboard**)

---

## Signup Form Fields

- First Name  
- Last Name  
- Profile Picture  
- Username  
- Email ID  
- Password  
- Confirm Password  
- Address (Line1, City, State, Pincode)  
- User Type (Patient / Doctor)

---

## Folder Structure

auth_system/
│ manage.py
│ db.sqlite3
│
├── auth_system/
│ ├── init.py
│ ├── asgi.py
│ ├── settings.py
│ ├── urls.py
│ └── wsgi.py
│
├── users/
│ ├── init.py
│ ├── admin.py
│ ├── apps.py
│ ├── forms.py
│ ├── migrations/
│ ├── models.py
│ ├── tests.py
│ ├── urls.py
│ ├── views.py
│ └── templates/
│ └── users/
│ ├── doctor_dashboard.html
│ ├── home.html
│ ├── login.html
│ ├── patient_dashboard.html
│ └── signup.html
├── media/


---

## How to Run

1. **Clone the repository**

    ```
    git clone https://github.com/Vikasprajapat1602/ATG_Task.git
    cd auth_system
    ```

2. **Apply Migrations**

    ```
    python manage.py migrate
    ```

3. **Create superuser (optional, for admin access)**

    ```
    python manage.py createsuperuser
    ```

4. **Run Server**

    ```
    python manage.py runserver
    ```

5. **Open in browser**  
    [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## Usage

- **Register:** Go to `/register/` and fill all the required fields, upload a profile picture, select your user type.  
- **Login:** Go to `/login/` and login with your credentials.
- **Dashboard:** After login, you are redirected to either:  
    - `/patient/dashboard/` (for Patients)  
    - `/doctor/dashboard/` (for Doctors)  
- **Dashboard** shows all your information given at signup.

---

## Checks/Validations

- Password and Confirm Password fields must match during registration.  
- All fields except profile picture are required for signup.  
- Only authenticated users can access dashboards.

---
