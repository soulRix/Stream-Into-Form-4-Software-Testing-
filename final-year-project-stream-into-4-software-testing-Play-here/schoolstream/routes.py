from flask import render_template, redirect, url_for, flash, request,abort, jsonify
from PIL import Image
from schoolstream import app, db, bcrypt,login_manager, mail
from schoolstream.form import (RegistrationForm, LoginForm, UpdateAccountForm, AddSubjectElectiveForm, SchoolForm,UpdateSchoolForm, TeacherForm, 
                                UpdateTeacherForm, StudentForm,streamCheckForm,UpdateStudentForm, requestChangeForm, RequestResetForm, ResetPasswordForm, ChangePasswordForm)
from schoolstream.models import User, Role, users_roles , Subject, Form4Syllabus,Form5Syllabus,Career, School, StreamPackage,Student, SchoolAddress, State, Zone, Teacher, Grade, RequestChange
#from flask_user import  roles_required, UserManager, UserMixin
from flask_login import login_user, current_user, logout_user, login_required
from flask_mail import Message
from functools import wraps
import secrets
import os


def role_login_required(role = "ANY"):
    def wrapper(fn):
        @wraps(fn)
        def decorated_view(*args, **kwargs):
            if not current_user.is_authenticated:
                login_manager.login_message = "Please login to the website!"
                return login_manager.unauthorized()
            if((current_user.roles[0].name != role) and (role != "ANY")):
                login_manager.login_message = "Unauthorized Access Page"
                return login_manager.unauthorized()
            return fn(*args, **kwargs)
        return decorated_view
    return wrapper



@app.route("/hello")
def hello():
    return "Hello World!"

#################################################################################################
#                                       Public                                                  #  
#################################################################################################

@app.route("/")
@app.route("/home/")
def homepage():
    return render_template("index.html")

#Subject & Elective List
@app.route("/subjectList/")
def subjectList():
    subjects = Subject.query.all()
    return render_template("public/subjectList.html", subjects=subjects, title='Subject & Elective List')

#@app.route("/schoolList/int<subjectNumber>")
@app.route("/subjectList/<int:subject_id>")
def subjectListDetails(subject_id):
    subjects = Subject.query.get_or_404(subject_id)
    return render_template("public/subjectInfoDetail.html", subjects=subjects, title= subjects.subject_title)



#School Stream Offer 
@app.route("/schoolList/")
def schoolStreamList():
    page = request.args.get('page', 1, type = int)
    schools_list = School.query.order_by(School.id.desc()).paginate(page = page, per_page = 5)
    return render_template("public/schoolList.html", schools_list = schools_list , title = 'School List')

#@app.route("/schoolList/int<schoolnumber>")
#@app.route("/school/<str:school_name>")
#Passing School Name Argument
@app.route("/school/<int:school_id>")
def schoolStreamDeatils(school_id):
    #school = School.query.filter_by(school_name = school_name).first_or_404()
    school = School.query.get_or_404(school_id)
    total_stream = StreamPackage.query.filter_by(school_id = school_id).count()
    school_stream = StreamPackage.query.filter_by(school_id = school_id).all()
    #total_subject = db.session.query(stream_package_subject).join(StreamPackage).join(Subject).filter(Subject.stream_package.id == school_stream.id )
    #total_subject = db.session.query(StreamPackage).join(Subject, StreamPackage.id == Subject.stream_package).count()
    return render_template("public/schoolInfo.html", school = school,total_stream = total_stream, school_stream = school_stream)






#################################################################################################
#                                       User                                                   #  
#################################################################################################

