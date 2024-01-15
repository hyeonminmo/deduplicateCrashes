import os

PATH = '/home/autofz/aflasan'
FTSPATH = os.path.join(PATH, 'fuzzer-test-suite')
UNIPATH = os.path.join(PATH, 'unibench')
CRASHPATH = '/home/autofz/crashes'
OUTPUTPATH = '/home/autofz/out'
TARGETPATH = {
    # FTS target program
    'boringssl-2016-02-12': os.path.join(FTSPATH, 'boringssl-2016-02-12/boringssl-2016-02-12'),
    'c-ares-CVE-2016-5180': os.path.join(FTSPATH, 'c-ares-CVE-2016-5180/c-ares-CVE-2016-5180'),
    'c-ares': os.path.join(FTSPATH, 'c-ares-CVE-2016-5180/c-ares-CVE-2016-5180'),
    'guetzli-2017-3-30': os.path.join(FTSPATH, 'guetzli-2017-3-30/guetzli-2017-3-30'),
    'harfbuzz-1.3.2': os.path.join(FTSPATH, 'harfbuzz-1.3.2/harfbuzz-1.3.2'),
    'json-2017-02-12': os.path.join(FTSPATH, 'json-2017-02-12/json-2017-02-12'),
    'lcms-2017-03-21': os.path.join(FTSPATH, 'lcms-2017-03-21/lcms-2017-03-21'),
    'libarchive-2017-01-04': os.path.join(FTSPATH, 'libarchive-2017-01-04/libarchive-2017-01-04'),
    'libjpeg-turbo-07-2017': os.path.join(FTSPATH, 'libjpeg-turbo-07-2017/libjpeg-turbo-07-2017'),
    'libpng-1.2.56': os.path.join(FTSPATH, 'libpng-1.2.56/libpng-1.2.56'),
    'libpng-1.2.56-structure-aware': os.path.join(FTSPATH, 'libpng-1.2.56-structure-aware/libpng-1.2.56-structure-aware'),
    'libssh-2017-1272': os.path.join(FTSPATH, 'libssh-2017-1272/libssh-2017-1272'),
    'libxml2-v2.9.2': os.path.join(FTSPATH, 'libxml2-v2.9.2/libxml2-v2.9.2'),
    'openssl-1.0.1f': os.path.join(FTSPATH, 'openssl-1.0.1f/openssl-1.0.1f'),
    'openssl-1.0.2d': os.path.join(FTSPATH, 'openssl-1.0.2d/openssl-1.0.2d'),
    'openssl-1.1.0c-bignum': os.path.join(FTSPATH, 'openssl-1.1.0c-bignum/openssl-1.1.0c-bignum'),
    'openssl-1.1.0c-x509': os.path.join(FTSPATH, 'openssl-1.1.0c-x509/openssl-1.1.0c-x509'),
    'openthread-2018-02-27-ip6': os.path.join(FTSPATH, 'openthread-2018-02-27-ip6/openthread-2018-02-27-ip6'),
    'openthread-ip6': os.path.join(FTSPATH, 'openthread-2018-02-27-ip6/openthread-2018-02-27-ip6'),
    'openthread-2018-02-27-radio': os.path.join(FTSPATH, 'openthread-2018-02-27-radio/openthread-2018-02-27-radio'),
    'openthread-radio': os.path.join(FTSPATH, 'openthread-2018-02-27-radio/openthread-2018-02-27-radio'),
    'pcre2-10.00': os.path.join(FTSPATH, 'pcre2-10.00/pcre2-10.00'),
    'proj4-2017-08-14': os.path.join(FTSPATH, 'proj4-2017-08-14/proj4-2017-08-14'),
    'proj4': os.path.join(FTSPATH, 'proj4-2017-08-14/proj4-2017-08-14'),
    're2-2014-12-09': os.path.join(FTSPATH, 're2-2014-12-09/re2-2014-12-09'),
    'sqlite-2016-11-14': os.path.join(FTSPATH, 'sqlite-2016-11-14/sqlite-2016-11-14'),
    'vorbis-2017-12-11': os.path.join(FTSPATH, 'vorbis-2017-12-11/vorbis-2017-12-11'),
    'woff2-2016-05-06': os.path.join(FTSPATH, 'woff2-2016-05-06/woff2-2016-05-06'),
    'woff2': os.path.join(FTSPATH, 'woff2-2016-05-06/woff2-2016-05-06'),
    'wpantund-2018-02-27': os.path.join(FTSPATH, 'wpantund-2018-02-27/wpantund-2018-02-27'),
    # UNIBENCH target program
    'ar': os.path.join(UNIPATH, 'ar/ar'),
    'cflow': os.path.join(UNIPATH, 'cflow/cflow'),
    'cxxfilt': os.path.join(UNIPATH, 'cxxfilt/cxxfilt'),
    'exiv2': os.path.join(UNIPATH, 'exiv2/exiv2'),
    'ffmpeg': os.path.join(UNIPATH, 'ffmpeg/ffmpeg'),
    'flvmeta': os.path.join(UNIPATH, 'flvmeta/flvmeta'),
    'imginfo': os.path.join(UNIPATH, 'imginfo/imginfo'),
    'infotocap': os.path.join(UNIPATH, 'infotocap/infotocap'),
    'jhead': os.path.join(UNIPATH, 'jhead/jhead'),
    'jq': os.path.join(UNIPATH, 'jq/jq'),
    'lame': os.path.join(UNIPATH, 'lame/lame'),
    'mp3gain': os.path.join(UNIPATH, 'mp3gain/mp3gain'),
    'mp42aac': os.path.join(UNIPATH, 'mp42aac/mp42aac'),
    'mujs': os.path.join(UNIPATH, 'mujs/mujs'),
    'nm': os.path.join(UNIPATH, 'nm/nm'),
    'objdump': os.path.join(UNIPATH, 'objdump/objdump'),
    'pdftotext': os.path.join(UNIPATH, 'pdftotext/pdftotext'),
    'readelf': os.path.join(UNIPATH, 'readelf/readelf'),
    'size': os.path.join(UNIPATH, 'size/size'),
    'sqlite3': os.path.join(UNIPATH, 'sqlite3/sqlite3'),
    'strings': os.path.join(UNIPATH, 'strings/strings'),
    'tcpdump': os.path.join(UNIPATH, 'tcpdump/tcpdump'),
    'tiffsplit': os.path.join(UNIPATH, 'tiffsplit/tiffsplit'),
    'wav2swf': os.path.join(UNIPATH, 'wav2swf/wav2swf')
}

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

