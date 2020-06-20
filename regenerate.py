#!/usr/bin/python3
import pandas as pd

# download the lastest list of media types
tables = pd.read_html("http://www.iana.org/assignments/media-types/media-types.xhtml")

# categories
prefix = ["application", "audio", "font", "image", "message", "model", "multipart", "text", "video"]

# dump to files by categories
[tables[i]['Template'].dropna().to_csv(f"data/{prefix[i]}.txt", index=False, header=False) for i in range(len(prefix))]
