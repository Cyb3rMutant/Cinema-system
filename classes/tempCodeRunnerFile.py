
    def print_film(self, film):
        film = film.__dict__
        self.__film_label = tk.Label(self.__app.body_frame, text="\n".join(
            [f"{x.replace('_', ' ')}: {y}" for x, y in film.items()])).place(x=50, y=400)
