from flask import Blueprint, request, jsonify, Response
from myflaskapp.models import users
import json
from bson.objectid import ObjectId

users_bp = Blueprint('users', __name__)


@users_bp.route("/users", methods=["POST"])
def create_user():
    try:
        if request.method == "POST":
            user = users(name=request.form["name"], email=request.form["email"])
            dbResponse = user.save()
            return jsonify(dbResponse)
    except Exception as ex:
        return 'ex'


@users_bp.route("/users/list", methods=["GET"])
def users_list():
    try:
        data = users.objects()
        return jsonify(data)
    except Exception as ex:
        return jsonify(ex)


@users_bp.route("/users/<id>", methods=["GET"])
def user(id):
    try:
        data = users.objects.get(id=ObjectId(id))
        return jsonify(data)
    except Exception as ex:
        return jsonify(ex)



@users_bp.route("/users/update/<id>", methods=["PUT"])
def user_update(id):
    try:
        if request.method == "PUT":
            user = users.objects.get(id=ObjectId(id))
            user = user.update(name=request.form["name"], email=request.form["email"])
            return jsonify({"message":"user updated successfully"})
           
            
    except Exception as ex:
        return Response(
            response= json.dumps(
                {"message":"Sorry cannot update user"}),
            status=500,
            mimetype="application/json"
        )


@users_bp.route("/users/delete/<id>", methods=["DELETE"])
def user_delete(id):
    try:
        if request.method == "DELETE":
            dbResponse = users.objects.get(id=ObjectId(id)).delete()
            return jsonify({"message":"user deleted successfully", "id":f"{id}"})
        
    except Exception as ex:
        return Response(
            response= json.dumps(
                {"message":"Sorry cannot delete user"}),
            status=500,
            mimetype="application/json"
        )


# @users_bp.route('/user', methods=["POST"])
# def new_user():
#     user = users(name=request.form['name'], email=request.form['email'])
#     user = user.save()
#     data = []
#     for u in user:
#         data.append(u)
#     print(data)
#     return 'Saved :)'

# @users_bp.route('/users/list/')
# def list_users():
#     user = users.query.all()
      

#     content = '<p>users:</p>'
#     for u in user:
#         content += f'name = {u.name}'    #'<p>%s</p>' % u.name
#     return content


# if "__name__" == "__main__":
#     app.run(debug=True)