import pygame
import os
pygame.font.init()#esto inicializa la biblioteca de fuentes de juego de pygame

width,height= 900,500
pantalla= pygame.display.set_mode((width,height))
pygame.display.set_caption("Casals")
blanco=(255,255,255)
negro= (0 , 0 , 0)
rojo= (255, 0 ,0)
amarillo= (255,255,0)
BORDE = pygame.Rect(width//2 -5, 0 ,5, height)

vida_font = pygame.font.SysFont("Roboto" , 40)
fuente_ganador = pygame.font.SysFont("Roboto" , 100)

fps= 60
Vel= 5
balas_vel= 7
max_balas= 4
WARRIORS_WIDHT, WARRIORS_HEIGHT = 80,70
golpe_rony= pygame.USEREVENT + 1
golpe_cbum= pygame.USEREVENT + 2
imagen_1= pygame.image.load(r"C:\Users\BACO\Downloads\lar rocasss.jpg")
medidas_de_imagen=pygame.transform.scale(imagen_1,(80,70))
imagen_2=pygame.image.load(r"C:\Users\BACO\Downloads\Tibur%3Fn.webp")
medidas_imagen_2=pygame.transform.scale(imagen_2,(80,70))
fondo= pygame.image.load(r"C:\Users\BACO\Downloads\fondo.webp" )
medidas_fondo= pygame.transform.scale(fondo,(900,500))

def rony_movimiento(keys_pressed, rony):
    
    if keys_pressed[pygame.K_a] :
        rony.x -= Vel #Izquierda
    if keys_pressed[pygame.K_d] :
        rony.x += Vel #Derecha
    if keys_pressed[pygame.K_s] :
        rony.y += Vel #Abajo  
    if keys_pressed[pygame.K_w] :
        rony.y -= Vel #Arriba
        
def cbum_movimiento(keys_pressed, cbum):
    
    if keys_pressed[pygame.K_LEFT] :
        cbum.x -= Vel #Izquierda
    if keys_pressed[pygame.K_RIGHT] :
        cbum.x += Vel #Derecha
    if keys_pressed[pygame.K_DOWN] :
        cbum.y += Vel #Abajo  
    if keys_pressed[pygame.K_UP] :
        cbum.y -= Vel #Arriba
    
           
def draw_window(rony , cbum, balas_de_rony , balas_de_cbum, vida_cbum , vida_rony):
    pantalla.blit(medidas_fondo,(0,0))
    pygame.draw.rect(pantalla, negro , BORDE)
    
    vida_cbum_texto = vida_font.render("Vida: " + str(vida_cbum),  0, blanco)# str= secuencia de caracteres para representar un texto
    vida_rony_texto = vida_font.render("Vida: " + str(vida_rony), 0 , blanco)
    pantalla.blit(vida_cbum_texto,(width - vida_cbum_texto.get_width() - 10, 10))
    pantalla.blit(vida_rony_texto, (10, 10))
      
    pantalla.blit(medidas_de_imagen,(rony.x , rony.y))
    pantalla.blit(medidas_imagen_2,(cbum.x , cbum.y))
    
    for bala in balas_de_cbum:
        pygame.draw.rect(pantalla,rojo, bala)
    
    for bala in balas_de_rony:
        pygame.draw.rect(pantalla,amarillo, bala)
   
    pygame.display.update()

def movimiento_balas(balas_de_rony, balas_de_cbum, rony, cbum):
    for bala in balas_de_rony:
        bala.x += balas_vel
        if cbum.colliderect(bala):
            pygame.event.post(pygame.event.Event(golpe_cbum))
            balas_de_rony.remove(bala)
        elif bala.x > width:
            balas_de_rony.remove(bala)#si se pasa del borde x, remover
            
    for bala in balas_de_cbum:
        bala.x -= balas_vel
        if rony.colliderect(bala):
            pygame.event.post(pygame.event.Event(golpe_rony))
            balas_de_cbum.remove(bala)
        elif bala.x < 0:
            balas_de_cbum.remove(bala)
            
def dibuja_ganador(text):
    dibujar_text= fuente_ganador.render(text,1,blanco)#render=se usa para crear una imagen de texto que se puede dibujar en una superficie.
    pantalla.blit(dibujar_text, (width//2 - dibujar_text.get_width()//2, height//2 - dibujar_text.get_height()//2))
    pygame.display.update
    pygame.time.delay(200)


def main():
    rony= pygame.Rect(100,300, WARRIORS_WIDHT , WARRIORS_HEIGHT)
    cbum= pygame.Rect(700,300, WARRIORS_WIDHT , WARRIORS_HEIGHT)
    
    balas_de_rony= []
    balas_de_cbum= []
    
    vida_rony= 10
    vida_cbum= 10
    
    tiempo= pygame.time.Clock()
    run= True
    while run:
        tiempo.tick(fps)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run= False
            
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_d and len(balas_de_rony) < max_balas:#len=sirve para obtener el número de elementos que tiene un objeto iterable, como una lista.
                    bala = pygame.Rect(rony.x + rony.width, rony.y + rony.height//2 , 10,5)
                    balas_de_rony.append(bala)
                
                if event.key == pygame.K_LEFT and len(balas_de_cbum) < max_balas:
                    bala = pygame.Rect(cbum.x , cbum.y + cbum.height//2 , 10,5)#se le quita el cbum.widht porque quiero que salga de la izquierda, no de la derecha.
                    balas_de_cbum.append(bala)
                    
            if event.type == golpe_cbum:
                vida_cbum -= 1
            
            if event.type == golpe_rony:
                vida_rony -= 1
        
        texto_ganador = ""
        if vida_cbum <= 0:
            texto_ganador = "¡cbum a ganado! "
        
        if vida_rony <= 0:
            texto_ganador = "¡rony a ganado!"
        
        if texto_ganador != "":
            dibuja_ganador(texto_ganador)
            break
                
        keys_pressed = pygame.key.get_pressed()
        rony_movimiento(keys_pressed,rony) 
        cbum_movimiento(keys_pressed,cbum)
        movimiento_balas(balas_de_rony ,balas_de_cbum ,rony ,cbum )

        draw_window(rony,cbum,balas_de_rony,balas_de_cbum , vida_cbum , vida_rony)
                
    pygame.quit()
if __name__=="__main__":
    main()# se asegura que lo vamos a ejecutar desde la funcion desde el principal


    
