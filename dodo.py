def task_hello():
    """hello"""

    def python_hello(targets):
        with open(targets[0], "a") as output:
            output.write("Python says Hello World!!!\n")

    return {
        'actions': [python_hello],
        'targets': ["hello.txt"],
        }


def task_instaladep():
    """Instala dependencias"""

    return {'actions': ["pip3 install pyflakes"],
            'verbosity': 2}


def task_hello2():
    """hello cmd """
    msg = 3 * "hi! "
    return {
        'actions': ['echo %s ' % msg],
        }

def task_aver():
    """say hello"""
    return {'actions': ["ls -l"],
            'verbosity': 2}

def task_checker():
    return {'actions': ["pyflakes src/pregunta.py"],
            'file_dep': ["src/pregunta.py"],
            'actions': ["ls -l"],
            


            'verbosity': 2}

def task_prueba():
    return {
        'actions': [['python', 'puts', 'hola']]
        }

def show_cmd(task):
    return "executing... %s" % task.name

def task_custom_display():
    return {'actions':['echo abc efg'],
            'title': show_cmd}

def comprueba_sintaxis():
    yield {'basename': 'sintaxis_pregunta',
           'actions': ["pyflakes src/pregunta.py"],
           'file_dep': ["src/pregunta.py"]}

    yield {'basename': 'sintaxis_respuesta',
           'actions': ["pyflakes src/respuesta.py"],
           'file_dep': ["src/respuesta.py"]}

    yield {'basename': 'sintaxis_to_csv',
           'actions': ["pyflakes src/to_csv.py"],
           'file_dep': ["src/to_csv.py"]}

    yield {'basename': 'sintaxis_usuario',
           'actions': ["pyflakes src/usuario.py"],
           'file_dep': ["src/usuario.py"]}

def task_checkerr():
    return {'actions':[comprueba_sintaxis],
            'verbosity': 2}
