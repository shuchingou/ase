from __future__ import unicode_literals
import ase.gui.ui as ui
from ase.gui.i18n import _


class Constraints:
    def __init__(self, gui):
        win = ui.Window(_('Constraints'))
        win.add([ui.Button(_('Constrain'), self.selected),
                 _('selected atoms')])
        win.add([ui.Button(_('Constrain'), self.immobile),
                 _('immobile atoms')])
        win.add([ui.Button(_('Unconstrain'), self.unconstrain),
                 _('selected atoms')])
        win.add(ui.Button(_('Clear constraints'), self.clear))
        self.gui = gui

    def selected(self):
        self.gui.images.set_dynamic(self.gui.images.selected, False)
        #self.gui.images.dynamic[self.gui.images.selected] = False
        self.gui.draw()

    def unconstrain(self):
        self.gui.images.set_dynamic(self.gui.images.selected, True)
        #self.gui.images.dynamic[self.gui.images.selected] = True
        self.gui.draw()

    def immobile(self):
        #self.gui.images.set_dynamic()
        self.gui.draw()

    def clear(self):
        # This clears *all* constraints.  But when we constrain, we
        # only add FixAtoms....
        for atoms in self.gui.images:
            atoms.set_constraints([])

        # Also, these methods are repeated from settings.py *grumble*
        #self.gui.images.dynamic[:] = True
        self.gui.draw()
