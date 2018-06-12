import pyqb

qbc = pyqb.Client(url="https://wesco.quickbase.com")
qbc.authenticate(username='rfiedler@wesco.com', password='510rf327')
db = 'bm7e4rizk?'
url = 'https://wesco.quickbase.com/db/'
urldb = url + db
ticket = qbc.ticket