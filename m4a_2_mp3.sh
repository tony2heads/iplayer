#!/bin/sh
for f in *.m4a
do ( 
n=${f%%.m4a}
AtomicParsley $f -E ;
# jpg files made
nice /usr/bin/avconv -i $f -b 64k $n.mp3;
#converted to mp3
eyeD3 --add-image=${n}_artwork_1.jpg:ICON $n.mp3;
# image added
)
done
