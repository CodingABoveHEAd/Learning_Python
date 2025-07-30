class pycharm:
    def execute(self):
        print('compiling');
        print('executing');
        print('from pycharm');

class numpy:
    def execute(self):
        print('compiling');
        print('running');
        print('executing');
        print('from numpy');


class laptop:
    def code(self,ide):
        ide.execute()

lap1=pycharm();
lap2=numpy();

machine=laptop();

machine.code(lap2);

