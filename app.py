from flask import Flask, render_template, request, jsonify, session
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///maine_restaurant.db'
app.config['SECRET_KEY'] = 'your-secret-key-here'
db = SQLAlchemy(app)

# Database Models
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128))
    login_count = db.Column(db.Integer, default=0)
    last_login = db.Column(db.DateTime)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    orders = db.relationship('Order', backref='user', lazy=True)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    items = db.Column(db.Text)  # JSON string of ordered items
    total = db.Column(db.Float)
    status = db.Column(db.String(20), default='Pending')
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class ActivityLog(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    activity = db.Column(db.String(100))
    details = db.Column(db.Text)
    ip_address = db.Column(db.String(50))
    timestamp = db.Column(db.DateTime, default=datetime.utcnow)

# Create tables
with app.app_context():
    db.create_all()

# Helper functions
def log_activity(user_id, activity, details, ip):
    new_log = ActivityLog(
        user_id=user_id,
        activity=activity,
        details=details,
        ip_address=ip
    )
    db.session.add(new_log)
    db.session.commit()

# Routes
@app.route('/')
def home():
    return render_template('index.html')

# API Endpoints
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()
    user = User.query.filter_by(username=data['username']).first()
    
    if user and check_password_hash(user.password_hash, data['password']):
        user.login_count += 1
        user.last_login = datetime.utcnow()
        db.session.commit()
        
        session['user_id'] = user.id
        log_activity(user.id, 'Login', 'User logged in', request.remote_addr)
        
        return jsonify({
            'success': True,
            'user': {
                'id': user.id,
                'username': user.username,
                'login_count': user.login_count
            }
        })
    return jsonify({'success': False, 'error': 'Invalid credentials'})

@app.route('/api/register', methods=['POST'])
def register():
    data = request.get_json()
    if User.query.filter_by(username=data['username']).first():
        return jsonify({'success': False, 'error': 'Username exists'})
    
    new_user = User(
        username=data['username'],
        email=data['email'],
        password_hash=generate_password_hash(data['password'])
    )
    db.session.add(new_user)
    db.session.commit()
    
    log_activity(new_user.id, 'Registration', 'New user registered', request.remote_addr)
    return jsonify({'success': True, 'user_id': new_user.id})

@app.route('/api/order', methods=['POST'])
def create_order():
    data = request.get_json()
    new_order = Order(
        user_id=data['user_id'],
        items=str(data['items']),  # Convert list to JSON string
        total=data['total'],
        status='Received'
    )
    db.session.add(new_order)
    db.session.commit()
    
    log_activity(data['user_id'], 'New Order', f'Order #{new_order.id} placed', request.remote_addr)
    return jsonify({'success': True, 'order_id': new_order.id})

@app.route('/api/stats', methods=['GET'])
def get_stats():
    total_users = User.query.count()
    total_orders = Order.query.count()
    today_orders = Order.query.filter(
        db.func.date(Order.created_at) == datetime.today().date()
    ).count()
    
    recent_activities = ActivityLog.query.order_by(
        ActivityLog.timestamp.desc()
    ).limit(10).all()
    
    return jsonify({
        'total_users': total_users,
        'total_orders': total_orders,
        'today_orders': today_orders,
        'activities': [
            {
                'user': act.user.username if act.user else 'Guest',
                'activity': act.activity,
                'timestamp': act.timestamp.strftime('%Y-%m-%d %H:%M:%S')
            } for act in recent_activities
        ]
    })

if __name__ == '__main__':
    app.run(debug=True)