import inspect
import sys
import json
import os
import importlib


def get_nodes(package_file: str) -> list:
    nodes = []

    with open(package_file, 'r') as f:
        package = json.loads(f.read())

        sys.path.append(os.path.dirname(package_file))
        if 'nodes' in sys.modules.keys():
            del sys.modules['nodes']
        mod = __import__('nodes')
        sys.path.remove(os.path.dirname(package_file))

        for node_name in package['nodes']:
            nodes.append(mod.__dict__[node_name])
    
    return nodes


def parse_module(mod_name, color, target_path):
    module = __import__(mod_name)

    routines = []
    
    for name, obj in inspect.getmembers(module):
        if inspect.isroutine(obj):
            routines.append((name, obj))
    # print(routines)
    node_defs = []
    
    node_names = []
    
    for name, obj in routines:
        try:
            sig = inspect.getfullargspec(obj)
        except Exception as e:
            # print(e)
            continue

        # print(f'routine {name} of {mod_name}: {sig}')
        
        inputs = '\n'.join([f'rc.NodeInputBP(label=\'{param_name}\'),' for param_name in sig.args])
        node_name = f'AutoNode_{mod_name}_{name}'
        node_names.append(node_name)
        doc = obj.__doc__.replace('\0', '<NULL>') if obj.__doc__ else ''

        node_def = f'''
class {node_name}(rc.Node):
    title = \'{name}\'
    type_ = \'{mod_name}\'
    doc = \'\'\'{doc}\'\'\'
    init_inputs = [
        {inputs}
    ]
    init_outputs = [
        rc.NodeOutputBP(type_='data'),
    ]
    color = \'{color}\'

    def update_event(self, input_called=-1):
        self.set_output_val(0, {mod_name}.{name}({ ', '.join([f'self.input({i})' for i in range(len(sig.args))]) }))
        '''

        node_defs.append(node_def)
    
    if not os.path.exists(target_path):
        os.mkdir(target_path)

    with open(target_path+'/nodes.py', 'w') as f:
        f.write('''import ryvencore_qt as rc
import '''+mod_name+'''

'''+'\n\n'.join(node_defs))

    package = {
        'type': 'Ryven auto generated nodes package',
        'nodes': node_names
    }
    
    package_file = target_path+'/'+mod_name+'.rpc'
    with open(package_file, 'w') as f:
        f.write(json.dumps(package, indent=4))
    
    # print(get_nodes(package_file))

if __name__ == '__main__':
    
    if len(sys.argv) > 1:
        mod_name = sys.argv[1]
        color = sys.argv[2]
        target_path = sys.argv[3] if len(sys.argv) > 3 else mod_name
        parse_module(mod_name, color, target_path)
    else:
        for m in sys.builtin_module_names:
            parse_module(m, '#32DA22', m)




