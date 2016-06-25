#!/bin/bash
# Interesting: wimpmode

#TrumpScript
#https://github.com/samshadwell/TrumpScript
git clone https://github.com/samshadwell/TrumpScript.git langs/

#ArnoldC
#http://lhartikk.github.io/ArnoldC/
git clone https://github.com/lhartikk/ArnoldC langs/

if ! [ -f bin/ArnoldC.jar ]; then
    wget https://lhartikk.github.io/ArnoldC.jar -O bin/ArnoldC.jar
fi
echo """
#!/bin/sh

here=\$(dirname \"\$0\")
file_dir=\$(dirname \"\$1\")
filename=\$(basename \"\$1\")
classname=\"\${filename%.*}\"

cd \"\$file_dir\"
java -jar \"\$here/ArnoldC.jar\" \"\$filename\"
java \"\$classname\"
""" > bin/arnoldc
chmod +x bin/arnoldc


#Ook

#INTERCAL

#Brainfuck

#Anguish