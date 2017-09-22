import os
import commands
status, output = commands.getstatusoutput("locate -b '\splash'")
print output
cd="cd "+output
os.system(cd+" && rm Splash.qml")
os.system(cd+" && wget https://raw.githubusercontent.com/saurabhlondhe/plasma-customize/master/Splash.qml")
cd_images=cd+"/images && "
os.system(cd_images+"wget https://raw.githubusercontent.com/saurabhlondhe/plasma-customize/master/images/1234.jpg")
os.system(cd_images+"wget https://raw.githubusercontent.com/saurabhlondhe/plasma-customize/master/images/logo.png")
os.system(cd_images+"wget https://raw.githubusercontent.com/saurabhlondhe/plasma-customize/master/images/8iEknLaia.png")
