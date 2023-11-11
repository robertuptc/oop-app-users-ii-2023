

class User:
    def __init__(self, name, last_name, age, email, password ):  
        self.name = name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.password = password
        self.posts = {}
        self.posts_count = 1

    def __str__(self):
        return f"Welcome {self.name}! Your account has been created. Check your {self.email} for a confirmation code!"
    
    def user_post(self, post_content):
        self.posts[self.posts_count] = post_content
        self.posts_count += 1

    def delete_post(self, val):
        post_num = int(val)
        if int(post_num) in self.posts:
            del self.posts[post_num]


robert_user = User('Robert', 'Puentes', 25, "myemail.@gmail.com", "123asd456")
robert_user.user_post('This is my first post')
robert_user.user_post('This is my second post')
robert_user.user_post('This is my third post')
print("ALL POSTS", robert_user.posts)

# mike_user = User('Mike', 'Lambert', 35, 'myemail@yahoo.com', '123456')
# mike_user.user_post('first post')
# mike_user.user_post('second post')
# print(mike_user.posts)
# print(robert_user.posts)

robert_user.delete_post(1)
robert_user.delete_post(2)
print("AFTER DELETION", robert_user.posts)