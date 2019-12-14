import pygame
import math

def stateChecker(r1,r2,d):
	if(d==0):
		if(r1!=r2):
			return "Cocentric"
		else:
			return "Coinciding"
	else:
		xsq=(((r1**2)-(r2**2)+(d**2))/(2*d))**2
		r2sq=r1**2
		ysq=r2sq-xsq
		if(ysq==0):
			return "Tangent"
		elif(ysq>0):
			return "Intersecting at two points"
		else:
			return "Non-Intersecting"			

def visualize(r1,r2,d):
    pygame.init()
    scr_w=1024
    scr_h=600
    screen = pygame.display.set_mode((scr_w,scr_h))
    pygame.display.set_caption('Circle-Visualizer')
    black=(0,0,0)
    red=(255,109,109)
    yellow=(250,255,0)
    green=(3,255,0)
    orange=(255,165,0)
    white=(255,255,255)
    clock=pygame.time.Clock()
    bgImage=pygame.image.load('bg.png')
    shadowImg=pygame.image.load('page_shadow.png')
    graphImg=pygame.image.load('graph.png')
    font=pygame.font.Font('freesansbold.ttf',25,bold=True,underline=True)
    text=pygame.font.Font('freesansbold.ttf',32,bold=True,underline=True).render('Circle - Visualizer',True,white)
    textRect=text.get_rect()
    textRect.center=(250,49)
    text1=font.render('Radius of Circle-1: '+str(r1),True,orange)
    text1Rect=text1.get_rect()
    text1Rect.left=50
    text1Rect.top=124
    text2=font.render('Radius of Circle-2: '+str(r2),True,green)
    text2Rect=text2.get_rect()
    text2Rect.left=50
    text2Rect.top=174
    text3=font.render('Distance between Circles: '+str(d),True,yellow)
    text3Rect=text3.get_rect()
    text3Rect.left=50
    text3Rect.top=224
    text4=font.render('The two Circles are:',True,white)
    text4Rect=text4.get_rect()
    text4Rect.left=60
    text4Rect.top=299
    text5=font.render(stateChecker(r1,r2,d),True,yellow,red)
    text5Rect=text5.get_rect()
    text5Rect.center=(250,374)

    a=1
    while(a):
        screen.blit(bgImage,(0,0))
        screen.blit(shadowImg,(-85,-60))
        screen.blit(graphImg,(490,30))
        screen.blit(text,textRect)
        pygame.draw.rect(screen,red,pygame.Rect(textRect.left-10,textRect.top-10,textRect.width+20,textRect.height+20),5)
        screen.blit(text1,text1Rect)
        screen.blit(text2,text2Rect)
        screen.blit(text3,text3Rect)
        pygame.draw.rect(screen,green,pygame.Rect(text4Rect.left-20,text4Rect.top-20,425,200),7)
        screen.blit(text4,text4Rect)
        screen.blit(text5,text5Rect)
        pygame.draw.circle(screen,orange,(740,290),int(math.floor(r1))*10,4)
        pygame.draw.circle(screen,orange,(740,290),5)
        pygame.draw.circle(screen,green,(740+10*int(math.floor(d)),290),int(math.floor(r2))*10,4)
        pygame.draw.circle(screen,green,(740+10*int(math.floor(d)),290),5)
        pygame.draw.line(screen,yellow,(741,290),(739+10*int(math.floor(d)),290),5)
        for event in pygame.event.get():
            if(event.type==pygame.QUIT):
               pygame.quit()
               quit()
        pygame.display.update()
        clock.tick(60)

def main():
	print("\n	------------------------------------------------------------")
	print("	|                  Circle - Visualizer                     |")
	print("	|__________________________________________________________|\n")
	
	R1=float(input("	Enter the Radius for Circle-1 : "))
	R2=float(input("	Enter the Radius for Circle-2 : "))
	D=float(input("\n	Enter the Distance between the two Circles : "))
	
	visualize(R1,R2,D)
	
if __name__ == "__main__":
	main()
