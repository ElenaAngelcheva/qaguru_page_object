from selene import have
from selene.support.shared import browser

from demoqa_tests.model.controls.table import Table


class ResultRegisteredUuserDalog:
    def __init__(self):
        self.element = browser.element('.modal-dialog')
        self.table = Table(self.element.element('.table'))

    def sould_have_row_with_exact_texst(self, row, *values):
        self.table.cells_of_row(row).should(have.exact_texts(*values))
