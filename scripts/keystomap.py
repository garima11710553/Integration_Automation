import os, json
'''
import xlrd
import openpyxl
wb = openpyxl.Workbook()
sheet = wb.active
'''
ktm=list()
l=[
    "Party_GM_001",
    "Party_GR_001",
    "Party_GR_004",
    "Party_GR_006",
    "Party_GR_009",
    "Party_LC_002",
    "Party_MSz_001",
    "Party_MSz_002",
    "Party_GR_008",
    "Thank_you_EA_003",
    "Thank_you_GM_001",
    "Thank_you_LC_001",
    "Thank_you_LC_002",
    "Thank_you_MSz_002",
    "Winter_EA_002",
    "Winter_GR_002",
    "Winter_GR_003",
    "Winter_GR_004",
    "Winter_LC_002",
    "Winter_LC_004",
    "Winter_EA_001",
    "Winter_EA_003",
    "Music_EA_001",
    "Music_EA_002",
    "Music_GR_001",
    "Music_LC_002",
    "Music_LC_003",
    "Music_LC_001",
    "Music_GR_003",
    "Music_EA_003",
    "Music_GR_002",
    "Generic_EA_004",
    "Generic_GM_001",
    "Generic_GR_001",
    "Generic_GR_009",
    "Generic_GR_010",
    "Generic_LC_002",
    "Generic_LC_006",
    "Generic_MSz_001",
    "Generic_MSz_002",
    "Congratulations_GR_003",
    "Congratulations_GR_007",
    "Congratulations_LC_004",
    "Congratulations_LC_001",
    "Congratulations_EA_001",
    "Congratulations_GR_006",
    "Congratulations_EA_002",
    "Congratulations_GR_005",
    "Congratulations_GR_008",
    "Congratulations_GR_002",
    "Comic_GR_001",
    "Comic_GR_002",
    "Comic_LC_001",
    "Comic_EK_003",
    "Comic_EK_002",
    "Birthday_EA_002",
    "Birthday_GR_001",
    "Birthday_GR_003",
    "Birthday_LC_007",
    "Birthday_MS_001",
    "Birthday_GR_004",
    "Birthday_EA_001",
    "Birthday_GR_002",
    "Birthday_LC_008",
    "Invitation_GR_006",
    "Invitation_LC_001",
    "Abstract_JD_003",
    "Abstract_JD_004",
    "Abstract_JD_005",
    "Abstract_JD_006",
    "Abstract_RB_001",
    "Abstract_RB_003",
    "Abstract_RB_004",
    "Abstract_RB_005",
    "Anniversary_JD_001",
    "Anniversary_JD_002",
    "Anniversary_JD_004",
    "Anniversary_JD_007",
    "Anniversary_JD_009",
    "Anniversary_JD_010",
    "Anniversary_JD_011",
    "Anniversary_MS_001",
    "Anniversary_MS_003",
    "Anniversary_RB_002",
    "Anniversary_RB_003",
    "BBQ_GR_002",
    "BBQ_LC_001",
    "BBQ_RB_002",
    "Family_EW_001",
    "Family_GR_001",
    "Family_GR_002",
    "Family_JD_001",
    "Family_JD_002",
    "Family_JD_003",
    "Family_JD_004",
    "Holiday_JD_002",
    "Holiday_JD_003",
    "Holiday_JD_005",
    "Holiday_RB_001",
    "Holiday_RB_002",
    "Holiday_RB_003",
    "Holiday_RB_006",
    "Holiday_RB_007",
    "Holiday_RB_008",
    "School_EA_003",
    "School_JD_001",
    "School_JD_003",
    "school_LC_001",
    "School_LC_004",
    "Sports_EK_003",
    "Sports_EW_001",
    "Sports_GR_001",
    "Sports_GR_002",
    "Sports_GS_001",
    "Sports_JD_001",
    "Sports_JD_002",
    "Sports_JD_003",
    "Sports_LC_002",
    "Sports_MS_001",
    "Sports_RB_001",
    "Sports_RB_002",
    "Valentines_JD_001",
    "Valentines_JD_003",
    "Valentines_JD_004",
    "Valentines_JD_005",
    "Valentines_MS_001",
    "Valentines_RB_003",
    "Valentines_RB_007",
]
p1='/Users/garimsin/Documents/psx-ios/PSExpress/Classes/Collage/ThemeAssets'
os.chdir(p1)
def get_keys(g):
    if type(g) == dict :
        tk=g.keys()
        for i in tk:
            if i not in ktm:
                ktm.append(i)
                if type(g[i]) == dict:
                    get_keys(g[i])
                if type(g[i]) == list:
                    for j in g[i]:
                        get_keys(j)
    if type(g) == list:
        for j in g[i]:
            if type(j) == dict():
                tk=j.keys()
                for i in tk:
                    if i not in ktm:
                        ktm.append(i)
                        if type(j[i]) == dict():
                            get_keys(g[i])
                        if type(j[i]) == list:
                            for j in g[i]:
                                get_keys(j)
            if type(j) == list():
                for k in j:
                    get_keys(k)


for z in range(0,len(l)):
        theme=l[z]
        asp=['1X1','3X4','4X3','9X16','16X9']
        os.chdir(p1+'/LayoutDescriptions/Layout'+theme)
        for i in range(1,10):
            for j in asp:
                file='Layout'+theme+'_'+str(i)+'_'+j+'.json'
                if os.path.exists(file):
                    with open(file) as fname:
                            #print(file)
                            d = json.load(fname)
                            #print(type(d))
                            get_keys(d)
                            print(file)
                            print(ktm)  
                            print(len(ktm)) 

