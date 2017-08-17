
def read_config(key):
    prop_file = open(".env", 'r')
    # Read property "key" value from property file
    for line in prop_file:
        if key in line:
            keyval = line.rstrip().split("=")[1]
    prop_file.close()
    return keyval
