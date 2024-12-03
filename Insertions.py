import sys
sys.path.append('/Users/zacharym/Documents')

from SchoolEnrollmentDB import db, Building, Department, Professor, Student, Class, app

# Perform insertions within the application context
with app.app_context():
    # Insert into Building
    building1 = Building(building_name="Science Building", num_rooms=50)
    building2 = Building(building_name="Arts Building", num_rooms=30)
    db.session.add_all([building1, building2])

    # Insert into Department
    department1 = Department(
        department_name="Physics Department",
        department_email="physics@university.edu",
        department_head="Dr. Newton",
        payment_fees=500.00,
        building_id=1  # Assuming Building with ID 1 exists
    )
    department2 = Department(
        department_name="Arts Department",
        department_email="arts@university.edu",
        department_head="Dr. Picasso",
        payment_fees=300.00,
        building_id=2  # Assuming Building with ID 2 exists
    )
    db.session.add_all([department1, department2])

    # Insert into Professor
    professor1 = Professor(
        professor_name="Dr. Einstein",
        professor_email="einstein@university.edu",
        overview="Expert in Quantum Physics"
    )
    professor2 = Professor(
        professor_name="Dr. Shakespeare",
        professor_email="shakespeare@university.edu",
        overview="Expert in Literature"
    )
    db.session.add_all([professor1, professor2])

    # Insert into Student
    student1 = Student(
        first_name="Alice",
        last_name="Johnson",
        email="alice.johnson@student.edu",
        year=2,
        gpa=3.8,
        gender="Female",
        dob="2003-05-20",
        major="Physics",
        phone_number="123-456-7890",
        unit_count=30,
        payment_status=True
    )
    student2 = Student(
        first_name="Bob",
        last_name="Smith",
        email="bob.smith@student.edu",
        year=1,
        gpa=3.5,
        gender="Male",
        dob="2004-08-15",
        major="Arts",
        phone_number="987-654-3210",
        unit_count=25,
        payment_status=False
    )
    db.session.add_all([student1, student2])

    # Insert into Class
    class1 = Class(
        class_name="Quantum Mechanics",
        class_number="PHYS101",
        class_time="10:00:00",
        syllabus="Introductory course to Quantum Physics.",
        unit_amount=4,
        schedule="MWF",
        semester="Fall 2024",
        prerequisites="Intro to Physics",
        cost_per_class=1000.00,
        available_seats=20,
        max_capacity=30,
        room_number="B201",
        building_id=1,  # Science Building
        professor_id=1  # Dr. Einstein
    )
    class2 = Class(
        class_name="Literature 101",
        class_number="ARTS101",
        class_time="12:00:00",
        syllabus="Introductory course to Literature.",
        unit_amount=3,
        schedule="TTh",
        semester="Fall 2024",
        prerequisites="None",
        cost_per_class=800.00,
        available_seats=25,
        max_capacity=30,
        room_number="A101",
        building_id=2,  # Arts Building
        professor_id=2  # Dr. Shakespeare
    )
    db.session.add_all([class1, class2])

    # Commit all changes to the database
    db.session.commit()
    print("All entities inserted successfully!")
