RED='\033[0;31m'
BLUE='\033[0;34m'
NC='\033[0m'
dir="hmdb51/Frames"
classes=`ls $dir`
for class in $classes
do
	printf "${BLUE} $class ${NC}\n"
	videos=`ls $dir"/"$class"/"`
	for video in $videos
	do
		printf "${BLUE} $dir/$class/v_${video::-4}  ${NC}\n"
		python convert_avi_jpg.py -i $dir"/"$class"/"$video -o $dir"/"$class"/v_"${video::-4} 
	done
done
