from dao.model.user import User


class UserDAO:
    def __init__(self, session):
        self.session = session

    """Получение всех пользователей"""

    def get_all_users(self):
        return self.session.query(User).all()

    """Получение пользователя по id"""

    def get_user_by_id(self, uid):
        return self.session.query(User).get(uid)

    """Получение пользователя по username"""

    def get_by_username(self, username):
        return self.session.query(User).filter(User.username == username).first()

    """Создание пользователя"""

    def create(self, user_d):
        ent = User(**user_d)
        self.session.add(ent)
        self.session.commit()
        return ent

    """Удаление пользователя по id"""

    def delete(self, uid):
        user = self.get_user_by_id(uid)
        self.session.delete(user)
        self.session.commit()

    """Обновление пользователя"""

    def update(self, user_d):
        user = self.get_user_by_id(user_d.get("id"))
        user.username = user_d.get("username")
        user.password = user_d.get("password")
        user.role = user_d.get("role")

        self.session.add(user)
        self.session.commit()
