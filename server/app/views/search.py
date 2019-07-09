from flask import Blueprint

search_blueprint = Blueprint("search", __name__)


# search crud.
@search_blueprint.route("/search", methods=["GET", "POST", "PUT", "DELETE"])
def search():
    if request.method == "GET":

        return

    if request.method == "POST":
        
        return
    
    if request.method == "PUT":
        
        return
    
    if request.method == "DELETE":
        
        return
    
    return jsonify({"code": 500, "message": "method error"})
