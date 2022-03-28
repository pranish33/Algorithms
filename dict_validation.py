'''Python Program to check the validation of dict'''

def check_structure(conf_struct, conf):
    if isinstance(conf_struct, dict) and isinstance(conf, dict):
        # conf_struct is a dict of types or other dicts
        return all(k in conf and check_structure(conf_struct[k], conf[k]) for k in conf_struct)
    
    elif isinstance(conf_struct, type):
        # conf_struct is the type of conf
        return isinstance(conf, conf_struct)
        
    else:
        # conf_struct is neither a dict, nor list, not type
        return False
    
    
# test Data for dict validation 
my_conf = {
    'version': 1,

    'info': {
        'my_conf_one': 5.5,
        'my_conf_two': 'Pranish',
        'my_conf_three': False,
        'programming_conf': 'Python'
    }
}
conf_structure = {
    'version': int,

    'info': {
        'my_conf_one': float,
        'my_conf_two': str,
        'my_conf_three': bool,
        'programming_conf': str
    }
}

print(check_structure(conf_structure, my_conf))
