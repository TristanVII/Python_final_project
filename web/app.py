from flask import Flask, render_template, jsonify, request, redirect, url_for, abort
from web.models.users import User, Userlist


app = Flask(__name__)



@app.route("/")
def home():
    userlist = Userlist()
    return render_template("home.html", userlist=userlist)

@app.route('/search', methods=['POST'])
def search():
    match = []
    username = request.form.get('username') 
    print(username)
    userlist = Userlist()
    for user in userlist.list_users:
        print(user.username)
        if username.lower() in user.username.lower():
            match.append(user)
    return render_template("search.html", users = match)

@app.route('/delete/<username>', methods=['POST', 'GET'])
def delete(username):
    userlist = Userlist()
    print(username)
    deleted = userlist.delete(username)
    if len(deleted) < 1:
        return "Unsucessful", 404
    else:
        userlist.save()
        return redirect("/"), 302

if __name__ == "__main__":
    app.run(debug=True)