#Password
# admin@test.com and password is 'testing'
@app.route("/login/", methods = ['GET', 'POST'])
def loginPage():
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            #The remember-me data will return True or False
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            #tenary conditional python
            return redirect(next_page) if next_page else redirect(url_for('homepage'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('auth/loginPage.html', title='Login', form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('homepage'))

def save_picture(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path =os.path.join(app.root_path,'static/profile_pics', picture_fn)
    output_size = (125, 125)
    imageResize =  Image.open(form_picture)
    imageResize.thumbnail(output_size)
    imageResize.save(picture_path)

    return picture_fn

def save_school_logo(form_picture):
    random_hex = secrets.token_hex(8)
    _, f_ext = os.path.splitext(form_picture.filename)
    picture_fn = random_hex + f_ext
    picture_path =os.path.join(app.root_path,'static/school_logo', picture_fn)
    output_size = (125, 125)
    imageResize =  Image.open(form_picture)
    imageResize.thumbnail(output_size)
    imageResize.save(picture_path)

    return picture_fn


@app.route("/account/", methods=['GET', 'POST'])
@login_required
def account():
    form = UpdateAccountForm()
    form1 = ChangePasswordForm()
    if form.validate_on_submit():
        if form.picture.data:
            picture_file = save_picture(form.picture.data)
            current_user.image_file = picture_file
        current_user.name = form.name.data
        current_user.icNumber =  form.icNumber.data
        current_user.email = form.email.data
        db.session.commit()
        flash('Account has been updated!', 'success')
        return redirect(url_for('account'))
    elif request.method == 'GET':
        form.name.data = current_user.name
        form.icNumber.data = current_user.icNumber
        form.email.data = current_user.email
    
    if form1.validate_on_submit():
        user = User.query.filter_by(email = current_user.email).first()
        if user and bcrypt.check_password_hash(user.password, form1.old_password.data):
            if form1.old_password.data == form1.password.data:
                flash('Your new password should not be the same as your old password!', 'danger')
                return redirect(url_for('account'))
            hashed_password = bcrypt.generate_password_hash(form1.password.data).decode("utf8")
            user.password = hashed_password
            db.session.commit()
            flash('Your password has been Updated!', 'success')
            return redirect(url_for('account'))
        else:
            flash('Wrong Password, Please try again!', 'danger')
            return redirect(url_for('account'))
    
    image_file = url_for('static', filename='profile_pics/' + current_user.image_file)
    return render_template('account.html', title = 'Account', image_file = image_file, form=form, form1 = form1)

def send_reset_email(user):
    token = user.get_reset_token()
    msg = Message('Password Reset Request', \
                sender='noreply@demo.com', \
                recipients = [user.email])
    msg.body = f'''To Reset Your Password, visit the following link:
{url_for('reset_token', token=token, _external=True)}
If you did not make this request then simply ignore this email and no changes will be made.
'''
    mail.send(msg)


# Request A Password Reset
@app.route("/reset_password/", methods = ['GET', 'POST'])
def reset_request():
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    form = RequestResetForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email = form.email.data).first()
        send_reset_email(user)
        flash('An email has been sent, Please Check your email for reset password', 'info')
        return redirect(url_for('loginPage'))

    return render_template('auth/reset_request.html', title = "Reset Password", form = form)

# Using The Token to do the Reset Password Process
@app.route("/reset_password/user-<token>", methods = ['GET', 'POST'])
def reset_token(token):
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    user = User.verify_reset_token(token)
    if user is None:
        flash('Invalid or expired Token', 'warning')
        return redirect(url_for('reset_request'))
    form = ResetPasswordForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf8")
        user.password = hashed_password
        #Commit the change into Database
        db.session.commit()
        flash('Your password has been updated! You are now able to log in', 'success')
        return redirect(url_for('loginPage'))
    return render_template('auth/reset_token.html', title = "Reset Password", form = form)

#################################################################################################
#                                       Admin                                                   #  
#################################################################################################
@app.route("/admin/account-getting/register/", methods=["POST", "GET"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('homepage'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode("utf8")
        user = User(name = form.name.data, icNumber =  form.icNumber.data, email = form.email.data, phoneNumber = form.phoneNumber.data, password = hashed_password)
        user.roles.append(Role(name='admin_SchoolStream'))
        #Add the user to Database
        db.session.add(user)
        #Commit the change into Database
        db.session.commit()
        #f is a f String which is a new way to format string!
        #The second argument is the Bootstrap attribute, 'success'
        flash('Your Account has been created! You are now able to log in', 'success')
        return redirect(url_for('loginPage'))
    return render_template('admin/registerAdmin.html', title='Register', form=form)


@app.route("/admin/manageSchool" ,methods=["GET", "POST"])
@role_login_required(role = "admin_SchoolStream")
def manageSchool():
    state = State.query.all()
    page = request.args.get('page', 1, type = int)
    school_list = School.query.order_by(School.id.desc()).paginate(page = page, per_page = 5)
    return render_template('admin/manageSchool.html', title = 'Manage School',  state = state, school_list = school_list)

@app.route("/admin/manageSchool/school/add/" , methods=["GET", "POST"])
@role_login_required(role = "admin_SchoolStream")
def add_school():
    form = SchoolForm()
    subject = Subject.query.all()
    
    stringFormat = "{} - {}"
    form.schoolState.choices = [(state.id, stringFormat.format(state.state_code, state.state_name)) for state in State.query.all()]
    
    if form.validate_on_submit() and request.method == "POST":
        schoolLogo = 'default_logo.png'
        projectStatus = "Student Proposed"
        if form.schoolLogo.data:
            logo_file = save_school_logo(form.schoolLogo.data)
            schoolLogo = logo_file
        school = School(school_name = form.schoolName.data, school_logo = schoolLogo, school_description = form.schoolDescription.data, school_email = form.schoolEmail.data\
                        ,school_phoneNumber = form.schoolPhoneNumber.data, school_code = form.schoolCode.data, shortForm = form.shortForm.data, school_moto = form.schoolMoto.data,\
                        school_vision = form.schoolVision.data, shortSchool_name = form.shortSchoolName.data)
        getState = State.query.filter_by(id = form.schoolState.data).first()
        getZone =  Zone.query.filter_by(id = form.schoolZon.data).first()
        school.school_address.append(SchoolAddress(address_name = form.schoolAddress.data, state_id = getState.id, zone_id = getZone.id))
        streamPackageName = request.form.getlist('streamName[]')
        subjectChoice = request.form.getlist('checkboxSubject')
        subjectChoice2 = request.form.getlist('checkboxSubject2')
        subjectChoice3 = request.form.getlist('checkboxSubject3')
        subjectChoice4 = request.form.getlist('checkboxSubject4')
        subjectChoice5 = request.form.getlist('checkboxSubject5')
        subjectChoice6 = request.form.getlist('checkboxSubject6')
        subjectChoice7 = request.form.getlist('checkboxSubject7')
        subjectChoice8 = request.form.getlist('checkboxSubject8')
        subjectChoice9 = request.form.getlist('checkboxSubject9')
        subjectChoice10 = request.form.getlist('checkboxSubject10')

        subjectChoiceBool = True
        subjectChoiceBool2 = True
        subjectChoiceBool3 = True
        subjectChoiceBool3 = True
        subjectChoiceBool4 = True
        subjectChoiceBool5 = True
        subjectChoiceBool6 = True
        subjectChoiceBool7 = True
        subjectChoiceBool8 = True
        subjectChoiceBool9 = True
        subjectChoiceBool10 = True

        newStreamName = []
        for index,valueName in enumerate(streamPackageName):
            if (not(valueName and not valueName.isspace())):
                continue
            newStreamName.append(valueName)

        sizeStreamName = len(newStreamName)
        for index,valueName in enumerate(newStreamName):
            if (not(valueName and not valueName.isspace())):
                continue
            school.stream_packages.append(StreamPackage(stream_name = valueName))
            # db.session.add(school)
            # db.session.commit()
            if subjectChoice and index <= sizeStreamName and subjectChoiceBool:
                for valueSubject in subjectChoice:
                    if (not(valueSubject and not valueSubject.isspace())):
                        continue
                    search_subject = Subject.query.filter_by(subject_title = valueSubject).first()
                    school.stream_packages[index].subjects.append(search_subject)
                    subjectChoiceBool = False
                    #school.stream_packages.append(StreamPackage(stream_name = valueName, subjects = search_subject))
            elif subjectChoice2 and index <= sizeStreamName and subjectChoiceBool2:
                for valueSubject2 in subjectChoice2:
                    if (not(valueSubject2 and not valueSubject2.isspace())):
                        continue
                    search_subject2 = Subject.query.filter_by(subject_title = valueSubject2).first()
                    school.stream_packages[index].subjects.append(search_subject2)
                    subjectChoiceBool2 = False

            elif subjectChoice3 and index <= sizeStreamName and subjectChoiceBool3:
                for valueSubject3 in subjectChoice3:
                    if (not(valueSubject3 and not valueSubject3.isspace())):
                        continue
                    search_subject2 = Subject.query.filter_by(subject_title = valueSubject3).first()
                    school.stream_packages[index].subjects.append(search_subject2)
                    subjectChoiceBool3 = False

            elif subjectChoice4 and index <= sizeStreamName and subjectChoiceBool4:
                for valueSubject4 in subjectChoice4:
                    if (not(valueSubject4 and not valueSubject4.isspace())):
                        continue
                    search_subject2 = Subject.query.filter_by(subject_title = valueSubject4).first()
                    school.stream_packages[index].subjects.append(search_subject2)
                    subjectChoiceBool4 = False

            elif subjectChoice5 and index <= sizeStreamName and subjectChoiceBool5:
                for valueSubject5 in subjectChoice5:
                    if (not(valueSubject5 and not valueSubject5.isspace())):
                        continue
                    search_subject2 = Subject.query.filter_by(subject_title = valueSubject5).first()
                    school.stream_packages[index].subjects.append(search_subject2)
                    subjectChoiceBool5 = False
            
            elif subjectChoice6 and index <= sizeStreamName and subjectChoiceBool6:
                for valueSubject6 in subjectChoice6:
                    if (not(valueSubject6 and not valueSubject6.isspace())):
                        continue
                    search_subject2 = Subject.query.filter_by(subject_title = valueSubject6).first()
                    school.stream_packages[index].subjects.append(search_subject2)
                    subjectChoiceBool6 = False

            elif subjectChoice7 and index <= sizeStreamName and subjectChoiceBool7:
                for valueSubject7 in subjectChoice7:
                    if (not(valueSubject7 and not valueSubject7.isspace())):
                        continue
                    search_subject2 = Subject.query.filter_by(subject_title = valueSubject7).first()
                    school.stream_packages[index].subjects.append(search_subject2)
                    subjectChoiceBool7 = False
            
            elif subjectChoice8 and index <= sizeStreamName and subjectChoiceBool8:
                for valueSubject8 in subjectChoice8:
                    if (not(valueSubject8 and not valueSubject8.isspace())):
                        continue
                    search_subject2 = Subject.query.filter_by(subject_title = valueSubject8).first()
                    school.stream_packages[index].subjects.append(search_subject2)
                    subjectChoiceBool8 = False

            elif subjectChoice9 and index <= sizeStreamName and subjectChoiceBool9:
                for valueSubject9 in subjectChoice9:
                    if (not(valueSubject9 and not valueSubject9.isspace())):
                        continue
                    search_subject2 = Subject.query.filter_by(subject_title = valueSubject9).first()
                    school.stream_packages[index].subjects.append(search_subject2)
                    subjectChoiceBool9 = False
            
            elif subjectChoice10 and index <= sizeStreamName and subjectChoiceBool10:
                for valueSubject10 in subjectChoice10:
                    if (not(valueSubject10 and not valueSubject10.isspace())):
                        continue
                    search_subject2 = Subject.query.filter_by(subject_title = valueSubject10).first()
                    school.stream_packages[index].subjects.append(search_subject2)
                    subjectChoiceBool10 = False
        
        db.session.add(school)
        db.session.commit()   
        
        #db.session.commit()
        flash('The School has been added!','success')
        return redirect(url_for('manageSchool'))
    else:
        if form.errors:
            flash('The School has not been added!','danger')

    return render_template('admin/addSchool.html', title = "Add School", form = form , subject = subject )

@app.route("/admin/manageSchool/school-<int:school_id>/update/", methods=["GET", "POST"])
@role_login_required(role = "admin_SchoolStream")
def update_school(school_id):
    school = School.query.get_or_404(school_id)
    subject = Subject.query.all()
    if current_user.roles[0].name != "admin_SchoolStream":
        abort(403)
    school_stream = StreamPackage.query.filter_by(school_id = school_id).all()
    form = UpdateSchoolForm(school = school)
    stringFormat = "{} - {}"
    form.schoolState.choices = [(state.id, stringFormat.format(state.state_code, state.state_name)) for state in State.query.all()]

    if form.validate_on_submit():
        if form.schoolLogo.data:
            logo_file = save_school_logo(form.schoolLogo.data)
            school.school_logo = logo_file   

        print("===================================================================")   
        print(form.schoolName.data, type(form.schoolName.data), school.school_name, type(school.school_name))
        print(form.shortSchoolName.data, type(form.shortSchoolName.data),school.shortSchool_name, type(school.shortSchool_name))
        print(form.schoolAddress.data, type(form.schoolAddress.data), school.school_address[0].address_name, type(school.school_address[0].address_name) )
        print(form.schoolCode.data, type(form.schoolCode.data), school.school_code, type(school.school_code) )
        print(form.schoolEmail.data, type(form.schoolEmail.data), school.school_email,type(school.school_email))
        # print(form.schoolState.data, type(form.schoolState.data),form.schoolState.data,type(form.schoolState.data))
        # print(form.schoolZon.data, type(form.schoolZon.data),,type(form.schoolZon.data))
        # print(form.schoolState.data,type(form.schoolState.data),,type())
        # print(form.schoolEmail.data,  type(form.schoolEmail.data),,type())
        # print(form.schoolPhoneNumber.data, type(form.schoolPhoneNumber.data),,type())
        # print(form.schoolMoto.data, type(form.schoolMoto.data),,type())
        # print(form.schoolVision.data, type(form.schoolVision.data),,type())
        # print(form.schoolDescription.data, type(form.schoolDescription.data),,type())
        print("===================================================================")   
        print(school.shortForm)
        print(school.school_address[0].state_id)
        print(school.school_address[0].zone_id)
        print(school.school_email)
        print(school.school_phoneNumber)
        print(school.school_moto)
        print(school.school_vision)
        print(school.school_description)

        school.school_name = form.schoolName.data
        school.shortSchool_name = form.shortSchoolName.data
        school.school_address[0].address_name = form.schoolAddress.data
        school.school_code = form.schoolCode.data
        school.shortForm = form.shortForm.data
        getState = State.query.filter_by(id = form.schoolState.data).first()
        getZone =  Zone.query.filter_by(id = form.schoolZon.data).first()
        school.school_address[0].state_id = getState.id
        school.school_address[0].zone_id = getZone.id
        school.school_email = form.schoolEmail.data 
        school.school_phoneNumber = form.schoolPhoneNumber.data
        school.school_moto =  form.schoolMoto.data
        school.school_vision =  form.schoolVision.data 
        school.school_description =  form.schoolDescription.data
        
        db.session.commit()
        flash('The school details has been updated~!', 'info')
        return redirect(url_for('manageSchool'))
    elif request.method == 'GET':
        form.schoolName.data = school.school_name
        form.schoolDescription.data = school.school_description
        form.schoolAddress.data = school.school_address[0].address_name
        form.shortSchoolName.data = school.shortSchool_name
        form.schoolCode.data = school.school_code
        form.shortForm.data = school.shortForm
        form.schoolEmail.data = school.school_email
        form.schoolPhoneNumber.data = school.school_phoneNumber
        form.schoolMoto.data = school.school_moto
        form.schoolVision.data = school.school_vision
    
    # subject_list = Subject.query.all()
    return render_template('admin/updateSchool.html', title = 'Manage Subject', form = form, school = school, school_stream = school_stream, subject = subject)

@app.route("/admin/manageSchool/school-<int:school_id>/delete/", methods=["POST"])
@role_login_required(role = "admin_SchoolStream")
def delete_school(school_id):
    school = School.query.get_or_404(school_id)  
    if current_user.roles[0].name != "admin_SchoolStream":
        abort(403)
    db.session.delete(school)
    db.session.commit()
    flash("The school has been deleted!", 'success')
    return redirect(url_for('manageSchool'))

@app.route("/zone/<state>")
def zone(state):
    zone_data = Zone.query.filter_by(state_id = state).all()
    zoneArray = []

    for zone in zone_data:
        zoneObject = {}
        zoneObject['id'] = zone.id
        zoneObject['name'] = zone.zone_name
        zoneObject['code'] = zone.zone_code
        zoneArray.append(zoneObject)
    return jsonify({'zonelist': zoneArray})



@app.route("/admin/manageSubjectElectives/",methods=["GET", "POST"])
@role_login_required(role = "admin_SchoolStream")
def manageSubjectElectives():
    message = ""
    form = AddSubjectElectiveForm()
    careerOption = Career.query.all()
    if form.validate_on_submit():
        subject = Subject(subject_title = form.nameSubject.data, subject_category = form.subjectCategory.data, subject_description = form.subjectDescription.data)
        chapterNameForm4 = request.form.getlist('field[]')
        chapterNameForm5 = request.form.getlist('field2[]')
        careerChoice = request.form.getlist('checkboxCareer')
        for value in chapterNameForm4:
            if (not(value and not value.isspace())):
                continue
            subject.form4Syallabus.append(Form4Syllabus(syllabusName = value))
        
        for value2 in chapterNameForm5:
            if (not(value2 and not value2.isspace())):
                continue
            subject.form5Syallabus.append(Form5Syllabus(syllabusName = value2))
        
        for career in careerChoice:
            search_career = Career.query.filter_by(career_name = career).first()
            subject.careers.append(search_career)

        #subject.careers.append(form.careerChoose)
        
        db.session.add(subject)
        db.session.commit()
        
        flash('The Subject has been added!','success')
        return redirect(url_for('manageSubjectElectives'))

    #subject_list = Subject.query.all()
    #get the page and default value @ 1
    page = request.args.get('page', 1, type = int)
    #Subject Per Page is 5
    #subject_list = Subject.query.paginate(page = page, per_page = 5)
    subject_list = Subject.query.order_by(Subject.id.desc()).paginate(page = page, per_page = 5)
    
    return render_template('admin/manageSubjectElectives.html', title = 'Manage Subject', form = form, careerOption = careerOption, subject_list = subject_list )




@app.route("/admin/manageSubjectElectives/subject-<int:subject_id>/update/", methods=["GET", "POST"])
@role_login_required(role = "admin_SchoolStream")
def update_subject(subject_id):
    subject = Subject.query.get_or_404(subject_id)
    count_subject = Subject.query.filter(Subject.id).count()
    if current_user.roles[0].name != "admin_SchoolStream":
        abort(403)
    form = AddSubjectElectiveForm()
    if form.validate_on_submit():
        subject.subject_title = form.nameSubject.data
        subject.subject_category = form.subjectCategory.data
        subject.subject_description = form.subjectDescription.data

        chapterNameForm4 = request.form.getlist('field[]')
        chapterNameForm5 = request.form.getlist('field2[]')
        total_chapter4 = Form4Syllabus.query.filter_by(subject_id = subject.id).count()
        total_chapter5 = Form5Syllabus.query.filter_by(subject_id = subject.id).count()
        
        for index,value in enumerate(chapterNameForm4):
            if index  < total_chapter4 :
                if value == '':
                    testing =  subject.form4Syallabus[index]
                    db.session.delete(testing)
                if subject.form4Syallabus[index].syllabusName == value:
                    continue
                elif subject.form4Syallabus[index].syllabusName != value:
                    subject.form4Syallabus[index].syllabusName = value
            else:
                subject.form4Syallabus.append(Form4Syllabus(syllabusName = value))
        
        for index,value in enumerate(chapterNameForm5):
            if index < total_chapter5:
                if value == '':
                    testing =  subject.form5Syallabus[index]
                    db.session.delete(testing)
                elif subject.form5Syallabus[index].syllabusName == value:
                    continue
                elif subject.form5Syallabus[index].syllabusName != value:
                    subject.form5Syallabus[index].syllabusName = value
            else:
                subject.form5Syallabus.append(Form5Syllabus(syllabusName = value))

        db.session.commit()
        flash('The subject has been updated~!', 'success')
        return redirect(url_for('manageSubjectElectives'))
    elif request.method == 'GET':
        form.nameSubject.data = subject.subject_title
        form.subjectCategory.data = subject.subject_category
        form.subjectDescription.data = subject.subject_description

    # subject_list = Subject.query.all()
    return render_template('admin/subjectUpdate.html', title = 'Manage Subject', form = form, subject = subject)

@app.route("/admin/manageSubjectElectives/subject-<int:subject_id>/delete/", methods=["POST"])
@role_login_required(role = "admin_SchoolStream")
def delete_subject(subject_id):
    subject = Subject.query.get_or_404(subject_id)  
    if current_user.roles[0].name != "admin_SchoolStream":
        abort(403)
    db.session.delete(subject)
    db.session.commit()
    flash("The subject has been deleted!", 'success')
    return redirect(url_for('manageSubjectElectives'))



@app.route("/admin/manageTeacher/", methods=["POST", "GET"])
@role_login_required(role = "admin_SchoolStream")
def manageTeacher():
    form = TeacherForm()
    page = request.args.get('page', 1, type = int)
    teacher_list = Teacher.query.order_by(Teacher.id.desc()).paginate(page = page, per_page = 5)
    form.school.choices = [(school.id, school.school_name) for school in School.query.all()]
    if form.validate_on_submit():
        hashed_pass = bcrypt.generate_password_hash(form.password.data).decode("utf8")
        user = User(name = form.name.data, icNumber = form.icNumber.data, email = form.email.data, phoneNumber = form.phoneNumber.data, password = hashed_pass)
        user.roles.append(Role(name='teacher'))
        user.teachers.append(Teacher( teacher_name = form.name.data, teacher_id = form.teacher_id.data, school_id = form.school.data))
        db.session.add(user)
        db.session.commit()

        flash("The Teacher's Account has been created!", 'success')
        return redirect(url_for('manageTeacher'))
    else:
        if form.errors:
            flash("The Teacher Account has not been created!", 'danger')

    return render_template("admin/manageTeacherAccounts.html", title = 'Manage Teacher', form = form, teacher_list = teacher_list )

@app.route("/admin/manageTeacher/account/teacher-<int:teacher_id>/update/", methods = ['GET',"POST"])
@role_login_required(role = "admin_SchoolStream")
def update_teacher_account(teacher_id):
    teacher = Teacher.query.get_or_404(teacher_id)
    teacher_user = User.query.get_or_404(teacher.user_id)
    form = UpdateTeacherForm(teacher = teacher)
    form.school.choices = [(school.id, school.school_name) for school in School.query.all()]

    if current_user.roles[0].name != "admin_SchoolStream":
        abort(403)
    if form.validate_on_submit():
        teacher.teacher_name = form.name.data
        teacher_user.name = form.name.data
        teacher.teacher_id = form.teacher_id.data
        teacher_user.icNumber = form.icNumber.data
        teacher_user.email = form.email.data
        teacher_user.phoneNumber = form.phoneNumber.data
        teacher.school.id = form.school.data
        db.session.commit()
        flash('Teacher Account has been update!', 'success')
        return redirect(url_for('manageTeacher'))

    elif request.method == "GET":
        form.name.data = teacher.teacher_name
        form.teacher_id.data = teacher.teacher_id
        form.icNumber.data = teacher.user.icNumber
        form.email.data = teacher.user.email
        form.phoneNumber.data = teacher.user.phoneNumber
        form.school.data = teacher.school.id
    
    return render_template('admin/updateTeacher.html', title = "Update Teacher", form = form, teacher = teacher)

@app.route("/admin/manageTeacher/account/teacher-<int:teacher_id>/delete/" , methods=["POST"])
@role_login_required(role = "admin_SchoolStream")
def delete_teacher_account(teacher_id):
    teacher = Teacher.query.get_or_404(teacher_id)
    teacher_user = User.query.get_or_404(teacher.user_id)
    if current_user.roles[0].name != "admin_SchoolStream":
        abort(403)
    db.session.delete(teacher)
    db.session.delete(teacher_user)
    db.session.commit()
    flash("The Teacher Account has been deleted!", 'success')
    return redirect(url_for('manageTeacher'))

@app.route("/admin/dashboard/")
@role_login_required(role = "admin_SchoolStream")
def adminDashboard():
    total_account = User.query.filter(User.id).count()
    total_subject = Subject.query.filter(Subject.id).count()
    total_school = School.query.filter(School.id).count()
    return render_template('admin/adminDashboard.html', title='Dashboard - Admin', total_account = total_account, total_subject = total_subject, total_school = total_school)


    




#################################################################################################
#                                       Teacher                                                 #  
#################################################################################################

@app.route("/teacher/dashboard/")
@role_login_required(role = "teacher")
def teacherDashboard():
    teacher = Teacher.query.filter_by(id = current_user.teachers[0].id).first()
    total_student = Student.query.filter_by(school_id = teacher.school_id).count()

    total_unreviewed = RequestChange.query.filter_by(school_id = teacher.school_id).count()
    #total_pureScience = Student.query.filter(Student.stream_package. = "Pure Science")
    return render_template('teacher/teacherDashboard.html', title = 'Dashboard - Teacher' , total_student = total_student, teacher = teacher, total_unreviewed = total_unreviewed)

@app.route("/teacher/manageStudent/")
@role_login_required(role = "teacher")
def manageStudent():
    teacher = Teacher.query.filter_by(id = current_user.teachers[0].id).first()
    school_focus = School.query.filter_by(id = teacher.school.id).first()

    page = request.args.get('page', 1, type = int)
    student_list = Student.query.filter_by(school_id = school_focus.id).order_by(Student.id.desc()).paginate(page = page, per_page = 5)
    
    return render_template('teacher/manageStudent.html', title= 'Manage Student', school_focus = school_focus, student_list = student_list)

def checkIfDuplicates_1(listOfElems):
    ''' Check if given list contains any duplicates '''
    if len(listOfElems) == len(set(listOfElems)):
        return False
    else:
        return True

@app.route("/teacher/manageStudent/add-Student/", methods = ['GET',"POST"])
@role_login_required(role = "teacher")
def add_student():
    form = StudentForm()
    subjectPT3 = ["Bahasa Melayu", "English", "Mathematics", "Science", "Geography", "Sejarah", "Bahasa Arab", "Bahasa Cina", "Bahasa Tamil", "Pendidikan Islam" , "Kemahiran Hidup Bersepadu (Kemahiran Teknikal)",\
                "Kemahiran Hidup Bersepadu (Ekonomi Rumah Tangga)", "Kemahiran Hidup Bersepadu (Pertanian)",  "Kemahiran Hidup Bersepadu (Perdagangan & Keusahawanan)", "Pendidikan Moral" ]
    grade = ["A", "B", "C", "D", "E", "F", "TH"]
    teacher = Teacher.query.filter_by(id = current_user.teachers[0].id).first()
    school_focus = School.query.filter_by(id = teacher.school.id).first()
    form.streamPackage.choices = [(stream.id, stream.stream_name) for stream in StreamPackage.query.filter_by(school_id = school_focus.id).all()]

    if form.validate_on_submit() and request.method == "POST":
        subjectChoicePt3 = request.form.getlist('subjectPT3Name')
        subjectGrade = request.form.getlist('subjectGrade')
        checkDuplicate = checkIfDuplicates_1(subjectChoicePt3)
        if checkDuplicate:
            flash('The Student Subject PT3 List contains the same subject', 'danger')
            return redirect(url_for('add_student'))
        elif len(subjectChoicePt3) != len(subjectGrade):
            flash('Please fill in the Grades!','danger')
            return redirect(url_for('add_student'))
        else:
            student = Student(student_name = form.studentName.data, student_icNum = form.studentICNum.data, student_form4_class = form.studentClass.data, school_id = school_focus.id ,streamPackage_id = form.streamPackage.data)
           
            for index, value in enumerate(subjectChoicePt3):
                for index2, value2 in enumerate(subjectGrade):
                    if (not(value and not value.isspace())) or (not(value2 and not value2.isspace())):
                        break
                    if index2 == index:
                        student.grades.append(Grade(name_subjectPT3 = value, grade_subject = value2))
                        break

            db.session.add(student)
            db.session.commit()
            flash('The Student has been added!','success')
            return redirect(url_for('manageStudent'))
    else:
        if form.errors:
            flash('The Student has not been added!', 'danger')
        

    return render_template('teacher/addStudent.html', title = "Add Student" , form = form, school_focus = school_focus, subjectPT3 = subjectPT3, grade = grade)

@app.route("/teacher/manageStudent/update-Student-<int:student_id>/", methods = ['GET',"POST"])
@role_login_required(role = "teacher")
def update_student(student_id):
    teacher = Teacher.query.filter_by(id = current_user.teachers[0].id).first()
    school_focus = School.query.filter_by(id = teacher.school.id).first()
    student = Student.query.get_or_404(student_id)
    form = UpdateStudentForm(student = student)
    form.streamPackage.choices = [(stream.id, stream.stream_name) for stream in StreamPackage.query.filter_by(school_id = school_focus.id).all()]
    subjectPT3 = ["Bahasa Melayu", "English", "Mathematics", "Science", "Geography", "Sejarah", "Bahasa Arab", "Bahasa Cina", "Bahasa Tamil", "Pendidikan Islam" , "Kemahiran Hidup Bersepadu (Kemahiran Teknikal)",\
                "Kemahiran Hidup Bersepadu (Ekonomi Rumah Tangga)", "Kemahiran Hidup Bersepadu (Pertanian)",  "Kemahiran Hidup Bersepadu (Perdagangan & Keusahawanan)", "Pendidikan Moral" ]
    grade = ["A", "B", "C", "D", "E", "F", "TH"]

    if form.validate_on_submit():
        student.student_name = form.studentName.data 
        student.student_icNum = form.studentICNum.data
        student.student_form4_class = form.studentClass.data 
        student.streamPackage_id = int(form.streamPackage.data)
        subjectChoicePt3 = request.form.getlist('subjectPT3Name')
        subjectGrade = request.form.getlist('subjectGrade')
        checkDuplicate = checkIfDuplicates_1(subjectChoicePt3)
        if checkDuplicate:
            flash('The Student Subject PT3 List contains the same subject', 'danger')
            return redirect(url_for('update_student', student_id = student_id))
        elif len(subjectChoicePt3) != len(subjectGrade):
            flash('Please fill in the Grades!','danger')
            return redirect(url_for('update_student', student_id = student_id))
        else:
            # Update the Results
            print("======================================================================")
            print(subjectChoicePt3)
            print(subjectGrade)
            print(student.grades.all())
            print("======================================================================")
            for index, value in enumerate(subjectChoicePt3):
                for index2, value2 in enumerate(subjectGrade):
                    if (not(value and not value.isspace())) or (not(value2 and not value2.isspace())):
                        break
                    if index2 == index and index < len(student.grades.all()) and index2 < len(student.grades.all()):
                        if student.grades[index2].grade_subject != value2 and student.grades[index].name_subjectPT3 == value:
                            find_subject = student.grades[index]
                            student.grades.remove(find_subject)
                            student.grades.append(Grade(name_subjectPT3 = value, grade_subject = value2))
                            break
                    elif index2 == index and index >= len(student.grades.all()) and index2 >= len(student.grades.all()):
                        student.grades.append(Grade(name_subjectPT3 = value, grade_subject = value2))
                        break
                        # else:
                        #     student.grades.append(Grade(name_subjectPT3 = value, grade_subject = value2))
                        #     break
            db.session.commit()
            flash('The Student has been edited!','success')
            return redirect(url_for('manageStudent'))

    elif request.method == 'GET':
        form.studentName.data = student.student_name
        form.studentICNum.data = student.student_icNum
        form.studentClass.data = student.student_form4_class
        form.streamPackage.data = str(student.streamPackage_id)
        


    return render_template('teacher/updateStudent.html',title = "Update Student", form = form, school_focus = school_focus, student = student,subjectPT3 = subjectPT3, grade = grade)

@app.route("/teacher/manageStudent/student-<int:student_id>/delete/", methods = ["POST"])
@role_login_required(role = "teacher")
def delete_student(student_id):
    student = Student.query.get_or_404(student_id)
    if current_user.roles[0].name != "teacher":
        abort(403)
    
    db.session.delete(student)
    db.session.commit()
    flash("The Student has been deleted!", 'success')
    return redirect(url_for('manageStudent'))

@app.route("/getStudentRequestInfo/", methods = ["GET", "POST"])
def reqStudentInfo():
    if request.method == "POST":
        studentID = request.form['userid']
        find_student = RequestChange.query.filter_by(id = studentID).first()
    return jsonify({'studentRequestView': render_template('teacher/studentInfoView.html', find_student = find_student)})



@app.route("/teacher/reviewRequest/")
@role_login_required(role = "teacher")
def reviewRequest():
    teacher = Teacher.query.filter_by(id = current_user.teachers[0].id).first()
    school_focus = School.query.filter_by(id = teacher.school.id).first()
    page = request.args.get('page', 1, type = int)
    student_list = RequestChange.query.filter_by(school_id = school_focus.id).order_by(RequestChange.id.asc()).paginate(page = page, per_page = 5)

    return render_template('teacher/reviewRequest.html', title = 'Review Request', student_list = student_list)

@app.route("/teacher/manage-reviewRequest/delete/student-<int:request_id>/", methods = ["POST"])
@role_login_required(role = "teacher")
def delete_reviewRequest(request_id):
    find_student = RequestChange.query.get_or_404(request_id)
    if current_user.roles[0].name != "teacher":
        abort(403)
    
    db.session.delete(find_student)
    db.session.commit()
    flash("The Review Request has been deleted", 'danger')
    return redirect(url_for('reviewRequest'))

@app.route('/teacher/manage-reviewRequest/update/student-<int:student_id>-<int:streampackage_id>/', methods = ["POST"])
@role_login_required(role = "teacher")
def update_studentRequest(student_id,streampackage_id):
    student = Student.query.get_or_404(student_id)
    if current_user.roles[0].name != "teacher":
        abort(403)
    reqChangeForm = RequestChange.query.filter_by(student_id=student.id).first()
    # stream_package = StreamPackage.query.get_or_404(streampackage_id)
    if request.method == "POST":
        student.streamPackage_id = streampackage_id
        db.session.delete(reqChangeForm)
        db.session.commit()

        flash("The Student Stream Package was successfully updated!", 'success')
        return redirect(url_for('reviewRequest'))


#################################################################################################
#                                       Student                                                 #  
#################################################################################################

@app.route("/getSchool/<zone>")
def school(zone):
    school_data =  SchoolAddress.query.filter_by(zone_id = zone).all()
    schoolArray = []

    for index,school in enumerate(school_data):
        schoolObject = {}
        schoolObject['id'] = school.school_id
        find_school = School.query.filter_by(id = school.school_id).first()
        schoolObject['name'] = find_school.school_name
        schoolObject['code'] = find_school.school_code
        schoolArray.append(schoolObject)
    return jsonify({'schoolist':schoolArray})

@app.route("/getStreamPackage/<school>")
def getStream(school):
    stream_package = StreamPackage.query.filter_by(school_id = school).all()
    streamArray = []

    for streamValue in stream_package:
        streamObject = {}
        streamObject['id'] = streamValue.id
        streamObject['stream_name'] = streamValue.stream_name
        streamArray.append(streamObject)
    return jsonify({'streamlist': streamArray})





#Stream Checking 
@app.route("/streamcheck/", methods = ['GET', 'POST'])
def streamChecking():
    form = streamCheckForm()
    stringFormat = "{} - {}"
    form.schoolState.choices = [(state.id, stringFormat.format(state.state_code, state.state_name)) for state in State.query.all()]
    if form.validate_on_submit():
        #Do Checking if the Student Exist
        student = Student.query.filter_by(student_icNum = form.studentICNum.data).first()
        if student:
            if student.school.school_address[0].zones.id == int(form.schoolZon.data) and student.school.school_address[0].states.id == int(form.schoolState.data) and student.school.id == int(form.schoolName.data):
                return redirect(url_for('studentResults', student_id = student.id))
            else:
                flash('Student does not exists. Please try again.','danger')
                return redirect(url_for('streamChecking'))
        else:
            flash('Student does not exists. Please try again.','danger')
            return redirect(url_for('streamChecking')) 
    else:
        if form.errors:
            flash('Something is wrong with the input. Please try again.', 'danger')

    return render_template("student/checkResultForm.html", title = 'Stream Result Checking', form = form)


@app.route("/student/results/requestChange/", methods = ['GET', 'POST'])
def requestStreamChange():
    form = requestChangeForm()
    stringFormat = "{} - {}"
    form.schoolState.choices = [(state.id, stringFormat.format(state.state_code, state.state_name)) for state in State.query.all()]
    if form.validate_on_submit():
        find_student = Student.query.filter_by(student_icNum = form.studentIC.data).first()
        if find_student:
            # If Student submit form already, prevent it from being submitted again
            if find_student.requestChange:
                flash('The Student has submmited the request change stream form before, Please wait or contact your school teacher to check on your request change.','danger')
                return redirect(url_for('requestStreamChange'))
            if find_student.school.school_address[0].zones.id == int(form.schoolZon.data) and find_student.school.school_address[0].states.id == int(form.schoolState.data) and find_student.school.id == int(form.schoolName.data) and find_student.student_name == form.studentName.data:
                if find_student.stream_package.id == int(form.streamNewPackage.data):
                    flash("Please choose another stream package" , 'danger')
                    return redirect(url_for('requestStreamChange'))
                find_student.requestChange.append(RequestChange(student_name = form.studentName.data, 
                                                student_ic = form.studentIC.data, phoneNum = form.studentPhoneNum.data, \
                                                student_email = form.student_email.data ,
                                                streamPackage_id = form.streamNewPackage.data,
                                                school_id = form.schoolName.data, 
                                                reasonToChange =  form.reasonToChange.data,
                                                has_submitted = True))
                db.session.commit()
                flash('The Request change has been successfully saved!','success')
                return redirect(url_for('requestStreamChange'))
            else:
                flash("Student does not exists in our database2",'danger')
                return redirect(url_for('requestStreamChange'))
        else:
            flash("Student does not exists in our database", 'danger')
            return redirect(url_for('requestStreamChange'))
     
    return render_template("student/requestChangeForm.html", title = "Class Stream", form = form)

#@app.route("/student/results/<int:studIC>/")
@app.route("/student/results/<int:student_id>/")
def studentResults(student_id):
    student = Student.query.get_or_404(student_id)
    return render_template("student/ResultsOutput.html", title = "Class Stream" ,student =student)



