import telebot
from telebot import types
import sqlite3

admin = 1027338863
admin_group = -1001215418826
ssilka = "https://t.me/joinchat/AAAAAEhx0cpogckCJK3zHw"
token = "905874416:AAFbw2-jX_DGg-IFBKhcH3KqQGdznumtgh8"
ssilka2 = "http://t.me/tanishuv_uz_bot"


bot = telebot.TeleBot(token)


sud = 0
res = {}

def info(id):
    there = False
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    sql = "SELECT * FROM albums WHERE id=?"
    cursor.execute(sql, [(id)])
    anketa = cursor.fetchall()
    conn.close()
    for punct in range(len(anketa[0])-1):
        if anketa[0][1+punct] == "Не заполнено":
            there = True
            return (1+punct)
            break
    if there == False: return "None"

def text(punct, root, name, id):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    sql = "SELECT * FROM albums WHERE id=?"
    cursor.execute(sql, [(id)])
    result = cursor.fetchall()
    conn.close()
    if "photos/file" in result[0][1]: photot = "Поставлена 🖼"
    else: photot = result[0][1]
    if root == False:
        form = "*Ваша анкета 📋*\n\n 〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n1.📸 *Фотография*:  _"\
                             +photot + "_\n➖\n2.👤 *Имя*:  _" + result[0][2] + "_\n➖\n3.🧬 *Пол*:  _" + result[0][3] + "_\n➖\n4.🔞 *Возраст*:  _" + result[0][4] + "_\n➖\n5.🌎 *Город*:  _" + \
           result[0][5] + "_\n➖\n6.📝 *О себе:*  _" + result[0][6] + "_\n➖\n7.🔎 *Кого ищете:*  _" + result[0][7] + "_\n➖\n8.💌 *Контакты:*  _" + result[0][8] + "_"
        if punct == 1: end = "\n\n 〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n\n👇 *ОТПРАВЬТЕ ВАШУ ФОТОГРАФИЮ*❗ 👇\n"
        elif punct == 2: end = "\n\n 〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n\n👇 *НАПИШИТЕ СВОЁ ИМЯ*❗ 👇\n"
        elif punct == 3: end = "\n\n 〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n\n👇 *НАПИШИТЕ ВАШ ПОЛ ЦИФРОЙ ( 1 - Муж. / 2 - Жен. )*❗ 👇\n"
        elif punct == 4: end = "\n\n 〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n\n👇 *НАПИШИТЕ СВОЙ ВОЗРАСТ*❗ 👇\n"
        elif punct == 5: end = "\n\n 〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n\n👇 *НАПИШИТЕ СВОЙ ГОРОД*❗ 👇\n"
        elif punct == 6: end = "\n\n 〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n\n👇 *РАССКАЖИТЕ НЕМНОГО О СЕБЕ*❗ 👇\n"
        elif punct == 7: end = "\n\n 〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n\n👇 *УКАЖИТЕ КОГО ВЫ ХОТИТЕ НАЙТИ*❗ 👇\n"
        elif punct == 8: end = "\n\n 〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n\n👇 *ОТПРАВЬТЕ СВОИ КОНТАКТНЫЕ ДАННЫЕ*❗ 👇\n"
        else: end = ""
    else:
        form = "*Новая заявка* _|_ *id "+ str(name) +"*\n\n 〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️\n1.📸 *Фотография*:  _"\
                             +photot + "_\n➖\n2.👤 *Имя*:  _" + result[0][2] + "_\n➖\n3.🧬 *Пол*:  _" + result[0][3] + "_\n➖\n4.🔞 *Возраст*:  _" + result[0][4] + "_\n➖\n5.🌎 *Город*:  _" + \
           result[0][5] + "_\n➖\n6.📝 *О себе:*  _" + result[0][6] + "_\n➖\n7.🔎 *Кого ищете:*  _" + result[0][7] + "_\n➖\n8.💌 *Контакты:*  _" + result[0][8] + "_\n\n 〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️〰️"
        end = ""
    return str(form + end)



