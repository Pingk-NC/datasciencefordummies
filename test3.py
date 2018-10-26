from lxml import objectify
import pandas as pd

xml = objectify.parse(open("XMLData2.xml"))
root = xml.getroot()
data_frame = pd.DataFrame(columns=("Number", "String", "Boolean"))

for i in range(0, 4):
    object = root.getchildren()[i].getchildren()
    row = dict(zip(["Number", "String", "Boolean"], [object[0].text, object[1].text, object[2].text]))
    row_s = pd.Series(row)
    row_s.name = i
    data_frame = data_frame.append(row_s)

print(data_frame.drop_duplicates())
