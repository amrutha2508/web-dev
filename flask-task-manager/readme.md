## Flask-task-manager
<img width="337" height="278" alt="image" src="https://github.com/user-attachments/assets/90696d28-5778-4f73-bf6c-59eb19e043c7" />


1. Open the folder to have your project on VScode
2. Run following commands on terminal
3.     pip3 install virtualenv
4.     python3 -m virtualenv env # for creating env in the folder.
5.     source env/bin/activate # to activate the env
6.     pip3 install flask flask-sqlalchemy
Some syntax for template inheritance
1.      {% block head %} {% endblock head %} # for write code parts like if/else for loops statements
2.      {{ code }} # gives you the result of the code as a string
3.      href = {{ url_for('static', filename="css/main.css") }} # in filename you show mention all the subdirectories to reach the file

