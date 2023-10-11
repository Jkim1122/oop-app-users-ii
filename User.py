class User:
    all_users = {}
    user_id = 0
    posts = []

    def __init__(self, username):
        User.user_id += 1
        self._username = username
        self._id = User.user_id
        self.post = []
        User.all_users[self._id] = self
    
    def __repr__(self):
        return f"{self._username}"
    
    # @property
    # def get_username(self):
    #     return self._username------------------
    # @get_username.setter-------------------no getter/setter
    # def set_username(self, new_username):-----for username
    #     self._username = new_username -----------------

    @property
    def get_post(self):
        return self._post
    @get_post.setter
    def set_post(self, new_post):
        if type(new_post) == str:
            self.post.append(new_post)

    @classmethod
    def add_a_user(cls):
        username = input("Enter username:   ")
        cls(username)
        print(cls.all_users)

    @staticmethod
    def view_all_users():
        for user in User.all_users.values():
            print(user)

    @staticmethod
    def make_a_post():
        post = input("post your comment here:   ")
        User.posts.append(f"{User.username}: {User.get_post}")
        print(User.posts)

# user1 = User("jkim1122")
# user2 = User("andrew.h123")
# user3 = User("p.bui77")

User.add_a_user()
User.make_a_post()
