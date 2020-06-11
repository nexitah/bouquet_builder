# -*- coding: utf-8 -*-
from typing import Dict

from design import create_design, receive_flower, new_bouquet, \
    Design

designs = []
large_flowers = {}
small_flowers = {}
bouquets = []


def format_bouquet(design: Design, bouquet: Dict) -> str:
    """
    The final return string
    :param design:
    :param bouquet:
    :return:
    """
    bouquet.pop('completed')
    bouquet.items()
    result = f'{design.name}{design.size}'
    for key, value in bouquet.items():
        result += f'{value}{key}'
    return result


def read_from_cmd_line() -> None:
    prepare_flowers = False
    print("Please enter values: (Write exit to terminate)")  # pink
    while True:
        try:
            data = input()
        except EOFError:
            break

        if 'exit' == data:
            break

        if data == '':
            prepare_flowers = True
            continue

        if not prepare_flowers:
            designs.append(create_design(data))
            bouquets.append({})
        else:
            receive_flower(data, large_flowers, small_flowers)

        for i, design, bouquet in zip(range(0, len(designs)), designs, bouquets):
            if 'completed' not in bouquet:
                new_bouquet(design, large_flowers, small_flowers, bouquet)

            if bouquet.get('completed', False):
                print(format_bouquet(design, bouquets.pop(i)))

    print('Done')


if __name__ == '__main__':
    read_from_cmd_line()
