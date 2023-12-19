from streamlit.testing.v1 import AppTest

def test_en_ru():
    # создаем приложение
    at = AppTest.from_file("translator.py")
    at.run()
    assert not at.exception

    # вводим текст на английском
    at.text_area(key='in_text').input('lesson').run()
    # запускаем перевод
    at.button(key="translate").click().run(timeout=60)
    # проверяем что нет ошибок и переведенная строка равна ожидаемой
    assert not at.exception
    assert at.text_area(key='out_text').value.strip("!?,. ").lower() == 'урок'

def test_ru_en():
    # создаем приложение
    at = AppTest.from_file("translator.py")
    at.run()
    assert not at.exception

    # меняем направление перевода на русско-английский
    at.button(key="btn_direction").click().run()
    # вводим текст на русском
    at.text_area(key='in_text').input('урок').run()
    # запускаем перевод
    at.button(key="translate").click().run(timeout=60)
    # проверяем что нет ошибок и переведенная строка равна ожидаемой
    assert not at.exception
    assert at.text_area(key='out_text').value.strip("!?,. ").lower() == 'lesson'
