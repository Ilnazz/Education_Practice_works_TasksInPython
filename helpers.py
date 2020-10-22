"""Вспомогательные функции"""


def ask(question, yes, no):
    """Возвращает ответ на вопрос question в форме True/False"""
    answer = input('{0}? ({1}/{2}): '.format(question, yes, no))
    answer = answer.strip()
    if answer == yes:
        return True
    return False
