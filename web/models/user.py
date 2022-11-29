class User:
    def __init__(self, username, password, score=[], time=[]):
        """
        Create a User class for Userlist 
        Args:
            username (string): username created at pygame.login
            password (string): password created at pygame.login
            score (list, int): list scores initialized with empty list
            time (list, int): list times initialized with empty list
        """
        self.username = username
        self.password = password
        self.score = score
        self.time = time

    def to_dict(self):
        return {
            "password": self.password,
            "score": self.score,
            "time": self.time,
        }

    def get_highest_score(self):
        """
        return the highest score from users list of scores
        if user has no time pass
        """
        scores = sorted(self.score, key = lambda x: x, reverse=True)
        if scores:
            return scores[0]
        else:
            pass

    def get_highest_time(self):
        """
        return the highest time from users list of scores
        if user has no time pass
        
        """
        times = sorted(self.time, key = lambda x: x, reverse=True)
        if times:
            return times[0]
        else:
            pass