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
def compareASANLogs(logA, logB):
    DUPLICATED = True
    UNDUPLICATED = False

    if logA == logB:
        return DUPLICATED
    else:
        return UNDUPLICATED

## return ASAN logs from file path.
def getLogsFromFile(filePath):
    asanLogs = []
    on = False
    with open(filePath, 'r') as log:
        for line in log:
            if on:
                if line == '\n':
                    break
                asanLogs.append(line)
            elif line.find('ERROR'):
                on = True
    return asanLogs

def deduplicateCrashes(targetProgram):
    targetPath = os.path.join(LOGPATH, targetProgram)
    
    # get directory list in target program directory
    for trial in os.listdir(targetPath):
        # read ASAN log files in trial* 
        for log in os.listdir(trial):
            print(log)

def main():
    print("DONE!")

if __name__ == "__main__":
    main()
