from model import Model


def parse_requests(file, model):
    while ((line := file.readline().rstrip('\n')) != 'FIN DEMANDAS'):
        model.requests.append(int(line.split(" ")[1]))


def parse_cords(file, model):
    while ((line := file.readline().rstrip('\n')) != 'EOF'):
        parsed_line = line.split(" ")
        model.nodes.append((float(parsed_line[1]), float(parsed_line[2])))


def parse_file(file_name):
    model = Model()
    with open(file_name, 'r') as f:
        while ((line := f.readline().rstrip('\n')) != 'EOF'):
            #print('LINEA', line)
            parsed_line = line.split(" ")
            cmd = parsed_line[0]
            if (cmd == 'CAPACIDAD:'):
                model.capacity = int(parsed_line[1])
            elif (cmd == 'DIMENSION:'):
                model.dimension = int(parsed_line[1])
            elif (cmd == 'DEMANDAS'):
                parse_requests(f, model)
            elif (cmd == 'EDGE_WEIGHT_TYPE:'):
                model.distance_type = parsed_line[1]
            elif (cmd == 'NODE_COORD_SECTION'):
                parse_cords(f, model)
                return model
