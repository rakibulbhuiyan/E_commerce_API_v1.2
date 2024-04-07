import pytest
pytestmark=pytest.mark.django_db

class TestCategoryModel:
    def test_str_method(self,category_factory):
        #   Arrange---> Act-----> Assert.
        obj=category_factory(name="test_cat")
        assert obj.__str__()=="test_cat"



class TestBrandModel:
    def test_str_method(self,brand_factory):
        #   Arrange---> Act-----> Assert.
        x=brand_factory(name="test_brand")
        assert x.__str__()=="test_brand"


class TestProductModel:
    def test_str_method(self,product_factory):
        #   Arrange---> Act-----> Assert.
        qry=product_factory(name="test_prod")
        assert qry.__str__()=="test_prod"