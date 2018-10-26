from lxml import objectify
import pandas as pd
from distutils import util

def str_to_bool(to_convert):
    """
    Takes a string-type boolean value and converts it to a full boolean value.
    e.g. 'True' --> True
    """
    assert(to_convert == "True" or "False")
    if to_convert == "True":
        return True
    elif to_convert == "False":
        return False

xml = objectify.parse(open('XMLData.xml'))
root = xml.getroot()
print(root)
df = pd.DataFrame(columns=('Number', 'Boolean'))

for i in range(0,4):
    obj = root.getchildren()[i].getchildren()
    print("Object from {} is {}".format(i, str_to_bool(obj[2].text)))
    row = dict(zip(
        ['Number', 'Boolean'],
        [obj[0].pyval,
        bool(util.strtobool(obj[2].text))]))
    row_s = pd.Series(row)
    row_s.name = obj[1].text
    df = df.append(row_s)

print(type(df.ix['First']['Number']))
print(type(df.ix['First']['Boolean']))
