

def combine_data(statista_data, worldometers_data):
    main_dict = dict()
    keys = set()
    keys.update(statista_data.keys())
    keys.update(worldometers_data.keys())

    for key in keys:
        statista_value = statista_data.get(key)
        worldometers_value = worldometers_data.get(key)
        if worldometers_value is None:
            main_dict[key] = [statista_value[0], statista_value[1], statista_value[2], statista_value[3], statista_value[4], statista_value[5], 'no data', 'no data']
        elif statista_value is None:
            main_dict[key] = [int(worldometers_value[1]), 'no data', 'no data', 'no data', 'no data', 'no data', worldometers_value[0], worldometers_value[2]]
        else:
            main_dict[key] = [round((int(statista_value[0]) + int(worldometers_value[1])) / 2), statista_value[1], statista_value[2], statista_value[3], statista_value[4], statista_value[5], worldometers_value[0], worldometers_value[2]]

    data = []
    for key in main_dict:
        value = main_dict.get(key)
        data.append((
            key,
            value[0],
            value[1],
            value[2],
            value[3],
            value[4],
            value[5],
            value[6],
            value[7]
        ))
    return data
