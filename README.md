# LOLSHOOTER

## Description
Lolshooter is a League of Legends inspired shooting/dodging game where you must kite and kill the enemies that come at you.

## Starter
* In order to play, you must first download this repository
* Since the webapp is not hosted, you must launch the webapp before playing. (Skip this step to play offline)
* You can now run *lolshooter.py*

## Login Page

<img width="500" alt="Screenshot 2022-11-30 at 11 06 22 AM" src="https://user-images.githubusercontent.com/100272904/204886636-a6433806-a79c-4350-9f72-e63a2194dfb6.png">

The first screen you will land on once opening the game is the Login page
You have two options
* Play Offline
* Login

### Play Offline
If you don't have access to internet, or if the webapp isn't running. You can play offline for fun without having a username and password

### Login Screen
The login page acts as a signup and login at the same time. This means if you already have a username and know the password, typing those in will log you in. If you don't have a username and try loging in with a username and password, you will automatically create a new account, unless the username is already taken. 

If the webapp is running, after creating a user you should be able to see the user at ```http://127.0.0.1:5000``` with None scores

## Welcome Screen

<img width="500" alt="Screenshot 2022-11-30 at 11 06 22 AM" src="https://user-images.githubusercontent.com/100272904/204888803-4a1ea5ea-ede9-4bc3-a5bc-fcd6e4eb32cb.png">

This is what the Welcome page looks like, you are able to pick between 3 iconic LoL champions. Each choice has their own champion graphic, sounds and ability.

## Game Screen & How to Play

<img width="500" alt="Screenshot 2022-11-30 at 11 06 22 AM" src="https://user-images.githubusercontent.com/100272904/204889442-183c9af5-496a-4f66-8745-c1097735b8f3.png">

The game is pretty simple, move your champion by ```right clicking``` on the map, where you want it to move, to use your ability, press ```q``` and point ur cursor in the direction you want the projectile to go.

The enemies spawn at random intervals, and they spawn more after every 30 seconds up until 60 seconds. (0-30s 1%, 30-60s 2%, 60-∞ 3%)
If the enemy touches the champion you lose. 

You have 2 scores while playing. **SCORE** which is the amount of enemies you killed, and **TIME** which is ur time survived.
If you are playing online, these scores will be recorded you your users profile automatically, once you die.

Once you die, you will be prompt with the ***Game Over*** screen, where you can ```exit``` ```play again``` or ```View leaderboard```


## How the webapp (flask) works

### Create a user

```
            username = self.input_box.entered
            password = self.input_password.entered
            data = {"username": username, "password": password}
            x = requests.post(f"http://127.0.0.1:5000/register", json=data)
            valid_user = x.status_code
            print(valid_user)

            if valid_user == 200:
                self.state["username"] = username
                self.state["password"] = password
                self.state["online"] = True
                self.next_screen = 'welcome'
                self.running = False
            elif valid_user == 404:
                self.invalid_user = username
                self.invalid = True
```

Once you type a username and password and click ```Login``` pygames sends a post request to /register with json data containing the username and password typed. The server can respond 2 ways, with status code 200 or 404. If the the password for the username is wrong, server returns 404, you cannot proceed to welcome screen. If a Username and password is correct, or you enter a new username with password, server returns status code 200, you can proceed to welcome screen. In this case, either a new account is created or you login to an existing account.

### Posting the Score

```
requests.post(f"http://127.0.0.1:5000/addscore/{self.state['username']}", json=self.state)
```

At the end of a game, if you are logged in (not offline) you will send a post request to the server, at /addscore/<username> with a json of all scores.
The server will then save the scores for the users. The scores are viewable at ```http://127.0.0.1:5000/leaderboard```

