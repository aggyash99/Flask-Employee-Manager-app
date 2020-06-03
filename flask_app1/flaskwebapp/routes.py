from flask import render_template, url_for, flash, redirect, request
from flaskwebapp.forms import AddEmployeeForm, SearchForm
from flaskwebapp.models import Employees
from flaskwebapp import app, db
from sqlalchemy import or_



@app.route('/')
@app.route('/home', methods= ['GET', 'POST'])
def home():
    form = SearchForm()
    datas = Employees.query.all()
    if form.validate_on_submit():
        string=form.string.data
        return redirect(url_for('search',string = string))
    
    return render_template('home.html',title='Home', form=form, datas = datas)




@app.route('/addemployee', methods= ['GET', 'POST'])
def addemployee():
    form = AddEmployeeForm()
    if form.validate_on_submit():
        employees=Employees(name = form.name.data, designation = form.designation.data, address = form.address.data, phone = form.phone.data)
        db.session.add(employees)
        db.session.commit()
        flash(f'Employee Added Successfully with {form.name.data} !','success')
        return redirect(url_for('home'))
    return render_template('addemployee.html',title='Add Employee', form = form )

@app.route('/delete/<int:emp_id>', methods= ['POST'])
def delete_emp(emp_id):
    employee=Employees.query.get_or_404(emp_id)
    db.session.delete(employee)
    db.session.commit()
    flash('Employee data has been deleted !!!','success')
    return redirect(url_for('home'))


@app.route('/search/<string:string>', methods= ['GET','POST'])
def search(string):
    string = string
    datas = Employees.query.filter(or_(Employees.name == string, Employees.designation == string, Employees.phone == string))
    rows = Employees.query.filter(or_(Employees.name == string, Employees.designation == string, Employees.phone == string)).count()
    if rows == 0 :
        flash('No Result Found !!!','danger')
        return redirect(url_for('home'))
    return render_template('searchresult.html',title = 'Search Result',datas = datas)

