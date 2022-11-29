import json, os
from .user import User


class Userlist: 
    def __init__(self):
        """
        Initialize a Userlist object that stores Users
        """
        self.path_json = os.path.join(os.getcwd(), 'users.json')
        self.list_users = []
        self.load_from_json()

    def add(self, user):
        """
        Add a user to self.list_users
        """
        self.list_users.append(user)

    def load_from_json(self):
        with open(self.path_json, 'r') as f:
            data = json.load(f)
            for users in data:
                self.list_users.append(User(users, data[users]['password'], data[users]['score'], data[users]['time']))

    def get_users(self):
        """
        Returns:
            list of users
        """
        return sorted(self.list_users, key = lambda x: x.username, reverse=False)

    def get_user(self, user):
        username = None
        for i in self.list_users:
            if i.username == user:
                username = i
        return username


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
                


