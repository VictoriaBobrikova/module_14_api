import requests
import json
'''
Swagger API call v 0.5
'''
# задали базовый урл
base_url = 'https://petstore.swagger.io/v2'

# получаем информацию о питомце по ид
def pet(petid):
    api_url = f"{base_url}/pet/{petid}"
    r = requests.get(api_url)
    return r
# для обновления информации нам надо послать ИД, имя и статус
def pet_upd(petid, name, status="available"):
    api_url = f"{base_url}/pet/{petid}"
    # словарь с параметрами
    api_data = {
        'petId':petid,
        'name':name,
        'status':status
        }
    r = requests.post(api_url, api_data)
    return r    

# выводим и анализируем результат
def req_info(r):
    try:
        answer = r.json()
    # если случилась ошибка декодирования
    except json.decoder.JSONDecodeError:
        answer = r.content
    # узнаем статус-код
    print("Status Code:",r.status_code)
    # и печатаем что там в ответе
    print(answer)

if __name__ == '__main__':
    # с ид 1 должно быть все ок -200
    r = pet(1)
    req_info(r)
    # тут должно быть 404
    r = pet(0)
    req_info(r)
    # по документаци при неверном ид должен возвращаться статус 400
    r = pet(5.01)
    req_info(r)

    print("UPD")
    # апд. по апи
    r = pet_upd(1, "dog")
    req_info(r)