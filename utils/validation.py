import re


class Validator:
    def __init__(self):
        pass

    # Функция валидации заполненности полей
    def ip_validate(self, value):
        if not isinstance(value, str):
            return False
        if len(value.strip()) < 6:
            return False
        # if re.match(r"^[a-zA-Z0-9_.+-]+$", value) is not None:
        #     return None
        # if (re.match(r"[а-яА-ЯёЁ]", value) is not None) == True:
        #     return False
        return True

    # Функция валидации e-mail адреса
    # def ip_validate(self, value):
    #     pattern = r"^[0-9]+.[0-9]+.[0-9]+.[0-9]"
    #     # print(re.match(pattern, email))
    #     if re.match(pattern, value) != None:
    #         return True
    #     return False
    # return False if re.match(pattern, email) is not None else True
