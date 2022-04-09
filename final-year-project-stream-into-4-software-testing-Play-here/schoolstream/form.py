#Import Package
from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, TelField, BooleanField, SelectField, TextAreaField, FieldList, Form, FormField, SelectMultipleField,widgets
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError, Optional
from wtforms.widgets import TextArea
from schoolstream.models import User, Role, users_roles , Subject, stream_package_subject, School, StreamPackage, Student, SchoolAddress, State, Zone,Teacher, RequestChange
from flask_login import current_user

#Regular Expression
import re

class NonValidatingSelectField(SelectField):
    """
    Attempt to make an open ended select multiple field that can accept dynamic
    choices added by the browser.
    """
    def pre_validate(self, form):
        pass

def ic_format_field(form, field):
    icChecker = re.match("^\\d{6}\\-\\d{2}\\-\\d{4}$",field.data)
    validateIC = bool(icChecker)
    if validateIC is False:
        raise ValidationError('Field must be format in  XXXXXX-XX-XXXX')
    
    # if len(field.data) == 14:
    #     if not "-" in field.data and not field.data.isalpha():
    #         raise ValidationError('Field must be format in  XXXXXX-XX-XXXX')
    # #If the other variable is not equal 14 then raise the validation
    # else:
    #     raise ValidationError('Field must be format in  XXXXXX-XX-XXXX')

def phone_number_format(form, field):
    phoneChecker = re.match("^(\+?6?01)[0-46-9]-*[0-9]{7,8}$", field.data)
    validatePhone = bool(phoneChecker)
    if validatePhone is False:
        raise ValidationError('The phone number format must be XXX-XXXXXX')

def validate_state(form,field):
    if field.data is None:
        raise ValidationError('Please Select Your State')

def validate_zone(form,field):
    if field.data is None:
        raise ValidationError('Please Select Your Zone')

def validate_teacher_school(form,field):
    if field.data is None:
        raise ValidationError("Please Select The Teacher's school")

def validate_streamPackage(form, field):
    if field.data is None:
        raise ValidationError("Please Select The Student Class Stream")

def validate_student_school(form, field):
    if field.data is None:
        raise ValidationError("Please Select The School")



class RegistrationForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max = 50)])
    icNumber = StringField('IC Number', validators=[DataRequired(),ic_format_field])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phoneNumber = TelField('Phone Number', validators=[DataRequired(),phone_number_format])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    #Validation Methods
    #This is template for validation... 
    # def validate_field(self, field):
    #     if True:
    #         raise ValidationError('Validation Message')

    def validate_icNumber(self, icNumber):
        user_ic = User.query.filter_by(icNumber = icNumber.data).first()
        if user_ic:
            raise ValidationError('The IC Number is already registered')
    
    def validate_phoneNumber(self, phoneNumber):
        user_phone = User.query.filter_by(phoneNumber = phoneNumber.data).first()
        if user_phone:
            raise ValidationError('The Phone Number is already registered')
    
    def validate_email(self, email):
        user_email = User.query.filter_by(email = email.data).first()
        if user_email:
            raise ValidationError('The Email is already registered')
        
    


class LoginForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')



class UpdateAccountForm(FlaskForm):
    name = StringField('Name', validators=[DataRequired(), Length(min=2, max = 50)])
    icNumber = StringField('IC Number', validators=[DataRequired(),ic_format_field])
    email = StringField('Email', validators=[DataRequired(), Email()])
    picture = FileField('Update Profile Picture', validators=[FileAllowed(['jpg', 'png'])])
    submit = SubmitField('Update Account')
    
    def validate_email(self, email):
        if email.data != current_user.email:
            user_email = User.query.filter_by(email = email.data).first()
            if user_email:
                raise ValidationError('The Email is already taken')

    def validate_icNumber(self, icNumber):
        if icNumber.data != current_user.icNumber:
            user_ic = User.query.filter_by(icNumber = icNumber.data).first()
            if user_ic:
                raise ValidationError('The IC Number is already registered')


class AddSubjectElectiveForm(FlaskForm):
    nameSubject =  StringField('Subject Name', validators = [DataRequired(), Length(min = 2, max = 50)])
    subjectCategory = SelectField('Subject Category', validators = [DataRequired()], choices=[('Pure Science', 'Pure Science'), ('Social Science & Religion', 'Social Science & Religion'), ('Arts and Health', 'Arts and Health'), ('Languages and Literature', 'Languages and Literature'), ('Economics & Business', 'Economics & Business'), ('Technical and Vocational', 'Technical and Vocational')])
    subjectDescription = TextAreaField('Subject Description', render_kw={"rows": 15, "cols": 20}, validators = [DataRequired()])
    submit = SubmitField('Add Subject')


