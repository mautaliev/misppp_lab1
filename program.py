from data_service_lib import DataService


print("******************************************************************************")
print("* Спринт #1                                                                  *")
print("* Тема: Добавление к решению итоговых проектов по спринту                    *")
print("* Задание #7                                                                 *")
print("* Вариант #15                                                                *")
print("* Выполнил: Тяжов Леонид Александрович | ПКТ6-24-1                           *")
print("******************************************************************************")
print("* УСЛОВИЕ:                                                                   *")
print("* Написать программу, которая вычисляет математическое выражение по          *")
print("* исходным значениям данных, вводимых пользователем. Ответ округлите до      *")
print("* знаков после запятой.                                                      *")
print("*                                                                            *")
print("******************************************************************************")
print("* ИСХОДНЫЕ ДАННЫЕ :                                                          *")
print("******************************************************************************")
x = int(input('X: '))
print("******************************************************************************")
print(f"* РЕЗУЛЬТАТ:                               {DataService.calc(x)}            *")
print("******************************************************************************")
