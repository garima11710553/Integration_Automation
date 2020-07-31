import os
import uuid
s=str()
l=list()
path='/Users/garimsin/Documents/Integration/BBQ_GR_002 copy'
psx="/Users/garimsin/Documents/psx-ios"
asset=os.listdir(path+'/need')
if os.path.exists('/Users/garimsin/Documents/Integration/BBQ_GR_002 copy/Background'):
    b=os.listdir(path+'/Background')
    for j in b:
        asset.append(j)
p=psx+"/PSExpress.xcodeproj/project.pbxproj"
#p="/Users/garimsin/Documents/Integration/project.pbxproj"
#print(asset)
with open(p) as fname:
    print(fname)
    s=fname.read()
    l=s.split('\n')
    p1='/* Begin PBXBuildFile section */'
    p2='/* Begin PBXFileReference section */'
    p3='		2F1BBAFE227AF778005C1BC3 /* COLLAGE */ = {'
    p4='		B712595916B66E6A006B2E2C /* Resources */ = {'
    p5='		1D82AF4A1F32F74C0064B57A /* PatternsTiles */ = {'
    p6=""
    for f in asset:
        if f !=".DS_Store":
            u1=''.join(str(uuid.uuid4()).upper().split('-')[1:])
            u2=''.join(str(uuid.uuid4()).upper().split('-')[1:])
            if f[-4:] == 'json':
                s1='		'+u1+' /* '+f+' in Resources */ = {isa = PBXBuildFile; fileRef = '+u2+' /* '+f+' */; settings = {ASSET_TAGS = (collage_theme_resource, ); }; };'
                s2='		'+u2+' /* '+f+' */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = text.json; name = '+f+'; path = thirdparty/adobe/PSXCommonFeatures/resources/text/stickers/COLLAGE/'+f+'; sourceTree = SOURCE_ROOT; };'
                s3='				'+u2+' /* '+f+' */,'
                s4='				'+u1+' /* '+f+' in Resources */,'
                p6=p3
            elif f[-3:] == 'svg':
                s1='		'+u1+' /* '+f+' in Resources */ = {isa = PBXBuildFile; fileRef = '+u2+' /* '+f+' */; settings = {ASSET_TAGS = (collage_theme_resource, ); }; };'
                s2='		'+u2+' /* '+f+' */ = {isa = PBXFileReference; fileEncoding = 4; lastKnownFileType = text.xml; name = '+f+'; path = thirdparty/adobe/PSXCommonFeatures/resources/text/stickers/COLLAGE/'+f+'; sourceTree = SOURCE_ROOT; };'
                s3='				'+u2+' /* '+f+' */,'
                s4='				'+u1+' /* '+f+' in Resources */,'
                p6=p3
            elif f[-3:] == 'jpg':
                print('hgdvwhged')
                s1='		'+u1+' /* '+f+' in Resources */ = {isa = PBXBuildFile; fileRef = '+u2+' /* '+f+' */; settings = {ASSET_TAGS = (background_PatternTiles, collage_theme_resource, ); }; };'
                s2='		'+u2+' /* '+f+' */ = {isa = PBXFileReference; lastKnownFileType = image.jpeg; path = "'+f+'"; sourceTree = "<group>"; };'
                s3='				'+u2+' /* '+f+' */,'
                s4='				'+u1+' /* '+f+' in Resources */,'
                p6=p5
            i1=l.index(p1)+1
            l.insert(i1,s1)
            i2=l.index(p2)+1
            l.insert(i2,s2)
            i3=l.index(p6)+3
            l.insert(i3,s3)
            i4=l.index(p4)+4
            l.insert(i4,s4)
    s="\n".join(l)
with open(p,"w") as fname:
    fname.write(s)
    print("ENTRY DONE")
