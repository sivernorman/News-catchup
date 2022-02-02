from app.models import Articles
class ArticlesTest:
    '''
    method to test articles
    '''

    def setUp(self):
        self.new_article = Articles(123,'Silver', 'Norman','nourl','url')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_article))