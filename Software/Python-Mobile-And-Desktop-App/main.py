import firebase_admin
from firebase_admin import credentials, db
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivy.lang import Builder
from kivy.core.audio import SoundLoader
from kivymd.uix.label import MDLabel
from kivymd.uix.button import MDRectangleFlatButton, MDIconButton
from kivy.core.window import Window

# UI Layout for the branding image
IMAGE_KV = '''
Image:
    source: './AF.png'
    pos_hint: {'center_x': 0.5, 'center_y': 0.3}
    size_hint: (0.8, 0.8)
'''

class MySmartHomeApp(MDApp):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        # Firebase reference placeholder
        self.db_ref = None
        
    def setup_firebase(self):
        """Initializes Firebase connection using credentials file"""
        try:
            # IMPORTANT: Replace 'serviceAccountKey.json' with your local file path
            # DO NOT upload your actual JSON key file to GitHub!
            cred = credentials.Certificate("path/to/your/serviceAccountKey.json")
            firebase_admin.initialize_app(cred, {
                'databaseURL': 'https://your-project-id.firebaseio.com/'
            })
            self.db_ref = db.reference('relays')
            print("Firebase initialized successfully.")
        except Exception as e:
            print(f"Firebase Init Error: {e}")

    def build(self):
        # Window configuration
        Window.size = (400, 630)
        self.title = 'Smart Home Controller'
        self.theme_cls.primary_palette = "LightBlue"
        self.theme_cls.theme_style = "Dark"

        # Initialize Firebase inside the class
        self.setup_firebase()

        # Load Welcome Sound
        sound = SoundLoader.load('./welcome_again_sir.mp3')
        if sound:
            sound.play()

        screen = Screen()

        # Branding Label
        lbl = MDLabel(
            text='ENG. Ahmed Fayez',
            halign='center',
            theme_text_color="Primary",
            font_style="H6",
            pos_hint={'center_x': 0.5, 'center_y': 0.05}
        )

        # UI Components - Buttons
        # We store buttons in a dictionary for easier access later
        self.buttons = {}
        
        # Define button configurations: (Text, Pos_Y, Icon_Path, DB_Key)
        btn_configs = [
            ("Lamp", 0.85, './lamp.png', 'Relay1'),
            ("Ceiling fan", 0.73, './ceiling_fan.png', 'Relay2'),
            ("LED test", 0.61, './LED.png', 'Test')
        ]

        for text, y_pos, icon_path, db_key in btn_configs:
            # Create the control button
            btn = MDRectangleFlatButton(
                text=text,
                pos_hint={'center_x': 0.5, 'center_y': y_pos},
                size_hint=(0.8, 0.1),
                on_release=lambda x, k=db_key: self.toggle_device(k)
            )
            
            # Create the decorative icon button
            icon_btn = MDIconButton(
                icon=icon_path,
                pos_hint={'center_x': 0.2, 'center_y': y_pos},
                icon_size=60
            )
            
            self.buttons[db_key] = btn
            screen.add_widget(btn)
            screen.add_widget(icon_btn)

        # Add remaining widgets
        screen.add_widget(Builder.load_string(IMAGE_KV))
        screen.add_widget(lbl)

        # Initial color update from Firebase
        self.update_ui_colors()
        
        return screen

    def toggle_device(self, key):
        """Toggles the state of a device in Firebase (0 to 1 or 1 to 0)"""
        if self.db_ref:
            current_data = self.db_ref.get()
            current_state = current_data.get(key, 0)
            new_state = 1 - current_state
            self.db_ref.update({key: new_state})
            self.update_ui_colors()

    def update_ui_colors(self):
        """Updates button border colors based on real-time database state"""
        if self.db_ref:
            data = self.db_ref.get()
            
            # Colors: Green for ON (1), Red for OFF (0)
            for db_key, button in self.buttons.items():
                state = data.get(db_key, 0)
                button.line_color = (0, 1, 0, 1) if state == 1 else (1, 0, 0, 1)

if __name__ == '__main__':
    MySmartHomeApp().run()