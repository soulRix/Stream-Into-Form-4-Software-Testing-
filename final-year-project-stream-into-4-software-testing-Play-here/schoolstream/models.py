from datetime import datetime
from itsdangerous import TimedJSONWebSignatureSerializer as Serializer
from flask_sqlalchemy import SQLAlchemy
#from flask_user import roles_required, UserManager, 
from schoolstream import app,db, login_manager
from flask_login import current_user,UserMixin

@login_manager.user_loader
def load_user(user_id):
        return User.query.get(int(user_id))


users_roles = db.Table(
    'users_roles',
    db.Column('user_id', db.Integer, db.ForeignKey('users.id', ondelete='CASCADE')),
    db.Column('role_id', db.Integer, db.ForeignKey('roles.id', ondelete='CASCADE'))
)

#Associate Table
subject_careers = db.Table(
    'subject_careers', 
    db.Column('subject_id' ,db.Integer, db.ForeignKey('subject.id', ondelete = 'CASCADE')), 
    db.Column('career_id' ,db.Integer, db.ForeignKey('careers.id', ondelete = 'CASCADE'))
)

stream_package_subject = db.Table(
    'stream_package_subjects',
    db.Column('subject_id' ,db.Integer, db.ForeignKey('subject.id', ondelete = 'CASCADE')), 
    db.Column('streamPackage_id', db.Integer, db.ForeignKey('stream_packages.id', ondelete = 'CASCADE'))
)


student_grade = db.Table(
    'student_grades',
    db.Column('student_id', db.Integer, db.ForeignKey('students.id', ondelete = 'CASCADE')),
    db.Column('grade_id', db.Integer, db.ForeignKey('grades.id', ondelete = 'CASCADE'))
)

#User class Model
#UserMixin is a class provides the implementation properties of (is_authenticated, is_active, is _anonymous, get_id)
class User(db.Model, UserMixin):
    __tablename__ = 'users'
    #Unique Id
    id = db.Column(db.Integer, primary_key=True) 

    #User Information
    name = db.Column(db.String(255), nullable = False) #Name
    icNumber = db.Column(db.String(14), unique = True,nullable = False)
    phoneNumber = db.Column(db.String(20), unique = True, nullable = False)
    email = db.Column(db.String(255),unique = True, nullable = False) #Email 
    image_file = db.Column(db.String(20), nullable = False, default='default.jpg') #Image, By default, they will have the same image
    password = db.Column(db.String(60), nullable = False)


    teachers = db.relationship('Teacher', backref = db.backref("user", lazy = True, passive_deletes = True))
   
    
    #Define the relationship to Role vis UserRoles
    #'user_roles' uses the tablename
    roles = db.relationship('Role', secondary = users_roles, backref = db.backref('roles', lazy = 'dynamic'))
    #teachers = db.relationship('Teacher', backref = 'teachers')

    #1800 seconds is 30 minutes
    def get_reset_token(self,expires_sec=1800):
        s = Serializer(app.config['SECRET_KEY'], expires_sec)
        return s.dumps({'user_id': self.id}).decode('utf-8')

    @staticmethod
    def verify_reset_token(token):
        s = Serializer(app.config['SECRET_KEY'])
        try:
            # User Id is the payload that user passed
            user_id = s.loads(token)['user_id']
        except:
            return None
        return User.query.get(user_id)

    #Object / Self Variable
    def __repr__(self):
        return f"User('{self.name}', '{self.email}', '{self.image_file}')"
    



