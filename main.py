from flask import Flask, redirect, render_template, url_for, request
from boto3.dynamodb.conditions import Attr
from numpy import require
from db import table

app = Flask(__name__)

@app.route('/read')
def read():
    response = table.scan()
    return render_template('read.html', data=response['Items'])

@app.route('/create', methods=["GET", "POST"])
def create():
    if(request.method == "GET"):
        return render_template('create.html')
    else:
        empid = int(request.form['empid'])
        dept = request.form['dept']
        name = request.form['fname']

        response = table.put_item(
            Item = {
                "EmpID": empid,
                "Department": dept,
                "Name": name
            }
        )
        if(response['ResponseMetadata']['HTTPStatusCode'] == 200):
            return redirect(url_for("read"))
        else:
            return "<h1>Some thing went wrong. Please try again </h1>"

@app.route('/update')
def update():
    return render_template('update.html')

@app.route('/delete', methods=["GET", "POST"])
def delete():
    if(request.method == "GET"):
        return render_template('delete.html')
    else:
        empid = int(request.form['empid'])
        response = table.delete_item(
            Key = {
                "EmpID": empid
            }
        )

        if(response['ResponseMetadata']['HTTPStatusCode'] == 200):
            return redirect(url_for("read"))
        else:
            return "<h1>Some thing went wrong. Please try again </h1>"

@app.route('/')
def home():
    return render_template('index.html')



if __name__ == '__main__':
    app.run(debug=True)