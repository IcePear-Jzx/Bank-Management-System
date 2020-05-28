from flask import Blueprint, jsonify, request, render_template, flash
from .models import Customer
from . import db


bp = Blueprint('customer', __name__, url_prefix='/customer')


@bp.route('/create', methods=['GET'])
def create_init():
    errors = []
    return render_template('customer/create.html', errors=errors)


@bp.route('/create', methods=['POST'])
def create():
    errors = []
    cusID = request.form['cusID']
    cusname = request.form['cusname']
    cusphone = request.form['cusphone']
    address = request.form['address']
    contact_phone = request.form['contact_phone']
    contact_name = request.form['contact_name']
    contact_email = request.form['contact_email']
    relation = request.form['relation']
    if len(cusID) != 18:
        errors.append('cusID')
    if len(cusname) == 0 or len(cusname) > 10:
        errors.append('cusname')
    if len(cusphone) != 11:
        errors.append('cusphone')
    if len(address) > 50:
        errors.append('address')
    if len(contact_phone) != 11:
        errors.append('contact_phone')
    if len(contact_name) == 0 or len(contact_name) > 10:
        errors.append('contact_name')
    if len(contact_email) > 0 and '@' not in contact_email:
        errors.append('contact_email')
    if len(relation) == 0 or len(relation) > 10:
        errors.append('relation')
    if not errors:
        new_customer = Customer(cusID=cusID, cusname=cusname, cusphone=cusphone, 
            address=address, contact_name=contact_name, contact_phone=contact_phone, 
            contact_email=contact_email, relation=relation)
        db.session.add(new_customer)
        db.session.commit()
    return render_template('customer/create.html', errors=errors)


@bp.route('/search', methods=['GET'])
def search_init():
    customers = Customer.query.all()
    return render_template('customer/search.html', customers=customers)


@bp.route('/search', methods=['POST'])
def search():
    customers = Customer.query.filter_by()
    return render_template('customer/search.html')
