from demoqa_tests.model.components.result_registered_user_dialog import ResultRegisteredUuserDalog
from demoqa_tests.model.pages.sudent_registration_page import StudentRegistrationPage


class Application_manager:
    registration_form = StudentRegistrationPage()
    resalt = ResultRegisteredUuserDalog()



app = Application_manager