@bot.message_handler(commands=['start'])
def start(message):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    try:
        cursor.execute("""CREATE TABLE albums
                      (id integer, photo text, name text, sex text, age text,
                       city text, myself text, find text, contact text)
                   """)

    except:
        exc = True
    sql = "SELECT * FROM albums WHERE id=?"
    cursor.execute(sql, [(message.chat.id)])
    if cursor.fetchall() == []:
        albums = [0,'Не заполнено', 'Не заполнено', 'Не заполнено', 'Не заполнено', 'Не заполнено', 'Не заполнено', 'Не заполнено', 'Не заполнено']
        albums[0] = int(message.chat.id)
        cursor.execute("INSERT INTO albums VALUES (?,?,?,?,?,?,?,?,?)", albums)
        conn.commit()
    conn.close()

    conn = sqlite3.connect("moder.db")
    cursor = conn.cursor()
    try:
        cursor.execute("""CREATE TABLE albums
                      (id integer, message integer)
                   """)

    except:
        exc = True

    conn.commit()
    conn.close()


    bot.send_message(message.chat.id, text(info(message.chat.id), False, "None", message.chat.id), parse_mode="Markdown")


@bot.message_handler(commands=['delete'])
def delete(message):
    conn2 = sqlite3.connect("post.db")
    cursor2 = conn2.cursor()
    sql = "SELECT * FROM albums WHERE id=" + str(message.from_user.id)
    cursor2.execute(sql)
    tak = cursor2.fetchall()
    if tak != []:
        bot.delete_message(admin_group,tak[0][1])
        sql2 = "DELETE FROM albums WHERE id=?"
        cursor2.execute(sql2, [(message.from_user.id)])
        conn2.commit()
        conn2.close()
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        sql = "DELETE FROM albums WHERE id=?"
        cursor.execute(sql, [(message.from_user.id)])
        albums = [message.from_user.id, "Не заполнено", "Не заполнено", "Не заполнено", "Не заполнено", "Не заполнено", "Не заполнено", "Не заполнено", "Не заполнено"]
        cursor.execute("INSERT INTO albums VALUES (?,?,?,?,?,?,?,?,?)", albums)
        conn.commit()
        conn.close()
        bot.send_message(message.chat.id, "❗ *Анкета удалена. Теперь вы можете создать новую!*", parse_mode="Markdown")
        res = bot.send_message(message.chat.id, text(info(message.chat.id), False, "None", message.from_user.id),
                            parse_mode="Markdown")
        conn10 = sqlite3.connect("last.db")
        cursor10 = conn10.cursor()
        sql10 = "SELECT * FROM albums WHERE id=?"
        cursor10.execute(sql10, [(message.from_user.id)])
        if cursor10.fetchall() == []:
            albums = [message.from_user.id, res.message_id]
            cursor10.execute("INSERT INTO albums VALUES (?,?)", albums)
        else:
            sql10 = """
            UPDATE albums 
            SET message = '""" + str(res.message_id) + """'
            WHERE id = """ + str(message.from_user.id)
            cursor10.execute(sql10)
        conn10.commit()
        conn10.close()




