import sys
import json
import datetime

if __name__ == '__main__':
    inname = "doc/"
    if (len(sys.argv) == 2):
        inname = sys.argv[1]

    outname = inname+"br.html"
    inname = inname+"bugs.json"

    print("Reading input file '" + inname + "'...")
    with open(inname) as inf:
        data = json.load(inf)

    print("Creating and opening log file '" + outname + "'...")
    f = open(outname, "w")
    f.write("<!doctype html>\n")
    f.write("<html>\n")
    f.write("<head>\n")
    f.write("<title>" + data["project"] + ": bugs</title>\n")
    f.write("</head>\n")
    f.write("<head>\n")
    f.write("<body>\n")
    f.write("<h1>" + data["project"] + "</h1>\n")
    f.write("<h2>Bug Report</h2>\n")

    f.write("<table border=\"1\">\n")

    # Headline
    f.write("<tr>")
    f.write("<td><b>State</b></td>")
    f.write("<td><b>Target Version</b></td>")
    f.write("<td><b>Title</b></td>")
    f.write("<td><b>Description/Comment</b></td>")
    f.write("</tr>\n")

    # Bugs list
    bugs = data["bugs"]
    bugs = sorted(
        bugs, key=lambda kv: kv["tv"] + kv["state"] + kv["title"], reverse=True)
    for bug in bugs:

        f.write("<tr>")

        f.write("<td")
        if "state" in bug:
            state = bug["state"]
            color = "black"
            if state == "open":
                color = "red"
            elif state == "fixed":
                color = "green"
            f.write(" style=\"text-align: center; color: " + color + "\"")
            f.write(">")

            f.write(bug["state"])
        else:
            f.write(">")
        f.write("</td>\n")

        f.write("<td style=\"text-align: center;\">")
        if "tv" in bug:
            f.write(bug["tv"])
        f.write("</td>\n")

        f.write("<td>")
        if "title" in bug:
            f.write(bug["title"])
        f.write("</td>\n")

        f.write("<td>")
        if "description" in bug:
            f.write(bug["description"])
        f.write("</td>\n")

        f.write("</tr>\n")

    f.write("</table>\n")
    f.write("<h2>Releases</h2>\n")

    f.write("<table border=\"1\">\n")

    # Headline
    f.write("<tr>")
    f.write("<td><b>Release</b></td>")
    f.write("<td><b>State</b></td>")
    f.write("<td><b>Date</b></td>")
    f.write("<td><b>Description/Comment</b></td>")
    f.write("</tr>\n")

    # Revisions list
    releases = data["releases"]
    releases = sorted(releases, key=lambda kv: kv["release"], reverse=True)
    for rel in releases:

        f.write("<tr>")

        f.write("<td style=\"text-align: center;\">")
        if "release" in rel:
            f.write(rel["release"])
        f.write("</td>\n")

        f.write("<td>")
        if "state" in rel:
            f.write(rel["state"])
        f.write("</td>\n")

        f.write("<td style=\"text-align: center;\">")
        if "date" in rel:
            f.write(rel["date"])
        f.write("</td>\n")

        f.write("<td>")
        if "description" in rel:
            f.write(rel["description"])
        f.write("</td>\n")

        f.write("</tr>\n")

    f.write("</table>\n")

    f.write("<p>&copy; 2019-2020 Philipp Klein | Generated: " +
            str(datetime.datetime.now()) + "</p>")

    f.write("</body>\n")
    f.write("</html>\n")
    f.close()
