#Setup Flask-USer and specify the User data-model
#user_manager = UserManager(app,db,User)



#db.create_all()
#db.drop_all()
#Creating a dummy User
#user_1 = User(name = "tuan", icNumber="001104-14-1495", phoneNumber = "0193013988", email = "admin@test.com", password = "12345")
#user_2 = User(name = "arif", icNumber="001104-14-1496", phoneNumber = "0193013983", email = "arif@test.com", password = "12345")
#db.session.add(user_1) #Just to add
#db.session.commit() #Commit the user into the database

#Subject
#subject_1 = Subject(subject_title = "Physics",subject_category = "Pure Science", subject_description = "Physics is Awesome", user_id=user.id)
#subject_2 = Subject(subject_title = "Pendidikan Seni Visual",subject_category = "Arts and Health", subject_description = "Arts is really Awesome", user_id=user.id)

#user.subjects[1].subject_title

#Query SQL
#User.query.all()
# User.query.first()
# User.query.filter_by(name='tuan').all()

#Assign the user
# user = User.query.filter_by(name='tuan').first()
# so now if we want to find the user id
# we can just type in user.id

# #Elective to Subject
# class ElectivesCategory(db.Model):
#     __tablename__ = 'electives_catergory'
#     id = db.Column(db.Integer, primary_key=True)
#     elective_title = db.Column(db.String(50), nullable=False, unique = True)
#     subjects = db.relationship('Subject', backref = 'electives') #One to Many Relation Ship
#     #One Elective Section can have multiple of Subject

#======================================================================================
#New Database 6/3/2022
# from schoolstream import app, db, bcrypt
# from schoolstream.models import User, Role, users_roles,Subject,Student, Teacher,School, Career, Form5Syllabus, Form4Syllabus, subject_careers,SchoolAddress,State,Zone, stream_package_subject,StreamPackage, Grade, student_grade, RequestChange
#db.create_all()
#db.drop_all()
#user = User.query.filter_by(name='admin').first()
#user.roles
#user.roles.has_permission
#user.roles[0].name

#===============================================================================================#
#                           User Admin and Teacher Example                                      #
#===============================================================================================#
# password1 = bcrypt.generate_password_hash("testing").decode("utf8")
# user1 = User(name = "admin", icNumber = "001105-12-1849", phoneNumber = "0193111232", email = "admin@test.com", password = password1)
# user1.roles.append(Role(name = 'admin_SchoolStream'))
# db.session.add(user1)
# db.session.commit()


#### Do NOT RUN THIS IN THE PYTHON CODE ####
# password2 = bcrypt.generate_password_hash("testing").decode("utf8")
# user2 = User(name = "teacher", icNumber = "001203-12-1239", phoneNumber = "0192213292", email = "teacher@test.com", password = password2)
# user2.roles.append(Role(name = 'teacher'))
# user2.teachers.append(Teacher(teacher_name = 'teacher', teacher_id = "teacher", school_id = 1))
# db.session.add(user2)
# db.session.commit()


#===============================================================================================#
#                           Subject Example                                                     #
#===============================================================================================#
# physics = Subject(subject_title = "Physics", subject_category = "Pure Science", subject_description = "Physics is the natural science that studies matter, its fundamental constituents, its motion and behavior through space and time, and the related entities of energy and force. Physics is one of the most fundamental scientific disciplines, and its main goal is to understand how the universe behaves.")
# physics.form4Syallabus.append(Form4Syllabus(syllabusName = "Measurements"))
# physics.form4Syallabus.append(Form4Syllabus(syllabusName = "Force & Motion 1"))
# physics.form4Syallabus.append(Form4Syllabus(syllabusName = "Gravitation"))
# physics.form4Syallabus.append(Form4Syllabus(syllabusName = "Heat"))
# physics.form4Syallabus.append(Form4Syllabus(syllabusName = "Waves"))
# physics.form4Syallabus.append(Form4Syllabus(syllabusName = "Light & Optics"))
# physics.form5Syallabus.append(Form5Syllabus(syllabusName = "Force and Motion 2"))
# physics.form5Syallabus.append(Form5Syllabus(syllabusName = "Pressure"))
# physics.form5Syallabus.append(Form5Syllabus(syllabusName = "Electricity"))
# physics.form5Syallabus.append(Form5Syllabus(syllabusName = "Electromagnetism"))
# physics.form5Syallabus.append(Form5Syllabus(syllabusName = "Electronics"))
# physics.form5Syallabus.append(Form5Syllabus(syllabusName = "Nuclear Physics"))
# physics.form5Syallabus.append(Form5Syllabus(syllabusName = "Quantum Physics"))
# db.session.add(physics)
# db.session.commit()

