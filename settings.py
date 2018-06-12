import pyqb

qbc = pyqb.Client(url="https://wesco.quickbase.com")  # parent url here
qbc.authenticate(username='', password='')  # put user and password here
db = 'bm7e4rizk?' #put a database here
url = 'https://wesco.quickbase.com/db/'  # parent url /db/
urldb = url + db
ticket = qbc.ticket