'''
{
"drawings": [],
"nodes": [
    {
        "identifier": "AutoNode_math_acos",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 566.6316582531836,
        "pos y": 136.52993904350672
    },
    {
        "identifier": "AutoNode_math_acosh",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 570.4269605775792,
        "pos y": 201.57394901455564
    },
    {
        "identifier": "AutoNode_math_asin",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 569.888422861678,
        "pos y": 273.8577746728047
    },
    {
        "identifier": "AutoNode_math_asinh",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 566.854889062786,
        "pos y": 341.48424711129314
    },
    {
        "identifier": "AutoNode_math_atan",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 563.2531819936285,
        "pos y": 408.67287515656733
    },
    {
        "identifier": "AutoNode_math_atan2",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "y",
                "has widget": false
            },
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 563.5206057422515,
        "pos y": 486.051898427791
    },
    {
        "identifier": "AutoNode_math_atanh",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 565.4948031718857,
        "pos y": 561.977933875563
    },
    {
        "identifier": "AutoNode_math_ceil",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 1040.212425265817,
        "pos y": 167.91600436701367
    },
    {
        "identifier": "AutoNode_math_comb",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "n",
                "has widget": false
            },
            {
                "type": "data",
                "label": "k",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 1055.0179217742036,
        "pos y": 240.71304470865186
    },
    {
        "identifier": "AutoNode_math_copysign",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            },
            {
                "type": "data",
                "label": "y",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 1483.5755567182598,
        "pos y": 204.24121555323597
    },
    {
        "identifier": "AutoNode_math_cos",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 1047.757686565991,
        "pos y": 314.45550115862295
    },
    {
        "identifier": "AutoNode_math_cosh",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 1467.3737554821967,
        "pos y": 277.98367200320683
    },
    {
        "identifier": "AutoNode_math_degrees",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 1071.6961829327659,
        "pos y": 391.0342059335927
    },
    {
        "identifier": "AutoNode_math_dist",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "p",
                "has widget": false
            },
            {
                "type": "data",
                "label": "q",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 1463.895184707316,
        "pos y": 353.6169606698437
    },
    {
        "identifier": "AutoNode_math_erf",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 1048.363873882893,
        "pos y": 460.0495818418989
    },
    {
        "identifier": "AutoNode_math_erfc",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 1468.4548058592761,
        "pos y": 435.7463460848618
    },
    {
        "identifier": "AutoNode_math_exp",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 1050.8874957600617,
        "pos y": 529.9293606000932
    },
    {
        "identifier": "AutoNode_math_factorial",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 1492.912187261057,
        "pos y": 503.5083715981324
    },
    {
        "identifier": "Val_Node",
        "state data": "gASVEwAAAAAAAAB9lIwDdmFslEc/5mZmZmZmZnMu",
        "special actions": {
            "edit val via dialog": {
                "method": "action_edit_via_dialog"
            }
        },
        "inputs": [],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 401.3605296937426,
        "pos y": 316.56858678590515,
        "main widget data": "gASVEQAAAAAAAAB9lIwEdGV4dJSMAzAuN5RzLg=="
    },
    {
        "identifier": "Result_Node",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "",
                "has widget": false
            }
        ],
        "outputs": [],
        "pos x": 715.4623467893973,
        "pos y": 140.12398250941146,
        "main widget data": "gAR9lC4="
    },
    {
        "identifier": "Result_Node",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "",
                "has widget": false
            }
        ],
        "outputs": [],
        "pos x": 723.0677176633842,
        "pos y": 204.0090978509005,
        "main widget data": "gAR9lC4="
    },
    {
        "identifier": "Result_Node",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "",
                "has widget": false
            }
        ],
        "outputs": [],
        "pos x": 723.0677176633842,
        "pos y": 272.4574357167818,
        "main widget data": "gAR9lC4="
    },
    {
        "identifier": "Result_Node",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "",
                "has widget": false
            }
        ],
        "outputs": [],
        "pos x": 722.3071805759853,
        "pos y": 342.4268477574602,
        "main widget data": "gAR9lC4="
    },
    {
        "identifier": "Result_Node",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "",
                "has widget": false
            }
        ],
        "outputs": [],
        "pos x": 723.8282547507829,
        "pos y": 409.35411144854413,
        "main widget data": "gAR9lC4="
    },
    {
        "identifier": "Result_Node",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "",
                "has widget": false
            }
        ],
        "outputs": [],
        "pos x": 726.8704031003774,
        "pos y": 489.2105056254055,
        "main widget data": "gAR9lC4="
    },
    {
        "identifier": "Result_Node",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "",
                "has widget": false
            }
        ],
        "outputs": [],
        "pos x": 727.6309401877761,
        "pos y": 560.7009918408813,
        "main widget data": "gAR9lC4="
    },
    {
        "identifier": "Result_Node",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "",
                "has widget": false
            }
        ],
        "outputs": [],
        "pos x": 1272.1754947652314,
        "pos y": 529.899239801235,
        "main widget data": "gAR9lC4="
    },
    {
        "identifier": "Result_Node",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "",
                "has widget": false
            }
        ],
        "outputs": [],
        "pos x": 1268.3728093282377,
        "pos y": 313.1461698926113,
        "main widget data": "gAR9lC4="
    },
    {
        "identifier": "Result_Node",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "",
                "has widget": false
            }
        ],
        "outputs": [],
        "pos x": 1269.1333464156367,
        "pos y": 450.0428456243736,
        "main widget data": "gAR9lC4="
    },
    {
        "identifier": "Result_Node",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "",
                "has widget": false
            }
        ],
        "outputs": [],
        "pos x": 1268.3728093282377,
        "pos y": 244.69783202673,
        "main widget data": "gAR9lC4="
    },
    {
        "identifier": "Result_Node",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "",
                "has widget": false
            }
        ],
        "outputs": [],
        "pos x": 1267.6122722408393,
        "pos y": 383.1155819332897,
        "main widget data": "gAR9lC4="
    },
    {
        "identifier": "Result_Node",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "",
                "has widget": false
            }
        ],
        "outputs": [],
        "pos x": 1260.7674384542513,
        "pos y": 180.81271668524084,
        "main widget data": "gAR9lC4="
    },
    {
        "identifier": "Val_Node",
        "state data": "gASVEwAAAAAAAAB9lIwDdmFslEc/5mZmZmZmZnMu",
        "special actions": {
            "edit val via dialog": {
                "method": "action_edit_via_dialog"
            }
        },
        "inputs": [],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 909.3993040760608,
        "pos y": 328.73718018428406,
        "main widget data": "gASVEQAAAAAAAAB9lIwEdGV4dJSMAzAuN5RzLg=="
    },
    {
        "identifier": "AutoNode_math_floor",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 360.49457942697427,
        "pos y": 663.1883402116489
    },
    {
        "identifier": "AutoNode_math_fmod",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            },
            {
                "type": "data",
                "label": "y",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 510.3203856445142,
        "pos y": 663.1883402116489
    },
    {
        "identifier": "AutoNode_math_frexp",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 660.1461918620541,
        "pos y": 663.1883402116489
    },
    {
        "identifier": "AutoNode_math_fsum",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "seq",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 809.9719980795941,
        "pos y": 663.1883402116489
    },
    {
        "identifier": "AutoNode_math_gamma",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 959.0372672097353,
        "pos y": 663.1883402116489
    },
    {
        "identifier": "AutoNode_math_gcd",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            },
            {
                "type": "data",
                "label": "y",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 1108.8630734272751,
        "pos y": 663.1883402116489
    },
    {
        "identifier": "AutoNode_math_isclose",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "a",
                "has widget": false
            },
            {
                "type": "data",
                "label": "b",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 1257.9283425574165,
        "pos y": 663.1883402116489
    },
    {
        "identifier": "AutoNode_math_isfinite",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 1406.9936116875579,
        "pos y": 663.1883402116489
    },
    {
        "identifier": "AutoNode_math_isinf",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 1556.058880817699,
        "pos y": 663.1883402116489
    },
    {
        "identifier": "AutoNode_math_isnan",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 1705.884687035239,
        "pos y": 663.1883402116489
    },
    {
        "identifier": "AutoNode_math_isqrt",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "n",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 466.18785271763136,
        "pos y": 757.5943508216927
    },
    {
        "identifier": "AutoNode_math_ldexp",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            },
            {
                "type": "data",
                "label": "i",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 615.2531218477725,
        "pos y": 757.5943508216927
    },
    {
        "identifier": "AutoNode_math_lgamma",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 765.0789280653125,
        "pos y": 757.5943508216927
    },
    {
        "identifier": "AutoNode_math_log10",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 914.1441971954537,
        "pos y": 757.5943508216927
    },
    {
        "identifier": "AutoNode_math_log1p",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 1063.2094663255948,
        "pos y": 757.5943508216927
    },
    {
        "identifier": "AutoNode_math_log2",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 1212.274735455736,
        "pos y": 757.5943508216927
    },
    {
        "identifier": "AutoNode_math_modf",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 1362.100541673276,
        "pos y": 757.5943508216927
    },
    {
        "identifier": "AutoNode_math_perm",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "n",
                "has widget": false
            },
            {
                "type": "data",
                "label": "k",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 1511.1658108034171,
        "pos y": 757.5943508216927
    },
    {
        "identifier": "AutoNode_math_pow",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            },
            {
                "type": "data",
                "label": "y",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 340.5619173164971,
        "pos y": 856.3048264031909
    },
    {
        "identifier": "AutoNode_math_prod",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "iterable",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 489.62718644663914,
        "pos y": 856.3048264031909
    },
    {
        "identifier": "AutoNode_math_radians",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 638.6924555767794,
        "pos y": 856.3048264031909
    },
    {
        "identifier": "AutoNode_math_remainder",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            },
            {
                "type": "data",
                "label": "y",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 810.8775800966991,
        "pos y": 858.7891951034553
    },
    {
        "identifier": "AutoNode_math_sin",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 959.9428492268394,
        "pos y": 858.7891951034553
    },
    {
        "identifier": "AutoNode_math_sinh",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 1109.0081183569814,
        "pos y": 858.7891951034553
    },
    {
        "identifier": "AutoNode_math_sqrt",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 1258.8339245745206,
        "pos y": 858.7891951034553
    },
    {
        "identifier": "AutoNode_math_tan",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 1407.8991937046628,
        "pos y": 858.7891951034553
    },
    {
        "identifier": "AutoNode_math_tanh",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 1556.9644628348049,
        "pos y": 858.7891951034553
    },
    {
        "identifier": "AutoNode_math_trunc",
        "state data": "gAR9lC4=",
        "special actions": {},
        "inputs": [
            {
                "type": "data",
                "label": "x",
                "has widget": false
            }
        ],
        "outputs": [
            {
                "type": "data",
                "label": ""
            }
        ],
        "pos x": 1706.029731964945,
        "pos y": 858.7891951034553
    }
],
"connections": [
    {
        "parent node index": 0,
        "output port index": 0,
        "connected node": 19,
        "connected input port index": 0
    },
    {
        "parent node index": 1,
        "output port index": 0,
        "connected node": 20,
        "connected input port index": 0
    },
    {
        "parent node index": 2,
        "output port index": 0,
        "connected node": 21,
        "connected input port index": 0
    },
    {
        "parent node index": 3,
        "output port index": 0,
        "connected node": 22,
        "connected input port index": 0
    },
    {
        "parent node index": 4,
        "output port index": 0,
        "connected node": 23,
        "connected input port index": 0
    },
    {
        "parent node index": 5,
        "output port index": 0,
        "connected node": 24,
        "connected input port index": 0
    },
    {
        "parent node index": 6,
        "output port index": 0,
        "connected node": 25,
        "connected input port index": 0
    },
    {
        "parent node index": 7,
        "output port index": 0,
        "connected node": 31,
        "connected input port index": 0
    },
    {
        "parent node index": 8,
        "output port index": 0,
        "connected node": 29,
        "connected input port index": 0
    },
    {
        "parent node index": 10,
        "output port index": 0,
        "connected node": 27,
        "connected input port index": 0
    },
    {
        "parent node index": 12,
        "output port index": 0,
        "connected node": 30,
        "connected input port index": 0
    },
    {
        "parent node index": 14,
        "output port index": 0,
        "connected node": 28,
        "connected input port index": 0
    },
    {
        "parent node index": 16,
        "output port index": 0,
        "connected node": 26,
        "connected input port index": 0
    },
    {
        "parent node index": 18,
        "output port index": 0,
        "connected node": 0,
        "connected input port index": 0
    },
    {
        "parent node index": 18,
        "output port index": 0,
        "connected node": 1,
        "connected input port index": 0
    },
    {
        "parent node index": 18,
        "output port index": 0,
        "connected node": 2,
        "connected input port index": 0
    },
    {
        "parent node index": 18,
        "output port index": 0,
        "connected node": 3,
        "connected input port index": 0
    },
    {
        "parent node index": 18,
        "output port index": 0,
        "connected node": 4,
        "connected input port index": 0
    },
    {
        "parent node index": 18,
        "output port index": 0,
        "connected node": 5,
        "connected input port index": 0
    },
    {
        "parent node index": 18,
        "output port index": 0,
        "connected node": 6,
        "connected input port index": 0
    },
    {
        "parent node index": 18,
        "output port index": 0,
        "connected node": 5,
        "connected input port index": 1
    },
    {
        "parent node index": 32,
        "output port index": 0,
        "connected node": 7,
        "connected input port index": 0
    },
    {
        "parent node index": 32,
        "output port index": 0,
        "connected node": 8,
        "connected input port index": 0
    },
    {
        "parent node index": 32,
        "output port index": 0,
        "connected node": 8,
        "connected input port index": 1
    },
    {
        "parent node index": 32,
        "output port index": 0,
        "connected node": 10,
        "connected input port index": 0
    },
    {
        "parent node index": 32,
        "output port index": 0,
        "connected node": 12,
        "connected input port index": 0
    },
    {
        "parent node index": 32,
        "output port index": 0,
        "connected node": 14,
        "connected input port index": 0
    },
    {
        "parent node index": 32,
        "output port index": 0,
        "connected node": 16,
        "connected input port index": 0
    }
]
}'''