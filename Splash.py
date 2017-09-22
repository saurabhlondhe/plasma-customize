import os
import commands
status, output = commands.getstatusoutput("locate -b '\splash'")
lines = output.split('\n')
data=[]
for line in lines:
    data.append(line)
cd="cd "+data[0]
os.system(cd+" && sudo rm Splash.qml")
os.system(cd+" && sudo wget https://raw.githubusercontent.com/saurabhlondhe/plasma-customize/master/Splash.qml")
cd_images=cd+"/images && "
os.system(cd_images+"sudo wget https://raw.githubusercontent.com/saurabhlondhe/plasma-customize/master/images/1234.jpg")
os.system(cd_images+"sudo wget https://raw.githubusercontent.com/saurabhlondhe/plasma-customize/master/images/logo.png")
os.system(cd_images+"sudo wget https://raw.githubusercontent.com/saurabhlondhe/plasma-customize/master/images/8iEknLaia.png")
