import cv2
import sys
import os
import click

class avi2jpg:
    vid = None
    
    def convert(self, video, output_dir):
        vidcap = cv2.VideoCapture(video)
        success,image = vidcap.read()
        count = 0
        while success:
            framecount = "{number:06}".format(number=count)
            cv2.imwrite(output_dir + "/img_"  + framecount+".jpg", image)     # save frame as JPEG file      
            success,image = vidcap.read()
            count += 1

@click.command(help="")
@click.option('-i', '--input_file', type=str, help='Path to .avi', required= True)
@click.option('-o', '--output_dir', type=str, help='Output directory', required= True)

def main(input_file, output_dir):
    if(input_file is None):
    	print("Please give input_file and output_dir.")
    elif(input_file[-4:]!=".avi"):
        print("Please give an .avi video as an argument to this program")
    else:
    	if not os.path.exists(output_dir):
        	os.mkdir(output_dir)
    	converter = avi2jpg()
    	converter.convert(input_file, output_dir)
	

if __name__ == "__main__":
	main()