class SchoolForm(FlaskForm):
    schoolName = StringField('School Full Name', validators = [DataRequired(), Length(min = 2, max = 100)]) 
    schoolLogo = FileField('School Logo Picture', validators=[FileAllowed(['jpg', 'png'])])
    schoolDescription = TextAreaField('School Description', render_kw={"rows": 9, "cols": 20}, validators = [DataRequired()])
    schoolAddress = TextAreaField('School Address', render_kw={"rows": 9, "cols": 20}, validators = [DataRequired()])
    schoolState = SelectField('School State', choices = [], validators = [validate_state])
    schoolZon = SelectField('School Zone',choices=[],validators = [validate_zone] ,validate_choice = False)

    shortSchoolName = StringField('School Short Name', validators = [Optional(), Length(min = 2, max = 100)]) 

    schoolCode = StringField('School Code', validators = [DataRequired(), Length(min = 2, max = 100)]) 
    shortForm =  SelectField('School Type', validators = [DataRequired()], choices=[('SMK', 'Sekolah Menengah Kebangsaan (SMK)'), ('SM', 'Sekolah Menengah  (SM)'), ('SBP', 'Sekolah Berasrama Penuh (SBP)'), ('SMs', 'Sekolah Menengah Sains (SMs)'), ('KJ', 'Kolej (KJ)'),('SABK', 'Sekolah Agama Bantuan Kerajaan (SABK)'), ('KV', 'Kolej Vokasional (KV)'), ('SMKA','Sekolah Menengah Kebangsaan Agama (SMKA)'), ('SMT', 'Sekolah Menengah Teknik (SMT)'), ('MK', 'Modal Khas')])
    schoolEmail = StringField('School Email', validators=[Optional(), Email()])
    schoolPhoneNumber = TelField('School Contact Number', validators=[DataRequired()])
    schoolMoto = StringField('School Moto', validators = [Optional()]) 
    schoolVision = StringField('School Vision', validators = [Optional()]) 
    submit = SubmitField('Add School')


    def validate_schoolName(self, schoolName):
        school_exist = School.query.filter_by(school_name = schoolName.data).first()
        if school_exist:
            raise ValidationError('The School name is already registered')
        
        
    
    def validate_schoolCode(self, schoolCode):
        if len(schoolCode.data) < 30:
            school_code = School.query.filter_by(school_code = schoolCode.data).first()
            if school_code:
                raise ValidationError('The School Code Number is already registered')
    
    def validate_schoolPhoneNumber(self, schoolPhoneNumber):
        school_phone = School.query.filter_by(school_phoneNumber = schoolPhoneNumber.data).first()
        if school_phone:
            raise ValidationError('The School Number is already taken')


    def validate_email(self, email):
        current_school = School
        if email.data != current_user.email:
            user_email = User.query.filter_by(email = email.data).first()
            if user_email:
                raise ValidationError('The Email is already taken')


class UpdateSchoolForm(FlaskForm):
    schoolName = StringField('School Full Name', validators = [DataRequired(), Length(min = 2, max = 100)]) 
    schoolLogo = FileField('School Logo Picture', validators=[FileAllowed(['jpg', 'png'])])
    schoolDescription = TextAreaField('School Description', render_kw={"rows": 9, "cols": 20}, validators = [DataRequired()])
    schoolAddress = TextAreaField('School Address', render_kw={"rows": 9, "cols": 20}, validators = [DataRequired()])
    schoolState = SelectField('School State', choices = [], validators = [validate_state])
    schoolZon = SelectField('School Zone',choices=[],validators = [validate_zone] ,validate_choice = False)

    shortSchoolName = StringField('School Short Name', validators = [Optional(), Length(min = 2, max = 100)]) 

    schoolCode = StringField('School Code', validators = [DataRequired(), Length(min = 2, max = 100)]) 
    shortForm =  SelectField('School Type', validators = [DataRequired()], choices=[('SMK', 'Sekolah Menegah Kebangsaan (SMK)'), ('SM', 'Sekolah Menegah (SM)'), ('SBP', 'Sekolah Berasrama Penuh (SBP)'), ('SMs', 'Sekolah Menegah Sains (SMs)'), ('KJ', 'Kolej (KJ)'),('SABK', 'Sekolah Agama Bantuan Kerajaan (SABK)'), ('KV', 'Kolej Vokasional (KV)'), ('SMKA','Sekolah Menegah Kebangsaan Agama (SMKA)'), ('SMT', 'Sekolah Menegah Teknik (SMT)'), ('MK', 'Modal Khas')])
    schoolEmail = StringField('School Email', validators=[Optional(), Email()])
    schoolPhoneNumber = TelField('School Contact Number', validators=[DataRequired()])
    schoolMoto = StringField('School Moto', validators = [Optional()]) 
    schoolVision = StringField('School Vision', validators = [Optional()]) 
    submit = SubmitField('Update School')

    def __init__(self, school, *args, **kwargs):
        super(UpdateSchoolForm, self).__init__(*args, **kwargs)
        # super().__init__(*args, **kwargs) for Python 3
        self.school = school

    def validate_schoolName(self, schoolName):
        if self.school.school_name != schoolName.data:
            school_exist = School.query.filter_by(school_name = schoolName.data).first()
            if school_exist:
                raise ValidationError('The School name is already registered')
        
        
    
    def validate_schoolCode(self, schoolCode):
        if self.school.school_code != schoolCode.data:
            school_code = School.query.filter_by(school_code = schoolCode.data).first()
            if school_code:
                raise ValidationError('The School Code Number is already registered')
    
    def validate_schoolPhoneNumber(self, schoolPhoneNumber):
        if self.school.school_phoneNumber != schoolPhoneNumber.data:
            school_phone = School.query.filter_by(school_phoneNumber = schoolPhoneNumber.data).first()
            if school_phone:
                raise ValidationError('The School Number is already taken')


