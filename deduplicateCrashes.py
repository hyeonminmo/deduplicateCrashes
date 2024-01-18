import os

LOGPATH = '/home/autofz/out'

UNIFUZZ = [
    'ar',
    'cflow',
    'cxxfilt',
    'exiv2',
    'ffmpeg',
    'flvmeta',
    'imginfo',
    'infotocap',
    'jhead',
    'jq',
    'lame',
    'mp3gain',
    'mp42aac',
    'mujs',
    'nm',
    'objdump',
    'pdftotext',
    'readelf',
    'size',
    'sqlite3',
    'strings',
    'tcpdump',
    'tiffsplit',
    'wav2swf'
    ]

FTS = [
    'boringssl-2016-02-12',
    'c-ares-CVE-2016-5180',
    'guetzli-2017-3-30',
    'harfbuzz-1.3.2',
    'json-2017-02-12',
    'lcms-2017-03-21',
    'libarchive-2017-01-04',
    'libjpeg-turbo-07-2017',
    'libpng-1.2.56',
    'libpng-1.2.56-structure-aware',
    'libssh-2017-1272',
    'libxml2-v2.9.2',
    'openssl-1.0.1f',
    'openssl-1.0.2d',
    'openssl-1.1.0c-bignum',
    'openssl-1.1.0c-x509',
    'openthread-2018-02-27-ip6',
    'openthread-2018-02-27-radio',
    'pcre2-10.00',
    'proj4-2017-08-14',
    're2-2014-12-09',
    'sqlite-2016-11-14',
    'vorbis-2017-12-11',
    'woff2-2016-05-06',
    'wpantund-2018-02-27',
    ]

def checkOutputDirectory(outputDirectoryPath):
    if os.path.exists(outputDirectoryPath) == False:
        os.mkdir(outputDirectoryPath)

## return True if logA and logB is equal.
def isDuplicate(logList, log):
    DUPLICATED = True
    UNDUPLICATED = False

    if len(logList) == 0:
        return UNDUPLICATED
    
    for logA in logList:
        if logA == log:
            return DUPLICATED        
    return UNDUPLICATED

## return ASAN logs from file path.
def getLogsFromFile(filePath):
    asanLogs = []
    with open(filePath, 'r') as log:
        for line in log:
            if '#' in line:
                asanLogs.append(line)
            elif line == '\n':
                break
    return asanLogs

def deduplicateCrashes(targetProgram):
    targetPath = os.path.join(LOGPATH, targetProgram)
    logList = [] # Log details
    uniqueBugs = [] # File name

    # get directory list in target program directory
    for trial in os.listdir(targetPath):

        trialPath = os.path.join(targetPath, trial)
        # read ASAN log files in trial* 
        for logFile in os.listdir(trialPath):
            logPath = os.path.join(trialPath, logFile)
            log = getLogsFromFile(logPath)
            # if the crash is unique crash
            if isDuplicate(logList=logList, log=log):
                uniqueBugs[logList.index(log)].append(logFile)
            else:
                tmp = []
                tmp.append(logFile)
                uniqueBugs.append(tmp)
                logList.append(log)

    print("========================")
    print(logList)
    # print(uniqueBugs)

def main():
    deduplicateCrashes('c-ares')
    print("DONE!")

if __name__ == "__main__":
    main()  
