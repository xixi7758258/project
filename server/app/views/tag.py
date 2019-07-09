from flask import Blueprint ,request, jsonify

tag_blueprint = Blueprint("tag", __name__)


# tag crud.
@tag_blueprint.route("/", methods=["GET", "POST", "PUT", "DELETE"])
def tag():
    if request.method == "GET":
        
        return

    if request.method == "POST":
        
        return
    
    if request.method == "PUT":
        
        return
    
    if request.method == "DELETE":
        
        return
    
    return jsonify({"code": 500, "message": "method error"})