# chemistry = Subject(subject_title = "Chemistry", subject_category = "Pure Science", subject_description = "Chemistry is the study of substances—that is, elements and compounds—while biology is the study of living things. However, these two branches of science meet in the discipline of biochemistry, which studies the substances in living things and how they change within an organism.")
# chemistry.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 1 - Introduction to Chemistry"))
# chemistry.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 2 - The Structure of the Atom"))
# chemistry.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 3 - Chemical Formulae and Equations"))
# chemistry.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 4 - Periodic Table of Elements"))
# chemistry.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 5 - Chemical Bonds"))
# chemistry.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 6 - Acids, Bases and Salt"))
# chemistry.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 7 - Rate of Reaction"))
# chemistry.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 8 - Manufactured Substances in Industries"))
# chemistry.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 1 -	Redox Equilibrium"))
# chemistry.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 2 -	Carbon Compound"))
# chemistry.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 3 -	Thermochemistry"))
# chemistry.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 4 -	Polymer"))
# chemistry.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 5 -	Consumer and Industrial Chemistry"))
# db.session.add(chemistry)
# db.session.commit()


# bm = Subject(subject_title = "Malay Language" ,  subject_category = "Languages and Literature" , subject_description = "This is Malay Language, Trying Out Malay is Fun!")
# bm.form4Syallabus.append(Form4Syllabus(syllabusName = "Tema 1 - Merealisasikan Impian"))
# bm.form4Syallabus.append(Form4Syllabus(syllabusName = "Tema 2 - Insan Terdidik, Negara Sejahtera"))
# bm.form4Syallabus.append(Form4Syllabus(syllabusName = "Tema 3 - Memetik Bintang"))
# bm.form4Syallabus.append(Form4Syllabus(syllabusName = "Tema 4 - Menjulang Harapan Di Bumi Bertuah"))
# bm.form4Syallabus.append(Form4Syllabus(syllabusName = "Tema 5 - Memacu Producktiviti"))
# bm.form5Syallabus.append(Form5Syllabus(syllabusName = "Tema 1 - Anda Besih, Anda Sihat"))
# bm.form5Syallabus.append(Form5Syllabus(syllabusName = "Tema 2 - Sukan dan Rekreasi"))
# bm.form5Syallabus.append(Form5Syllabus(syllabusName = "Tema 3 - Kerjaya Meniti Jaya"))
# bm.form5Syallabus.append(Form5Syllabus(syllabusName = "Tema 4 - Bersatu Kita Teguh"))
# bm.form5Syallabus.append(Form5Syllabus(syllabusName = "Tema 5 - Pendidikan untuk Semua"))
# db.session.add(bm)
# db.session.commit()

# english = Subject(subject_title = "English Literature",  subject_category = "Languages and Literature", subject_description = "This is English Language, Trying Out English is Fun!")
# english.form4Syallabus.append(Form4Syllabus(syllabusName = "Module 1 - Speaking"))
# english.form4Syallabus.append(Form4Syllabus(syllabusName = "Module 2 - Writing a Poetry"))
# english.form4Syallabus.append(Form4Syllabus(syllabusName = "Module 3 - Talk with Me!"))
# english.form4Syallabus.append(Form4Syllabus(syllabusName = "Module 4 - Careers"))
# english.form5Syallabus.append(Form5Syllabus(syllabusName = "Module 1 - Vocalbulary"))
# english.form5Syallabus.append(Form5Syllabus(syllabusName = "Module 2 - Grammar & Error Grammar"))
# english.form5Syallabus.append(Form5Syllabus(syllabusName = "Module 3 - Grammar & Error Grammar"))
# english.form5Syallabus.append(Form5Syllabus(syllabusName = "Module 4 - Reading Skills"))
# db.session.add(english)
# db.session.commit()

# math = Subject(subject_title = "Mathematics",  subject_category = "Pure Science", subject_description = "This is Mathematics, Trying Out Math is Fun!")
# math.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 1 - Quadratic Functions and Equations in One Variable"))
# math.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 2 - Number Bases"))
# math.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 3 - Logical Reasoning"))
# math.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 4 - Opeartions on Sets"))
# math.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 5 - Network in Graph Theory"))
# math.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 6 - Linear Inequalities in Two Variables"))
# math.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 7 - Graph of Motion"))
# math.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 8 - Measures of Dispersion for Ungrouped Data"))
# math.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 9 - Probability of Combined Events"))
# math.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 10 - Counsumer Mathematics : Financial Management"))
# math.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 1 - Variation"))
# math.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 2 - Matrices"))
# math.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 3 - Consumer Mathematics : Insurance"))
# math.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 4 - Consumer Mathematics : Taxation"))
# math.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 5 - Congruency, Enlargement and Combined Transformations"))
# math.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 6 - Ratios and Graphs of Trigonometric Function"))
# math.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 7 - Measures of Dispersion for Grouped Data"))
# math.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 8 - Mathematical Modeling"))
# db.session.add(math)
# db.session.commit()

# islam = Subject(subject_title = "Islam Studies",  subject_category = "Social Science & Religion" , subject_description = "This is Islam Studies, Learning Islam Studies is Fun!")
# islam.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 1 - Al-Quran"))
# islam.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 2 - Hadiths"))
# islam.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 3 - Aqidah"))
# islam.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 4 - Feqah"))
# islam.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 1 - Sirah and Islamic Civilization"))
# islam.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 2 - Islamic Behaviours"))
# islam.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 3 - Welfare Management After Death"))
# db.session.add(islam)
# db.session.commit()

