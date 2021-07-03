# Script to create the session content files for Hugo from a csv file.

import csv
with open('sessions.csv') as csvfile:
    reader = csv.DictReader(csvfile)

    for row in reader:
        slot = row['slot'].lower()
        title = row['title']
        slug = row['slug']
        speakers = row['speakers'].split(", ")
        time_start = row['time_start']
        time_end = row['time_end']
        abstract = row['content']

        pre = slot
        if pre:
           pre = pre+"-" 

        url = "/sessions/"+slug

        filename =  "sessions/"+pre+slug+".md"
        with open(filename, "w") as f:
            f.write("---\n")
            f.write("id: "+slot+"\n")
            f.write("title: \""+title+"\"\n")
            f.write("url: "+url+"\n")
            f.write("speakers:\n")
            for s in speakers:
                f.write(" - "+s+"\n")
            f.write("time_start: "+time_start+".000Z\n")
            f.write("time_end: "+time_end+".000Z\n")
            f.write("block: "+slot[0:1]+"\n")
            f.write("slot: "+slot[1:3]+"\n")
            f.write("---\n\n")
            f.write(abstract)

