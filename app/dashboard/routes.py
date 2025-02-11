from flask import request, render_template, redirect, url_for, flash, Blueprint
from app.app import db
from email_validator import validate_email
from sqlalchemy.exc import IntegrityError
from flask_login import login_user, login_required, logout_user, current_user
from app.dashboard.forms import ProfileSetUpForm, UpdateProfileSetUpForm
from app.dashboard.models import ProfileSetupModel
from app.account.models import RegistrationModel
from werkzeug.utils import secure_filename
import os

dashboard = Blueprint('dashboard', __name__, template_folder='templates')


# setup page
@dashboard.route('/setup/<int:uid>', methods=['GET', 'POST'])
@login_required
def setup_page(uid):
    
    form = ProfileSetUpForm()

    get_user = RegistrationModel.query.get(uid).get_id()

    if request.method == 'POST':
        if form.validate_on_submit():
            full_name = form.full_name.data
            birth_date = form.birth_date.data
            gender = form.sex.data
            tags = form.achievement.data

            college = form.college.data
            university = form.higher_degree.data
            course = form.course.data
            extra_info = form.extra.data

            position = form.current_position.data
            govt_reg = form.govt_reg.data
            sign = form.signature.data
            office = form.office.data

            # image processing
            if sign:
                signature_image_name = secure_filename(sign.filename)
                file_path = os.path.join('uploads', signature_image_name)
                sign.save(file_path)

            create_profile = ProfileSetupModel(
                user_id = get_user,
                full_name = full_name,
                birth_date = birth_date,
                sex = gender,
                achievement = tags,
                college = college,
                higher_degree = university,
                course = course,
                extra = extra_info,
                current_position = position,
                govt_reg = govt_reg,
                office = office,
                signature = file_path
            )

            db.session.add(create_profile)

            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
                flash("Something Went Wrong", "error")
                return redirect(url_for('home.home_page')) 

            flash('Profile Setup done successfully!', 'success')
            return redirect(url_for('home.home_page'))

    context = {
        'form': form,
    }
    return render_template('dashboard/setup.html', **context)








@dashboard.route('/update_info/<int:uid>', methods=['GET', 'POST'])
@login_required
def update_profile_info(uid):
    # getting user data    
    get_info = ProfileSetupModel.query.get(uid)
    # form
    form = UpdateProfileSetUpForm(obj=get_info)

    if request.method == 'POST':

        if form.validate_on_submit():
            get_info.full_name = form.full_name.data
            get_info.birth_date = form.birth_date.data
            get_info.sex = form.sex.data
            get_info.achievement = form.achievement.data
            get_info.college = form.college.data
            get_info.higher_degree = form.higher_degree.data
            get_info.course = form.course.data
            get_info.extra = form.extra.data
            get_info.current_position = form.current_position.data
            get_info.govt_reg = form.govt_reg.data
            get_info.office = form.office.data

            sign = form.signature.data
            if sign:
                signature_image_name = secure_filename(sign.filename)
                file_path = os.path.join('uploads', signature_image_name)
                sign.save(file_path)

            get_info.signature = file_path

            try:
                db.session.commit()
            except IntegrityError:
                db.session.rollback()
                flash("Something Went Wrong", "error")
                return redirect(url_for('home.home_page')) 

            flash('Profile Information Updated successfully!', 'success')
            return redirect(url_for('home.home_page'))

            
    context = {
        'form': form,
        'data': get_info,
    }
    return render_template('dashboard/update.html', **context)







@dashboard.route('/profile_page/<int:uid>')
@login_required
def profile_page(uid):

    context = {}
    return render_template('dashboard/profile.html', **context)