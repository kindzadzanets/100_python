class InstagramUser(): #ДЕКЛАРИРОВАНИЕ класса (создание)
    def __init__(self, user_id, user_name):
        self.id = user_id
        self.user_name = user_name
        self.followers = 0
        self.following = 0

    def follow(self, user):  # создание метода класса. self - объект, вызывающий метод(подставляется сам). При вызове метода:
        user.followers += 1 # изменение значения атрибута для аргумента "user"
        self.following += 1 # изменение атрибута для непосредственного объекта


user_1 = InstagramUser("AR-1", "kisa")
user_2 = InstagramUser("AR-2", "katsman")


user_1.follow(user_2) # вызов функции self.follow(user) для объекта, которая принимает второй объект в качестве аргумента.
