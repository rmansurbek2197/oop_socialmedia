class Post:
    def __init__(self, pid, text):
        self.pid = pid
        self.text = text
        self.likes = 0


class User:
    def __init__(self, uid, name):
        self.uid = uid
        self.name = name
        self.posts = []


class SocialMedia:
    def __init__(self):
        self.users = {}

    def add_user(self, user):
        self.users[user.uid] = user

    def create_post(self, uid, post):
        self.users[uid].posts.append(post)

    def like_post(self, user_id, post_id):
        for user in self.users.values():
            for p in user.posts:
                if p.pid == post_id:
                    p.likes += 1
