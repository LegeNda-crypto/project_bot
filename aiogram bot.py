from aiogram import Bot, Dispatcher, types
from aiogram.utils import executor
from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton
from config import API_TOKEN

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
men_eggs = 0
a1 = 0
a2 = 0
a3 = 0
a4 = 0
a5 = 0
a6 = 0
a7 = 0
a8 = 0
a9 = 0
a10 = 0
a11 = 0


def create_inline_keyboard(buttons):
    keyboard = InlineKeyboardMarkup(row_width=2)
    for text, callback_data in buttons:
        keyboard.add(InlineKeyboardButton(text=text, callback_data=callback_data))
    return keyboard


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.answer(
        "Привет, прямо сейчас мы разбираем тему в презентации, но тут ты можешь узнать информацию чуть быстрее:)\n \n Жми на кнопку <информация>, прочти ее, запомни суть, далее нажми на кнопку <Пройти тест>, пользователь с самый большим количеством баллов получит ПРИЗ!! 🥇",
        reply_markup=create_inline_keyboard([
            ("Информация", "button1"),
            ("Пройти тест", "button2")

        ]))


@dp.callback_query_handler(lambda c: c.data and c.data.startswith('button'))
async def button_pressed(callback_query: types.CallbackQuery):
    await callback_query.answer()
    global men_eggs, a1, a2, a3, a4, a5, a6, a7, a8, a9, a10, a11
    if callback_query.data == 'button1':
        await callback_query.message.edit_text(
            "В этом телеграфе представлена вся нужная для теста информация \n https://telegra.ph/Teoriticheskaya-informaciya-po-testu-11-11",
            reply_markup=None)

    elif callback_query.data == 'button2':
        await callback_query.message.edit_text(
            "Что такое алгоритмическое мышление? \n  а) Способность решать математические задачи.\n б) Способность решать логические головоломки.\n в) Способность рассматривать задачи как последовательность шагов.\n г) Способность писать программы на компьютере.",
            reply_markup=create_inline_keyboard([
                ("a", "button3"),
                ("б", "button4"),
                ("в", "button5"),
                ("г", "button6")
            ]))
    elif callback_query.data == 'button3' or callback_query.data == 'button4' or callback_query.data == 'button6':
        await callback_query.message.edit_text("Прочти теорию еще раз )", reply_markup=create_inline_keyboard([
            ("Дальше", "button7")
        ]))

    elif callback_query.data == 'button5':
        await callback_query.message.edit_text("Aбсолютно верно", reply_markup=create_inline_keyboard([
            ("Дальше", "button8")
        ]))
        men_eggs += 1
        a1 += 1
    elif callback_query.data == 'button7' or callback_query.data == 'button8':
        await callback_query.message.edit_text(
            "Какой из следующих компонентов не является частью алгоритмического мышления? \n а) Разложение задачи. \n б) Абстрагирование. \n в) Творчество.\n г) Распознавание патернов.",
            reply_markup=create_inline_keyboard([
                ("a", "button9"),
                ("б", "button10"),
                ("в", "button11"),
                ("г", "button12")
            ]))
    elif callback_query.data == 'button9' or callback_query.data == 'button10' or callback_query.data == 'button12':
        await callback_query.message.edit_text("Почитай теорию еще раз )", reply_markup=create_inline_keyboard([
            ("Дальше", "button13")
        ]))

    elif callback_query.data == 'button11':
        await callback_query.message.edit_text("Aбсолютно верно", reply_markup=create_inline_keyboard([
            ("Дальше", "button14")
        ]))
        men_eggs += 1
        a2 += 1
    elif callback_query.data == 'button13' or callback_query.data == 'button14':
        await callback_query.message.edit_text(
            "Что такое разложение задачи в контексте алгоритмического мышления? \n а)Создание схемы задачи.\n б)Разделение сложной задачи на более простые подзадачи \n в)Составление списка необходимых ресурсов.\n г)Поиск информации в Интернете.",
            reply_markup=create_inline_keyboard([
                ("a", "button15"),
                ("б", "button16"),
                ("в", "button17"),
                ("г", "button18")
            ]))
    elif callback_query.data == 'button15' or callback_query.data == 'button17' or callback_query.data == 'button18':
        await callback_query.message.edit_text("Почитай теорию еще раз )", reply_markup=create_inline_keyboard([
            ("Дальше", "button19")
        ]))

    elif callback_query.data == 'button16':
        await callback_query.message.edit_text("Aбсолютно верно", reply_markup=create_inline_keyboard([
            ("Дальше", "button20")
        ]))
        men_eggs += 1
        a3 += 1
    elif callback_query.data == 'button19' or callback_query.data == 'button20':
        await callback_query.message.edit_text(
            "Какие логические операции используются в алгоритмическом мышлении? \n а)Сложение, вычитание, умножение, деление.\n б)И, ИЛИ, НЕ.\n в)Больше, меньше, равно.\n г)True, False.",
            reply_markup=create_inline_keyboard([
                ("a", "button21"),
                ("б", "button22"),
                ("в", "button23"),
                ("г", "button24")
            ]))
    elif callback_query.data == 'button21' or callback_query.data == 'button23' or callback_query.data == 'button24':
        await callback_query.message.edit_text("Почитай теорию еще раз )", reply_markup=create_inline_keyboard([
            ("Дальше", "button25")
        ]))

    elif callback_query.data == 'button22':
        await callback_query.message.edit_text("Aбсолютно верно", reply_markup=create_inline_keyboard([
            ("Дальше", "button26")
        ]))
        men_eggs += 1
        a4 += 1
    elif callback_query.data == 'button25' or callback_query.data == 'button26':
        await callback_query.message.edit_text(
            "Что такое оценка результатов в алгоритмическом мышлении? \n а)Проверка правильности решения.\n б)Измерение времени выполнения алгоритма.\n в)Определение стоимости решения.\n г)Все перечисленное выше.",
            reply_markup=create_inline_keyboard([
                ("a", "button27"),
                ("б", "button28"),
                ("в", "button29"),
                ("г", "button30")
            ]))
    elif callback_query.data == 'button27' or callback_query.data == 'button28' or callback_query.data == 'button29':
        await callback_query.message.edit_text("Почитай теорию еще раз )", reply_markup=create_inline_keyboard([
            ("Дальше", "button31")
        ]))

    elif callback_query.data == 'button30':
        await callback_query.message.edit_text("Aбсолютно верно", reply_markup=create_inline_keyboard([
            ("Дальше", "button32")
        ]))
        men_eggs += 1
        a5 += 1
    elif callback_query.data == 'button31' or callback_query.data == 'button32':
        await callback_query.message.edit_text(
            "Что изучает дискретная математика? \n а)Непрерывные величины.\n б)Дискретные объекты и структуры.\n в)Геометрические фигуры.\n г) Статистические данные.",
            reply_markup=create_inline_keyboard([
                ("a", "button33"),
                ("б", "button34"),
                ("в", "button35"),
                ("г", "button36")
            ]))
    elif callback_query.data == 'button33' or callback_query.data == 'button35' or callback_query.data == 'button36':
        await callback_query.message.edit_text("Почитай теорию еще раз )", reply_markup=create_inline_keyboard([
            ("Дальше", "button37")
        ]))

    elif callback_query.data == 'button34':
        await callback_query.message.edit_text("Aбсолютно верно", reply_markup=create_inline_keyboard([
            ("Дальше", "button38")
        ]))
        men_eggs += 1
        a6 += 1
    elif callback_query.data == 'button37' or callback_query.data == 'button38':
        await callback_query.message.edit_text(
            "Какие из следующих концепций дискретной математики релевантны для алгоритмического мышления? \n а)Логика и множества.\n б)Интегральное исчисление.\n в)Тригонометрия.\n г)Линейная алгебра.",
            reply_markup=create_inline_keyboard([
                ("a", "button39"),
                ("б", "button40"),
                ("в", "button41"),
                ("г", "button42")
            ]))
    elif callback_query.data == 'button40' or callback_query.data == 'button41' or callback_query.data == 'button42':
        await callback_query.message.edit_text("Почитай теорию еще раз )", reply_markup=create_inline_keyboard([
            ("Дальше", "button43")
        ]))

    elif callback_query.data == 'button39':
        await callback_query.message.edit_text("Aбсолютно верно", reply_markup=create_inline_keyboard([
            ("Дальше", "button44")
        ]))
        men_eggs += 1
        a7 += 1
    elif callback_query.data == 'button43' or callback_query.data == 'button44':
        await callback_query.message.edit_text(
            "Что такое графы в дискретной математике?\n а)Таблицы данных.\n б)Геометрические фигуры.\n в)Структуры данных, представляющие связи между объектами.\n г)Математические формулы.",
            reply_markup=create_inline_keyboard([
                ("a", "button45"),
                ("б", "button46"),
                ("в", "button47"),
                ("г", "button48")
            ]))
    elif callback_query.data == 'button45' or callback_query.data == 'button46' or callback_query.data == 'button48':
        await callback_query.message.edit_text("Почитай теорию еще раз )", reply_markup=create_inline_keyboard([
            ("Дальше", "button49")
        ]))
    elif callback_query.data == 'button47':
        await callback_query.message.edit_text("Aбсолютно верно", reply_markup=create_inline_keyboard([
            ("Дальше", "button50")
        ]))
        men_eggs += 1
        a8 += 1
    elif callback_query.data == 'button49' or callback_query.data == 'button50':
        await callback_query.message.edit_text(
            "Как комбинаторика применяется в алгоритмическом мышлении?\n а)Для определения числа возможных решений.\n б)Для построения графиков зависимостей.\n в)Для решения линейных уравнений.\n г)Для вычисления производных.",
            reply_markup=create_inline_keyboard([
                ("a", "button51"),
                ("б", "button52"),
                ("в", "button53"),
                ("г", "button54")
            ]))
    elif callback_query.data == 'button52' or callback_query.data == 'button53' or callback_query.data == 'button54':
        await callback_query.message.edit_text("Почитай теорию еще раз )", reply_markup=create_inline_keyboard([
            ("Дальше", "button55")
        ]))
    elif callback_query.data == 'button51':
        await callback_query.message.edit_text("Aбсолютно верно", reply_markup=create_inline_keyboard([
            ("Дальше", "button56")
        ]))
        men_eggs += 1
        a9 += 1
    elif callback_query.data == 'button55' or callback_query.data == 'button56':
        await callback_query.message.edit_text(
            "Как дискретная математика помогает определять алгоритмы?\n а)Предоставляет методы для доказательства правильности алгоритмов.\n б) Предоставляет методы для анализа сложности алгоритмов\n в)Предоставляет строгий язык и инструменты для описания алгоритмов.\n г)Все перечисленное выше.",
            reply_markup=create_inline_keyboard([
                ("a", "button57"),
                ("б", "button58"),
                ("в", "button59"),
                ("г", "button60")
            ]))
    elif callback_query.data == 'button57' or callback_query.data == 'button58' or callback_query.data == 'button59':
        await callback_query.message.edit_text("Почитай теорию еще раз )", reply_markup=create_inline_keyboard([
            ("Дальше", "button61")
        ]))
    elif callback_query.data == 'button60':
        await callback_query.message.edit_text("Aбсолютно верно", reply_markup=create_inline_keyboard([
            ("Дальше", "button62")
        ]))
        men_eggs += 1
        a10 += 1
    elif callback_query.data == 'button61' or callback_query.data == 'button62':
        await callback_query.message.edit_text(
            "Что является главным выводом из текста Обучение алгоритмическому мышлению с использованием дискретной математики?\n а)Алгоритмическое мышление не связано с дискретной математикой.\n б)Дискретная математика не нужна для развития алгоритмического мышления.\n в)Дискретная математика является основой для развития алгоритмического мышления.\n г) Алгоритмическое мышление не важно для современного мира.",
            reply_markup=create_inline_keyboard([
                ("a", "button63"),
                ("б", "button64"),
                ("в", "button65"),
                ("г", "button66")
            ]))
    elif callback_query.data == 'button63' or callback_query.data == 'button64' or callback_query.data == 'button66':
        await callback_query.message.edit_text("Почитай теорию еще раз )", reply_markup=create_inline_keyboard([
            ("Дальше", "button67")
        ]))
    elif callback_query.data == 'button60':
        await callback_query.message.edit_text("Aбсолютно верно", reply_markup=create_inline_keyboard([
            ("Дальше", "button68")
        ]))
        men_eggs += 1
        a11 += 1
    elif a1 > 1:
        a1 = 1
    elif a2 > 1:
        a2 = 1
    elif a3 > 1:
        a3 = 1
    elif a4 > 1:
        a4 = 1
    elif a5 > 1:
        a5 = 1
    elif a6 > 1:
        a6 = 1
    elif a7 > 1:
        a7 = 1
    elif a8 > 1:
        a8 = 1
    elif a9 > 1:
        a9 = 1
    elif a10 > 1:
        a10 = 1
    elif a11 > 1:
        a11 = 1
    elif callback_query.data == 'button67' or callback_query.data == 'button68':
        await callback_query.message.edit_text(
            f'Поздравляю!!! Вы прошли наш тест и набрали в нем {men_eggs}/11 \n 1 вопрос : {a1} \n 2 вопрос : {a2} \n 3 вопрос : {a3}\n 4 вопрос : {a4} \n 5 вопрос : {a5}\n 6 вопрос : {a6} \n 7 вопрос : {a7}\n 8 вопрос : {a8} \n 9 вопрос : {a9}\n 10 вопрос : {a10}\n 11 вопрос : {a11} \n A в этом документе вы сможете узнать правильность выполнения заданийм \n  https://telegra.ph/Razyasneniya-11-11',
            reply_markup=None)


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
