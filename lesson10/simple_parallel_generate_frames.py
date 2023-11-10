import generate_frame
from simplempi.parfor import parfor, pprint

for i in parfor(range(720)):
    pprint(f"working on {i}")
    generate_frame.generate_frame(i, output_dir= "./animation_frames_alt")
        #if you want to run this on a different file, note it will overwrite your stuff from generate_frame define directory