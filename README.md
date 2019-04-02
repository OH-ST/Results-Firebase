# OpenTestRig-Results-Firebase
Pushes Test Report to Firebase


## Usage
```rfb = resultsFirebase()
        
rfb.pushResults("System", "verification",pytest.deviceId)
```

This pushes the `report.html` file in the root of the test project to a Firebase Storage Bucket `System/verification/"deviceID"`


**todo**
--Push linked to storage into DB
--Save actual results as well as PASS/FAIL

