#!/usr/bin/env python3
import sys
import argparse
import csv
from typing import List, Dict, Tuple


def main(args: List[str]) -> int:
    arg_parser = argparse.ArgumentParser()
    arg_parser.add_argument('-s', '--stop', required=True, type=str)
    arg_parser.add_argument('-r', '--route', required=True, type=str)
    arg_parser.add_argument('-o', '--output', required=True, type=str)
    arguments = arg_parser.parse_args(args[1:])

    # Load stop ID to node ID mapping
    stop_id_to_node_id: Dict[int, int] = {}
    with open(arguments.stop, 'r') as in_file:
        dict_reader = csv.DictReader(in_file, delimiter=',')
        for row in dict_reader:
            stop_id_to_node_id[int(row['stop_id'])] = int(row['node_id'])

    # Load route to stops mapping
    route_to_stops: Dict[str, List[int]] = {}
    with open(arguments.route, 'r') as in_file:
        dict_reader = csv.DictReader(in_file, delimiter=',')
        for row in dict_reader:
            route = row['route']
            stop_id = int(row['stop_id'])
            if stop_id in stop_id_to_node_id:  # Only consider stop IDs that exist in the stops file
                route_to_stops.setdefault(route, []).append(stop_id)

    # Map node IDs to list of routes
    node_id_to_routes: Dict[int, List[str]] = {}
    for route, stops in route_to_stops.items():
        for stop_id in stops:
            node_id = stop_id_to_node_id.get(stop_id)
            if node_id:
                if node_id not in node_id_to_routes:
                    node_id_to_routes[node_id] = []
                node_id_to_routes[node_id].append(route)

    # Write output CSV
    with open(arguments.output, 'w', newline='') as out_file:
        csv_writer = csv.writer(out_file, quoting=csv.QUOTE_ALL)
        csv_writer.writerow(['stop_id', 'node_id', 'routes'])
        for stop_id, node_id in stop_id_to_node_id.items():
            routes = node_id_to_routes.get(node_id, [])
            csv_writer.writerow([stop_id, node_id, str(sorted(routes))])

    return 0


if __name__ == '__main__':
    sys.exit(main(sys.argv))
