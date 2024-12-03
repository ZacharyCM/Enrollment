from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:zach9096@127.0.0.1:3306/SchoolEnrollmentDB'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
# Models
class Building(db.Model):
    __tablename__ = 'buildings'
    building_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    building_name = db.Column(db.String(255), nullable=False)
    num_rooms = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"<Building {self.building_name}>"


class Department(db.Model):
    __tablename__ = 'departments'
    department_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    department_name = db.Column(db.String(255), nullable=False)
    department_email = db.Column(db.String(255), nullable=False)
    department_head = db.Column(db.String(255), nullable=False)
    payment_fees = db.Column(db.Numeric(10, 2), nullable=False)
    building_id = db.Column(db.Integer, db.ForeignKey('buildings.building_id'), nullable=False)

    building = db.relationship('Building', backref=db.backref('department', uselist=False))

    def __repr__(self):
        return f"<Department {self.department_name}>"


class Professor(db.Model):
    __tablename__ = 'professors'
    professor_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    professor_name = db.Column(db.String(255), nullable=False)
    professor_email = db.Column(db.String(255), nullable=False)
    overview = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return f"<Professor {self.professor_name}>"


class Student(db.Model):
    __tablename__ = 'students'
    student_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(255), unique=True, nullable=False)
    year = db.Column(db.Integer, nullable=False)
    gpa = db.Column(db.Numeric(4, 2), nullable=True)
    gender = db.Column(db.String(10), nullable=False)
    dob = db.Column(db.Date, nullable=False)
    major = db.Column(db.String(100), nullable=False)
    phone_number = db.Column(db.String(15), nullable=True)
    unit_count = db.Column(db.Integer, nullable=False)
    payment_status = db.Column(db.Boolean, default=False)

    def __repr__(self):
        return f"<Student {self.first_name} {self.last_name}>"


class Class(db.Model):
    __tablename__ = 'classes'
    class_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    class_name = db.Column(db.String(255), nullable=False)
    class_number = db.Column(db.String(50), unique=True, nullable=False)
    class_time = db.Column(db.Time, nullable=False)
    syllabus = db.Column(db.Text, nullable=True)
    unit_amount = db.Column(db.Integer, nullable=False)
    schedule = db.Column(db.String(255), nullable=True)
    semester = db.Column(db.String(50), nullable=False)
    prerequisites = db.Column(db.String(255), nullable=True)
    cost_per_class = db.Column(db.Numeric(10, 2), nullable=False)
    available_seats = db.Column(db.Integer, nullable=False)
    max_capacity = db.Column(db.Integer, nullable=False)
    room_number = db.Column(db.String(50), nullable=False)
    building_id = db.Column(db.Integer, db.ForeignKey('buildings.building_id'), nullable=False)
    professor_id = db.Column(db.Integer, db.ForeignKey('professors.professor_id'), nullable=True)

    building = db.relationship('Building', backref=db.backref('classes', lazy=True))
    professor = db.relationship('Professor', backref=db.backref('classes', lazy=True))
    students = db.relationship('Student', secondary='class_student', backref=db.backref('enrolled_classes', lazy=True))

    def __repr__(self):
        return f"<Class {self.class_name}>"


# Association table for many-to-many relationship
class_student = db.Table('class_student',
    db.Column('class_id', db.Integer, db.ForeignKey('classes.class_id'), primary_key=True),
    db.Column('student_id', db.Integer, db.ForeignKey('students.student_id'), primary_key=True)
)

# Create all tables
with app.app_context():
    db.create_all()
    print("All tables created successfully!")