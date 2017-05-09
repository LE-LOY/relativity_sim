import thorpy, intervening_text_1

def setProperties(simButton):
    simButton.set_main_color((255,255,255))
    simButton.set_font_color_hover((255, 0, 0))
    simButton.set_font_size(23)
    simButton.set_size((200,50))
    simButton.set_font('Calibri')



class Menu:
    def run(self):
        ###
        application = thorpy.Application(size=(640, 640), caption="Relativity Simulation")    

        #make buttons
        simButton1 = thorpy.make_button("Einstein1", func = self.sim1)

    
        #separate properties for quitButton
        quitButton = thorpy.make_button("Quit", func=thorpy.functions.quit_menu_func)
        quitButton.set_main_color((255,255,255))
        quitButton.set_font_color_hover((255, 0, 0))
        quitButton.set_font_size(20)
        quitButton.set_size((200,50))
        quitButton.set_font('Calibri')

                                             
        #set button properties
        setProperties(simButton1)
        setProperties(quitButton)


        # add help/descriptions
        """
        thorpy.makeup.add_basic_help(simButton1,"insert description here")
        thorpy.makeup.add_basic_help(simButton2,"insert description here")
        """


        #set button text
        simButton1.set_text("  Start  ")
        quitButton.set_text("  Exit  ")


        #put buttons in box
        Elem = [simButton1, quitButton]
        central_box = thorpy.Box.make(elements = Elem)
        central_box.fit_children(margins=(20,20))
        central_box.center()

        central_box.set_main_color((220, 220, 220, 180))

        #make title
        title_element = thorpy.make_text("Relativity Simulation\n", 60, (0,0,0))
        title_element.set_font('Jokerman')
        title_element.center()
                    
        #set background
        background = thorpy.Background.make(color=(200, 200, 255),
                                            elements=[title_element, central_box])
        thorpy.store(background)

        #menu event handling
        menu = thorpy.Menu(background) 
        menu.play()

        application.quit()

    ####
    
    def sim1(self):
        x = intervening_text_1.Text()
        x.display_text()

        
        
if __name__ == '__main__':
    my_menu = Menu()
    my_menu.run()
