from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import mapped_column, relationship, Session
from sqlalchemy import ForeignKey, create_engine
import os
from dotenv import load_dotenv

load_dotenv()

Base = declarative_base()


class Program(Base):
    __tablename__ = 'programs'
    id: mapped_column(int) = mapped_column(primary_key=True)
    name: mapped_column(str) = mapped_column(nullable=False)
    years_of_study: mapped_column(int) = mapped_column(nullable=False)
    courses: mapped_column(list['Course']) = relationship(backref='program', passive_deletes=True)

    def __repr__(self) -> str:
        return f"<Program {self.name}>"


class Student(Base):
    __tablename__ = 'students'
    id: mapped_column(int) = mapped_column(primary_key=True)
    name: mapped_column(str) = mapped_column(nullable=False)
    age: mapped_column(int) = mapped_column(nullable=False)
    courses: mapped_column(list['Course']) = relationship(backref='student', passive_deletes=True)

    def __repr__(self) -> str:
        return f"<Student {self.name}>"


class Course(Base):
    __tablename__ = 'courses'
    id: mapped_column(int) = mapped_column(primary_key=True)
    title: mapped_column(str) = mapped_column(nullable=False, unique=True)
    code: mapped_column(str) = mapped_column(nullable=False)
    program_id: mapped_column(int) = mapped_column(ForeignKey('programs.id', ondelete='CASCADE'))
    student_id: mapped_column(int) = mapped_column(ForeignKey('students.id', ondelete='CASCADE'))

    def __repr__(self) -> str:
        return f"<Course {self.title}>"


from sqlalchemy import create_engine

try:
    NEON_DB_CONN_STR = os.getenv("NEON_DB_CONN_STR")
    engine = create_engine(NEON_DB_CONN_STR, echo=True)
    Base.metadata.create_all(bind=engine)

    with Session(bind=engine) as db:
        print("Connection Established")

        program1 = Program(
            name="Bachelors in CS",
            years_of_study=3
        )

        program2 = Program(
            name="Bachelors in Business",
            years_of_study=3
        )

        db.add_all([program1, program2])
        db.commit()

        # create course objects
        course1 = Course(
            title="Database Management Systems",
            code="CS 102"
        )

        course2 = Course(
            title="Data Science",
            code="CS 103"
        )

        course3 = Course(
            title="Data Structures and Algorithms",
            code="CS 110"
        )

        course4 = Course(
            title="Business Communication",
            code="BS 123"
        )

        # adding child object to parent
        program1.courses.extend([course1, course2, course3])
        program2.courses.append(course4)

        db.commit()

        # create student objects
        student1 = Student(
            name="Yasir",
            age=25
        )

        student2 = Student(
            name="Nasir",
            age=28
        )

        student3 = Student(
            name="Tahir",
            age=19
        )

        student4 = Student(
            name="Jafar",
            age=18
        )

        # adding child object to parent
        course1.students.extend([student1, student2])
        course2.students.extend([student3, student4])

        db.commit()

except Exception as e:
    print(f"Error connecting to the database: {e}")


# E:\Yasir\PIAIC\GenAI\step8_everythingAPI\orm.py 