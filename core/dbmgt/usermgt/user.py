class User:
    def __init__(self, FullName="",
                 ContactNos="",
                 Email="",
                 NIC="",
                 Nationality="",
                 Gender="",
                 DateofBirth="",
                 MaritalStatus="",
                 SpokenLanguages="",
                 Address="",
                 computerSkills="",
                 project=""):
        self.project = project
        self.computerSkills = computerSkills
        self.Address = Address
        self.FullName = FullName
        self.ContactNos = ContactNos
        self.Email = Email
        self.NIC = NIC
        self.Nationality = Nationality
        self.Gender = Gender
        self.DateofBirth = DateofBirth
        self.MaritalStatus = MaritalStatus
        self.SpokenLanguages = SpokenLanguages
