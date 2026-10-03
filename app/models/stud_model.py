from app.extentions import db

class StudentModel(db.Model):
    __tablename__="students"
    id=db.Column(db.Integer,primary_key=True,autoincrement=True)
    name=db.Column(db.String(25),nullable=False)
    age=db.Column(db.Integer,nullable=False)

    def to_dict(self):
        return {
            'id':self.id,
            'name':self.name,
            'age':self.age,
        }