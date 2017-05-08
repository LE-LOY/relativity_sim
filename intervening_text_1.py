import pygame, thorpy
from relativity import Environment


content= """
        Simulation of the train as it travels along the x-dimension
        as viewed from it's reference frame
    """
subcontent = """
        <notes:>
        <make 6 more of these>
        <add more text/instructions>
        <change event listener in this file
        (mouseclick --> keypress) >

        f1 = show transformation
        space = pause
        esc = main menu
        left arrow key = back
        <Click to continue>
        """
class Text(object):
        

    def __init__(self):
        def start_sim(event):
            self.sim()
            ##Change this reaction to KeyPress > Right Arrow Key
        my_reaction = thorpy.Reaction(reacts_to=pygame.MOUSEBUTTONDOWN,
                                      reac_func=start_sim)
        title_element = thorpy.make_text(content, 25, (255, 255, 255))
        title_element.set_font("Arial")
        instruct_element = thorpy.make_text(subcontent, 15, (255,255,255))
        
        self.e_background = thorpy.Background.make( color = (0, 0, 0), elements = [title_element, instruct_element])                                            
        self.e_background.add_reaction(my_reaction)
        thorpy.store(self.e_background, gap = 20)
    
    
    def sim(self):
        env = Environment(self, sim_type='stationary_train', light_type='einstein')
        env.run()


            
    def display_text(self):
        menu = thorpy.Menu(self.e_background)
        menu.play()

    