class TeacherForm(FlaskForm):
    name = StringField("Teacher's Name", validators=[DataRequired(), Length(min=2, max = 50)])
    icNumber = StringField('IC Number', validators=[DataRequired(),ic_format_field])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phoneNumber = TelField('Phone Number', validators=[DataRequired(),phone_number_format])
    teacher_id = StringField('Teacher ID', validators = [DataRequired(), Length(min = 2, max = 100)]) 
    password = PasswordField('Password', validators=[DataRequired()])
    school = SelectField("Teacher's School", choices = [], validators = [validate_teacher_school])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Create Teacher Account')


    def validate_icNumber(self, icNumber):
        user_ic = User.query.filter_by(icNumber = icNumber.data).first()
        if user_ic:
            raise ValidationError('The IC Number is already registered')
    
    def validate_phoneNumber(self, phoneNumber):
        user_phone = User.query.filter_by(phoneNumber = phoneNumber.data).first()
        if user_phone:
            raise ValidationError('The Phone Number is already registered')
    
    def validate_email(self, email):
        user_email = User.query.filter_by(email = email.data).first()
        if user_email:
            raise ValidationError('The Email is already registered')
    
    def validate_teacher_id(self, teacher_id):
        teacher = Teacher.query.filter_by(teacher_id = teacher_id.data).first()
        if teacher:
            raise ValidationError('The Teacher ID is already registered')

class UpdateTeacherForm(FlaskForm):
    name = StringField("Teacher's Name", validators=[DataRequired(), Length(min=2, max = 50)])
    icNumber = StringField('IC Number', validators=[DataRequired(),ic_format_field])
    email = StringField('Email', validators=[DataRequired(), Email()])
    phoneNumber = TelField('Phone Number', validators=[DataRequired(),phone_number_format])
    teacher_id = StringField('Teacher ID', validators = [DataRequired(), Length(min = 2, max = 100)]) 
    school = SelectField("Teacher's School", choices = [], validators = [validate_teacher_school])
    submit = SubmitField('Update Account')

    def __init__(self, teacher, *args, **kwargs):
        super(UpdateTeacherForm, self).__init__(*args, **kwargs)
        # super().__init__(*args, **kwargs) for Python 3
        self.teacher = teacher

    def validate_icNumber(self, icNumber):
        if self.teacher.user.icNumber != icNumber.data:
            user_ic = User.query.filter_by(icNumber = icNumber.data).first()
            if user_ic:
                raise ValidationError('The IC Number is already registered')
    
    def validate_phoneNumber(self, phoneNumber):
        if self.teacher.user.phoneNumber != phoneNumber.data:
            user_phone = User.query.filter_by(phoneNumber = phoneNumber.data).first()
            if user_phone:
                raise ValidationError('The Phone Number is already registered')
    
    def validate_email(self, email):
        if self.teacher.user.email != email.data:
            user_email = User.query.filter_by(email = email.data).first()
            if user_email:
                raise ValidationError('The Email is already registered')
    
    def validate_teacher_id(self, teacher_id):
        if self.teacher.teacher_id != teacher_id.data:
            teacher = Teacher.query.filter_by(teacher_id = teacher_id.data).first()
            if teacher:
                raise ValidationError('The Teacher ID is already registered')







