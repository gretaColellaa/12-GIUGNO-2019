import flet as ft


class Controller:
    def __init__(self, view, model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model

    def handle_ingredienti(self, e):
       calorie= self._view.txtcalorie.value
       if calorie=="":
           self._view.create_alert("Inserire un numero di calorie")
           return
       grafo = self._model.creaGrafo(int(calorie))
       self._view.txt_result.controls.append(ft.Text("Grafo correttamente creato."))
       self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                     f"{self._model.getNumNodes()} nodi."))
       self._view.txt_result.controls.append(ft.Text(f"Il grafo contiene "
                                                     f"{self._model.getNumEdges()} archi."))
       lista=self._model.analisimetodo()
       for elemento in lista:
           self._view.ddingredienti.options.append(ft.dropdown.Option(f"{elemento[0]}"))
           self._view.txt_result.controls.append(ft.Text(f"L'ingrediente {elemento[0]} ha {elemento[1]} calorie ed è presente in {elemento[2]} ingredienti"))
       self._view.update_page()

    def handle_dieta(self, e):
        ingrediente=self._view.ddingredienti.value
        if ingrediente is None:
            self._view.create_alert("Selezionare un ingrediente")
            return
        soluzione,peso = self._model.getBestPath(ingrediente)
        self._view.txt_result.controls.append(ft.Text(f"Il massimo numero di calorie individuato è {peso} ed include i seguenti ingredienti:"))
        for elemento in soluzione:
            self._view.txt_result.controls.append(ft.Text( f"{elemento}"))
        self._view.update_page()
