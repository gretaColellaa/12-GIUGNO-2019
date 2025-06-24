import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_grafo(self, e):
        try: float(self._view.txt_cal.value)
        except: self._view.create_alert("Inserire un numero valido")

        self._model.crea_grafo(float(self._view.txt_cal.value))
        self._view.txt_result.controls.append(ft.Text(f"il grafo ha {self._model.getNumNodes()} nodi"
                                                      f" e {self._model.getNumEdges()} archi"))

        food = self._model.getFood()
        food_ordinati = sorted(food, key=lambda x:x.calories, reverse=True)
        for f in food_ordinati:
            self._view.txt_result.controls.append(ft.Text(f"{str(f)}. {self._model.getFoodData(f)}"))

            self._view.update_page()

    def handle_dieta(self, e):
        pass
