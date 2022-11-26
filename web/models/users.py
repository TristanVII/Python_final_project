import json, os

class User:
    def __init__(self, username, score, time, ):
        self.username = username
        self.score = score
        self.time = time

    def to_dict(self):
        return {
            "score": self.score,
            "time": self.time,
        }
    

class Userlist: 
    def __init__(self):
        self.path_json = os.path.join(os.getcwd(), 'web', 'users.json')
        self.list_users = []
        self.load_from_json()

    def add(self, user):
        self.list_users.append(user)

    def load_from_json(self):
        with open(self.path_json, 'r') as f:
            data = json.load(f)
            for users in data:
                print(users)
                print(data[users]['score'])
                self.list_users.append(User(users, data[users]['score'], data[users]['time']))

    def get_users(self):
            return sorted(self.list_users, key = lambda x: x.score, reverse=True)


    def to_dict(self):
        user_dict = {}
        for i in self.list_users:
            user_dict[i.username] = i.to_dict()
        return user_dict
    
    def save(self):
        with open(self.path_json, 'w') as w:
            json.dump(self.to_dict(), w)

    def delete(self, username):
        deleted = []
        for user in self.list_users:
            if username.lower() == user.username.lower():
                self.list_users.remove(user)
                deleted.append(user)
        return deleted
                