@bot.message_handler(content_types=['photo'])
def handle_docs_photo(message):
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    if info(message.from_user.id) == 1 and message.from_user.id !=admin:
        file_info = bot.get_file(message.photo[len(message.photo) - 1].file_id)
        sql = """
                        UPDATE albums 
                        SET photo = '""" + str(file_info.file_path) + """' 
                        WHERE id = """ + str(message.from_user.id)

        cursor.execute(sql)
        conn.commit()

        photo = types.InlineKeyboardButton("❌ Удалить ФОТО", callback_data='photo')
        name = types.InlineKeyboardButton("❌ Удалить ИМЯ", callback_data='name')
        sex = types.InlineKeyboardButton("❌ Удалить ПОЛ", callback_data='sex')
        age = types.InlineKeyboardButton("❌ Удалить ВОЗРАСТ", callback_data="age")
        city = types.InlineKeyboardButton("❌ Удалить ГОРОД", callback_data="city")
        myself = types.InlineKeyboardButton("❌ Удалить О СЕБЕ", callback_data="myself")
        find = types.InlineKeyboardButton("❌ Удалить КОГО ИЩЕТЕ", callback_data="find")
        contact = types.InlineKeyboardButton("❌ Удалить КОНТАКТЫ", callback_data="contact")
        enter = types.InlineKeyboardButton("📩 Отправить анкету", callback_data="enter")
        clear = types.InlineKeyboardButton("🗑 Очистить", callback_data="clear")

        sql = "SELECT * FROM albums WHERE id=?"
        cursor.execute(sql, [(message.from_user.id)])
        anketa = cursor.fetchall()

        markup = types.InlineKeyboardMarkup(row_width=2)

        markup.add(clear)

        buttons = []
        for punct in range(len(anketa[0]) - 1):
            if anketa[0][1 + punct] != "Не заполнено":
                if punct == 0: buttons.append(photo)
                if punct == 1: buttons.append(name)
                if punct == 2: buttons.append(sex)
                if punct == 3: buttons.append(age)
                if punct == 4: buttons.append(city)
                if punct == 5: buttons.append(myself)
                if punct == 6: buttons.append(find)
                if punct == 7: buttons.append(contact)

        k = 0
        if len(buttons) == 8: k = 9

        while buttons != []:
            if len(buttons) > 1:
                markup.add(buttons[0], buttons[1])
                buttons.remove(buttons[1])
                buttons.remove(buttons[0])
            else:
                markup.add(buttons[0])
                buttons.remove(buttons[0])

        if k == 9: markup.add(enter)


        res = bot.send_message(message.chat.id, text(info(message.chat.id), False, "None", message.from_user.id),
                               reply_markup=markup, parse_mode="Markdown")
        conn10 = sqlite3.connect("last.db")
        cursor10 = conn10.cursor()
        sql10 = "SELECT * FROM albums WHERE id=?"
        cursor10.execute(sql10, [(message.from_user.id)])
        if cursor10.fetchall() == []:
            albums = [message.from_user.id, res.message_id]
            cursor10.execute("INSERT INTO albums VALUES (?,?)", albums)
        else:
            sql10 = """
            UPDATE albums 
            SET message = '""" + str(res.message_id) + """'
            WHERE id = """ + str(message.from_user.id)
            cursor10.execute(sql10)
        conn10.commit()
        conn10.close()


