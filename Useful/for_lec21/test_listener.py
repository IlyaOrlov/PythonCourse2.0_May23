import unittest.mock as mock
import listener_mock_example as lme


class TestListener:
    MSG = 'message'

    @staticmethod
    def check_msg(msg):
        assert msg == TestListener.MSG

    def test_listen_forever(self):
        # Подготовка к тестированию
        # Создаем объект тестируемого класса
        listener = lme.Listener()

        # Заменяем зависимости на mock-объекты
        lme.Listener.msg_broker = mock.Mock()
        lme.Listener.client = mock.Mock()

        # Настраиваем поведение mock-объектов
        # При инициализации атрибута side_effect итерируемым объектом
        # при каждом обращении к wait_message будет возвращаться очередной
        # элемент итерируемого объекта (сначала 'message', затем Exception).
        lme.Listener.msg_broker.wait_message.side_effect = [TestListener.MSG, Exception]

        # При инициализации атрибута side_effect функциональным (callable)
        # объектом при каждом обращении к process_message будет вызываться
        # этот функциональный объект.
        lme.Listener.client.process_message.side_effect = TestListener.check_msg

        # Тестируем и выполняем проверки
        listener.listen_forever()
        assert listener.running is False
        lme.Listener.client.process_message.assert_called_once_with(TestListener.MSG)
        assert lme.Listener.msg_broker.wait_message.call_count == 2