# history = Subject(subject_title = "History" ,  subject_category = "Social Science & Religion" , subject_description = "This is History, Trying Out History is Fun!")
# history.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 1 - Warisan Negara Bangsa"))
# history.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 2 - Kebangkitan Nasionalisme"))
# history.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 3 - Konflik Dunia dan Pendudukan Jepun di Negara Kita"))
# history.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 4 - Era Peralihan Kuasa British di Negara Kita"))
# history.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 1 - Kedaulatan Negara"))
# history.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 2 - Perlembagaan Persekutuan"))
# history.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 3 - Raja Berperlembagaan dan Demokrasi Berparlimen"))
# db.session.add(history)
# db.session.commit()


# acc = Subject(subject_title = "Principles of Accounting",  subject_category = "Economics & Business", subject_description = "This is Accounting, Trying Out Accounting is Fun!")
# acc.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 01 - Introduction to Accounting"))
# acc.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 02: Account classification: Assets, Liabilities, Owner's Equity, Revenue, Expenses and Contra Accounts"))
# acc.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 03: Business Documents as the Source of Information"))
# acc.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 04: Journal As The First Book of Entry"))
# acc.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 05: Ledgers"))
# acc.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 06: Trial Balance"))
# acc.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 07: Financial Statements - Sole Proprietorship"))
# acc.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 01: Accounting for Cash"))
# acc.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 02: Accounting for Payroll"))
# acc.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 03: Partnership"))
# acc.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 04: Limited Company"))
# acc.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 05: Clubs and Societies"))
# acc.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 06: Incomplete Records"))
# acc.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 07: Introduction to Management Accounting"))
# acc.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 08: Information for Decision Making"))
# db.session.add(acc)
# db.session.commit()


# addmath = Subject(subject_title = "Additional Mathematics" ,  subject_category = "Pure Science" , subject_description = "This is Additional Mathematics, Trying Out Additional Mathematics is Fun!")
# addmath.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 1 : Functions"))
# addmath.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 2 : Quadratic Functions"))
# addmath.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 3 : Equation Systems"))
# addmath.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 4 : Indices, Surds and Logarithms"))
# addmath.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 5 : Progressions"))
# addmath.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 6 : Linear Law"))
# addmath.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 7 : Statistics"))
# addmath.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 8 : Vectors"))
# addmath.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 1 : Circular Measure"))
# addmath.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 2 : Differentiation"))
# addmath.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 4 : Permutations and Combinations"))
# addmath.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 5 : Probability Distributions"))
# addmath.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 6 : Trigonometric Functions"))
# db.session.add(addmath)
# db.session.commit()

# ict = Subject(subject_title = "Computer Science",  subject_category = "Technical and Vocational", subject_description = "This is Computer Science, Trying Out Computer Sciences is Fun!")
# ict.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 1 : Programming Language"))
# ict.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 2 : Human Intraction with Computers"))
# ict.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 3 : Networking"))
# ict.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 1 : Computation"))
# ict.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 2 : Database"))
# ict.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 2 : Web Development"))
# db.session.add(ict)
# db.session.commit()


# bio = Subject(subject_title = "Biology" ,  subject_category = "Pure Science" , subject_description = "This is Biology, Trying Out Biology is Fun!")
# bio.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 1 : Cell Structure"))
# bio.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 2 : Movement across Plasma Membrane"))
# bio.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 3 : Chemical Composition of Cell Chemical"))
# bio.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 1 : Support and Locomotion"))
# bio.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 2 : Coordination and Response"))
# bio.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 3 : Reproduction and Growth"))
# db.session.add(bio)
# db.session.commit()



# seni = Subject(subject_title = "Art Visual Studies",  subject_category = "Arts and Health" , subject_description = "This is Arts, Trying Out Art Visual is Fun!")
# seni.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 1 : Colours"))
# seni.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 1 : Shapes"))
# db.session.add(seni)
# db.session.commit()

# science = Subject(subject_title = "Science" ,  subject_category = "Pure Science" , subject_description = "This is Science, Trying Out Science is Fun!")
# science.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 1 : Techniques of Measuring the Parameters of Body Health"))
# science.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 1 : Nutrition and Food Technology"))
# db.session.add(science)
# db.session.commit()


# economy = Subject(subject_title = "Economy" ,  subject_category = "Economics & Business" , subject_description = "This is Economy, Trying Out Economy is Fun!")
# economy.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 1 : Introduction to Economy"))
# economy.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 2 : Marketing"))
# economy.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 3 : Money, Bank, Individual Income"))
# economy.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 4 : Production"))
# economy.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 1 : Economy and Government"))
# economy.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 2 : Malaysia and The Global Economy"))
# db.session.add(economy)
# db.session.commit()

