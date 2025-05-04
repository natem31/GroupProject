from flask import Flask, render_template, redirect, url_for, request
from config import Config
from models import db, User, Commitment
from forms import UserForm, CommitmentForm
from scheduler import generate_weekly_schedule

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/', methods=['GET', 'POST'])
def home():
    form = UserForm()
    if form.validate_on_submit():
        user = User(name=form.name.data, email=form.email.data)
        db.session.add(user)
        db.session.commit()
        return redirect(url_for('add_commitments', user_id=user.id))
    return render_template('home.html', form=form)

@app.route('/user/<int:user_id>/commitments', methods=['GET', 'POST'])
def add_commitments(user_id):
    form = CommitmentForm()
    if form.validate_on_submit():
        commitment = Commitment(
            user_id=user_id,
            title=form.title.data,
            day_of_week=form.day_of_week.data,
            start_time=form.start_time.data,
            end_time=form.end_time.data,
            category=form.category.data
        )
        db.session.add(commitment)
        db.session.commit()
    user = User.query.get_or_404(user_id)
    commitments = Commitment.query.filter_by(user_id=user_id).all()
    return render_template('add_commitments.html', form=form, user=user, commitments=commitments)

@app.route('/user/<int:user_id>/schedule', methods=['GET'])
def view_schedule(user_id):
    user = User.query.get_or_404(user_id)
    weekly_schedule = generate_weekly_schedule(user)

    # Always show full week – no dropdown or day selection
    return render_template(
        'schedule.html',  # Make sure your template is named this
        user=user,
        schedule=weekly_schedule
    )

if __name__ == '__main__':
    app.run(debug=True)

