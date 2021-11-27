# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import firebase_admin
from firebase_admin import auth
from firebase_admin import credentials
from firebase_admin import db
import uuid
import random

cred = credentials.Certificate(
    "/home/raga/Documents/Adiuvo/FirebaseBackups/dev/adiuvodev-firebase-adminsdk-mv8qr-a94fd89211.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://adiuvodev.firebaseio.com/'
})




def createUser():
    username = ""
    for x in range(0, 10):
        locStr = random.randint(0, 9)
        username += str(locStr)
    user = auth.create_user(email=username + '@adiuvodiagnostics.com', password='secretPassword')
    print('Sucessfully created new user: {0}'.format(user.uid))
    return user.uid


def populateDb(userId):
    print("uuid\t",uuid.uuid4().hex)
    ref = db.reference(userId)
    ref.set({
    "aboutDevice" : {
      "appVersion" : "11.6.6 Pro",
      "chassisVersion" : "na",
      "firmwareId" : "na",
      "hardwareVersion" : "na",
      "mlVersion" : "MLMain20210529_ILLUMINATEV2_CLAHE, MLMain20200801_FUNGUS_FEATUREEXTRACTION",
      "serialNumber" : "na",
      "simNumber" : "na"
    },
    "dynamicUserConfiguration" : {
      "idPrefix" : "ADDEMO4_",
      "userName" : "Field Test device"
    },
    "generalUserAnalytics" : {
      "logEvents" : {
        "2021-11-26--11-27-35" : "totalSessionStartCountIncremented"
      },
      "progressiveReportDownloadCount" : 0,
      "progressiveReportShareCount" : 0,
      "progressiveReportViewCount" : 1,
      "reportDownloadCount" : 11,
      "reportNotesSavedCount" : 0,
      "reportSearchCount" : 0,
      "reportShareCount" : 1,
      "reportViewCount" : 27,
      "totalPatientCount" : 3,
      "totalSessionStartCount" : 26,
      "totalVisitCount" : 7
    },
    "serviceThrottling" : {
      "imagingLimit" : 500,
      "isCloudImageBackupEnabled" : 1,
      "isEventLogEnabled" : 0,
      "isFungusImagingEnabled" : 0,
      "isUserEligibleForImaging" : 1
    }
    })
    print(userId)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    # for x in range(0, 10):
    populateDb(createUser())

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
