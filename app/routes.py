from flask import Blueprint, jsonify, request

from app.models import User, Category, Expense
from app import db

bp = Blueprint('api', __name__)

@bp.route('/')
def hello_world():
    return jsonify({"message": "Hello, World!"})

@bp.route('/users', methods=['POST'])
def create_user():
    """Create a new user"""
    data = request.json
    new_user = User(username=data['username'], email=data['email'], password=data['password'])
    db.session.add(new_user)
    db.session.commit()
    return jsonify({"message": "User created!"}), 201

@bp.route('/users', methods=['GET'])
def get_users():
    """Fetch all users"""
    users = User.query.all()
    return jsonify([{"id": user.id, "username": user.username, "email": user.email} for user in users])


@bp.route('/expenses', methods=['GET'])
def get_expenses():
    """Fetch all expenses"""
    expenses = Expense.query.all()
    return jsonify([{
        "id": expense.id,
        "date": expense.date,
        "amount": expense.amount,
        "category": expense.category.name,
        "user": expense.user.username,
        "notes": expense.notes
    } for expense in expenses])

@bp.route('/categories/test', methods=['GET'])
def test_category():
    """Test if Category is accessible"""
    categories = Category.query.all()
    return jsonify({"message": f"Found {len(categories)} categories"})
