def user_data(**info):
    out_data = ""
    for key, value in info.items():
        out_data += "{} - {} . ".format(key, value)
    print(out_data.lstrip())


user_data(имя="Евгений", фамилия="Райлян", год=1979, город="Кишинев", email="railean@mail.ru", cellphone="+37369863456")
