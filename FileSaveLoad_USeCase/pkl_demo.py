import pickle

class TestClass:
    def __init__(self, a: int, b_lt: list):
        self.a = a
        self.b_lt = b_lt

        self.test_fun1()

    def test_fun1(self):
        for i in range(10):
            self.b_lt.append(i)

class ObjPickleSaveLoad:
    """
    object svae or load by pickle
    """

    def __init__(self, file_name: str, obj_type = None):
        """
        Args:
            file_name(str): the filename we want to save or load
            obj_type: I will check obj_type if it is not None
        """

        self.file_name = file_name
        self.obj_type = obj_type


    def obj_save(self, my_obj):
        """
        svae the my_obj into a file
        
        Args:
            my_obj: the object we want to save

        Returns:
            True/False: return True if we successfully save the object, otherwise return Flase
        """

        if self.obj_type and type(my_obj) != self.obj_type:
            return False

        try:
            fp = open(self.file_name, 'wb')
            pickle.dump(my_obj, fp)
            fp.close()
            return True
        except:
            return False


    def obj_load(self):
        """
        load a object from a file
        
        Returns:
            my_obj/False: return my_obj if we successfully load the object, otherwise return Flase
        """

        try:
            fp = open(self.file_name, 'rb')
            my_obj = pickle.load(fp)
            fp.close()
            if self.obj_type and type(my_obj) != self.obj_type:
                return None
            return my_obj
        except:
            return None


if __name__ == "__main__":
    #test_obj = TestClass(999, ['a','b'])
    #print(test_obj, test_obj.a, test_obj.b_lt)

    #obj_pkl_sl_obj = ObjPickleSaveLoad('test1.pkl', TestClass)

    #rv = obj_pkl_sl_obj.obj_save(my_obj=test_obj)
    #print(rv)

    obj_pkl_sl_obj2 = ObjPickleSaveLoad('test1.pkl', TestClass)
    my_obj = obj_pkl_sl_obj2.obj_load()
    print(my_obj)
    if my_obj:
        print(my_obj, my_obj.a, my_obj.b_lt)

    pass

