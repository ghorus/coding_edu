from flask import render_template, Blueprint, flash, redirect, url_for
from coding_edu.main.forms import SignupForm
from coding_edu.models.models import UsersData
from coding_edu import db
main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
def index():
    form = SignupForm()
    if form.validate_on_submit():
        user = UsersData.query.filter_by(email=form.email.data).first()
        if user:
            flash("This email already signed up.", "error")
        else:
            user = UsersData(email=form.email.data)
            db.session.add(user)
            db.session.commit()
            flash("Thanks for signing up! Be sure to check your email soon.", "success")
        return redirect(url_for("main.index"))
        
    return render_template("main/index.html", form=form)
