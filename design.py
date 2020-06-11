# -*- coding: utf-8 -*-
import re
from collections import namedtuple
from typing import Dict

Design = namedtuple('Design', 'name, size, flowers')


def create_design(new_design: str) -> Design:
    """
    Generate design namedtuple comprised of name, size, flowers
    :param new_design:
    :return:
    """
    items = re.split('(\d+)', new_design)
    name, size = items.pop(0)
    items.pop(-1)
    flowers = {'other': int(items.pop(-1))}

    for i in range(0, len(items), 2):
        flowers[items[i+1]] = int(items[i])

    return Design(name=name, size=size, flowers=flowers)


def receive_flower(
        flower: str, large_flowers: Dict, small_flowers: Dict) -> None:
    """
    Separate flowers per size
    :param flower:
    :param large_flowers:
    :param small_flowers:
    :return:
    """
    type, size = flower
    if size == 'L':
        large_flowers[type] = 1 + large_flowers.get(type, 0)
    else:
        small_flowers[type] = 1 + small_flowers.get(type, 0)


def generate_bouquet(
        design: Design, stock_flowers: Dict, bouquet: Dict) -> None:
    """
    Build the bouquet based on design
    :param design:
    :param stock_flowers:
    :param bouquet:
    :return:
    """

    requested_flowers = dict(design.flowers)
    other = requested_flowers.pop('other', None)
    remainder = other - sum(requested_flowers.values())

    for item, amount in requested_flowers.items():
        if stock_flowers.get(item, 0) == amount:
            bouquet[item] = stock_flowers.get(item, 0)
            stock_flowers[item] = stock_flowers.get(item, 0) - amount

    if bouquet.keys() == requested_flowers.keys() and remainder > 0:
        for flower, quantity in stock_flowers.items():
            if quantity >= remainder:
                bouquet[flower] = remainder
                stock_flowers[flower] = stock_flowers.get(flower, 0) - remainder
                bouquet['completed'] = True
                break


def new_bouquet(
        design: Design, large_flowers: Dict, small_flowers: Dict,
        bouquet: Dict):
    """
    Create small or large bouquet
    :param design:
    :param large_flowers:
    :param small_flowers:
    :param bouquet:
    :return:
    """

    if design.size == 'L':
        generate_bouquet(design, large_flowers, bouquet)
    else:
        generate_bouquet(design, small_flowers, bouquet)
