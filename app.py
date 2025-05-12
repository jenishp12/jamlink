from datetime import datetime
from flask import Flask, request, jsonify, render_template,redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jamlink.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

# User Model
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

# Post Model
class Post(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user = db.relationship('User', backref=db.backref('posts', lazy=True))

# Serve signup page
@app.route('/signup')
def serve_signup():
    return render_template('signup.html')

# Route to handle login
@app.route('/api/login', methods=['POST'])
def login():
    data = request.get_json()  # Get the data from the frontend
    email = data.get('email')
    password = data.get('password')

    if not email or not password:
        return jsonify({'message': 'Please enter both email and password.'}), 400

    user = User.query.filter_by(email=email).first()
    if user and check_password_hash(user.password_hash, password):
        return jsonify({'message': 'Login uccessfull'}), 201
    else:
        return jsonify({'message': 'Invalid email or password.'}), 400  # Invalid login


# Serve login page
@app.route('/login')
def serve_login():
    return render_template('login.html')

# Signup API (for JS/JSON)
@app.route('/api/signup', methods=['POST'])
def signup():
    data = request.get_json()
    username = data.get('username')
    email = data.get('email')
    password = data.get('password')

    if not username or not email or not password:
        return jsonify({'message': 'All fields are required'}), 400

    if User.query.filter_by(email=email).first():
        return jsonify({'message': 'Email already registered'}), 400

    password_hash = generate_password_hash(password)
    new_user = User(username=username, email=email, password_hash=password_hash)

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify({'message': 'User created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        print("Error:", e)
        return jsonify({'message': 'Failed to create user'}), 500

# Create a post
@app.route('/api/posts', methods=['POST'])
def create_post():
    data = request.get_json()
    user_id = data.get('user_id')
    title = data.get('title')
    content = data.get('content')

    if not user_id or not title or not content:
        return jsonify({'message': 'All fields are required'}), 400

    new_post = Post(user_id=user_id, title=title, content=content)

    try:
        db.session.add(new_post)
        db.session.commit()
        return jsonify({'message': 'Post created successfully'}), 201
    except Exception as e:
        db.session.rollback()
        print("Post creation error:", e)
        return jsonify({'message': 'Failed to create post'}), 500

# Get all posts
@app.route('/api/posts', methods=['GET'])
def get_posts():
    posts = Post.query.order_by(Post.created_at.desc()).all()
    post_list = []
    for post in posts:
        post_list.append({
            'id': post.id,
            'user_id': post.user_id,
            'username': post.user.username,
            'title': post.title,
            'content': post.content,
            'created_at': post.created_at.strftime('%Y-%m-%d %H:%M:%S')
        })
    return jsonify(post_list)

# Main page route
@app.route('/main')
def serve_main_page():
    return render_template('JamLink.html')

# Profile page route
@app.route('/profile')
def profile():
    return render_template('profile.html')

# Messaging page route
@app.route('/messaging')
def messaging():
    return render_template('messaging.html');

# Redirect to the login page initially
@app.route('/')
def index():
    return redirect(url_for('serve_login'))

# Run the app
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
