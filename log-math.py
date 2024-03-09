from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import sympy

# Функция для обработки команды /start
def start(update, context):
    update.message.reply_text('Привет! Я бот для решения логарифмических уравнений. Просто отправь мне уравнение вида "log(x, base) = result".')

# Функция для решения логарифмического уравнения
def solve_log_equation(update, context):
    equation = update.message.text

    try:
        # Разделяем уравнение на левую и правую части
        left, right = equation.split('=')

        # Используем sympy для решения уравнения
        x = sympy.symbols('x')
        solution = sympy.solve(sympy.Eq(sympy.log(x, sympy.sympify(left)), sympy.sympify(right)), x)

        update.message.reply_text(f'Решение: x = {solution}')
    except Exception as e:
        update.message.reply_text(f'Ошибка: {e}')

def main():
    # Создаем объект Updater и передаем в него токен вашего бота
    updater = Updater("YOUR_TELEGRAM_BOT_TOKEN", use_context=True)

    # Получаем диспетчер для регистрации обработчиков
    dp = updater.dispatcher

    # Регистрируем обработчик команды /start
    dp.add_handler(CommandHandler("start", start))

    # Регистрируем обработчик для текстовых сообщений
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, solve_log_equation))

    # Запускаем бота
    updater.start_polling()

    # Останавливаем бота при нажатии Ctrl+C
    updater.idle()

if __name__ == '__main__':
    main()
