from quickbase import uploadfiles, find_record_id, files64


encodedfiles = files64(r'C:\Users\RFiedler\PycharmProjects\quickbase\ApprovedSNFs')
print(encodedfiles[4].rid)
uploadfiles(encodedfiles)
