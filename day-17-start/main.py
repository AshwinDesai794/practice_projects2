class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0
    #pass

    def follow(self, user):
        user.followers += 1
        self.following +=1

user_1 = User(user_id="001", username="Ashwin")
user_2 = User("002", "Anand")

# user1 = User()
# user1.id = "001"
# user1.username = "ashwin"


print(f"your name is {user_1.username} and is is {user_1.id}")

user_1.follow(user_2)
print(f"followers : {user_1.followers}")
print(f"following : {user_1.following}")
print(f"followers : {user_2.followers}")
print(f"following : {user_2.following}")


