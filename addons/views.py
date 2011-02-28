class Manifest(object):
    """Extracts and contains information from a java manifest file (manifest.mf)"""
    
    def __init__(self, path):
        self.path = path
        self.data = {}
        for line in self._normalize_data():
            entry = line.split(':')
            key = entry[0].strip()
            value = None
            if len(entry) > 2:
                value = ':'.join(entry[1:]).strip()
            elif len(entry) == 2:
                value = entry[1].strip()
            self.data[key] = value
    
    def _normalize_data(self):
        lines = []
        f = open(os.path.join(self.path, 'META-INF', 'MANIFEST.MF'))
        for line in f.readlines():
            line = line.rstrip()
            if line:
                if line.startswith(' '):
                    lines[-1] += line[1:]
                else:
                    lines.append(line)
        f.close()
        return lines
    
    def find(self, name):
        return self.data.get(key)

        
class Extractor(object):
    """Extract add-on info from a manifest file in a jar."""
    
    def __init__(self, path):
        self.path = path
        self.manifest = manifest = Manifest(path)
        self.data = {
            'id': manifest.find("Bundle-SymbolicName"),
            'name': manifest.find("Bundle-Name"),
            'version': manifest.find("Bundle-Version"),
        }
        
    @classmethod
    def parse(cls, path):
        return cls(path).data
    

def parse_jar(jar_file):
    """Extract and parse a JAR file."""
    path = tempfile.mkdtemp()
    zip = zipfile.ZipFile(jar_file)
    for f in zip.namelist():
        if '..' in f or f.startswith('/'):
            raise Exception("Invalid archive.")
    zip.extractall(path)
    data = Extractor.parse(path)
    return data