#Define the Role data-model
class Role(db.Model):
    __tablename__ = 'roles'
    id = db.Column(db.Integer(), primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    #Reference 'users.id' is from the User tablename users


class Subject(db.Model):
    __tablename__ = 'subject'
    id = db.Column(db.Integer, primary_key=True)
    subject_title = db.Column(db.String(200), nullable=False)
    subject_category = db.Column(db.String(50), nullable = False)
    subject_description = db.Column(db.Text, nullable=False)
    form4Syallabus = db.relationship('Form4Syllabus', backref = db.backref("subject", lazy = True, passive_deletes=True))
    form5Syallabus = db.relationship('Form5Syllabus', backref = db.backref("subject", lazy = True, passive_deletes=True))
    
    careers = db.relationship('Career', secondary = subject_careers, backref = 'career_path')


    def __repr__(self):
        return f"Subject('{self.subject_title}', '{self.subject_category}')"
        #f"User('{self.name}', '{self.email}', '{self.image_file}')"

class Form4Syllabus(db.Model):
    __tablename__ = 'form4_syllabus'
    id = db.Column(db.Integer, primary_key=True)
    syllabusName = db.Column(db.String(500), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id', ondelete = 'CASCADE'))
    
    def __repr__(self):
        return f"Form4Syllabus('{self.syllabusName}', {self.subject_id})"

class Form5Syllabus(db.Model):
    __tablename__ = 'form5_syllabus'
    id = db.Column(db.Integer, primary_key=True)
    syllabusName = db.Column(db.String(500), nullable=False)
    subject_id = db.Column(db.Integer, db.ForeignKey('subject.id', ondelete = 'CASCADE'))

    
    def __repr__(self):
        return f"Form5Syllabus('{self.syllabusName}', {self.syllabusName})"




class Career(db.Model):
    __tablename__ = 'careers'
    id = db.Column(db.Integer, primary_key=True)
    career_name = db.Column(db.String(200), nullable=False)
    #career_pic = db.Column(db.String(20), nullable = False, default = 'default.jpg')


    def __repr__(self):
        return f"Career('{self.career_name}')"


class School(db.Model):
    __tablename__ = 'schools'
    id = db.Column(db.Integer, primary_key=True)
    school_name = db.Column(db.String(500), unique = True,nullable=False)
    shortSchool_name = db.Column(db.String(100))
    school_logo = db.Column(db.String(30), nullable = False, default='default_logo.png') #Image, By default, they will have the same image
    school_description = db.Column(db.Text)
    school_email = db.Column(db.String(100))
    school_code = db.Column(db.String(50), unique = True, nullable = False)
    shortForm = db.Column(db.String(20), nullable = False, default = "SMK")
    school_phoneNumber = db.Column(db.String(30), unique = True, nullable = False)
    school_moto = db.Column(db.Text)
    school_vision = db.Column(db.Text)
    

    #Relationship Database
    school_address = db.relationship('SchoolAddress', backref = db.backref('school', lazy = True, passive_deletes=True, uselist = False))
    stream_packages = db.relationship('StreamPackage', backref = db.backref('school', lazy = True, passive_deletes=True))
    students = db.relationship('Student', backref = db.backref('school', lazy = True, passive_deletes = True))
    teachers = db.relationship('Teacher', backref = db.backref('school', lazy = True, passive_deletes = True))
    requestChangeStudent = db.relationship('RequestChange', backref = db.backref('school',lazy = True, passive_deletes = True)) #Student Request for change
 
    def __repr__(self):
        return f"School('{self.id}','{self.school_name}','{self.school_code}' )"

class StreamPackage(db.Model):
    __tablename__ = 'stream_packages'
    id = db.Column(db.Integer, primary_key=True)
    stream_name = db.Column(db.String(100), nullable=False)

    #Relationship
    student = db.relationship('Student', backref = db.backref('stream_package', lazy = True, passive_deletes = True))
    subjects = db.relationship('Subject', secondary = stream_package_subject, lazy='dynamic', backref = db.backref('stream_package', lazy = True, passive_deletes = True))
    requestChangeStudent = db.relationship('RequestChange', backref = db.backref('stream_package', lazy = True, passive_deletes = True))

    #Relationship Database as ForeignKey
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id', ondelete = 'CASCADE'))

    def __repr__(self):
        return f"StreamPackage('{self.stream_name}', '{self.school_id}')"

class Student(db.Model):
    __tablename__ = 'students'
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(200), nullable = False)
    student_icNum = db.Column(db.String(14), unique = True, nullable = False)
    student_form4_class = db.Column(db.String(100), nullable = False)

    #Relationship

    #Relationship Database as ForeignKey
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id', ondelete = 'CASCADE'))
    streamPackage_id = db.Column(db.Integer, db.ForeignKey('stream_packages.id', ondelete = 'CASCADE'))
    grades = db.relationship('Grade', secondary = student_grade, lazy = 'dynamic', backref = db.backref('student',lazy = True, passive_deletes = True))
    requestChange = db.relationship('RequestChange', backref = db.backref('student', lazy = True, passive_deletes=True))
    
    def __repr__(self):
        return f"Student('{self.student_name}', '{self.student_icNum}', '{self.student_form4_class}')"
    
class Grade(db.Model):
    __tablename__ = 'grades'
    id = db.Column(db.Integer, primary_key=True)
    name_subjectPT3 = db.Column(db.String(255))
    grade_subject = db.Column(db.String(50))
    #subject_id = db.Column(db.Integer, db.ForeignKey('pt3Subjects.id',ondelete = 'CASCADE' ))
    

    def __repr__(self):
        return f"Grade('{self.name_subjectPT3}', '{self.grade_subject}')"



class SchoolAddress(db.Model):
    __tablename__ = 'school_address'
    id = db.Column(db.Integer, primary_key=True)
    address_name = db.Column(db.String(255), nullable = False)
    state_id = db.Column(db.Integer, db.ForeignKey('states.id', ondelete = 'CASCADE'))
    zone_id = db.Column(db.Integer, db.ForeignKey('zones.id', ondelete = 'CASCADE'))
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id', ondelete = 'CASCADE'), unique = True)
   
    def __repr__(self):
        return f"SchoolAddress('{self.id}','{self.state_id}','{self.zone_id}', '{self.school_id}')"


class State(db.Model):
    __tablename__ = 'states'
    id = db.Column(db.Integer, primary_key=True)
    state_code = db.Column(db.String(10), unique = True, nullable = False)
    state_name = db.Column(db.String(100), unique = True,nullable=False)
    zones = db.relationship('Zone' , backref=db.backref('states', lazy = True, passive_deletes = True))
    #One to One Relationship with School Address
    school_state = db.relationship('SchoolAddress' , backref=db.backref('states', lazy = True, passive_deletes = True, uselist =False))
    def __repr__(self):
        return f"State('{self.state_code}', '{self.state_name}')"


class Zone(db.Model):
    __tablename__ = 'zones'
    id = db.Column(db.Integer, primary_key=True)
    zone_name = db.Column(db.String(100), unique = True,nullable=False)
    zone_code = db.Column(db.String(100), unique = True,nullable=False)
    state_id = db.Column(db.Integer, db.ForeignKey('states.id', ondelete = 'CASCADE'))
    #One to One Relationship with School Address
    school_zone = db.relationship('SchoolAddress', backref=db.backref('zones', lazy = True, passive_deletes = True, uselist =False))

    def __repr__(self):
        return f"Zone('{self.zone_name}', '{self.zone_code}', '{self.state_id}')"
    

class Teacher(db.Model):
    __tablename__ = 'teachers'
    id = db.Column(db.Integer, primary_key=True)
    teacher_name  = db.Column(db.String(200),nullable=False)
    teacher_id = db.Column(db.String(50), unique = True,nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id', ondelete = 'CASCADE'))
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id', ondelete = 'CASCADE'))


    def __repr__(self):
        return f"Teacher('{self.teacher_name}', '{self.teacher_id}')"


class RequestChange(db.Model):
    __tablename__ = 'requestChange'
    id = db.Column(db.Integer, primary_key=True)
    student_name = db.Column(db.String(200),nullable=False)
    student_ic = db.Column(db.String(14), unique = True, nullable = False)
    phoneNum = db.Column(db.String(20), unique = True, nullable = False)


    student_email = db.Column(db.String(255), unique = True, nullable = False)

    reasonToChange = db.Column(db.Text)
    has_submitted = db.Column(db.Boolean, default= False)
    
    #Relationship
    school_id = db.Column(db.Integer, db.ForeignKey('schools.id', ondelete = 'CASCADE'))
    #The Requested Change Stream Package
    streamPackage_id = db.Column(db.Integer, db.ForeignKey('stream_packages.id', ondelete = 'CASCADE'))
    student_id = db.Column(db.Integer,db.ForeignKey('students.id', ondelete = 'CASCADE'))

    def __repr__(self):
        return f"Request Change('{self.student_name}', '{self.reasonToChange}')"
    




