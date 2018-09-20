import cdecompression
import os

source = "wiki_inputs/"
for root, dirs, filenames in os.walk(source):
    for f in filenames:
        fullpath = os.path.join(source, f)
        cdecompression.text_parse(fullpath)
