To Run :
  1. Copy the flaskapp1 file to your system
  2. Read the requirements.txt file and run all the commands 
  3. Open your terminal and go to the flaskapp1 in the terminal
  4. Open the file flaskapp1
  5. Enter in python environment by typing the command :
                    python / python3
                    press ENTER
  6. Type these command in python to create our table in Database: 
                    from flaskwebapp import db
                    press ENTER
                    db.create_all()
                    press ENTER
                    exit()
                    press ENTER
  7. To run the application type the command :
                    python run.py
                    press ENTER
  8. Open your browser and open this link :   http://127.0.0.1:5000/
  
NOTE : Keep in mind you also have to create the database flaskdb in my sql


File Hierarchy or Package Structure :

  flaskapp1
  |_run.py
  |_flaskwebapp
    |_ __init__.py
    |_forms.py
    |_routes.py
    |_models.py
    |_static
    |  |_main.css
    |_templates
       |_layout.html
       |_home.html
       |_addemployee.html
       |_searchresult.html
       
       
