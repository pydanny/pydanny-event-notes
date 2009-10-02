def test():
    assert True    
    
class TestClass(object):
    
    def setUp(self):
        'Sets up per test'
        pass
        
    def tearDown(self):
        'Tears down per test'        
        pass
        
    def test2(self):
        assert False
        
    def test(self):
        assert False