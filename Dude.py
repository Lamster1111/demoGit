import pygame
pygame.init()
win = pygame.display.set_mode((500,600))

blue = (0,50,155)

def m(x,y,w,h,colour):
    pygame.draw.rect(win,colour,(x,y,w,h))
    pygame.draw.rect(win,colour,((x+w),(y+h),w,h))
    pygame.draw.rect(win,colour,(x+6*w,y,w,h))
    pygame.draw.rect(win,colour,(x+5*w,(y+h),w,h))
    #second Line
    pygame.draw.rect(win,colour,(x,(y+2*h),w,h))
    pygame.draw.rect(win,colour,(x+w,(y+2*h),w,h))
    #Third Line
    pygame.draw.rect(win,colour,(x+2*w,(y+2*h),w,h))
    pygame.draw.rect(win,colour,(x+3*w,(y+2*h),w,h))
    pygame.draw.rect(win,colour,(x+4*w,(y+2*h),w,h))
    pygame.draw.rect(win,colour,(x+5*w,(y+2*h),w,h))
    pygame.draw.rect(win,colour,(x+6*w,(y+2*h),w,h))
    

    #Forth Line
    pygame.draw.rect(win,colour,(x-w,(y+3*h),w,h))
    pygame.draw.rect(win,colour,(x,y+3*h,w,h))
    
    pygame.draw.rect(win,colour,(x+2*w,(y+3*h),w,h))
    pygame.draw.rect(win,colour,(x+3*w,(y+3*h),w,h))
    pygame.draw.rect(win,colour,(x+4*w,(y+3*h),w,h))
    
    
    pygame.draw.rect(win,colour,(x+6*w,(y+3*h),w,h))
    pygame.draw.rect(win,colour,(x+7*w,(y+3*h),w,h))
    #Line Five
    pygame.draw.rect(win,colour,(x-2*w,(y+4*h),w,h))
    pygame.draw.rect(win,colour,(x-w,(y+4*h),w,h))
    pygame.draw.rect(win,colour,(x,(y+4*h),w,h))
    pygame.draw.rect(win,colour,(x+w,(y+4*h),w,h))
    pygame.draw.rect(win,colour,(x+2*w,(y+4*h),w,h))
    pygame.draw.rect(win,colour,(x+3*w,(y+4*h),w,h))
    pygame.draw.rect(win,colour,(x+4*w,(y+4*h),w,h))
    pygame.draw.rect(win,colour,(x+5*w,(y+4*h),w,h))
    pygame.draw.rect(win,colour,(x+6*w,(y+4*h),w,h))
    pygame.draw.rect(win,colour,(x+7*w,(y+4*h),w,h))
    pygame.draw.rect(win,colour,(x+8*w,(y+4*h),w,h))
    
    #Line Six
    pygame.draw.rect(win,colour,(x-2*w,(y+5*h),w,h))
    
    pygame.draw.rect(win,colour,(x,(y+5*h),w,h))
    pygame.draw.rect(win,colour,(x+w,(y+5*h),w,h))
    pygame.draw.rect(win,colour,(x+2*w,(y+5*h),w,h))
    pygame.draw.rect(win,colour,(x+3*w,(y+5*h),w,h))
    pygame.draw.rect(win,colour,(x+4*w,(y+5*h),w,h))
    pygame.draw.rect(win,colour,(x+5*w,(y+5*h),w,h))
    pygame.draw.rect(win,colour,(x+6*w,(y+5*h),w,h))
    
    
    pygame.draw.rect(win,colour,(x+8*w,(y+5*h),w,h))
    #Line Seven
    pygame.draw.rect(win,colour,(x-2*w,(y+6*h),w,h))
    
    pygame.draw.rect(win,colour,(x,(y+6*h),w,h))
    
    pygame.draw.rect(win,colour,(x+6*w,(y+6*h),w,h))
    
    pygame.draw.rect(win,colour,(x+8*w,(y+6*h),w,h))

    #Line 8
    
    pygame.draw.rect(win,colour,(x+1*w,(y+7*h),w,h))
    pygame.draw.rect(win,colour,(x+2*w,(y+7*h),w,h))
    pygame.draw.rect(win,colour,(x+4*w,(y+7*h),w,h))
    pygame.draw.rect(win,colour,(x+5*w,(y+7*h),w,h))

    
    pygame.display.update()

red = (255,0,0)

m(0,0,50,50,red)


    