# business = Subject(subject_title = "Business" ,  subject_category = "Economics & Business" , subject_description = "This is Business, Trying Out Business is Fun!")
# business.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 1 : Purpose of Business and Business Ownership"))
# business.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 2 : The Trend of Business "))
# business.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 3 : Setting Business Vision, Mission and Objectives"))
# business.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 4 : Functionality of Business Organization"))
# business.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 1 : Business resources"))
# business.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 2 : Resource Management and Technology"))
# business.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 3 : Sources of Business Financing"))
# business.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 4 : Business Financial Statements"))
# db.session.add(business)
# db.session.commit()

# home = Subject(subject_title = "Home Science" ,  subject_category = "Social Science & Religion" , subject_description = "This is Home Science, Trying Out Home Science is Fun!")
# home.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 1 : Human Teamwork"))
# home.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 2 : Family and Residential Resource Management"))
# home.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 3 : Clothing and Sewing"))
# home.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 4 : Science in Food"))
# home.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 5 : Business and entrepreneurship"))
# home.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 1 : Workplace Safety in the Hospitality Industry"))
# home.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 2 : Sanitation in Food Preparation and Storage"))
# home.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 3 : Food Preparation and Serving Equipment"))
# home.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 4 : Food Management"))
# db.session.add(home)
# db.session.commit()

# tasawwurIslam = Subject(subject_title = "Tasawwur Islam" ,  subject_category = "Social Science & Religion" , subject_description = "This is Tasawwur Islam, Trying Out Tasawwur Islam is Fun!")
# tasawwurIslam.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 1 : Islam as al-Din"))
# tasawwurIslam.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 2 : Islam Socialism"))
# tasawwurIslam.form4Syallabus.append(Form4Syllabus(syllabusName = "Chapter 3 : Human as a servant and caliph of Allah SWT"))
# tasawwurIslam.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 1 : Islamic Economic and Financial System"))
# tasawwurIslam.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 2 : Islamic Legal and Judicial System"))
# tasawwurIslam.form5Syallabus.append(Form5Syllabus(syllabusName = "Chapter 3 : Islamic System of Administration and Government"))
# db.session.add(tasawwurIslam)
# db.session.commit()

#===============================================================================================#
#                                   Career                                                      #
#===============================================================================================#
# career = Career(career_name = "Architect")
# career1 = Career(career_name = "Physicist")
# career2 = Career(career_name = "Electric Engineer")
# career3 = Career(career_name = "Teacher")
# career4 = Career(career_name = "Technician")
# career5 = Career(career_name = "Pilot")
# career6 = Career(career_name = "Software Engineer")
# career7 = Career(career_name = "Mobile App Developer")
# career8 = Career(career_name = "Accountant")
# career9 = Career(career_name = "Civil Engineer")
# career10 = Career(career_name = "Human Resource Manager")
# career11 = Career(career_name = "Graphic Designers")
# career12 = Career(career_name = "Game Developers")
# career13 = Career(career_name = "Lawyer")
# career14 = Career(career_name = "Food Scientist")
# career15 = Career(career_name = "Doctor")
# career16 = Career(career_name = "Animator")
# career17 = Career(career_name = "Mechanical Engineer")
# career18 = Career(career_name = "Accountant")
# career19 = Career(career_name = "Business Manager")
# career20 = Career(career_name = "Business Analyst")
# career21 = Career(career_name = "Chemical Engineer")
# career22 = Career(career_name = "Pharmacologist")
# career23 = Career(career_name = "Forensic Scientist")
# career24 = Career(career_name = "Scientist")

# career25 = Career(career_name = "Translator")
# career26 = Career(career_name = "Journalist")
# career27 = Career(career_name = "Interpreters")
# career28 = Career(career_name = "Preacher")
# career29 = Career(career_name = "Islamic Studies")
# career30 = Career(career_name = "Zoologist")
# career31 = Career(career_name = "Historical consultant")
# career32 = Career(career_name = "Politician")

# db.session.add_all([career,career1,career2, career3,career4,career5,career6,career7,career8,career9,career10,career11,career12,\
# career13,career14,career15,career16,career17, career18, career19, career20, career21, career22,career23,career24, career25,career26,career27,career28,\
# career29, career30,career31,career32])
# db.session.commit()

# physics.careers.append(career)
# physics.careers.append(career1)
# physics.careers.append(career2)
# physics.careers.append(career3)
# db.session.commit()

# chemistry.careers.append(career14)
# chemistry.careers.append(career21)
# chemistry.careers.append(career22)
# chemistry.careers.append(career23)
# chemistry.careers.append(career24)
# chemistry.careers.append(career23)
# db.session.commit()

# bm.careers.append(career3)
# bm.careers.append(career25)
# bm.careers.append(career26)
# bm.careers.append(career27)
# db.session.commit()


# english.careers.append(career3)
# english.careers.append(career3)
# english.careers.append(career25)
# english.careers.append(career26)
# english.careers.append(career27)
# db.session.commit()

