def parse_manifest_file(path):
    f = open(path)
    lines = []
    for line in f.readlines():
        line = line.rstrip()
        if line:
            if line.startswith(' '):
                lines[-1] += line[1:]
            else:
                lines.append(line)
    f.close()
    data = {}
    for line in lines:
        entry = line.split(':')
        key = entry[0].strip()
        value = None
        if len(entry) > 2:
            value = ':'.join(entry[1:]).strip()
        elif len(entry) == 2:
            value = entry[1].strip()
        data[key] = value
    return data