@bot.message_handler(content_types=['text'])
def lalala(message):
    global markdown
    global res, sud, ssilka
    conn = sqlite3.connect("data.db")
    cursor = conn.cursor()
    if message.from_user.id != admin:
        conn2 = sqlite3.connect("moder.db")
        cursor2 = conn2.cursor()
        sql = "SELECT * FROM albums WHERE id=?"
        cursor2.execute(sql, [(message.from_user.id)])
        reres = cursor2.fetchall()
        conn2.close()
        if reres == []:
            conn2 = sqlite3.connect("post.db")
            cursor2 = conn2.cursor()
            sql = "SELECT * FROM albums WHERE id=" + str(message.from_user.id)
            cursor2.execute(sql)
            tak = cursor2.fetchall()
            conn2.close()
            if tak == []:
                try:
                    punct = "None"
                    if info(message.chat.id) == 1: punct = "photo"
                    if info(message.chat.id) == 2: punct = "name"
                    if info(message.chat.id) == 3: punct = "sex"
                    if info(message.chat.id) == 4: punct = "age"
                    if info(message.chat.id) == 5: punct = "city"
                    if info(message.chat.id) == 6: punct = "myself"
                    if info(message.chat.id) == 7: punct = "find"
                    if info(message.chat.id) == 8: punct = "contact"

                    if punct  != "None":

                        if punct != "photo":
                            sql = """
                            UPDATE albums 
                            SET """+punct+""" = '"""+str(message.text)+"""' 
                            WHERE id = """ + str(message.from_user.id)
                        else:
                            sql = """
                            UPDATE albums 
                            SET """ + punct + """ = 'Пустая (Не поставлена)' 
                            WHERE id = """ + str(message.from_user.id)

                        cursor.execute(sql)
                        conn.commit()



                    photo = types.InlineKeyboardButton("❌ Удалить ФОТО", callback_data='photo')
                    name = types.InlineKeyboardButton("❌ Удалить ИМЯ", callback_data='name')
                    sex = types.InlineKeyboardButton("❌ Удалить ПОЛ", callback_data='sex')
                    age = types.InlineKeyboardButton("❌ Удалить ВОЗРАСТ", callback_data="age")
                    city = types.InlineKeyboardButton("❌ Удалить ГОРОД", callback_data="city")
                    myself = types.InlineKeyboardButton("❌ Удалить О СЕБЕ", callback_data="myself")
                    find = types.InlineKeyboardButton("❌ Удалить КОГО ИЩЕТЕ", callback_data="find")
                    contact = types.InlineKeyboardButton("❌ Удалить КОНТАКТЫ", callback_data="contact")
                    enter = types.InlineKeyboardButton("📩 Отправить анкету", callback_data="enter")
                    clear = types.InlineKeyboardButton("🗑 Очистить", callback_data="clear")


                    sql = "SELECT * FROM albums WHERE id=?"
                    cursor.execute(sql, [(message.from_user.id)])
                    anketa = cursor.fetchall()


                    markup = types.InlineKeyboardMarkup(row_width=2)

                    markup.add(clear)

                    buttons = []
                    for punct in range(len(anketa[0]) - 1):
                        if anketa[0][1 + punct] != "Не заполнено":
                            if punct == 0: buttons.append(photo)
                            if punct == 1: buttons.append(name)
                            if punct == 2: buttons.append(sex)
                            if punct == 3: buttons.append(age)
                            if punct == 4: buttons.append(city)
                            if punct == 5: buttons.append(myself)
                            if punct == 6: buttons.append(find)
                            if punct == 7: buttons.append(contact)

                    k = 0
                    if len(buttons) == 8: k = 9

                    while buttons != []:
                        if len(buttons) > 1:
                            markup.add(buttons[0], buttons[1])
                            buttons.remove(buttons[1])
                            buttons.remove(buttons[0])
                        else:
                            markup.add(buttons[0])
                            buttons.remove(buttons[0])

                    if k==9: markup.add(enter)

                    conn.close()
                    res = bot.send_message(message.chat.id, text(info(message.chat.id), False, "None", message.from_user.id), reply_markup=markup, parse_mode="Markdown")
                    conn10 = sqlite3.connect("last.db")
                    cursor10 = conn10.cursor()
                    sql10 = "SELECT * FROM albums WHERE id=?"
                    cursor10.execute(sql10, [(message.from_user.id)])
                    if cursor10.fetchall() == []:
                        albums = [message.from_user.id, res.message_id]
                        cursor10.execute("INSERT INTO albums VALUES (?,?)", albums)
                    else:
                        sql10 = """
                        UPDATE albums 
                        SET message = '""" + str(res.message_id) + """'
                        WHERE id = """ + str(message.from_user.id)
                        cursor10.execute(sql10)
                    conn10.commit()
                    conn10.close()



                except Exception as e:
                    print(repr(e))
            else:
                bot.send_message(chat_id=message.chat.id, text="‼️*У вас уже есть одобренная анкета.*\n\nЧтобы удалить старую и создать новую, введите */delete*", parse_mode="Markdown")
        else:
            bot.send_message(chat_id=message.chat.id,
                             text="❗ *Вы не можете подать новую анкету. У вас уже есть одна на проверке. Ожидайте её одобрение модератором.*", parse_mode="Markdown")


    else:
        if sud != 0:
            conn2 = sqlite3.connect("moder.db")
            cursor2 = conn2.cursor()
            sql2 = "SELECT * FROM albums WHERE id=?"
            cursor2.execute(sql2, [(sud)])
            result2 = cursor2.fetchall()
            sql2 = "DELETE FROM albums WHERE id=?"
            cursor2.execute(sql2, [(sud)])
            conn2.commit()
            conn2.close()
            conn = sqlite3.connect("data.db")
            cursor = conn.cursor()
            sql = "SELECT * FROM albums WHERE id=?"
            cursor.execute(sql, [(result2[0][0])])
            result = cursor.fetchall()
            conn.close()
            bot.send_message(sud, "*Вашу анкету отклонили.*\n\n*Причина:* _" + message.text+"_", parse_mode="Markdown")
            bot.send_message(sud, "*😉 Попробуйте прислушаться к причине отказе и написать новую анкету!.*\n\nЧтобы появилось окно анкеты, напишите что-нибудь сюда.",
                             parse_mode="Markdown")
            try:
                bot.edit_message_caption(chat_id=admin, message_id=result2[0][1],
                                         caption=text(info(result[0][0]), True, str(result[0][0]),
                                                      result[0][0]) + "\n\nОТКЛОНЕНО ❌", parse_mode="Markdown")
            except:
                bot.edit_message_text(chat_id=admin, message_id=result2[0][1],
                                         text=text(info(result[0][0]), True, str(result[0][0]),
                                                      result[0][0]) + "\n\nОТКЛОНЕНО ❌", parse_mode="Markdown")
            bot.send_message(message.chat.id, "*Пользователь получил сообщение об отказе.* 📫", parse_mode="Markdown")
            sud = 0



