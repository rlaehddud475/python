
import tkinter as tk


class DistanceView(tk.Frame):
    def __init__(self, master):
        super().__init__(master)
        self.pack(padx=15, pady=15)

        self.ent = tk.Entry(self, width=15)
        self.ent.grid(row=0, column=0, columnspan=2, pady=5)

        self.km_btn = tk.Button(self, text="km → 마일")
        self.km_btn.grid(row=1, column=0, padx=2)

        self.mile_btn = tk.Button(self, text="마일 → km")
        self.mile_btn.grid(row=1, column=1, padx=2)

        self.lbl = tk.Label(self, text="값을 입력하세요", width=25)
        self.lbl.grid(row=2, column=0, columnspan=2, pady=10)

    def get_input(self):
        return self.ent.get()

    def show_result(self, text):
        self.lbl.config(text=text)

class DistanceModel:
    KM_PER_MILE = 1.609344

    def km_to_miles(self, km):
        return km / self.KM_PER_MILE

    def miles_to_km(self, miles):
        return miles * self.KM_PER_MILE

class DistancePresenter:
    def __init__(self, model, view):
        self.model = model
        self.view = view

        self.view.km_btn.config(command=self.on_km_to_miles)
        self.view.mile_btn.config(command=self.on_miles_to_km)

    def _read_value(self):
        """입력값을 숫자로 변환. 실패하면 None과 함께 안내."""
        try:
            return float(self.view.get_input())
        except ValueError:
            self.view.show_result("숫자를 입력하세요")
            return None

    def on_km_to_miles(self):
        value = self._read_value()
        if value is not None:
            miles = self.model.km_to_miles(value)
            self.view.show_result(f"{value} km = {miles:.2f} 마일")

    def on_miles_to_km(self):
        value = self._read_value()
        if value is not None:
            km = self.model.miles_to_km(value)
            self.view.show_result(f"{value} 마일 = {km:.2f} km")
if __name__ == "__main__":
    root = tk.Tk()
    presenter = DistancePresenter(DistanceModel(), DistanceView(root))
    root.mainloop()