import mosspy

userid = 987654321

m = mosspy.Moss(userid, "python")

m.addBaseFile("C:\\Users\\varda\\OneDrive\\Desktop\\New folder\\new27.py")
# m.addBaseFile("submission/test_student.py")

# Submission Files
m.addFile("C:\\Users\\varda\\OneDrive\\Desktop\\New folder\\new27.py")
# m.addFile("C:\\Users\\varda\\OneDrive\\Desktop\\New folder\\new28.py")

# m.addFilesByWildcard("submission/a01-*.py")

url = m.send() # Submission Report URL

print ("Report Url: " + url)

# Save report file
m.saveWebPage(url, "submission/report.html")

# Download whole report locally including code diff links
mosspy.download_report(url, "submission/report/", connections=8)