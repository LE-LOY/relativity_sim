import pygame, thorpy
import Gooey

content= """
        END OF SIMULATION
    """
subcontent = """

        Left Click - Main Menu
        """
class Text(object):
        

    def __init__(self):
        def start_sim(event):
            self.sim()
        my_reaction = thorpy.Reaction(reacts_to=pygame.MOUSEBUTTONDOWN,
                                      reac_func=start_sim)
        title_element = thorpy.make_text(content, 25, (255, 255, 255))
        title_element.set_font("Arial")
        instruct_element = thorpy.make_text(subcontent, 15, (255,255,255))
        
        self.e_background = thorpy.Background.make( color = (0, 0, 0), elements = [title_element, instruct_element])                                            
        self.e_background.add_reaction(my_reaction)
        thorpy.store(self.e_background, gap = 20)
    
    
    def sim(self):
        x= Gooey.Menu()
        x.run()


            
    def display_text(self):
        menu = thorpy.Menu(self.e_background)
        menu.play()

    
