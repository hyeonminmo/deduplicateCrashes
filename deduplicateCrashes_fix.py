import os
import shutil

LOGPATH = '/home/autofz/out'
SHELLPATH = '/home/autofz/deduplicateCrashes'

UNIFUZZ = [
    #'ar',
    #'cflow',
    #'cxxfilt',
    'exiv2',
    #'ffmpeg',
    #'flvmeta',
    'imginfo',
    'infotocap',
    'jhead',
    #'jq',
    'lame',
    'mp3gain',
    #'mp42aac',
    #'mujs',
    'nm',
    #'objdump',
    #'pdftotext',
    #'readelf',
    #'size',
    #'sqlite3',
    #'strings',
    #'tcpdump',
    'tiffsplit',
    #'wav2swf'
    ]

FTS = [
    'boringssl-2016-02-12',#
    # 'c-ares-CVE-2016-5180',
    #'c-ares',#
    'guetzli-2017-3-30',#
    #'harfbuzz-1.3.2',#
    #'json-2017-02-12',#
    'lcms-2017-03-21',#
    #'libarchive-2017-01-04',#
    #'libjpeg-turbo-07-2017',#
    'libjpeg-turbo',
    #'libpng-1.2.56',#
    # 'libpng-1.2.56-structure-aware',
    #'libssh-2017-1272',#
    #'libxml2-v2.9.2',
    'libxml2',
    #'openssl-1.0.1f',#
    # 'openssl-1.0.2d',
    # 'openssl-1.1.0c-bignum',
    #'openssl-1.1.0c-x509',#
    #'openthread-2018-02-27-ip6',#
    #'openthread-2018-02-27-radio',#
    #'pcre2-10.00',#
    #'proj4-2017-08-14',#
    #'re2-2014-12-09',#
    #'sqlite-2016-11-14',#
    #'vorbis-2017-12-11',#
    'woff2-2016-05-06',#
    #'wpantund-2018-02-27',#
    'wpantund',
    ]

totalUniqueBugs = []

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

## make text file with input contents
def makeTextFile(fileName: str, contents: list, filePath: str):
    file = open(os.path.join(filePath, fileName), 'w')
    for content in contents:
        file.write(content + '\n')
    file.close()

def getSampleCrashFile(filePath, targetProgram):
    with open(os.path.join(filePath, 'duplicatedFiles.txt'), 'r') as file:
        for line in file:
            sampleFile = line.split('.')
            print(filePath)
            with open(os.path.join(SHELLPATH, targetProgram+'.sh'), 'r') as shell:
                for script in shell:
                    if sampleFile[0] in script:
                        command = script.split(' ')
                        for input in command:
                            if 'input' in input:
                                input = input.replace('\n', '')
                                shutil.copy(input, os.path.join(filePath, 'sampleCrash'), follow_symlinks=True)
                        break
            break
        
def deduplicateCrashes(targetProgram):
    targetPath = os.path.join(LOGPATH, targetProgram)
    logList = [] # Log details
    uniqueBugs = [] # File name

    ## Start classificate ASAN logs
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
    ## END classificate ASAN logs

    ## Start save classificated logs
    # make uniqueBugs directory for saving logs
    uniqueBugPath = os.path.join(targetPath, 'uniqueBugs')
    checkOutputDirectory(uniqueBugPath)
    makeTextFile(fileName='uniqueBugs_'+str(len(uniqueBugs)),
                 contents=['# of uniqueBugs: '+str(len(uniqueBugs))],
                 filePath=uniqueBugPath)
    totalUniqueBugs.append(targetProgram + '_uniqueBugs_' + str(len(uniqueBugs)))
    if len(uniqueBugs) != 0:
        for num in range(1, len(uniqueBugs)+1):
            checkOutputDirectory(os.path.join(uniqueBugPath, str(num)))
            # make log file
            makeTextFile(fileName='asanLog.txt',
                        contents=logList[num-1],
                        filePath=os.path.join(uniqueBugPath, str(num)))
            # make duplicated file list text file
            makeTextFile(fileName='duplicatedFiles.txt',
                        contents=uniqueBugs[num-1],
                        filePath=os.path.join(uniqueBugPath, str(num)))
    ## End save classificated logs
    
    if len(uniqueBugs) != 0:
        for num in range(1, len(uniqueBugs)+1):
            getSampleCrashFile(filePath=os.path.join(uniqueBugPath, str(num)), targetProgram=targetProgram)
    
def main():
    targetProgram = ['boringssl-2016-02-12', 'exiv2', 'guetzli-2017-3-30', 'imginfo', 'infotocap', 'jhead', 'lame', 'lcms-2017-03-21', 'libjpeg-turbo', 'libxml2', 'mp3gain', 'nm', 'tiffsplit', 'woff2-2016-05-06', 'wpantund']
                    #  'c-ares',
                     #'cflow',
                     #'flvmeta',
                     #'guetzli-2017-3-30',
                     #'harfbuzz-1.3.2',
                     #'jhead',
                     #'json-2017-02-12',
                     #'lame',
                     #'libjpeg-turbo-07-2017',
                     #'libjpeg-turbo',
                     #'libpng-1.2.56',
                     #'libssh-2017-1272',
                     #'libxml2-v2.9.2',
                     #'libxml2',
                    #  'mp42aac',
                     #'mujs',
                     #'openssl-1.0.1f',
                     #'openssl-1.0.2d',
                     #'openssl-1.1.0c-bignum',
                     #'openssl-1.1.0c-x509',
                     #'pcre2-10.00',
                    #  'proj4',
                     #'sqlite-2016-11-14',
                     #'sqlite3',
                     #'tcpdump',
                     #'vorbis-2017-12-11'
                     ]
    targetProgram = FTS
    for target in targetProgram:
        deduplicateCrashes(target)

    # make total unique bug file in output directory
    makeTextFile(fileName='result.txt',
                 contents=totalUniqueBugs,
                 filePath=LOGPATH)
    
    print("DONE!")

if __name__ == "__main__":
    main()
