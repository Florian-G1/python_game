import pygame

# Création d'une classe qui s'occupera de gérer les scores à conserver.
class Highscore:

    def __init__(self, file):
        self.file_name = file
        self.read_file(self.file_name)
        self.new_highscore = False
        self.font = pygame.font.Font("assets/ubuntu.ttf", 24)
        self.highscore_font = pygame.font.Font("assets/ubuntu.ttf", 40)
        self.title_font = pygame.font.Font("assets/ubuntu.ttf", 50)

    def read_file(self, file_name):
        # Récupérer la liste de score enregistré
        with open(file_name, "r+") as file:
            self.highscore_list = file.read().splitlines()
            file.close()

    def new_score(self, score):
        # Ranger le nouveau score dans la liste et définir s'il s'agit du meilleur.
        self.current_score = 5
        self.new_highscore = False
        for i in range(0, len(self.highscore_list)):
            if score > int(self.highscore_list[i]):
                self.highscore_list.insert(i, score)
                self.current_score = i
                if i == 0:
                    self.new_highscore = True
                break
        # Ajout d'un score en dessous de ceux retenus
        if self.current_score == 5:
            self.highscore_list.append(score)

    def print(self, screen):
        # Affiche le contenu écrit du tableau des scores.
        score_title = self.title_font.render("Tableau des scores :", 1, (0, 0, 0), )
        screen.blit(score_title, (screen.get_width()/2-score_title.get_width()/2, 100))
        # Vérification d'un nouveau record.
        if self.new_highscore:
            highscore_text = self.highscore_font.render("Nouveau record !", 1, (0, 0, 0), )
            screen.blit(highscore_text, (screen.get_width()/2-highscore_text.get_width()/2, 200))
        for i in range(0, len(self.highscore_list)):
            if i == self.current_score:
                score_text = self.font.render(f"{i+1} : {self.highscore_list[i]}        Nouveau score !", 1, (0, 0, 0), )
                screen.blit(score_text, (200, 300 + i * 50))
            else:
                score_text = self.font.render(f"{i+1} : {self.highscore_list[i]}", 1, (0, 0, 0), )
                screen.blit(score_text, (200, 300 + i * 50))

    def clean(self):
        if len(self.highscore_list) > 4:
            for i in range(5, len(self.highscore_list)):
                self.highscore_list.pop(i)


    def save(self, file_name):
        with open(file_name, "w") as file:
            for i in range(0, len(self.highscore_list)):
                file.write(f"{self.highscore_list[i]}\n")
            file.close()
