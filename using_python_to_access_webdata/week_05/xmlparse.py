import xml.etree.ElementTree as ET

data = '''
<person>
    <name>Chuck</name>
    <phone type="intl">
        +1 234 567 890
    </phone>
    <email hide ="yes"/>
</person>
'''

tree = ET.fromstring(data)
print('Name:', tree.find('name').text)
print('Attr:', tree.find('email').get('hide'))
print('Phone:', (tree.find('phone').text).strip())
print('Phone type:', tree.find('phone').get('type'))
