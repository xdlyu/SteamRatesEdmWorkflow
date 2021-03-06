'''
This file allows you to produce a set of jobs to be sent to a batch queue.
The jobs will be located in the 'Jobs' directory.
After producing them, it is advisable to test one of the jobs locally before sending them all.

Example of a local test:
./Jobs/sub_job/sub_0.jobb

Submitting all jobs on batch:
./sub_total.jobb
'''

import os
import sys


'''
--------------------------OPTIONS TO BE FILLED OUT-----------------------------------------
'''
#If you already have a list of input files with the proper format, you may not want to remake it
#Type True if you want to remake them, False otherwise
makeInputFilesList = False
#Directory where your input root files are located
inputFilesDir = "/eos/cms/store/group/dpg_trigger/comm_trigger/TriggerStudiesGroup/STEAM/xulyu/menu_v4.2/HLTPhysics_PS1p5e34_new"

#Were your input files produced by STEAM? If yes, file_type = "custom"
#Are these raw data files?
#If yes, are you running specifically on L1Accept files? Then file_type = "L1Accept"
#Are you running on other non-L1Accept data files? Then file_type = "RAW"
file_type = "L1Accept"#"RAW"#"custom"

#Directory where the top of your CMSSW release is located
cmsswDir = "/afs/cern.ch/work/d/dbeghin/Work/2017_STEAM/For_Data/CMSSW_9_2_12/src"

#Json file
json_file = "/afs/cern.ch/work/d/dbeghin/public/json/json_306154_PS2_LS93_PU57.txt"

#Do you wish to use any unusual (non-default) options for the batch queue, and the number of files processed per job?
#If you do, set the following boolean to True
isUnusual = True
#If you do, please also specify the following parameters:
#number of files processed per job
n = 1
#Batch queue where you wish to send the jobs
queue = "8nh"
'''
--------------------------OPTIONS TO BE FILLED OUT-----------------------------------------
'''


#run the script
command = ""
if makeInputFilesList:
    command = "python batchScriptForRates.py -j %s -e %s -i %s -f %s" %(json_file, cmsswDir, inputFilesDir, file_type)
else:
    command = "python batchScriptForRates.py -j %s -e %s -f %s" %(json_file, cmsswDir, file_type)

if isUnusual:
    command += " -n %s -q %s" %(n, queue)

os.system(command)