# Used target program list (autofz - 11)
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

crashes = []
def makeASANLogs():
    # get target program properly
    n = 0
    f = open('command.sh', 'w')
    for dir in os.listdir(CRASHPATH):
        trial = 0 # fuzzing trial number
        if '_' in dir:
            dirName = dir.split('_')
            targetProgram = dirName[0]
            targetProgramPath = TARGETPATH[dirName[0]]
            trial = int(dirName[1])
        else:
            targetProgram = dir
            targetProgramPath = TARGETPATH[dir]
            trial = 1

        checkOutputDirectory(os.path.join(OUTPUTPATH, targetProgram))
        saveDir = os.path.join(OUTPUTPATH, os.path.join(targetProgram, 'trial' + str(trial)))
        checkOutputDirectory(saveDir)
        
        crashPath = os.path.join(CRASHPATH, os.path.join(dir, 'mab_'+ targetProgram + '/eval/global/unique_bugs'))
        for (root, directories, files) in os.walk(crashPath):
            for dir in directories:
                dirPath = os.path.join(root, dir)
                for (root_, directories_, files_) in os.walk(dirPath):
                    for file in files_:
                        if 'input' in file:
                            filePath = os.path.join(root_, file)
                            if filePath not in crashes:
                                command = "ASAN_OPTIONS=\"log_path=" + os.path.join(saveDir, str(trial) + str(n)) + "\" " + targetProgramPath + " " + filePath + "\n"
                                n += 1
                                f.write(command)
                                crashes.append(filePath)
                            else:
                                continue
    f.close()                        

    


def main():
    checkOutputDirectory(OUTPUTPATH)
    makeASANLogs()

        

if __name__ == "__main__":
    main()
