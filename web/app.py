from flask import Flask, render_template, jsonify, request, redirect, url_for, abort
from models.users import User, Userlist


app = Flask(__name__)


@app.route('/leaderboard')
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

@app.route('/register', methods=['POST'])
def register():
    valid_user = True
    userlist = Userlist()
    data = request.json
    print(data)
    users = userlist.list_users
    for i in users:
        if i.username == data['username']:
            if i.password != data['password']:
                valid_user = False
                return jsonify(valid_user), 404
            else:
                return jsonify(valid_user), 200
    if valid_user == True:
        userlist.add(User(data['username'], data['password']))
        userlist.save()
        return jsonify(valid_user), 200

@app.route('/addscore/<username>', methods=['POST'])
def addscore(username):
    userlist = Userlist()
    scores = request.json
    user = userlist.get_user(username)
    if user != None:
        user.score.append(scores["score"])
        user.time.append(int(scores["time_alive"]))
        userlist.save()
        return f'Saved data', 200
    else:
        return f'{user}', 404

@app.route('/viewscore/<string:username>')
def viewscore(username):
    userlist = Userlist()
    user = userlist.get_user(username)
    if user!= None:
        return render_template("viewscore.html", username = user.username, scores=zip(user.score, user.time))
    else:
        return f'{username} not found', 404

if __name__ == "__main__":
    app.run(debug=True)