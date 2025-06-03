from flask import Blueprint, render_template, request, jsonify, Flask, flash
from app import db
from app.models import ProductLookup
from flask import redirect, url_for
import pandas as pd
from datetime import datetime
from app import db
from app.models import (
          ProductLookup
)
import os
from werkzeug.utils import secure_filename




bp = Blueprint('routes', __name__)

# @bp.route('/')
# def home():
#     return render_template('search.html')

# @bp.route('/search')
# def search():
#     query = request.args.get('q', '')
#     if query:
#         companies = Company.query.filter(Company.company.ilike(f"%{query}%")).all()
#     else:
#         companies = []
#     return render_template('partials/search_results.html', companies=companies)

# @bp.route('/suggest')
# def suggest():
#     query = request.args.get('q', '')
#     suggestions = []
#     if query:
#         suggestions = Company.query \
#             .filter(Company.company.ilike(f"%{query}%")) \
#             .with_entities(Company.company) \
#             .limit(5).all()
#     return render_template('partials/suggestions.html', suggestions=suggestions)

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'xlsx', 'xls'}

@bp.route('/upload')
def upload():
    return render_template('upload.html')

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@bp.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('No file part')
            return redirect(request.url)
        
        file = request.files['file']
        file_type = request.form.get('file_type')
        
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            
            if not os.path.exists(UPLOAD_FOLDER):
                os.makedirs(UPLOAD_FOLDER)
            
            file.save(filepath)
            
            try:
                process_excel(filepath, file_type)
                flash('File successfully uploaded and processed')
            except Exception as e:
                flash(f'Error processing file: {str(e)}')
                return redirect(request.url)
            
            return redirect(url_for('routes.upload_file'))
    
    return render_template('upload.html')
def process_excel(filepath, file_type):
    if file_type == 'product_lookup':
        df = pd.read_excel(filepath, sheet_name='Sheet1')
        
        print("Excel Columns:", df.columns.tolist())
        print("First 5 rows:\n", df.head())

        if df.empty:
            print("DataFrame is empty!")
            return

        for _, row in df.iterrows():
            record = ProductLookup(
                product_name=row.get('Product Name'),
                primary_industry_focus=row.get('Primary Industry Focus'),
                ideal_customer_profiles=row.get('Ideal Customer Profiles'),
                persona=row.get('Persona'),
                role=row.get('Role'),
                key_concerns=row.get('Key Concerns'),
                problem_statement=row.get('Problem Statement'),
                value_propositions=row.get('Value Propositions')
            )
            db.session.add(record)

        try:
            db.session.commit()
            print("Records committed.")
        except Exception as e:
            db.session.rollback()
            print("Error committing to database:", e)


        