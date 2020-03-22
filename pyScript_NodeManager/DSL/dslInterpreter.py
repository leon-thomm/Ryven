# path: python dslInterpreter.py metaCodeText.txt



from textx import metamodel_from_str, get_children_of_type
import sys
import os
import pathlib


class Interpreter:
    def __init__(self, _dsl_code=None, dsl_code_filename=None):
        self.dsl_code = ''
        self.dir = str(pathlib.Path(__file__).parent.absolute())
        self.mm = self.load_meta_model()
        
        if not _dsl_code:
            dsl_code_filename = sys.argv[1]
            f = open(dsl_code_filename, 'r')
            self.dsl_code = f.read()
            f.close()
        else:
            self.dsl_code = _dsl_code
        
            
    def iterateThroughCommands(self, cmds):
        commands = []
        for cmd in cmds:
            if cmd.__class__.__name__ != 'Func_Condition':
                commands.append('s += ' + self.translateCommand(cmd))
            else:
                commands.append(self.translateCommand(cmd))
    
                commandsInBlock = self.iterateThroughCommands(cmd.commands)
                for command in commandsInBlock:
                    indent = '    '
                    commands.append(indent + command)
    
        return commands
    
    
    def translateCommand(self, cmd):
        #print(cmd)
        #print(cmd.__class__)
        #print(cmd.__class__.__name__)
    
        if cmd.__class__.__name__ == 'int' or \
                        cmd.__class__.__name__ == 'float':
            return str(cmd)
        elif cmd.__class__.__name__ == 'Operand_Function':
            return self.translateCommand(cmd.f)
        elif cmd.__class__.__name__ == 'str':
            return '\'' + cmd + '\''
        elif cmd.__class__.__name__ == 'Func_InsertInputData':
            return 'insertInputData({})'.format(cmd.index)
        elif cmd.__class__.__name__ == 'Func_InsertOutputData':
            return 'insertOutputData({})'.format(cmd.index)
        elif cmd.__class__.__name__ == 'Func_OutputConnected':
            return 'outputConnected({})'.format(cmd.index)
        elif cmd.__class__.__name__ == 'Func_InputConnected':
            return 'inputConnected({})'.format(cmd.index)
    
        # CONDITIONS
        elif cmd.__class__.__name__ == 'Func_Condition':
            s = 'if '
            # print('condition here!')
            # print(cmd.condition.__class__.__name__)
            if cmd.condition.__class__.__name__ == 'Cond_Equal':
                s += self.translateCommand(cmd.condition.op1) + ' == ' + self.translateCommand(cmd.condition.op2) + ':'
            elif cmd.condition.__class__.__name__ == 'Cond_NotEqual':
                s += self.translateCommand(cmd.condition.op1) + ' != ' + self.translateCommand(cmd.condition.op2) + ':'
            elif cmd.condition.__class__.__name__ == 'Cond_And':
                s += self.translateCommand(cmd.condition.op1) + ' and ' + self.translateCommand(cmd.condition.op2) + ':'
            elif cmd.condition.__class__.__name__ == 'Cond_Or':
                s += self.translateCommand(cmd.condition.op1) + ' or ' + self.translateCommand(cmd.condition.op2) + ':'
            elif cmd.condition.__class__.__name__ == 'Cond_True':
                s += self.translateCommand(cmd.condition.op1) + ':'
            elif cmd.condition.__class__.__name__ == 'Cond_False':
                s += '!' + self.translateCommand(cmd.condition.op1) + ':'
            else:
                s += self.translateCommand(cmd.condition) + ':'
    
            return s
    
        print('warning - returning error')
        return 'ERROR, NO FUNCTION I KNOW'
    
    
    
    def parse_dsl_code(self):
    
        model = self.mm.model_from_str(self.dsl_code)
    
        # MAGIC --- TRANSLATING ALL THE COMMANDS
        commands = self.iterateThroughCommands(model.commands)
    
        # STORING THE COMMANDS IN TEMP FILE
        if os.path.exists(self.dir+'/temp/commands.txt'):
            os.remove(self.dir+'/temp/commands.txt')
    
        f = open(self.dir+'/temp/commands.txt', 'w')
        for command in commands:
            f.write(command + '\n')
        f.close()
    
        s = ''
        for c in commands:
            s += c
            print(c)
        # print(s)
        return s
    
    
    def load_meta_model(self):
        # LOADING THE DSL GRAMMAR
        f = open(self.dir+'/grammar.txt', 'r')
        grammar = f.read()
        f.close()
    
        return metamodel_from_str(grammar)
        


if __name__ == '__main__':
    interpreter = Interpreter(dsl_code_filename=sys.argv[1])
    interpreter.parse_dsl_code()