# math.careers.append(career3)
# math.careers.append(career19)
# math.careers.append(career)
# math.careers.append(career6)
# math.careers.append(career20)
# math.careers.append(career18)
# db.session.commit()

# islam.careers.append(career3)
# islam.careers.append(career28)
# islam.careers.append(career29)
# db.session.commit()

# history.careers.append(career3)
# history.careers.append(career31)
# history.careers.append(career32)
# db.session.commit()

# acc.careers.append(career3)
# acc.careers.append(career18)
# acc.careers.append(career20)
# acc.careers.append(career19)
# db.session.commit()

# addmath.careers.append(career3)
# addmath.careers.append(career)
# addmath.careers.append(career1)
# addmath.careers.append(career2)
# addmath.careers.append(career17)
# db.session.commit()

# ict.careers.append(career3)
# ict.careers.append(career6)
# ict.careers.append(career7)
# ict.careers.append(career12)
# db.session.commit()

# bio.careers.append(career3)
# bio.careers.append(career23)
# bio.careers.append(career30)
# bio.careers.append(career14)
# db.session.commit()

# seni.careers.append(career3)
# seni.careers.append(career16)
# seni.careers.append(career11)
# db.session.commit()

# science.careers.append(career3)
# science.careers.append(career23)
# science.careers.append(career30)
# science.careers.append(career14)
# db.session.commit()

# economy.careers.append(career3)
# economy.careers.append(career19)
# economy.careers.append(career20)
# economy.careers.append(career18)
# db.session.commit()

# business.careers.append(career3)
# business.careers.append(career19)
# business.careers.append(career20)
# business.careers.append(career18)
# db.session.commit()

# home.careers.append(career3)
# db.session.commit()


# tasawwurIslam.careers.append(career3)
# tasawwurIslam.careers.append(career25)
# tasawwurIslam.careers.append(career28)
# tasawwurIslam.careers.append(career29)
# db.session.commit()


#career.career_path
#physics = Subject.query.filter_by(subject_title = "Physics").first()





#====================================================================================================================#
#                                           State and Zone                                                           #
#====================================================================================================================#
# state = State(state_code = "01", state_name = "Johor")
# state.zones.append(Zone(zone_name = "PPD Batu Pahat", zone_code = "J010"))
# state.zones.append(Zone(zone_name = "PPD Johor Bahru", zone_code = "J020"))
# state.zones.append(Zone(zone_name = "PPD Kluang", zone_code = "J030"))
# state.zones.append(Zone(zone_name = "PPD Kota Tinggi", zone_code = "J040"))
# state.zones.append(Zone(zone_name = "PPD Mersing", zone_code = "J050"))
# state.zones.append(Zone(zone_name = "PPD Muar", zone_code = "J060"))
# state.zones.append(Zone(zone_name = "PPD Pontian", zone_code = "J070"))
# state.zones.append(Zone(zone_name = "PPD Segamat", zone_code = "J080"))
# state.zones.append(Zone(zone_name = "PPD Kulai", zone_code = "J090"))
# state.zones.append(Zone(zone_name = "PPD Pasir Gudang", zone_code = "J100"))
# state.zones.append(Zone(zone_name = "PPD Ledang", zone_code = "J110"))

# state2 = State(state_code = "02", state_name = "Kedah")
# state2.zones.append(Zone(zone_name = "PPD Baling", zone_code = "K010"))
# state2.zones.append(Zone(zone_name = "PPD Kota Setar", zone_code = "K020"))
# state2.zones.append(Zone(zone_name = "PPD Kuala Muda/Yan", zone_code = "K030"))
# state2.zones.append(Zone(zone_name = "PPD Kubang Pasu", zone_code = "K040"))
# state2.zones.append(Zone(zone_name = "PPD Kulim / Bandar Baru", zone_code = "K050"))
# state2.zones.append(Zone(zone_name = "PPD Langkawi", zone_code = "K060"))
# state2.zones.append(Zone(zone_name = "PPD Padang Terap", zone_code = "K070"))
# state2.zones.append(Zone(zone_name = "PPD Pendang", zone_code = "K080"))
# state2.zones.append(Zone(zone_name = "PPD Sik", zone_code = "K090"))


# state3 = State(state_code = "03", state_name = "Kelantan")
# state3.zones.append(Zone(zone_name = "PPD Kota Bharu", zone_code = "D010"))
# state3.zones.append(Zone(zone_name = "PPD Pasir Mas", zone_code = "D020"))
# state3.zones.append(Zone(zone_name = "PPD Pasir Putih", zone_code = "D030"))
# state3.zones.append(Zone(zone_name = "PPD Tanah Merah", zone_code = "D040"))
# state3.zones.append(Zone(zone_name = "PPD Kuala Krai", zone_code = "D050"))
# state3.zones.append(Zone(zone_name = "PPD Gua Musang", zone_code = "D060"))
# state3.zones.append(Zone(zone_name = "PPD Bachok", zone_code = "D070"))
# state3.zones.append(Zone(zone_name = "PPD Tumpat", zone_code = "D080"))
# state3.zones.append(Zone(zone_name = "PPD Machang", zone_code = "D090"))
# state3.zones.append(Zone(zone_name = "PPD Jeli", zone_code = "D100"))


