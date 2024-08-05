# Задание "Свой YouTube"
import time

class User:
    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __repr__(self):
        return f"{self.nickname}"

class Video:
    def __init__(self, title, duration, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode

    def play(self):
        if self.time_now < self.duration:
            self.time_now += 1
            print(f"{self.time_now}", end=' ')
        if self.time_now == self.duration:
            print(f"Конец видео")

    def __repr__(self):
        return (f"Ролик(title='{self.title}', продолжительность={self.duration}, секунда остановки={self.time_now}, "
                f"ограничение по возрасту={self.adult_mode})")

class UrTube:
    def __init__(self):
        self.users = []
        self.videos = []
        self.current_user = None
        self.logged = False

    def log_in(self, nickname, password):
        hash_password = hash(password)
        user = next((u for u in self.users if u.nickname == nickname and u.password == hash_password), None)
        if user:
            self.current_user = user
            # print(f"Пользователь'{self.current_user.nickname}' успешно вошел в систему")
            self.logged = True
        else:
            print("Неверное имя пользователя или пароль!")

    def register(self, nickname, password, age):
        if any(u.nickname == nickname for u in self.users):
            print(f"Пользователь {nickname} уже существует")
        else:
            new_user = User(nickname, password, age)
            self.users.append(new_user)
            # print(f"Пользователь {new_user.nickname} добавлен")
            self.log_in(nickname, password)

    def log_out(self):
        if self.current_user:
            print(f"Пользователь '{self.current_user.nickname}' вышел")
            self.current_user = None
        else:
            print("Ни один пользователь в настоящее время не вошел в систему")

    def add(self, *videos):
        for __video in videos:
            if not any(v.title == __video.title for v in self.videos):
                self.videos.append(__video)
                # print(f"Ролик '{__video.title}' добавлен")
            else:
                print(f"Ролик '{__video.title}' уже существует")

    def get_videos(self, search_word):
        search_word_l = search_word.lower()
        return [video.title for video in self.videos if search_word_l in video.title.lower()]

    def watch_video(self, title):

        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео")
            return
        if self.current_user.age < 18:
            print("Вам нет 18 лет, пожалуйста покиньте страницу")
            return
        video = next((v for v in self.videos if v.title == title), None)
        if video:
            # while video.time_now < video.duration:
            for sec in range(1, video.duration + 1):
                video.play()
                time.sleep(1)
        # else:
        #     print(f"Ролик '{title}' не найден")

    def __repr__(self):
        return (f"UrTube(пользователи={self.users}, ролики={self.videos}, "
                f"текущий пользователь={self.current_user})")

# if __name__ == '__main__':
ur = UrTube()

v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
