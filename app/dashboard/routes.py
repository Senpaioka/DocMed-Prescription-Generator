from flask import request, render_template, redirect, url_for, flash, Blueprint
from app.app import db
from sqlalchemy.exc import IntegrityError
from flask_login import login_required
from app.dashboard.forms import ProfileSetUpForm, UpdateProfileSetUpForm
from app.dashboard.models import ProfileSetupModel
from app.account.models import RegistrationModel
from app.pdf.models import PrescriptionModel
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
            phone = form.phone.data

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
                file_path = os.path.join('static','uploads', signature_image_name).replace("\\", "/")
                sign.save(file_path)
                

            create_profile = ProfileSetupModel(
                user_id = get_user,
                full_name = full_name,
                birth_date = birth_date,
                sex = gender,
                achievement = tags,
                phone = phone,
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
            get_info.phone = form.phone.data
            get_info.college = form.college.data
            get_info.higher_degree = form.higher_degree.data
            get_info.course = form.course.data
            get_info.extra = form.extra.data
            get_info.current_position = form.current_position.data
            get_info.govt_reg = form.govt_reg.data
            get_info.office = form.office.data

            sign = form.signature.data
            
            if sign != get_info.signature:
                signature_image_name = secure_filename(sign.filename)
                file_path = os.path.join('static','uploads', signature_image_name).replace("\\", "/")
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

    get_user_info = ProfileSetupModel.query.get(uid)

    context = {
        'info': get_user_info,
    }
    return render_template('dashboard/profile.html', **context)






@dashboard.route('/history/<int:uid>')
@login_required
def history_page(uid):
    # Get the current page from URL, default is 1
    get_page = request.args.get('page', 1, type=int) 
    # Number of items per page
    per_page = 25 

    paged_history = PrescriptionModel.query.filter_by(doc_id=uid).order_by(PrescriptionModel.created_at.desc()).paginate(page=get_page, per_page=per_page, error_out=False)
    
    context = {
        'info': paged_history,
    }
    return render_template('dashboard/history.html', **context)



