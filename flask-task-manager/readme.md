1. Open the folder to have your project on VScode
2. Run following commands on terminal
3.     pip3 install virtualenv
4.     python3 -m virtualenv env # for creating env in the folder.
Some syntax for template inheritance
1.      {% block head %} {% endblock head %} # for write code parts like if/else for loops statements
2.      {{ code }} # gives you the result of the code as a string
3.      href = {{ url_for('static', filename="css/main.css") }} # in filename you show mention all the subdirectories to reach the file

