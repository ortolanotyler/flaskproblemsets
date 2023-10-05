from flask import Flask, request, redirect, render_template
from flask_debugtoolbar import DebugToolbarExtension
from models import db, User

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql:///myblogly"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'mysecretkey'

toolbar = DebugToolbarExtension(app)

db.init_app(app)
db.create_all()

@app.route('/')
def home():
    """Redirect to the user list page."""
    return redirect("/users")

@app.route('/users')
def user_list():
    """Display a list of users."""
    users = User.query.order_by(User.last_name, User.first_name).all()
    return render_template('users/index.html', users=users)

@app.route('/users/new', methods=["GET"])
def new_user_form():
    """Show a form for creating a new user."""
    return render_template('users/new.html')

@app.route("/users/new", methods=["POST"])
def create_user():
    """Handle the form submission for creating a new user."""
    new_user = User(
        first_name=request.form['first_name'],
        last_name=request.form['last_name'],
        image_url=request.form['image_url'] or None
    )
    db.session.add(new_user)
    db.session.commit()
    return redirect("/users")

# ... Other routes for editing, updating, and deleting users ...

if __name__ == "__main__":
    app.run(debug=True)
