from datetime import datetime, timezone
import time


def get_valid_datetime():
    while True:
        date_str = input("Введите дату и время дедлайна в формате 'гггг-мм-дд чч:мм': ")
        try:
            # Удаляем лишние кавычки из введенной строки
            date_str = date_str.replace("'", "")

            deadline = datetime.strptime(date_str, '%Y-%m-%d %H:%M').replace(tzinfo=timezone.utc)
            current_time_utc = datetime.now(timezone.utc)

            if deadline > current_time_utc:
                return deadline
            else:
                print("Ошибка. Дедлайн должен быть в будущем.")
        except ValueError as e:
            print(f"Ошибка в формате ввода. Пожалуйста, введите корректную дату и время. Ошибка: {e}")


def deadline_timer():
    # Получаем ввод от пользователя для установки дедлайна
    deadline = get_valid_datetime()

    # Вычисляем разницу между текущим временем UTC и дедлайном
    time_until_deadline = deadline - datetime.now(timezone.utc)

    # Запускаем таймер
    print(f"Таймер установлен до {deadline}.")
    while time_until_deadline.total_seconds() > 0:
        print(f"Осталось времени: {time_until_deadline}")

        # Ожидание 24 часа перед следующим напоминанием
        time.sleep(24 * 60 * 60)

        # Обновляем разницу времени после каждого напоминания
        time_until_deadline = deadline - datetime.now(timezone.utc)

    print("Время истекло! Дедлайн достигнут.")


# Запуск таймера
deadline_timer()
