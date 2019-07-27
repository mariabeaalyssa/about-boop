from flask import Flask, render_template
import os
from app import app, db
from app.models import *

@app.route('/')
def about():
	return render_template('about.html')

if __name__ == '__main__':
	app.run(debug=True)