# state4 = State(state_code = "04", state_name = "Melaka")
# state4.zones.append(Zone(zone_name = "PPD Jasin", zone_code = "M010"))
# state4.zones.append(Zone(zone_name = "PPD Melaka Tengah", zone_code = "M020"))
# state4.zones.append(Zone(zone_name = "PPD Alor Gajah", zone_code = "M030"))

# state5 = State(state_code = "05", state_name = "Negeri Sembilan")
# state5.zones.append(Zone(zone_name = "PPD Kuala Pilah", zone_code = "N010"))
# state5.zones.append(Zone(zone_name = "PPD Seremban", zone_code = "N020"))
# state5.zones.append(Zone(zone_name = "PPD Tampin", zone_code = "N030"))
# state5.zones.append(Zone(zone_name = "PPD Port Dickson", zone_code = "N040"))
# state5.zones.append(Zone(zone_name = "PPD Rembau", zone_code = "N060"))
# state5.zones.append(Zone(zone_name = "PPD Jempol / Jelebu", zone_code = "N070"))

# state6 = State(state_code = "06", state_name = "Pahang")
# state6.zones.append(Zone(zone_name = "PPD Bentong", zone_code = "C010"))
# state6.zones.append(Zone(zone_name = "PPD Cameron Highlands", zone_code = "C020"))
# state6.zones.append(Zone(zone_name = "PPD Jerantut", zone_code = "C030"))
# state6.zones.append(Zone(zone_name = "PPD Lipis", zone_code = "C040"))
# state6.zones.append(Zone(zone_name = "PPD Kuantan", zone_code = "C050"))
# state6.zones.append(Zone(zone_name = "PPD Pekan", zone_code = "C060"))
# state6.zones.append(Zone(zone_name = "PPD Raub", zone_code = "C070"))
# state6.zones.append(Zone(zone_name = "PPD Temerloh", zone_code = "C080"))
# state6.zones.append(Zone(zone_name = "PPD Maran", zone_code = "C090"))
# state6.zones.append(Zone(zone_name = "PPD Rompin", zone_code = "C100"))
# state6.zones.append(Zone(zone_name = "PPD Bera", zone_code = "C200"))


# state7 = State(state_code = "07", state_name = "Pulau Pinang")
# state7.zones.append(Zone(zone_name = "PPD Timur Laut", zone_code = "P010"))
# state7.zones.append(Zone(zone_name = "PPD Seberang Prai Tengah", zone_code = "P020"))
# state7.zones.append(Zone(zone_name = "PPD Seberang Prai Selantan", zone_code = "P030"))
# state7.zones.append(Zone(zone_name = "PPD Barat Daya", zone_code = "P040"))
# state7.zones.append(Zone(zone_name = "PPD Seberang Perai Utara", zone_code = "P050"))

# state8 = State(state_code = "08", state_name = "Perak")
# state8.zones.append(Zone(zone_name = "PPD Batang Padang", zone_code = "A010"))
# state8.zones.append(Zone(zone_name = "PPD Manjung", zone_code = "A020"))
# state8.zones.append(Zone(zone_name = "PPD Krian", zone_code = "A040"))
# state8.zones.append(Zone(zone_name = "PPD Kuala Kangsar", zone_code = "A050"))
# state8.zones.append(Zone(zone_name = "PPD Hilir Perak", zone_code = "A060"))
# state8.zones.append(Zone(zone_name = "PPD Larut / Matang / Selama", zone_code = "A070"))
# state8.zones.append(Zone(zone_name = "PPD Hulu Perak", zone_code = "A080"))
# state8.zones.append(Zone(zone_name = "PPD Perak Tengah", zone_code = "A090"))
# state8.zones.append(Zone(zone_name = "PPD Kinta Utara", zone_code = "A100"))
# state8.zones.append(Zone(zone_name = "PPD Kinta Selatan", zone_code = "A110"))
# state8.zones.append(Zone(zone_name = "PPD Bagan Datuk", zone_code = "A120"))


# state9 = State(state_code = "09", state_name = "Perlis")
# state9.zones.append(Zone(zone_name = "PPD JPN Perlis ", zone_code = "R010"))

# state10 = State(state_code = "10", state_name = "Selangor")
# state10.zones.append(Zone(zone_name = "PPD Klang", zone_code = "B010"))
# state10.zones.append(Zone(zone_name = "PPD Kuala Langat", zone_code = "B020"))
# state10.zones.append(Zone(zone_name = "PPD Kuala Selangor", zone_code = "B030"))
# state10.zones.append(Zone(zone_name = "PPD Hulu Langat", zone_code = "B040"))
# state10.zones.append(Zone(zone_name = "PPD Hulu Selangor", zone_code = "B050"))
# state10.zones.append(Zone(zone_name = "PPD Sabak Bernam", zone_code = "B060"))
# state10.zones.append(Zone(zone_name = "PPD Gombak", zone_code = "B070"))
# state10.zones.append(Zone(zone_name = "PPD Sepang", zone_code = "B090"))
# state10.zones.append(Zone(zone_name = "PPD Petaling Perdana", zone_code = "B100"))
# state10.zones.append(Zone(zone_name = "PPD Petaling Utama", zone_code = "B110"))

