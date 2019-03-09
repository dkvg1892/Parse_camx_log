#Author: Deepakkumar Gupta

import re
def get_reg_PublishFrameControl():
    #Working
    reg_PublishFrameControl = r"""
    \d+-\d+\s+\d+:\d+:\d+\.\d+\s+\d+\s+\d+\s+\w+\s+\w+\s+:\s+
    \[\s+\w+\]
    \[\w+\]\s+camxcawbioutil\.cpp:\d+\s+
    (?P<Function>PublishFrameControlToMainMetadata)
    \(\)\s+\w+\s+\w+\s+\w+\s+\w+:\s+
    (?P<ReqId>\d+)
    \s+\w+:
    (?P<CID>\d+)
    \s+\w+\(\w+:
    (?P<Gain_R>(\d+\.\d+)|([-]\d+\.\d+))
    ,\s+\w+:
    (?P<Gain_G>(\d+\.\d+)|([-]\d+\.\d+))
    ,\s+\w+:
    (?P<Gain_B>(\d+\.\d+)|([-]\d+\.\d+))    
    \)\s+\w+\(
    (?P<CCT>\d+)
    \),\s+\w+:\(\w+/\w+:
    (?P<R_G_Ratio>(\d+\.\d+)|([-]\d+\.\d+))    
    \s+\w+\/\w+:
    (?P<B_G_Ratio>(\d+\.\d+)|([-]\d+\.\d+))    
    \)\s+\w+:\s+
    (?P<FlashState>\d+)
    """
    #pattern = re.compile(reg_PublishFrameControl, re.VERBOSE)
    #line = "02-21 09:16:36.973   720  2503 I CamX    : [ INFO][STATS_AWB] camxcawbioutil.cpp:2311 PublishFrameControlToMainMetadata() Published PropertyIDAWBFrameControl for reqID: 1 camId:0 Gain(R:1.953914, G:1.000000, B:1.708272) CCT(4593), Decision_AfterTC:(R/G:0.511793 B/G:0.585387) FlashState: 0"
    #print(pattern.search(line))
    
    return reg_PublishFrameControl

def get_empty_PublishFrameControl_dict():
    dicts = {'Function': 'PublishFrameControlToMainMetadata', 'Gain_B': '0.0', 'CID': '0', 'Gain_G': '0.000000', 'B_G_Ratio': '0.00', 'CCT': '0', 'FlashState': '0', 'Gain_R': '0.0', 'R_G_Ratio': '0.0', 'ReqId': '0'}
    return dicts


def parse_file(file_name):
    PublishFrameControl = [get_empty_PublishFrameControl_dict()]
    cid_avail = [0,0,0,0,0,0]  #assuming max six camera id available in log
    pattern_PublishFrameControl = re.compile(get_reg_PublishFrameControl(), re.VERBOSE)
    with open(file_name) as infile:
        for line in infile:
            match1 = pattern_PublishFrameControl.search(line)
            if match1 is not None:
                #print(line)
                dict = match1.groupdict()
                PublishFrameControl.append(dict)
                cid_avail[int(dict["CID"])] = 1

    #print(PublishFrameControl)
    return cid_avail, PublishFrameControl[1:]


def fill_empty_data(*argv):
    for arg in argv:
        for a in arg:
            a.append(-1)

def get_data(dictionary, var_name,var_type):
    var = [[],[],[],[],[],[]]
    for l in dictionary:
        cid = int(l["CID"])
        fill_empty_data(var)
        if var_type == 0: #int
            var[cid][-1] = int(l[var_name])
        elif var_type == 1: #float
            var[cid][-1] = float(l[var_name])
    return var
    
