#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#
# generated by wxGlade 1.0.5 on Sat May 11 11:27:46 2024
#

import wx

# begin wxGlade: dependencies
# end wxGlade

# begin wxGlade: extracode
# end wxGlade


class nueva_partida(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: nueva_partida.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((403, 175))
        self.SetTitle("Nueva partida")

        self.nueva_partida = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(sizer_2, 0, wx.EXPAND, 0)

        elegir_apuesta = wx.StaticBoxSizer(wx.StaticBox(self.nueva_partida, wx.ID_ANY, "Elija apuesta"), wx.VERTICAL)
        sizer_2.Add(elegir_apuesta, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        self.apuesta_dos = wx.RadioButton(self.nueva_partida, wx.ID_ANY, u"2€")
        elegir_apuesta.Add(self.apuesta_dos, 0, 0, 0)

        self.apuesta_diez = wx.RadioButton(self.nueva_partida, wx.ID_ANY, u"10€")
        elegir_apuesta.Add(self.apuesta_diez, 0, 0, 0)

        self.apuesta_cincuent = wx.RadioButton(self.nueva_partida, wx.ID_ANY, u"50€")
        elegir_apuesta.Add(self.apuesta_cincuent, 0, 0, 0)

        text_cont_jug = wx.StaticText(self.nueva_partida, wx.ID_ANY, u"¿Quiere seguir jugando?")
        sizer_2.Add(text_cont_jug, 0, 0, 0)

        op_cont_juego = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(op_cont_juego, 0, wx.ALIGN_RIGHT, 0)

        self.boton_si = wx.Button(self.nueva_partida, wx.ID_ANY, u"Sí")
        op_cont_juego.Add(self.boton_si, 0, 0, 0)

        self.boton_no = wx.Button(self.nueva_partida, wx.ID_ANY, "No")
        op_cont_juego.Add(self.boton_no, 0, 0, 0)

        self.nueva_partida.SetSizer(sizer_1)

        self.Layout()
        # end wxGlade

# end of class nueva_partida

class desarrollo(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: desarrollo.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((691, 538))
        self.SetTitle(u"Blackjack - Paradigmas de Programación 2024")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)
        self.panel_1.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_2 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)

        variables_juego = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(variables_juego, 1, wx.EXPAND, 0)

        modo_juego = wx.StaticBoxSizer(wx.StaticBox(self.panel_1, wx.ID_ANY, "Modo juego"), wx.HORIZONTAL)
        variables_juego.Add(modo_juego, 1, wx.EXPAND, 0)

        self.boton_manual = wx.RadioButton(self.panel_1, wx.ID_ANY, "Manual")
        self.boton_manual.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        modo_juego.Add(self.boton_manual, 0, 0, 0)

        self.boton_auto = wx.RadioButton(self.panel_1, wx.ID_ANY, u"Automático")
        self.boton_auto.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        modo_juego.Add(self.boton_auto, 0, 0, 0)

        retardo = wx.BoxSizer(wx.HORIZONTAL)
        variables_juego.Add(retardo, 0, wx.EXPAND, 0)

        label_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "Retardo:")
        label_1.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        retardo.Add(label_1, 0, 0, 0)

        self.text_ctrl_1 = wx.TextCtrl(self.panel_1, wx.ID_ANY, "")
        self.text_ctrl_1.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        retardo.Add(self.text_ctrl_1, 0, 0, 0)

        label_2 = wx.StaticText(self.panel_1, wx.ID_ANY, "ms.")
        label_2.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        retardo.Add(label_2, 0, 0, 0)

        accion = wx.StaticBoxSizer(wx.StaticBox(self.panel_1, wx.ID_ANY, u"Acción"), wx.VERTICAL)
        variables_juego.Add(accion, 0, wx.EXPAND, 0)

        self.boton_pedir = wx.Button(self.panel_1, wx.ID_ANY, "Pedir")
        self.boton_pedir.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        accion.Add(self.boton_pedir, 0, wx.EXPAND, 0)

        self.boton_doblar = wx.Button(self.panel_1, wx.ID_ANY, "Doblar")
        self.boton_doblar.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        accion.Add(self.boton_doblar, 0, wx.EXPAND, 0)

        self.boton_cerrar = wx.Button(self.panel_1, wx.ID_ANY, "Cerrar")
        self.boton_cerrar.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        accion.Add(self.boton_cerrar, 0, wx.EXPAND, 0)

        self.boton_separar = wx.Button(self.panel_1, wx.ID_ANY, "Separar")
        self.boton_separar.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        accion.Add(self.boton_separar, 0, wx.EXPAND, 0)

        partida = wx.StaticBoxSizer(wx.StaticBox(self.panel_1, wx.ID_ANY, "Partida"), wx.VERTICAL)
        variables_juego.Add(partida, 0, wx.EXPAND, 0)

        num_partida = wx.StaticText(self.panel_1, wx.ID_ANY, "0")
        num_partida.SetFont(wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        partida.Add(num_partida, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        balance_global = wx.StaticBoxSizer(wx.StaticBox(self.panel_1, wx.ID_ANY, "Balance global"), wx.VERTICAL)
        variables_juego.Add(balance_global, 0, wx.EXPAND, 0)

        num_balancet = wx.StaticText(self.panel_1, wx.ID_ANY, "0")
        num_balancet.SetFont(wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        balance_global.Add(num_balancet, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        balance_actual = wx.StaticBoxSizer(wx.StaticBox(self.panel_1, wx.ID_ANY, "Balance partida actual"), wx.VERTICAL)
        variables_juego.Add(balance_actual, 0, wx.EXPAND, 0)

        num_balancet_copy = wx.StaticText(self.panel_1, wx.ID_ANY, "0")
        num_balancet_copy.SetFont(wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        balance_actual.Add(num_balancet_copy, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        cuenta_atras = wx.StaticBoxSizer(wx.StaticBox(self.panel_1, wx.ID_ANY, u"Cuenta atrás"), wx.VERTICAL)
        variables_juego.Add(cuenta_atras, 1, wx.EXPAND, 0)

        num_balancet_copy_1 = wx.StaticText(self.panel_1, wx.ID_ANY, "10")
        num_balancet_copy_1.SetFont(wx.Font(18, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        cuenta_atras.Add(num_balancet_copy_1, 0, wx.ALIGN_CENTER_HORIZONTAL, 0)

        sizer_3 = wx.BoxSizer(wx.VERTICAL)
        sizer_2.Add(sizer_3, 1, wx.EXPAND, 0)

        sizer_4 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(sizer_4, 1, wx.EXPAND, 0)

        sizer_4.Add((0, 0), 0, 0, 0)

        self.manos_jugador = wx.ScrolledWindow(self.panel_1, wx.ID_ANY, style=wx.TAB_TRAVERSAL)
        self.manos_jugador.SetScrollRate(10, 10)
        sizer_3.Add(self.manos_jugador, 1, wx.EXPAND, 0)

        label_3 = wx.StaticText(self.panel_1, wx.ID_ANY, "Seleccione jugada")
        label_3.SetFont(wx.Font(9, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_NORMAL, 0, "Segoe UI"))
        sizer_1.Add(label_3, 0, 0, 0)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()
        # end wxGlade

# end of class desarrollo

class Blackjack(wx.Frame):
    def __init__(self, *args, **kwds):
        # begin wxGlade: Blackjack.__init__
        kwds["style"] = kwds.get("style", 0) | wx.DEFAULT_FRAME_STYLE
        wx.Frame.__init__(self, *args, **kwds)
        self.SetSize((466, 365))
        self.SetTitle("Ha conseguido Blackjack!")

        self.panel_1 = wx.Panel(self, wx.ID_ANY)

        sizer_1 = wx.BoxSizer(wx.VERTICAL)

        sizer_2 = wx.BoxSizer(wx.VERTICAL)
        sizer_1.Add(sizer_2, 1, wx.EXPAND, 0)

        bitmap_1 = wx.StaticBitmap(self.panel_1, wx.ID_ANY, wx.Bitmap("C:\\Users\\sofia\\OneDrive\\Documentos\\PAR\\práctica2\\secondary-thumb2x.jpg", wx.BITMAP_TYPE_ANY))
        sizer_2.Add(bitmap_1, 0, 0, 0)

        sizer_3 = wx.BoxSizer(wx.HORIZONTAL)
        sizer_2.Add(sizer_3, 0, wx.EXPAND, 0)

        etiq1_blackjack = wx.StaticText(self.panel_1, wx.ID_ANY, "Ha ganado ")
        sizer_3.Add(etiq1_blackjack, 0, 0, 0)

        dinero_acumulado = wx.BoxSizer(wx.HORIZONTAL)
        sizer_3.Add(dinero_acumulado, 0, wx.EXPAND, 0)

        valorg_blackjack = wx.StaticText(self.panel_1, wx.ID_ANY, "0")
        dinero_acumulado.Add(valorg_blackjack, 0, 0, 0)

        etiq2_blackjack = wx.StaticText(self.panel_1, wx.ID_ANY, u"€!")
        sizer_3.Add(etiq2_blackjack, 0, 0, 0)

        self.boton_ok = wx.Button(self.panel_1, wx.ID_ANY, "OK")
        sizer_3.Add(self.boton_ok, 0, 0, 0)

        self.panel_1.SetSizer(sizer_1)

        self.Layout()
        # end wxGlade

# end of class Blackjack

class MyApp(wx.App):
    def OnInit(self):
        self.frame = nueva_partida(None, wx.ID_ANY, "")
        self.SetTopWindow(self.frame)
        self.frame.Show()
        return True

# end of class MyApp

if __name__ == "__main__":
    app = MyApp(0)
    app.MainLoop()
