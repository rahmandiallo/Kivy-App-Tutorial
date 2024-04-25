from kivy.app import App
from kivy.uix.widget import Widget
from kivy.metrics import dp
from kivy.properties import StringProperty
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.stacklayout import StackLayout
from kivy.uix.gridlayout import GridLayout

class WidgetsExample(GridLayout):
    count = 1
    count_string = str(count)
    my_text = StringProperty(count_string)
    def on_button_click(self):
        self.my_text = str(self.count + 1)
        self.count += 1
        print("Button Clicked")
    
    def on_toggle_button_state(self,widget):
        print("toggle state" + widget.state)
        if widget.state == " normal":
            widget.text = "OFF"
        else:
            widget.text = "ON"    

class StackLayoutExample(StackLayout):
    def __init__(self,**kwargs):
        super().__init__(**kwargs)
        # self.orientation = "lr-bt"
        
        for i in range(0,50):
            b = Button(text = str(i + 1),size_hint=(None, None),size=(dp(100),dp(100)))
            self.add_widget(b)
    pass



class BoxLayoutExample(BoxLayout):
    pass
    # **kwargs allows us to pass a variable 
    # keyword arguments to a python function
"""    def __init__(self,**kwargs):
        super().__init__(**kwargs)

        self.orientation = "vertical"

        b1 = Button(text = 'A') 
        b2 = Button(text = 'B')
        b3 = Button(text = 'C') 

        self.add_widget(b2)
        self.add_widget(b1) 
        self.add_widget(b3)
"""

class MainWidget(Widget):
    pass


class TheLabApp(App):
    pass

TheLabApp().run()