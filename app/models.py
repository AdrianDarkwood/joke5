from datetime import datetime
from app import db


# class Company(db.Model):
#     id = db.Column(db.Integer, primary_key=True)
#     company = db.Column(db.String(200))
#     head_office_location = db.Column(db.String(100))
#     primary_industry = db.Column(db.String(100))
#     industry = db.Column(db.Text)
#     sub_industry = db.Column(db.String(100))
#     type = db.Column(db.String(50))
#     location = db.Column(db.String(100))
#     employee_count = db.Column(db.String(50))
#     revenue_range = db.Column(db.String(50))
#     num_employees = db.Column(db.Integer)
#     industry2 = db.Column(db.String(100))
#     website = db.Column(db.String(200))
#     company_linkedin_url = db.Column(db.String(200))
#     facebook_url = db.Column(db.String(200))
#     twitter_url = db.Column(db.String(200))
#     keywords = db.Column(db.Text)
#     company_phone = db.Column(db.String(20))
#     seo_description = db.Column(db.Text)
#     technologies = db.Column(db.Text)
#     total_funding = db.Column(db.Float)
#     latest_funding = db.Column(db.String(100))
#     latest_funding_amount = db.Column(db.Float)
#     last_raised_at = db.Column(db.DateTime)
#     annual_revenue = db.Column(db.Float)
#     number_of_retail_locations = db.Column(db.Integer)
#     short_description = db.Column(db.Text)
#     founded_year = db.Column(db.Integer)
#     comments = db.Column(db.Text)



class ProductLookup(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    product_name = db.Column(db.String(1000))
    primary_industry_focus = db.Column(db.Text)
    ideal_customer_profiles = db.Column(db.Text)
    persona = db.Column(db.String(1000))
    role = db.Column(db.String(1000))
    key_concerns = db.Column(db.Text)
    problem_statement = db.Column(db.Text)
    value_propositions = db.Column(db.Text)

    