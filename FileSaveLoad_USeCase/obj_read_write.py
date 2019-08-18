import dill

class ObjReadWrite:
    """
    object save or load by pickle
    """

    @classmethod
    def svae_obj(cls, my_obj, file_name: str, obj_type = None):
        """
        svae the my_obj into a file
        
        Args:
            my_obj: the object we want to save
            file_name(str): the filename we want to save or load
            obj_type: I will check obj_type if it is not None

        Returns:
            True / False: return True if we successfully save the object, otherwise return Flase
        """

        if obj_type != None and type(my_obj) != obj_type:
            return False

        try:
            fp = open(file_name, 'wb')
            dill.dump(obj=my_obj, file=fp)
            fp.close()
            return True
        except:
            return False

    @classmethod
    def load_obj(cls, file_name: str, obj_type = None):
        """
        load an object from a file

        Args:
            file_name(str): the filename we want to save or load
            obj_type: I will check obj_type if it is not None

        Returns:
            my_obj / None: return my_obj if we successfully load an object from a file, 
                           otherwise return None
        """

        try:
            fp = open(file_name, 'rb')
            my_obj = dill.load(file=fp)
            fp.close()
            if obj_type != None and type(my_obj) != obj_type:
                return None
            return my_obj
        except:
            return None


class TestClass:
    def __init__(self, a, b):
        self.a = a
        self.b = b
    
    def fun(self):
        self.a += 2
        self.b = self.b**2


def test_ob_read_write():
    import os
    crt_file_path = os.path.normpath(os.path.abspath(__file__))
    crt_folder_path = os.path.normpath(os.path.dirname(crt_file_path))
    data_folder_path = os.path.join(crt_folder_path, 'data')
    if not os.path.isdir(data_folder_path):
        os.makedirs(data_folder_path)

    module_file_name = os.path.join(data_folder_path, 'test.dill')
    
    test_obj = TestClass(2, 3)
    test_obj.fun()

    res = ObjReadWrite.svae_obj(my_obj=test_obj, file_name=module_file_name, obj_type=TestClass)
    assert res == True

    load_obj = ObjReadWrite.load_obj(file_name=module_file_name, obj_type=TestClass)
    assert load_obj is not None
    assert load_obj.a == test_obj.a
    assert load_obj.b == test_obj.b


if __name__ == "__main__":
    test_ob_read_write()
