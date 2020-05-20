import os
import time

# If the path has a '\', use another '\'.
source = ["C:\\workspace\\pywork\\*", "C:\\intel\\Logs\\*"]
backupDir = "C:\\temp"
# If there are spaces in the path, use "before and after the path.
programDir = 'C:\\\"Program Files\"\\7-Zip\\'

# os.sep means "\\", thus creating "C:\\temp\\YearMonthDayHourMinuteSeconds.7z" on Windows.
backupFileName = backupDir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.7z'
#print(backupFileName)   # C:\temp\20190113214911.7z

# Create if backup path does not exist
if not os.path.exists(backupDir):
    os.mkdir(backupDir)

cmd7zip = programDir + "7z a {} {}".format(backupFileName, ' '.join(source))
print('7zip command :', cmd7zip)

if os.system(cmd7zip) != 0:
    print('Compression failed!')
else:
    print('Compression succeeded!')
