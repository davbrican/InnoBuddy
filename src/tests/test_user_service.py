import os
import sys
import inspect
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(os.path.dirname(currentdir)+"/services")
import user_service
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
sys.path.append(os.path.dirname(currentdir)+"/../db")

## Necesita popular después de ejecutar estas pruebas, afectan directamente al contenido de la base de datos
## Correrlas dos veces seguidas sin popular conlleva el fallo de varias pruebas en la segunda ejecución
class Test:
    
    @classmethod
    def teardown_class(cls):
        import populate
        
    def test_find_user_by_id(self):
        assert user_service.find_user_by_id(267547511) == (267547511,'alumno')

    def test_find_all_users(self):
        assert user_service.find_all_users() == [(123131313, 'admin'), (207767757, 'alumno'), (267547511, 'alumno'), (686981968, 'alumno')]

    def test_add_user(self):
        assert user_service.find_user_by_id(123456789) == None
        user_service.add_user(123456789)
        assert user_service.find_user_by_id(123456789) == (123456789,'alumno')

    def test_add_user_if_new(self):
        assert user_service.find_user_by_id(123456788) == None
        user_service.add_user_if_new(123456788)
        assert user_service.find_user_by_id(123456788) == (123456788,'alumno')

    def test_is_admin_true(self):
        assert user_service.is_admin(123131313) == True

    def test_is_admin_false(self):
        assert user_service.is_admin(267547511) == False

    def test_upgrade_user(self):
        assert user_service.find_user_by_id(267547511)[1] == 'alumno'
        user_service.upgrade_user(267547511)
        assert user_service.find_user_by_id(267547511)[1] == 'admin'
        
    def test_get_recordatorios(self):
        assert user_service.get_recordatorios("483048011")[0][1] == "206188845387"
        
    def test_insert_recordatorios(self):
        assert len(user_service.get_recordatorios("483048011")) == 1
        user_service.insert_recordatorio("483048011", "205203869297")
        assert len(user_service.get_recordatorios("483048011")) == 2
        