# state11 = State(state_code = "11", state_name = "Terengganu")
# state11.zones.append(Zone(zone_name = "PPD Besut", zone_code = "T010"))
# state11.zones.append(Zone(zone_name = "PPD Dungun", zone_code = "T020"))
# state11.zones.append(Zone(zone_name = "PPD Kemaman", zone_code = "T030"))
# state11.zones.append(Zone(zone_name = "PPD Kuala Terengganu", zone_code = "T040"))
# state11.zones.append(Zone(zone_name = "PPD Hulu Terengganu", zone_code = "T050"))
# state11.zones.append(Zone(zone_name = "PPD Setiu", zone_code = "T060"))
# state11.zones.append(Zone(zone_name = "PPD Marang", zone_code = "T070"))
# state11.zones.append(Zone(zone_name = "PPD Kuala Nerus", zone_code = "T080"))


# state12 = State(state_code = "12", state_name = "Sabah")
# state12.zones.append(Zone(zone_name = "PPD Keningau", zone_code = "X010"))
# state12.zones.append(Zone(zone_name = "PPD Pensiangan", zone_code = "X011"))
# state12.zones.append(Zone(zone_name = "PPD Tambunan", zone_code = "X012"))
# state12.zones.append(Zone(zone_name = "PPD Tenom", zone_code = "X013"))
# state12.zones.append(Zone(zone_name = "PPD Sandakan", zone_code = "X020"))
# state12.zones.append(Zone(zone_name = "PPD Labuk Sagut", zone_code = "X021"))
# state12.zones.append(Zone(zone_name = "PPD Tongod", zone_code = "X022"))
# state12.zones.append(Zone(zone_name = "PPD Tawau", zone_code = "X030"))
# state12.zones.append(Zone(zone_name = "PPD Semporna", zone_code = "X031"))
# state12.zones.append(Zone(zone_name = "PPD Kota Kinabalu", zone_code = "X040"))
# state12.zones.append(Zone(zone_name = "PPD Penampang", zone_code = "X041"))
# state12.zones.append(Zone(zone_name = "PPD Tuaran", zone_code = "X042"))
# state12.zones.append(Zone(zone_name = "PPD Kota Belud", zone_code = "X050"))
# state12.zones.append(Zone(zone_name = "PPD Ranau", zone_code = "X051"))
# state12.zones.append(Zone(zone_name = "PPD Beaufort", zone_code = "X060"))
# state12.zones.append(Zone(zone_name = "PPD Sipitang", zone_code = "X062"))
# state12.zones.append(Zone(zone_name = "PPD Kuala Penyu", zone_code = "X063"))
# state12.zones.append(Zone(zone_name = "PPD Papar", zone_code = "X064"))
# state12.zones.append(Zone(zone_name = "PPD Lahad Datu", zone_code = "X070"))
# state12.zones.append(Zone(zone_name = "PPD Kinabatangan", zone_code = "X071"))
# state12.zones.append(Zone(zone_name = "PPD Kunak", zone_code = "X072"))
# state12.zones.append(Zone(zone_name = "PPD Kota Marudu", zone_code = "X080"))
# state12.zones.append(Zone(zone_name = "PPD Pitas", zone_code = "X081"))
# state12.zones.append(Zone(zone_name = "PPD Kudat", zone_code = "X082"))

