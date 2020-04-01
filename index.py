import vk_api
from vk_api.longpoll import VkLongPoll, VkEventType


def write_msg(user_id, message):
    vk.method('messages.send', {'user_id': user_id, 'message': message})

# API-ключ созданный ранее
token = "afbe2df68b46e6e036451d448d5d2c0fb8013c5b60125f55d8dc0809abf48a2c666ee95558f4ca2cf2ebc"

# Авторизуемся как сообщество
vk = vk_api.VkApi(token=token)



# Работа с сообщениями
longpoll = VkLongPoll(vk)

# Основной цикл
for event in longpoll.listen():

    # Если пришло новое сообщение
    if event.type == VkEventType.MESSAGE_NEW:
    
        # Если оно имеет метку для меня( то есть бота)
        if event.to_me:
        
            # Сообщение от пользователя
            request = event.text
            write_msg(event.user_id, "Отъебись и не пиши мне больше")
            
