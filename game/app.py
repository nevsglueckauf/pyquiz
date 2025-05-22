# App and runners for environment (cli, gui, web)
# AUTHOR: Sven Schrodt<sven.schrodt@schrodt.club
# SINCE: 2025-05-16
from game.entity import Question

class Runner:
    
    def __init__(self):
        pass
    
    
class CliRunner(Runner):
    def __init__(self):
        pass
    
    def render(self, question:Question):
        """ Rendering question for CLI
        FIXME: make it look nicer
        Args:
            question (Question): _description_
        """
        print('Cat:', question.category, '[Diff: ' + question.difficulty + ']')
        print('Question:', question.question)
        for idx, x in enumerate(question.answers):
            print(idx+1, x)
        
        
class App:
    mode:str = 'cli'
    runner:Runner
    
    def __init__(self):
        if self.mode=='cli':
            self.runner = CliRunner()
    