'''import pyscreenshot
# to capture the screenshot
image=pyscreenshot.grab()
#To show the screenshot
image.show()
#To save the screenshot
image.save('geekforgeek.pug')'''

#ex2
import pyscreenshot
#image=pyscreenshot.grab(bbox=(x1,x2,y1,y2))
image=pyscreenshot.grab(bbox=(100,100,1000,1000))

#view the screen shot
image.show()
image.save('hareeforharee')