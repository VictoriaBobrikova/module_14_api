import unittest
# подключа код, который написали
import swagger

'''
Swagger API  test v0.3
'''

# функция просто возвращает статус-код
def status(r):
    return r.status_code

# класс для апи тестов
class SwaggerAPITest(unittest.TestCase):
    def test_get_petinfo01(self):
        "Получение информации о питомце, позитивный"
        # сначала функция pet(1) выполнется в swagger и вернет объект ответа, 
        # затем функция status примет объект ответа и вернет целое число - статус-код
        self.assertEqual(status(swagger.pet(1)), 200)
    def test_get_petinfo02(self):
        "Получение информации о питомце, негативный - не найден"
        self.assertEqual(status(swagger.pet(600)), 404)
    def test_get_petinfo03(self):
        "Получение информации о питомце, негативный - Invalid ID supplied"
        self.assertEqual(status(swagger.pet("2+2")), 400)
    # Тест обновлений питомца    
    def test_get_pet_upd01(self):
        "Обновление информации о питомце, позитивный"
        # сначала функция pet_upd(1,"dog") выполнется в swagger и вернет объект ответа, 
        # затем функция status примет объект ответа и вернет целое число - статус-код
        self.assertEqual(status(swagger.pet_upd(1,"dog")), 200) 
    def test_get_pet_upd02(self):
        "Обновление информации о питомце, негативный"
        self.assertEqual(status(swagger.pet_upd(0,"cat")), 405) 
    def test_get_pet_upd03(self):
        "Обновление информации о питомце, Invalid ID"
        self.assertEqual(status(swagger.pet_upd("abc","frog")), 405)
        
    # тест поиск питомцев по статусу
    def test_get_find01(self):
        "Поиск питомцев по статусу, позитивный"
        self.assertEqual(status(swagger.pet_find_by_status("available")), 200)

    def test_get_find02(self):
        "Поиск питомцев по нескольким статусам, позитивный"
        self.assertEqual(status(swagger.pet_find_by_status(["available","sold"])), 200)

    def test_get_find03(self):
        "Поиск питомцев по статусу, негативный - Invalid status value"
        self.assertEqual(status(swagger.pet_find_by_status(123)), 400)

    # тест создать питомца
    def test_new_pet01(self):
        "Создание нового питомца, позитивный"
        self.assertEqual(status(swagger.pet_new(15, "erty")), 200)

    def test_new_pet02(self):
        "Создание нового питомца, негативный, послать символы в id - Invalid input"
        self.assertEqual(status(swagger.pet_new("abc", "erty")), 405)

    def test_new_pet03(self):
        "Создание нового питомца, негативный, ничего не послать в требуемое поле имя - Invalid input"
        self.assertEqual(status(swagger.pet_new(123, None)), 405)

    def test_new_pet04(self):
        "Создание нового питомца, негативный, послать отриц. число в id - Invalid input"
        self.assertEqual(status(swagger.pet_new(-10, "erty")), 405)

    def test_new_pet05(self):
        "Создание нового питомца, негативный, послать число в имя - Invalid input"
        self.assertEqual(status(swagger.pet_new(15, 123)), 405)


if __name__ == '__main__':
    unittest.main(verbosity=2)