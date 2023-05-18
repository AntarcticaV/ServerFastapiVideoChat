from app.repasitories.user import UserTemRepasitories


TMP_REPASITORY_USER = UserTemRepasitories()


def get_user_repo() -> UserTemRepasitories:
    return TMP_REPASITORY_USER
