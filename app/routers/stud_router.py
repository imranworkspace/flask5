from flask import jsonify,request,Blueprint
from app.extentions import db 
from app.models.stud_model import StudentModel

student_bp = Blueprint(
    "students",
    __name__
)

@student_bp.get('/students')
def getstuds():
    studs_ = StudentModel.query.all()
    # studs_ = StudentModel.query.count()
    # studs_ = StudentModel.query.first()
    studs_ = StudentModel.query.filter_by(name="imran").first()
    studs_ = StudentModel.query.filter(StudentModel.id>4).all()
    studs_ = StudentModel.query.order_by(
        StudentModel.age.desc()
        ).all()
    # studs_ = StudentModel.query.limit(3).all()
    print(studs_)
    # studs_ = StudentModel.query.filter_by(age=30)

    if not studs_:
        return jsonify({
            "status":"students not found in db"
        }),404 
    return jsonify([
        std.to_dict() for std in studs_
        # studs_
        # studs_.to_dict()
    ]),200 

@student_bp.post('/students')
def create():
    data = request.get_json()
    print('data ',data)
    stud_ = StudentModel(
        name=data['name'],
        age=data['age']
    )
    db.session.add(stud_)
    db.session.commit()
    return jsonify({
        'status':'student added',
        'data':stud_.to_dict()
    }),201 

@student_bp.put('/students/<int:id>')
def putstudsbyid(id):
    studs_ = db.session.get(StudentModel,id)
    if not studs_:
        return jsonify({
            "status":"students not found in db"
        }),404 
    data=request.get_json()
    studs_.name=data['name']
    studs_.age=data['age']
    db.session.commit()
    return jsonify({
        'status':f'student updated by {id}',
        'data':studs_.to_dict()}),200


@student_bp.get('/students/<int:id>')
def getstudsbyid(id):
    studs_ = db.session.get(StudentModel,id)
    print(studs_)
    if not studs_:
        return jsonify({
            "status":"students not found in db"
        }),404 
    return jsonify(studs_.to_dict()),200

@student_bp.delete('/students/<int:id>')
def deletestudsbyid(id):
    studs_ = db.session.get(StudentModel,id)
    if not studs_:
        return jsonify({
            "status":"students not found in db"
        }),404 
    db.session.delete(studs_)
    db.session.commit()
    return jsonify({"status":f"student deleted by id of {id}"}),200

