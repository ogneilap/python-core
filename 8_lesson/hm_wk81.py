# Завдання 1: Інкапсуляція

# Створіть клас "Користувач" (User), який має такі приватні поля (інкапсульовані дані):

# Ім'я (name)
# Електронна пошта (email)
# Пароль (password)

# Напишіть публічні методи для установки і отримання значень цих полів (геттери і сеттери). Потім створіть об'єкт класу "Користувач" 
# і встановіть значення полів, а також виведіть їх на екран.

class User:
    
    def __init__(self,name, email , pssword)-> None:
        self.__name = name
        self.__email = email
        self.__password = pssword
        
    def get_user_date(self):
        return self.__dict__
    
    def set_user_date(self, attr, value):
        self.__dict__[attr] = value
        
    def get_name(self):
        return self.__name
    
    def get_email(self):
        return self.__email
        
stas =  User('Stas','123@gmail.com', '12345')
sergi =  User('sergi','serrrgoi@gmail.com', 'sergipro')
sergi.set_user_date('_User__email','kkringe@gmail.com')
print(sergi.get_email())
print(sergi.get_user_date())
    