# state13 = State(state_code = "13", state_name = "Sarawak")
# state13.zones.append(Zone(zone_name = "PPD Kuching", zone_code = "Y010"))
# state13.zones.append(Zone(zone_name = "PPD Bau", zone_code = "Y011"))
# state13.zones.append(Zone(zone_name = "PPD Padawan", zone_code = "Y012"))
# state13.zones.append(Zone(zone_name = "PPD Lundu", zone_code = "Y014"))
# state13.zones.append(Zone(zone_name = "PPD Sri Aman", zone_code = "Y020"))
# state13.zones.append(Zone(zone_name = "PPD Lubok Antu", zone_code = "Y023"))
# state13.zones.append(Zone(zone_name = "PPD Sibu", zone_code = "Y030"))
# state13.zones.append(Zone(zone_name = "PPD Selangau", zone_code = "Y032"))
# state13.zones.append(Zone(zone_name = "PPD Kanowit", zone_code = "Y033"))
# state13.zones.append(Zone(zone_name = "PPD Miri", zone_code = "Y040"))
# state13.zones.append(Zone(zone_name = "PPD Baram", zone_code = "Y043"))
# state13.zones.append(Zone(zone_name = "PPD Subis", zone_code = "Y044"))
# state13.zones.append(Zone(zone_name = "PPD Limbang", zone_code = "Y050"))
# state13.zones.append(Zone(zone_name = "PPD Lawas", zone_code = "Y052"))
# state13.zones.append(Zone(zone_name = "PPD Sarikei", zone_code = "Y060"))
# state13.zones.append(Zone(zone_name = "PPD Julau", zone_code = "Y062"))
# state13.zones.append(Zone(zone_name = "PPD Maradong", zone_code = "Y063"))
# state13.zones.append(Zone(zone_name = "PPD Kapit", zone_code = "Y070"))
# state13.zones.append(Zone(zone_name = "PPD Belaga", zone_code = "Y072"))
# state13.zones.append(Zone(zone_name = "PPD Song", zone_code = "Y073"))
# state13.zones.append(Zone(zone_name = "PPD Samarahan", zone_code = "Y080"))
# state13.zones.append(Zone(zone_name = "PPD Serian", zone_code = "Y082"))
# state13.zones.append(Zone(zone_name = "PPD Simunjan", zone_code = "Y083"))
# state13.zones.append(Zone(zone_name = "PPD Bintulu", zone_code = "Y090"))
# state13.zones.append(Zone(zone_name = "PPD Tatau / Sebauh", zone_code = "Y092"))
# state13.zones.append(Zone(zone_name = "PPD Mukah", zone_code = "Y100"))
# state13.zones.append(Zone(zone_name = "PPD Dalat", zone_code = "Y101"))
# state13.zones.append(Zone(zone_name = "PPD Daro", zone_code = "Y102"))
# state13.zones.append(Zone(zone_name = "PPD Betong", zone_code = "Y110"))
# state13.zones.append(Zone(zone_name = "PPD Saratok", zone_code = "Y111"))


# state14 = State(state_code = "14", state_name = "WP Kuala Lumpur")
# state14.zones.append(Zone(zone_name = "PPW Bangsar Pudu", zone_code = "W010"))
# state14.zones.append(Zone(zone_name = "PPW Keramat", zone_code = "W020"))
# state14.zones.append(Zone(zone_name = "PPW Sentul", zone_code = "W030"))
# state14.zones.append(Zone(zone_name = "JP WP Kuala Lumpur - Zon Bangsar", zone_code = "W040"))

# state15 = State(state_code = "15", state_name = "WP Labuan")
# state15.zones.append(Zone(zone_name = "JPWP Labuan", zone_code = "L010"))

# state16 = State(state_code = "16", state_name = "WP Putrajaya")
# state16.zones.append(Zone(zone_name = "PPW Putrajaya", zone_code = "U010"))

# db.session.add_all([state, state2, state3, state4, state5, state6, state7, state8, state9, state10, state11,state12, state13, state14, state15, state16])
# db.session.commit()



#====================================================================================================================#
#                                           School                                                                   #
#====================================================================================================================#



# School and School Address
# school = School(school_name ="SMK Taman Setiawangsa", school_description = "This is taman Setiawangsa")
# school.school_address.append(SchoolAddress(address_name = "Jalan 14/55A, Taman Setiwangsa", state_id = state14.id, zone_id = state14.zones[3].id))
# school2 = School(school_name ="SMK Taman Johor", school_description = "This is taman Johor School")
# school2.school_address.append(SchoolAddress(address_name = "Jalan Johor, Taman Johor", state_id = state.id, zone_id = state.zones[3].id))
# school3 = School(school_name ="SMK TTaman Setiawangsa2", school_description = "This is taman Setiawangsa2")
# school3.school_address.append(SchoolAddress(address_name = "Jalan 14/55A, Taman Setiwangsa", state_id = state2.id, zone_id = state2.zones[1].id))


#db.session.add(school)

#schoolTest = School.query.filter_by(id = 1).first()
# schoolTest.school_address[0].state  by right it will return int 2
# But in order to get the value of that forign key kene buat mcm ni
# schoolTest.school_address[0].states.state_name ....Using the backref!
# schoolTest.school_address[0].zones.zone_name


#Student
#student2 = Student(student_name = "Tuan Arif Uwais Bin Tuan SyamsanP", student_icNum = "001104-14-1493", student_form4_class = "4 Cekap", school_id = school.id)
#student3 = Student(student_name = "Tuan Arif Uwais Bin Tuan Syamsanu",  school_id = school.id, student_icNum = "001104-14-1495", student_form4_class = "4 Cekap")

#school = School(school_name ="SMK Taman Setiawangsa", school_description = "This is taman Setiawangsa")
#school.school_address.append(SchoolAddress(address_name = "Jalan 14/55A, Taman Setiwangsa", state_id = state14.id, zone_id = state14.zones[3].id))
#school.stream_packages.append(StreamPackage(stream_name = "Pure Science"))
#db.session.add(school)
#db.session.commit()   
#streamTest = StreamPackage.query.filter_by(id=1).first()
# search_subject = Subject.query.filter_by(subject_title = "Physics").first()     
#streamTest.subjects.append(search_subject) 
#db.session.commit()
#school.stream_packages.subjects.append(search_subject) 













