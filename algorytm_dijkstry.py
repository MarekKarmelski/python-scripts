#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Dijkstry algorithm."""

import math
import re


def get_number_of_vertices():
    """Get number of vertices from input strem."""
    while True:
        try:
            number_of_verts = input('Enter the number of vertices: ')
            if number_of_verts.isdigit() is False:
                raise Exception('Number of vertices should be an integer.')
            number_of_verts = int(number_of_verts)
            if number_of_verts < 2:
                raise Exception('Number of vertices should be bigger then 1')
            break
        except Exception as e:
            print(e)
    return number_of_verts


def get_number_of_edges():
    """Get number of edges from input strem."""
    while True:
        try:
            number_of_edges = input('Enter the number of edges: ')
            if number_of_edges.isdigit() is False:
                raise Exception('Number of edges should be an integer.')
            number_of_edges = int(number_of_edges)
            if number_of_edges < 1:
                raise Exception('Number of edges should be bigger then 0')
            break
        except Exception as e:
            print(e)
    return number_of_edges


def get_start_vertice(number_of_verts):
    """Get number of start vertice."""
    while True:
        try:
            start_vertice = input('Enter the number of start vertice: ')
            if start_vertice.isdigit() is False:
                raise Exception('Start vertice should be an integer.')
            start_vertice = int(start_vertice)
            if start_vertice < 0 or start_vertice > number_of_verts - 1:
                error_msg = 'Start vertice should be an number from {0} to {1}'
                raise Exception(error_msg.format(*[0, number_of_verts - 1]))
            break
        except Exception as e:
            print(e)
    return start_vertice


def get_graph(number_of_verts, number_of_edges, verts):
    """Inicialize graph."""
    graph = [[math.inf for i in verts] for j in verts]
    print('Enter edge like: begin_vert_number:end_vert_number:edge_weight:')
    for ed in range(number_of_edges):
        while True:
            try:
                edge_str = input('Edge(%s)= ' % str(ed + 1))
                matched = re.match('^(\d+):(\d+):(\d+)$', edge_str)
                if matched is None:
                    raise Exception('You entered edge incorrect! Try again!')
                i_vert = int(matched.group(1))
                if i_vert < 0 or i_vert > number_of_verts - 1:
                    err_msg = 'Begin vert should be an number from {0} to {1}'
                    raise Exception(err_msg.format(*[0, number_of_verts - 1]))
                j_vert = int(matched.group(2))
                if j_vert < 0 or j_vert > number_of_verts - 1:
                    err_msg = 'End vert should be an number from {0} to {1}'
                    raise Exception(err_msg.format(*[0, number_of_verts - 1]))
                if i_vert == j_vert:
                    raise Exception("Verts can't be the same.")
                weight = int(matched.group(3))
                break
            except Exception as e:
                print(e)
        graph[i_vert][j_vert] = int(weight)
        edge = {
            'i': i_vert,
            'j': j_vert,
            'w': weight
        }
        print('Edge({i},{j})={w}'.format(**edge))
    return graph


def print_result(result, verts, start_vertice):
    """Print result to output stream."""
    for v in verts:
        path = []
        current_vert = v
        go = True
        while go:
            path.insert(0, str(current_vert))
            if result[current_vert]['prev'] <= -1:
                go = False
            else:
                current_vert = result[current_vert]['prev']
        print('Shortest path from {0} to {1}:'.format(*[start_vertice, v]))
        if math.isinf(result[v]['cost']):
            print('Shortest path not exist.')
        else:
            data_to_print = ['->'.join(path), result[v]['cost']]
            print('[{0}][cost: {1}]'.format(*data_to_print))
        print("\n")


def dijkstry_algorithm(graph, verts, start_vertice):
    """Dijkstry algorithm."""
    q = {}
    for v in verts:
        q[v] = math.inf
    q[start_vertice] = 0
    dp = {}
    for v in verts:
        dp[v] = {}
        dp[v]['cost'] = math.inf
        dp[v]['prev'] = -1
    dp[start_vertice]['cost'] = 0
    while len(q) > 0:
        min_val = min(q.values())
        idx = list(q.keys())[list(q.values()).index(min_val)]
        del(q[idx])
        for weight in graph[idx]:
            if math.isinf(weight) is not True:
                vert_idx = graph[idx].index(weight)
                new_cost = dp[idx]['cost'] + graph[idx][vert_idx]
                if dp[vert_idx]['cost'] > new_cost:
                    dp[vert_idx]['cost'] = new_cost
                    q[vert_idx] = new_cost
                    dp[vert_idx]['prev'] = idx
                graph[idx][vert_idx] = math.inf
    return dp


def main():
    """Program main function."""
    print("\n")
    print('Dijkstry Algorithm.')
    print('=' * 40)
    print("\n")
    number_of_verts = get_number_of_vertices()
    number_of_edges = get_number_of_edges()
    verts = range(number_of_verts)
    start_vertice = get_start_vertice(number_of_verts)
    graph = get_graph(number_of_verts, number_of_edges, verts)
    result = dijkstry_algorithm(graph, verts, start_vertice)
    print("\n")
    print_result(result, verts, start_vertice)
    print('End Algorithm.')
    print('=' * 40)
    print("\n")

main()
