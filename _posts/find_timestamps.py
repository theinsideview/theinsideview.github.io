# I have a transcript file 2023-05-02-breandan.md formatted as follow:

"""
**Michaël**: Do you think we need symbolic reasoning to get to AGI? 

**Breandan**: If you have symbols, it makes things a lot more efficient in some way. It's possible that you don't need symbols. I think symbols are important if you want to make machines that are compact and that can interface with humans who also use symbols. So I like symbols. <a href="#outline">⬆</a>

## Applying Machine Learning to SAT Solvers

**Michaël**: How do you actually do symbolic reasoning? What's your research, and how do you actually implement it?
"""

# And I have a caption file (format sbv) that includes the text from this transcript, such as this part: 

"""
0:01:08.100,0:01:16.440
that are compact and that can interface with 
humans who also use symbols. So I like symbols.

0:01:16.980,0:01:20.940
How do you actually do symbolic 
reasoning? What's your research,

0:01:20.940,0:01:22.740
and how do you actually implement it?
"""

# I want to write a python script that enables me to find the timestamp at which a sub-headline (e.g. "Applying Machine Learning to SAT Solvers") appears in the caption file.
# To be clear, sub-headlines start with a "##" and end with a newline character.

# The script should take two arguments:
# 1. the path to the transcript file
# 2. the path to the caption file

# The script should print the timestamp at which the sub-headline appears in the caption file.
# The output should look like this:
# 
# $ python find_timestamps.py _posts/2023-05-02-breandan.md _captions/2023-05-02-breandan.sbv
#
# Applying Machine Learning to SAT Solvers 0:01:16.980
# ...

# You can assume that the transcript file and the caption file are formatted as described above.

# The general steps to solve this problem are:
# 1. Read the transcript file and store the sub-headlines in a list
# 2. Read the caption file, by creating a dictionary that associates each timestamp with the text that appears at that timestamp, and also stores an ordered list of the keys of the dictionary
# 3. For each sub-headline, find the timestamp at which the sub-headline appears in the caption file. Note that if the sub-headline doesn't appear perfectly at the beginning of a timestamp, we will display the closest timestamp before the text appears.

# Note: to make sure that a timestamp is there, the easiest heuristic is to make sure we have about three words correct, since many sub-headlines might start with the same first word, or even same two words and we want to avoid duplicates.
# Another idea is to just make sure we have the first 10 characters of the sub-headline, but this might be too restrictive.

# Note: you can use the python library "datetime" to manipulate timestamps. For example, you can use the function "datetime.timedelta" to add a certain number of seconds to a timestamp.

# Note: you can use the python library "re" to manipulate regular expressions. For example, you can use the function "re.match" to check if a string matches a regular expression.

# Note: you can use the python library "sys" to read command line arguments. For example, you can use the function "sys.argv" to get the list of command line arguments.

import datetime
import re
import sys
from ipdb import set_trace as p

def find_timestamps(transcript_path, caption_path):
    # Read the transcript file and store a dictionary that associates each sub-headline with the text that follows the sub-headline, without including the speaker name and associated formatting.
    transcript = open(transcript_path, "r")
    sub_headlines_to_following_text = {}
    for idx, line in enumerate(transcript):
        if line.startswith("## "):
            next_line = transcript.readline()
            next_line = transcript.readline()
            sub_headlines_to_following_text[line[3:-1]] = next_line.replace("**Michaël**: ", "").replace("**Breandan**: ", "").replace("<a href=\"#outline\">⬆</a>", "")
    transcript.close()

    # Read the caption file, by creating a dictionary that associates each timestamp with the text that appears at that timestamp, and also stores an ordered list of the keys of the dictionary
    # Start by checking that the line actually includes timestamps of the form "0:01:08.100,0:01:16.440"
    # If yes, then the two next lines are the text that appears at that timestamp, which you might put into your dictionary value, the key being the first timestamp
    # If no, then the line is not something we care about and we might pass

    caption_file = open(caption_path, "r")
    caption_dict = {}
    caption_keys = []
    for line in caption_file:
        if re.match(r"\d+:\d+:\d+\.\d+,\d+:\d+:\d+\.\d+", line):
            timestamp = line.split(",")[0]
            # read two lines not just one
            caption = caption_file.readline()
            caption += caption_file.readline()
            caption_dict[timestamp] = caption
            caption_keys.append(timestamp)

    # For each sub-headline, find the timestamp at which the sub-headline appears in the caption file. Note that if the sub-headline doesn't appear perfectly at the beginning of a timestamp, we will display the closest timestamp before the text appears.
    # Note: you can use the python library "datetime" to manipulate timestamps. For example, you can use the function "datetime.timedelta" to add a certain number of seconds to a timestamp.   
    # Note: you can use the python library "re" to manipulate regular expressions. For example, you can use the function "re.match" to check if a string matches a regular expression.
    # Note: you can use the python library "sys" to read command line arguments. For example, you can use the function "sys.argv" to get the list of command line arguments.
    # Note: to make sure that a timestamp is there, the easiest heuristic is to make sure we have about three words correct, since many sub-headlines might start with the same first word, or even same two words and we want to avoid duplicates.
    # Another idea is to just make sure we have the first 10 characters of the sub-headline, but this might be too restrictive.

    for headline, text in sub_headlines_to_following_text.items():
        # find the timestamp at which the sub-headline appears in the caption file
        # if the sub-headline doesn't appear perfectly at the beginning of a timestamp, we will display the closest timestamp before the text appears
        # make sure we have about three words correct
        # print the timestamp at which the sub-headline appears in the caption file
        # print the sub-headline
        # print a newline
        for key in caption_keys:
            if len(text.strip()) > 10:
                # check if the sub-headline appears in the caption file
                # if yes, print the timestamp at which the sub-headline appears in the caption file
                # print the sub-headline
                # print a newline
                if text[:20].lower() in caption_dict[key].lower():
                    print(key, headline)
                    # print(f"{text[:20]}//,{caption_dict[key].lower()}")

if __name__ == "__main__":
    transcript_path = sys.argv[1]
    caption_path = sys.argv[2]
    find_timestamps(transcript_path, caption_path)