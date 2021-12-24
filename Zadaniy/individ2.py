#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import json
import click


@click.group()
def cliс():
    pass


@cliс.command()
@click.argument('filename')
@click.option("-n", "--name")
@click.option("-z", "--zodiac")
@click.option("-yr", "--year")
def add(filename, name, zodiac, year):
    """
    Добавить данные о человеке.
    """
    people = load_people(filename)
    people.append(
        {
            'name': name,
            'zodiac': zodiac,
            'year': year,
        }
    )
    with open(filename, "w", encoding="utf-8") as fout:
        json.dump(people, fout, ensure_ascii=False, indent=4)
    click.secho("Человек добавлен", fg='blue')


@cliс.command()
@click.argument('filename')
def display(filename):
    """
    Отобразить список людей.
    """
    people = load_people(filename)
    # Заголовок таблицы.
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 15
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
            "№",
            "Ф.И.О.",
            "Знак Зодиака",
            "Дата рождения"
        )
    )
    print(line)
    # Вывести данные о всех людях.
    for idx, human in enumerate(people, 1):
        print(
            '| {:>4} | {:<30} | {:<20} | {:>15} |'.format(
                idx,
                human['name'],
                human['zodiac'],
                ' '.join((str(i) for i in human['year']))
            )
        )
    print(line)


@cliс.command()
@click.argument('filename')
def select(filename):
    """
    Выбрать человека по фамилии.
    """
    people = load_people(filename)
    who = input('Кого ищем?: ')
    count = 0
    line = '+-{}-+-{}-+-{}-+-{}-+'.format(
        '-' * 4,
        '-' * 30,
        '-' * 20,
        '-' * 15
    )
    print(line)
    print(
        '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
            "№",
            "Ф.И.О.",
            "Знак Зодиака",
            "Дата рождения"
        )
    )
    print(line)
    for i, num in enumerate(people, 1):
        if who == num['name']:
            count += 1
            print(
                '| {:^4} | {:^30} | {:^20} | {:^15} |'.format(
                    count,
                    num['name'],
                    num['zodiac'],
                    ' '.join((str(i) for i in num['year']))))
    print(line)
    if count == 0:
        print('Никто не найден')


def load_people(file_name):
    """
    Загрузить всех людей из файла JSON
    """

    with open(file_name, "r", encoding="utf-8") as fin:
        return json.load(fin)


def main():
    cliс()


if __name__ == '__main__':
    main()
