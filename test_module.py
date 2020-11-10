from datetime import datetime

from trans import tools as trans_tools
from work import tools as work_tools


def test_trans_tool():
    id1=trans_tools.gen_trans_id()
    print(id1)
    date=datetime(2015, 10, 2, 12, 30, 45)
    id2=trans_tools.gen_trans_id(date)
    print(id2)

def test_work_tool():
    file_name='C:\\Users\\GGKG\\Desktop\\jmeter.png'
    rest=work_tools.get_file_type(file_name)
    print(rest)

if __name__=='__main__':
    test_trans_tool()
    test_work_tool()

