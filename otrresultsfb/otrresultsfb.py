import firebase_admin
from firebase_admin import credentials
from firebase_admin import db
from firebase_admin import storage




class resultsFirebase():
	def __init__(self):
		cred = credentials.Certificate('C:/Relectrify/OpenTestRig-Results-Firebase/auth/serviceAccountKey.json')
		self.fbapp = firebase_admin.initialize_app(cred,{
		    'databaseURL' : 'https://relectrify-testing-results.firebaseio.com',
		    'storageBucket': 'relectrify-testing-results.appspot.com'
		})
		self.db = db.reference()
		self.bucket = storage.bucket()
		

	def pushResults(self, testType, testLevel,DUTId):
		source_file_name =DUTId
		blob=self.bucket.blob(testType+"/"+testLevel+"/"+source_file_name)
		res = blob.upload_from_filename("report.html")
		print(res)
		print(f'File {source_file_name} uploaded to {testType}/{testLevel}/{source_file_name}.')

		self.db.child(testType+"/"+testLevel+"/"+DUTId).push({"reportURL":res})

	    
# System/PCB
# Verification/Production