class StudentForm(FlaskForm):
    studentName = StringField("Student Name", validators = [DataRequired(), Length(min = 2, max = 70)])
    studentICNum = StringField('IC Number', validators=[DataRequired(),ic_format_field])
    studentClass = StringField("Class Name", validators=[DataRequired()])
    streamPackage = SelectField("Stream Class", choices = [], validators = [validate_streamPackage])
    submit = SubmitField('Add Student')

    def validate_studentICNum(self,studentICNum):
        student_ic = Student.query.filter_by(student_icNum = studentICNum.data).first()
        if student_ic:
            raise ValidationError('The Student IC Number is already registered')

class UpdateStudentForm(FlaskForm):
    studentName = StringField("Student Name", validators = [DataRequired(), Length(min = 2, max = 70)])
    studentICNum = StringField('IC Number', validators=[DataRequired(),ic_format_field])
    studentClass = StringField("Class Name", validators=[DataRequired()])
    streamPackage = SelectField("Stream Class", choices = [], validators = [validate_streamPackage])
    submit = SubmitField('Update Student')

    def __init__(self, student, *args, **kwargs):
        super(UpdateStudentForm, self).__init__(*args, **kwargs)
        # super().__init__(*args, **kwargs) for Python 3
        self.student = student

    def validate_studentICNum(self,studentICNum):
        if self.student.student_icNum != studentICNum.data:
            student_ic = Student.query.filter_by(student_icNum = studentICNum.data).first()
            if student_ic:
                raise ValidationError('The Student IC Number is already registered')


class streamCheckForm(FlaskForm):
    studentICNum = StringField('IC Number', validators=[DataRequired(),ic_format_field])
    schoolState = SelectField('School State', choices = [], validators = [validate_state])
    schoolZon = SelectField('School Zone',choices=[],validators = [validate_zone] ,validate_choice = False)
    schoolName = SelectField("School", choices = [], validators = [validate_student_school], validate_choice = False)
    submit = SubmitField('Check')

    def validate_icNumber(self, icNumber):
        student_ic = Student.query.filter_by(icNumber = icNumber.data).first()
        if not(student_ic):
            raise ValidationError('The Student Idetity Card does not exist.')


class requestChangeForm(FlaskForm):
    studentName =  StringField("Student Name", validators = [DataRequired(), Length(min = 2, max = 70)])
    studentIC = StringField('Student Identity Card (IC Number)', validators=[DataRequired(),ic_format_field])
    studentPhoneNum = TelField('Phone Number', validators=[DataRequired(),phone_number_format])
    student_email = StringField('Email', validators=[Optional(), Email()])

    schoolState = SelectField('School State', choices = [], validators = [validate_state])
    schoolZon = SelectField('School Zone',choices=[],validators = [validate_zone] ,validate_choice = False)
    schoolName = SelectField("School", choices = [], validators = [validate_student_school], validate_choice = False)

    streamNewPackage = SelectField("Stream Option (Class Stream to Change) ", choices = [], validators = [validate_streamPackage], validate_choice = False)
    reasonToChange = TextAreaField('Reason to Change', render_kw={"rows": 9, "cols": 20}, validators = [DataRequired()])

    submit = SubmitField('Submit')

    def validate_studentIC(self, studentIC):
        student_ic = RequestChange.query.filter_by(student_ic = studentIC.data).first()
        if student_ic:
            raise ValidationError('This Student IC has submitted a request change form before, Please try later.')
    
    def validate_studentPhoneNum(self, studentPhoneNum):
        student_num = RequestChange.query.filter_by(phoneNum = studentPhoneNum.data).first()
        if student_num:
            raise ValidationError('This Student Phone Number has submitted a request change form before, Please try later.')
    
    def validate_student_email(self, student_email):
        student_email = RequestChange.query.filter_by(student_email = student_email.data).first()
        if student_email:
            raise ValidationError('This student Email has submitted a request change form before, Please try later.')


    
class RequestResetForm(FlaskForm):
    email = StringField('Email', validators=[DataRequired(), Email()])
    submit = SubmitField('Request Password Reset')


    def validate_email(self, email):
        user_email = User.query.filter_by(email = email.data).first()
        if user_email is None:
            raise ValidationError('Email is not found, Please try again.')

class ResetPasswordForm(FlaskForm):
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Reset Password')

class ChangePasswordForm(FlaskForm):
    old_password = PasswordField('Old Password', validators=[DataRequired()])
    password = PasswordField('New Password', validators=[DataRequired()])
    confirm_password = PasswordField('Confirm New Password', validators=[DataRequired(), EqualTo('password')])
    
    submit = SubmitField('Change Password')