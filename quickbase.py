import pyqb
import requests, pprint, base64, os
from settings import urldb, ticket


blankxml = """<qdbapi>
<udata>mydata</udata>
<ticket>{ticket}</ticket>
<apptoken>app_token</apptoken>
<rid>{file.rid}</rid>
<field fid="94" filename="{file.filename}">{file.data}</field>
</qdbapi>"""


blankxml2 = """<qdbapi>
<ticket>{ticket}</ticket>
<udata>mydata</udata>
<apptoken>app_token</apptoken>
<query>{file.query}</query>
<includeRids>1</includeRids>
<clist>3</clist>
<fmt>structured</fmt>
</qdbapi>"""


# for uploadfiles the list should be a list of file64 objects from filesto64

def uploadfiles(list):


    header = {
        "Content-Type": "application/xml",
        "QUICKBASE-ACTION": "API_" + "EditRecord"
    }

    for item in list:
        xml = blankxml.format(file=item, ticket=ticket)
        xml = xml.replace("'", "")
        #print(xml)
        res = requests.post(url=urldb, data=xml, headers=header)
        print('SNF for part {part} uploaded'.format(part=item.title))
        print(res)


def find_record_id(file):


    header = {
        "Content-Type": "application/xml",
        "QUICKBASE-ACTION": "API_" + "DoQuery"
    }

    xml = blankxml2.format(file=file, ticket=ticket)
    res = requests.post(url=urldb, data=xml, headers=header)
    response = res.content.decode('utf-8')
    response = str(response)
    rid = response.split('<f id="3">')[1].split("</f>")[0]
    print('Record ID matched to SNF')
    return rid


class file64():
    def __init__(self, data=None, filename=None, title=None, rid=None):
        self.data = data
        self.filename = filename
        self.title = title
        self.rid = rid
        self.query = ''


def files64(directory):

    os.chdir(directory)
    files = [f for f in os.listdir(directory) if os.path.isfile(f)]
    print(files)
    files64list = []
    for i in range(len(files)):
        dic = {'title': '', 'filename': '', 'data':''}
        f64 = file64()
        with open(files[i], "rb") as imageFile:
            rawpic64 = base64.b64encode(imageFile.read())
        pic64 = rawpic64.decode('UTF-8')
        pic64 = pic64 + '='
        f64.data = pic64
        f64.title = str(files[i].split('_')[0])
        f64.query = "{'6'.CT." + f64.title + "}"
        f64.filename = str(files[i])
        f64.rid = find_record_id(f64)

        files64list.append(f64)
    return files64list