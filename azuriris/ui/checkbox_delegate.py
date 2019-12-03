from PySide2 import QtCore, QtWidgets


class CheckBoxDelegate(QtWidgets.QItemDelegate):
    def __init__(self, parent):
        QtWidgets.QItemDelegate.__init__(self, parent)

    def createEditor(self, parent, option, index):
        """
        Overrided method to disallow creation of an editor on double click
        """
        return None

    def paint(self, painter, option, index):
        """
        Paint a checkbox without the label.
        """
        self.drawCheck(
            painter, option, option.rect,
            QtCore.Qt.Unchecked if not index.data() else QtCore.Qt.Checked)

    def editorEvent(self, event, model, option, index):
        """
        Change the data in the model and the state of the checkbox
        if the user presses the left mousebutton and this cell is editable
        """

        if not int(index.flags() & QtCore.Qt.ItemIsEditable) > 0:
            return False

        if (event.type() == QtCore.QEvent.MouseButtonPress and
                event.button() == QtCore.Qt.LeftButton):
            self.setModelData(None, model, index)
            return True
        return False

    def setModelData(self, editor, model, index):
        model.setData(index, not index.data(), QtCore.Qt.EditRole)