@bot.callback_query_handler(func=lambda call: True)
def callback_inline(call):
    global res, sud
    try:
        conn = sqlite3.connect("data.db")
        cursor = conn.cursor()
        sql = "SELECT * FROM albums WHERE id=?"
        cursor.execute(sql, [(call.from_user.id)])
        anketa = cursor.fetchall()
        try:
            conn10 = sqlite3.connect("last.db")
            cursor10 = conn10.cursor()
            sql10 = "SELECT * FROM albums WHERE id=?"
            cursor10.execute(sql10, [(call.from_user.id)])
            now_id = cursor10.fetchall()[0][1]
            conn10.close()
        except:
            exc = True
        if call.data == "show":
            if str(bot.get_chat_member(admin_group, call.from_user.id).status) == "member" or str(bot.get_chat_member(admin_group, call.from_user.id).status)=="admin" or str(bot.get_chat_member(admin_group, call.from_user.id).status)=="creator":
                sql = "SELECT * FROM albums WHERE id=?"
                cursor.execute(sql, [(call.from_user.id)])
                test = cursor.fetchall()
                if test == []:
                    bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                              text="Чтобы получить номер, запусти бота.")
                else:
                    try:
                        conn3 = sqlite3.connect("post.db")
                        cursor3 = conn3.cursor()
                        sql3 = "SELECT * FROM albums WHERE message=?"
                        cursor3.execute(sql3, [(call.message.message_id)])
                        test2 = cursor3.fetchall()
                        sql = "SELECT * FROM albums WHERE id=?"
                        cursor.execute(sql, [(test2[0][0])])
                        test3 = cursor.fetchall()
                        conn.close()
                        bot.send_message(chat_id=call.from_user.id, text="*Вот контакты выбранного пользователя*:\n\n_" + str(test3[0][8])+ "_", parse_mode="Markdown")
                    except:
                        bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                                  text="Ошибка. Попробуй перезапустить бота.")
            else:
                bot.answer_callback_query(callback_query_id=call.id, show_alert=False,
                                          text="Для начала подпишитесь на этот канал!")
        if call.data == "clear" and call.message.message_id == now_id:
            conn8 = sqlite3.connect("data.db")
            cursor8 = conn8.cursor()
            sql8 = "DELETE FROM albums WHERE id=?"
            cursor8.execute(sql8, [(call.message.chat.id)])
            albums = [call.message.chat.id, "Не заполнено", "Не заполнено", "Не заполнено", "Не заполнено", "Не заполнено", "Не заполнено", "Не заполнено", "Не заполнено"]
            cursor8.execute("INSERT INTO albums VALUES (?,?,?,?,?,?,?,?,?)", albums)
            conn8.commit()
            conn8.close()
            clear = types.InlineKeyboardButton("🗑 Очистить", callback_data="clear")
            markup = types.InlineKeyboardMarkup(row_width=2)
            markup.add(clear)
            bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id,
                                  text=text(info(call.message.chat.id), False, "None", call.message.chat.id),
                                  reply_markup=markup, parse_mode="Markdown")
        if call.message.chat.id != admin:
            try:
                if call.data == "enter" and call.message.message_id == now_id:
                    if str(bot.get_chat_member(admin_group, call.message.chat.id).status) == "member":
                        conn5 = sqlite3.connect("moder.db")
                        cursor5= conn5.cursor()
                        sql = "SELECT * FROM albums WHERE id=?"
                        cursor5.execute(sql, [(call.message.chat.id)])
                        if cursor5.fetchall() == []:
                            markup2 = types.InlineKeyboardMarkup(row_width=2)
                            yes = types.InlineKeyboardButton("✅ Одобрить", callback_data="yes")
                            no = types.InlineKeyboardButton("❌ Отклонить", callback_data="no")
                            markup2.add(yes, no)
                            bot.edit_message_text(chat_id=call.from_user.id, message_id=res.message_id,
                                                  text=text(info(call.message.chat.id), False, "None", call.message.chat.id), parse_mode="Markdown")
                            try:
                                picture = bot.download_file(anketa[0][1])
                                res = bot.send_photo(chat_id=admin, photo=picture,
                                                     caption=text(info(call.message.chat.id), True, str(call.message.chat.id),
                                                                  call.message.chat.id), reply_markup=markup2, parse_mode="Markdown")
                            except:
                                res = bot.send_message(chat_id=admin,
                                                       text=text(info(call.message.chat.id), True, str(call.message.chat.id),
                                                                 call.message.chat.id), reply_markup=markup2, parse_mode="Markdown")
                            bot.send_message(chat_id=call.from_user.id, text="*Анкета отправлена на проверку* ✅\n\n_Ожидайте пока модератор проверит её._", parse_mode="Markdown")
                            albums = [call.message.chat.id, res.message_id]
                            cursor5.execute("INSERT INTO albums VALUES (?,?)", albums)
                            conn5.commit()

                        else:
                            bot.send_message(chat_id=call.from_user.id,
                                             text="❗ *Вы уже подавали анкету ранее. Ожидайте её модерирования*", parse_mode="Markdown")
                        conn5.close()
                    else:
                        markup4 = types.InlineKeyboardMarkup(row_width=1)
                        subs = types.InlineKeyboardButton("Подписаться", callback_data="subs", url=ssilka)
                        markup4.add(subs)
                        bot.send_message(chat_id=call.from_user.id,
                                         text="Чтобы создать свою анкету, нужны быть подписанным на основной канал. 📣\n\nПодпишитесь и повторите попытку:", reply_markup=markup4)

                elif call.message.message_id == now_id:

                    sql = """
                                                UPDATE albums 
                                                SET """ + str(call.data) + """ = 'Не заполнено' 
                                                WHERE id = """ + str(call.message.chat.id)


                    cursor.execute(sql)
                    conn.commit()

                    photo = types.InlineKeyboardButton("❌ Удалить ФОТО", callback_data='photo')
                    name = types.InlineKeyboardButton("❌ Удалить ИМЯ", callback_data='name')
                    sex = types.InlineKeyboardButton("❌ Удалить ПОЛ", callback_data='sex')
                    age = types.InlineKeyboardButton("❌ Удалить ВОЗРАСТ", callback_data="age")
                    city = types.InlineKeyboardButton("❌ Удалить ГОРОД", callback_data="city")
                    myself = types.InlineKeyboardButton("❌ Удалить О СЕБЕ", callback_data="myself")
                    find = types.InlineKeyboardButton("❌ Удалить КОГО ИЩЕТЕ", callback_data="find")
                    contact = types.InlineKeyboardButton("❌ Удалить КОНТАКТЫ", callback_data="contact")
                    enter = types.InlineKeyboardButton("📩 Отправить анкету", callback_data="enter")
                    clear = types.InlineKeyboardButton("🗑 Очистить", callback_data="clear")

                    sql = "SELECT * FROM albums WHERE id=?"
                    cursor.execute(sql, [(call.message.chat.id)])
                    anketa = cursor.fetchall()

                    markup = types.InlineKeyboardMarkup(row_width=2)

                    markup.add(clear)

                    buttons = []
                    for punct in range(len(anketa[0]) - 1):
                        if anketa[0][1 + punct] != "Не заполнено":
                            if punct == 0: buttons.append(photo)
                            if punct == 1: buttons.append(name)
                            if punct == 2: buttons.append(sex)
                            if punct == 3: buttons.append(age)
                            if punct == 4: buttons.append(city)
                            if punct == 5: buttons.append(myself)
                            if punct == 6: buttons.append(find)
                            if punct == 7: buttons.append(contact)
                    k = 0
                    if len(buttons) == 8: k = 9

                    while buttons != []:
                        if len(buttons) > 1:
                            markup.add(buttons[0], buttons[1])
                            buttons.remove(buttons[1])
                            buttons.remove(buttons[0])
                        else:
                            markup.add(buttons[0])
                            buttons.remove(buttons[0])

                    if k == 9: markup.add(enter)
                    bot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text=text(info(call.message.chat.id), False, "None", call.message.chat.id),
                                              reply_markup=markup, parse_mode="Markdown")

            except Exception as e:
                print(repr(e))
        else:

            conn2 = sqlite3.connect("moder.db")
            cursor2 = conn2.cursor()
            sql2 = "SELECT * FROM albums WHERE message=?"
            cursor2.execute(sql2, [(call.message.message_id)])
            result2 = cursor2.fetchall()
            sql = "SELECT * FROM albums WHERE id=?"
            cursor.execute(sql, [(result2[0][0])])
            result = cursor.fetchall()
            conn.close()
            if call.data == "yes":
                sql2 = "DELETE FROM albums WHERE id=?"
                cursor2.execute(sql2, [(result2[0][0])])
                conn2.commit()
                sud = 0
                if "photos/file" in result[0][1]:
                    photot = "Поставлена"
                else:
                    photot = result[0][1]
                markup3 = types.InlineKeyboardMarkup(row_width=1)
                show = types.InlineKeyboardButton("Показать контакты 👀", callback_data="show")
                sbot = types.InlineKeyboardButton("Запустить бота ⚙", callback_data="sbot", url=ssilka2)
                markup3.add(show)
                markup3.add(sbot)
                if result[0][1] != "Пустая (Не поставлена)":
                    picture = bot.download_file(result[0][1])
                    bot.edit_message_caption(chat_id=admin, message_id=result2[0][1],
                                  caption=text(info(result[0][0]), True, str(result[0][0]), result[0][0]) + "\n\nОДОБРЕННО ✅", parse_mode="Markdown")
                else:
                    if (result[0][3]) == "2":
                        picture = bot.download_file("photos/file_3.jpg")
                    elif (result[0][3] == "1"):
                        picture = bot.download_file("photos/file_1.jpg")
                    else:
                        picture = bot.download_file("photos/file_2.jpg")
                    bot.edit_message_text(chat_id=admin, message_id=result2[0][1],
                                  text=text(info(result[0][0]), True, str(result[0][0]), result[0][0]) + "\n\nОДОБРЕННО ✅", parse_mode="Markdown")
                res = bot.send_photo(chat_id=admin_group, photo=picture,
                                     caption="\n👤 *Имя:* _" + result[0][2] + "_\n➖\n🔞 *Возраст:* _" + result[0][
                                         4] + "_\n➖\n🌎 *Город:* _" + \
                                             result[0][5] + "_\n➖\n📝 *О себе:* _" + result[0][6] + "_\n➖\n🔎 *Ищет:* _" +
                                             result[0][7] +
                                             "_\n", reply_markup=markup3, parse_mode="Markdown")
                bot.send_message(result[0][0], "*📣 Вашу анкету опубликовали.*\n\n_Надеемся, вам скоро кто-то напишет 😉_", parse_mode="Markdown")
                bot.send_message(result[0][0],
                                 "ℹ Если захотите *удалить* свою анкету или *создать* новую, напишите */delete*",
                                 parse_mode="Markdown")
                conn3 = sqlite3.connect("post.db")
                cursor3 = conn3.cursor()
                albums = [result[0][0], res.message_id]
                cursor3.execute("INSERT INTO albums VALUES (?,?)", albums)
                conn3.commit()
                conn3.close()
            if call.data == "no":
                bot.send_message(chat_id=admin, text="Напишите причину отказа или одобрите:")
                sud = result[0][0]
            conn2.close()
        conn.close()
    except Exception as e:
        print(repr(e))








bot.polling(none_stop=True, timeout=123)
