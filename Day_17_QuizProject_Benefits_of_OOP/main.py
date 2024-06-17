class User:
    def __init__(self, user_id, username):
        self.id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers += 1
        self.following += 1

user_1 = User("001","Ameya")
user_2 = User("002", "Sami")
user_3 = User("003","Ari")

user_1.follow(user_2)

print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)













##CONSTRUCTOR##

# class Car:
#     def __init__(self,seats):
#         #initialize attributes
#         self.seats = 5