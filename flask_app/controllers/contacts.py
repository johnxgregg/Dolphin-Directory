from flask import render_template,redirect,session,request,flash
from flask_app import app
from flask_app.models.contact import Contact
from flask_app.models.user import User


#ROUTES
@app.route("/create")
def new_contact():
    if "user_id" not in session:
        return redirect("/logout")
    data = {
        "id":session["user_id"]
    }
    return render_template("create_contact.html",user=User.get_by_id(data))


@app.route("/create/contact",methods=["POST"])
def create_contact():
    if "user_id" not in session:
        return redirect("/logout")
    if not Contact.validate_contact(request.form):
        return redirect("/create")
    data = {
        "name": request.form["name"],
        "phone_number": request.form["phone_number"],
        "city": request.form["city"],
        "state": request.form["state"],
        "vip": int(request.form["vip"]),
        "user_id": session["user_id"]
    }
    Contact.save(data)
    return redirect("/dashboard")


@app.route("/edit/<int:id>")
def edit_contact(id):
    if "user_id" not in session:
        return redirect("/logout")
    data = {
        "id":id
    }
    user_data = {
        "id":session["user_id"]
    }
    return render_template("edit_contact.html",edit=Contact.get_one(data),user=User.get_by_id(user_data))


@app.route("/update/contact",methods=["POST"])
def update_contact():
    if "user_id" not in session:
        return redirect("/logout")
    if not Contact.validate_contact(request.form):
        (f"/edit/{request.form['id']}")
    data = {
        "name": request.form["name"],
        "phone_number": request.form["phone_number"],
        "city": request.form["city"],
        "state": request.form["state"],
        "vip": int(request.form["vip"]),
        "id": request.form["id"]
    }
    Contact.update(data)
    return redirect("/dashboard")


# @app.route('/vip_contact/<int:id>')
# def show_vip(id):
#     if 'user_id' not in session:
#         return redirect('/logout')
#     data = {
#         "id":id
#     }
#     user_data = {
#         "id":session['user_id']
#     }
#     return render_template("vip_list.html",contact=Contact.get_all(data),user=User.get_by_id(user_data))


@app.route("/destroy/contact/<int:id>")
def destroy_contact(id):
    if "user_id" not in session:
        return redirect("/logout")
    data = {
        "id":id
    }
    Contact.destroy(data)
    return redirect("/dashboard")
