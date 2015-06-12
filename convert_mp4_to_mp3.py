# Adapted from
# https://github.com/andyp123/mp4_to_mp3/blob/master/mp4tomp3.py

# NOTE: you will need python 2, mplayer and lame for this script to work
# sudo apt-get install lame
# sudo apt-get install mplayer
# sudo apt-get install python2.7

from subprocess import call     # for calling mplayer and lame
from sys import argv            # allows user to specify input and output directories
import os                       # help with file handling

def convert_mp4_to_mp3(indir, outdir):
    print "[%s/*.mp4] --> [%s/*.mp3]" % (indir, outdir)
    files = [] # files for exporting
    
    # Rename files
    os.chdir(download_dir)
    raw_files = os.listdir(os.getcwd())
    for x in raw_files:
        new_name = re.sub(r'\W+', '', x)
        new_name = re.sub('mp4', '.mp4', new_name )
        os.rename(x, new_name)

    # get a list of all convertible files in the input directory
    filelist = [ f for f in os.listdir(indir) if f.endswith(".mp4") ]
    for path in filelist:
        basename = os.path.basename(path) 
        filename = os.path.splitext(basename)[0]
        files.append(filename)

    for filename in files:
        print "-- converting %s.mp4 to %s.mp3 --" % (indir + "/" + filename, outdir + "/" + filename)
        #os.system("mplayer -novideo -nocorrect-pts -ao pcm:waveheader " + indir + "/" + filename + ".mp4")
        call(["mplayer", "-novideo", "-nocorrect-pts", "-ao", "pcm:waveheader", indir + "/" + filename + ".mp4"])
        call(["lame", "-h", "-b", "192", "audiodump.wav", outdir + "/" + filename + ".mp3"])
        os.remove("audiodump.wav")
        os.remove(filename + '.mp4')
        print 'done with ' + filename

