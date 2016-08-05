import config
from core.dbmgt.usermgt.user import User
from core.packages.keyword_extractor.Keyword_Extractor import *
import re
# content = 'CV - Ravindu Rashmika.pdf'

from textract import process


def CV_reader(fileName):
    project = []
    technicalSkills = ""
    global FullName, ContactNos, Email, NICNo, Nationality, Gender, DateofBirth, MaritalStatus, SpokenLanguages
    file = config.PathToUpload + fileName
    text = process(file)
    data = text.split("\n")
    print data
    # print "------------------------------------", len(data)
    # try:
    #
    # except:
    #     return "Wrong Template"
    Address = data[1]
    for i in range(0, len(data)):
        if data[i] == "Full Name":
            FullName = data[i + 2]
        if data[i] == "Contact Nos.":
            ContactNos = data[i + 2]
        if data[i] == "Email":
            Email = data[i + 2]
        if data[i] == "NIC No":
            NICNo = data[i + 2]
        if data[i] == "Nationality":
            Nationality = data[i + 2]
        if data[i] == "Gender":
            Gender = data[i + 2]
        if data[i] == "Date of Birth":
            DateofBirth = data[i + 2]
        if data[i] == "Marital Status":
            MaritalStatus = data[i + 2]
        if data[i] == "Spoken Languages":
            SpokenLanguages = data[i + 2]
        if len(re.findall("\x0cProjects and Research", data[i], re.IGNORECASE)) == 1:
            k = i + 2
            while len(re.findall("Key Skills and Competencies", data[k], re.IGNORECASE)) != 1:
                print data[k]
                if len(re.findall("\xe2\x80\x93 Project", data[k], re.IGNORECASE)) == 1:
                    j = k + 4
                    description = ""
                    date = data[k + 2]
                    title = data[k]
                    while len(re.findall("\xe2\x80\x93 Project", data[j], re.IGNORECASE)) != 1:
                        if len(re.findall("Key Skills and Competencies", data[j], re.IGNORECASE)) == 1:
                            break
                        description += data[j]
                        description += "\n"
                        j += 1
                    project.append({"title": title, "date": date, "description": description})
                    k = j
        if len(re.findall("Key Skills and Competencies", data[i], re.IGNORECASE)) == 1:
            technicalSkills += data[i+1].replace('Computer skills \xe2\x80\x93', '')
            technicalSkills += "," + data[i+2].replace('Database \xe2\x80\x93','')

    extractor = Keyword_Extractor()
    extractor.modify_extractor()
    projectSet = ""
    for item in project:
        # print extractor.extract(item["description"])
        projectSet += ','.join(extractor.extract(item["description"]))
    user = User(FullName, ContactNos, Email, NICNo, Nationality, Gender, DateofBirth, MaritalStatus,
                SpokenLanguages, Address, technicalSkills, projectSet)

    return user
