from create_video_list import CreateVideoList
from update_videos import UpdateVideo
from video_library import LibraryItem

#ko test GUI
class CRVTestCase():
    def __init__(self):
        self.item1 = LibraryItem("Test", "One", 1)
        self.library = []

    def test_add_video_to_playlist01(self):
        test = CreateVideoList
        test.add_video_to_playlist(self.library)
        assert self.library[1] == ("Test", "One", 1)

    def test_add_video_to_playlist02(self):
        self.item2 = LibraryItem(0, "one", "what")
        test = CreateVideoList
        test.add_video_to_playlist(self.library)
        assert self.library[1] == ()




class UDVTestCase():
    def __init__(self):
        self.item = LibraryItem("Update", "One", 2)
        self.new_rate = 10
        self.updated_item = LibraryItem("Update", "One", self.new_rate)

    def test_update_video1(self):
        test = UpdateVideo
        test.update_video(self.item)
        assert self.item == self.updated_item

    def test_update_video2(self):
        test = UpdateVideo
        self.new_rate = "abcxyz"
        test.update_video(self.item)
        assert ValueError()
        


crvtest = CRVTestCase()
udvtest = UDVTestCase()




def test_add_video_to_playlist1():
    crvtest.test_add_video_to_playlist01

def test_add_video_to_playlist2():
    crvtest.test_add_video_to_playlist02

def test_update_video1():
    udvtest.test_update_video1

def test_update_video2():
    udvtest.test_update_video2







        

    
    


















    
    
    

    
