from random import randint
from graphic_arts.start_game_banner import run_screensaver


def attack(char_name: str, char_class: str):
    """Функция атаки.Возвращает значение нанесенного урона."""
    if char_class == 'warrior':
        return (f'{char_name: str} нанёс урон'
                f'противнику равный {5 + randint(3, 5)}')
    if char_class == 'mage':
        return (f'{char_name: str} нанёс урон противнику равный '
                f'{5 + randint(5, 10)}')
    if char_class == 'healer':
        return (f'{char_name: str} нанёс урон противнику равный'
                f'{5 + randint(-3, -1)}')


def defence(char_name: str, char_class: str):
    """Функция защиты.Возвращает значение заблокированного урона."""
    if char_class == 'warrior':
        return (f'{char_name: str} блокировал {10 + randint(5, 10)} урона')
    if char_class == 'mage':
        return (f'{char_name: str} блокировал {10 + randint(-2, 2)} урона')
    if char_class == 'healer':
        return (f'{char_name: str} блокировал {10 + randint(2, 5)} урона')


def special(char_name: str, char_class: str):
    """Функция вызова умений мага.Возвращает значение специального умения."""
    if char_class == 'warrior':
        return (f'{char_name: str} применил специальное умение'
                f' «Выносливость {80 + 25}»')
    if char_class == 'mage':
        return (f'{char_name: str} применил специальное'
                f' умение «Атака {5 + 40}»')
    if char_class == 'healer':
        return (f'{char_name: str} применил специальное'
                f' умение «Защита {10 + 30}»')


def start_training(char_name: str, char_class: str) -> str:
    """Функция тренировки умений."""
    if char_class == 'warrior':
        print(f'{char_name: str}, ты Воитель — отличный боец ближнего боя.')
    if char_class == 'mage':
        print(f'{char_name: str}, ты Магик — превосходный укротитель стихий.')
    if char_class == 'healer':
        print(f'{char_name: str}, ты Лекарь — чародей,'
              f' способный исцелять раны.')
        print('Потренируйся управлять своими навыками.')
        print('Введи одну из команд: attack — чтобы атаковать противника,'
              ' defence— чтобы блокировать атаку противника или special — '
              ' чтобы использовать свою суперсилу.')
        print('Если не хочешь тренироваться, введи команду skip.')
    cmd = None
    while cmd != 'skip':
        cmd = input('Введи команду: ')
        if cmd == 'attack':
            print(f'attack{char_name: str, char_class: str}')
        if cmd == 'defence':
            print(f'defence{char_name: str, char_class: str}')
        if cmd == 'special':
            print(f'special{char_name: str, char_class: str}')
    return 'Тренировка окончена.'


def choice_char_class(char_class, approve_choice) -> str:
    """Функция выбора класса перса."""
    approve_choice = None
    char_class = None
    while approve_choice != 'y':
        char_class = input('Введи название персонажа, за которого'
                           ' хочешь играть: Воитель — warrior,'
                           ' Магик — mage, Лекарь — healer: ')
        if char_class == 'warrior':
            print('Воитель — дерзкий воин ближнего боя. Сильный, выносливый и'
                  ' отважный.')
        if char_class == 'mage':
            print('Магик — находчивый воин дальнего боя. Обладает высоким'
                  ' интеллектом.')
        if char_class == 'healer':
            print('Лекарь — могущественный заклинатель. Черпает силы из'
                  ' природы, веры и духов.')
        approve_choice = input('Нажми (Y), чтобы подтвердить выбор, или'
                               ' любую другую кнопку, чтобы выбрать'
                               ' другого персонажа ').lower()
    return char_class


def main() -> None:
    if __name__ == '__main__':
        run_screensaver()
        print('Приветствую тебя, искатель приключений!')
        print('Прежде чем начать игру...')
        char_name = input('...назови себя: ')
        print(f'Здравствуй, {char_name}! '
              'Сейчас твоя выносливость — 80, атака — 5 и защита — 10.')
        print('Ты можешь выбрать один из трёх путей силы:')
        print('Воитель, Магик, Лекарь')
        char_class: str = choice_char_class(char_name, char_class)
        print(start_training(char_name, char_class))


main()
