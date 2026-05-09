import os
from kivy.app import App
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

DOSSIER_JEU = os.path.dirname(os.path.abspath(__file__))

class RestaurantApp(App):
    def build(self):
            self.score = 0
                    self.plat_actuel = "pizza" # On commence avec la pizza

                                    self.layout = BoxLayout(orientation='vertical', padding=20, spacing=10)

                                            # Titre
                                                    self.label_titre = Label(text="Menu : Pizza", font_size='30sp', size_hint_y=0.1)
                                                            self.layout.add_widget(self.label_titre)

                                                                    # Image
                                                                            self.chemin_pizza = os.path.join(DOSSIER_JEU, "pizza.png")
                                                                                    self.chemin_burger = os.path.join(DOSSIER_JEU, "burger.png") # Assure-toi d'avoir cette image !

                                                                                                    self.image_plat = Image(source=self.chemin_pizza, size_hint_y=0.5)
                                                                                                            self.layout.add_widget(self.image_plat)

                                                                                                                    # Bouton pour CHANGER de plat
                                                                                                                            self.btn_change = Button(text="Changer de plat", size_hint_y=0.1, background_color=(0.2, 0.2, 0.8, 1))
                                                                                                                                    self.btn_change.bind(on_press=self.basculer_plat)
                                                                                                                                            self.layout.add_widget(self.btn_change)

                                                                                                                                                    # Bouton pour VENDRE
                                                                                                                                                            self.btn_vendre = Button(text="Vendre !", size_hint_y=0.2, background_color=(0.2, 0.8, 0.2, 1))
                                                                                                                                                                    self.btn_vendre.bind(on_press=self.vendre_plat)
                                                                                                                                                                            self.layout.add_widget(self.btn_vendre)

                                                                                                                                                                                    # Score
                                                                                                                                                                                            self.label_score = Label(text="Ventes : 0", size_hint_y=0.1)
                                                                                                                                                                                                    self.layout.add_widget(self.label_score)

                                                                                                                                                                                                            return self.layout

                                                                                                                                                                                                                def basculer_plat(self, instance):
                                                                                                                                                                                                                        # Logique de bascule : si c'est pizza -> burger, sinon -> pizza
                                                                                                                                                                                                                                if self.plat_actuel == "pizza":
                                                                                                                                                                                                                                            self.plat_actuel = "burger"
                                                                                                                                                                                                                                                        self.image_plat.source = self.chemin_burger
                                                                                                                                                                                                                                                                    self.label_titre.text = "Menu : Burger"
                                                                                                                                                                                                                                                                            else:
                                                                                                                                                                                                                                                                                        self.plat_actuel = "pizza"
                                                                                                                                                                                                                                                                                                    self.image_plat.source = self.chemin_pizza
                                                                                                                                                                                                                                                                                                                self.label_titre.text = "Menu : Pizza"

                                                                                                                                                                                                                                                                                                                    def vendre_plat(self, instance):
                                                                                                                                                                                                                                                                                                                            self.score += 1
                                                                                                                                                                                                                                                                                                                                    self.label_score.text = f"Ventes : {self.score}"

                                                                                                                                                                                                                                                                                                                                    if __name__ == "__main__":
                                                                                                                                                                                                                                                                                                                                        RestaurantApp().run()
                                                                                                                                                                                                                                                                                                                                        
