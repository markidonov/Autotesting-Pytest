import pytest


@pytest.fixture
def a():
    return 25

@pytest.fixture
def b():
    return 35

@pytest.fixture
def c():
    return 25.5

@pytest.fixture
def d():
    return 0


@pytest.fixture
def e():
    return 2556756756730982092340598329478623045923874593287562830459237


@pytest.fixture
#"Ошибка вычисления"
def code_one():
    return ("\u041e\u0448\u0438\u0431\u043a\u0430 \u0432\u044b\u0447\u0438"
            "\u0441\u043b\u0435\u043d\u0438\u044f")


@pytest.fixture
#"Не указаны необходимые параметры"
def code_two():
    return ("\u041d\u0435 \u0443\u043a\u0430\u0437\u0430\u043d\u044b "
            "\u043d\u0435\u043e\u0431\u0445\u043e\u0434\u0438\u043c\u044b"
            "\u0435 \u043f\u0430\u0440\u0430\u043c\u0435\u0442\u0440\u044b")


@pytest.fixture
#"Значения параметров должны быть целыми"
def code_three():
    return ("\u0417\u043d\u0430\u0447\u0435\u043d\u0438\u044f \u043f\u0430"
            "\u0440\u0430\u043c\u0435\u0442\u0440\u043e\u0432 \u0434\u043e"
            "\u043b\u0436\u043d\u044b \u0431\u044b\u0442\u044c \u0446\u0435"
            "\u043b\u044b\u043c\u0438")


@pytest.fixture
#"Превышены максимальные значения параметров"
def code_four():
    return ("\u041f\u0440\u0435\u0432\u044b\u0448\u0435\u043d\u044b "
            "\u043c\u0430\u043a\u0441\u0438\u043c\u0430\u043b\u044c"
            "\u043d\u044b\u0435 \u0437\u043d\u0430\u0447\u0435\u043d"
            "\u0438\u044f \u043f\u0430\u0440\u0430\u043c\u0435\u0442"
            "\u0440\u043e\u0432")


@pytest.fixture
#"Не верное имя задачи или тип HTTP запроса"
def code_five():
    return str("\u041d\u0435 \u0432\u0435\u0440\u043d\u043e\u0435 "
           "\u0438\u043c\u044f \u0437\u0430\u0434\u0430\u0447\u0438 \u0438"
           "\u043b\u0438 \u0442\u0438\u043f HTTP \u0437\u0430\u043f\u0440"
           "\u043e\u0441\u0430")
