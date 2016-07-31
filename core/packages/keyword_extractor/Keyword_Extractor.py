from core.packages.rake import rake
import os


class Keyword_Extractor():

      def __init__(self, min_char_length = 3, max_word_length = 3, min_keyword_frequency = 1):
          self.stoppath =  os.path.join(os.path.dirname(os.path.dirname(__file__)), "rake/SmartStoplist.txt")
          self.keyword_list_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "rake/data/keyword_list.txt")
          self.rake = rake.Rake(self.stoppath, self.keyword_list_path, min_char_length, max_word_length, min_keyword_frequency)


      def extract(self, text):
            return self.rake.run(text)

      def modify_extractor(self, min_char_length = 3, max_word_length = 3, min_keyword_frequency = 0):
            self.rake = rake.Rake(self.stoppath, self.keyword_list_path, min_char_length, max_word_length, min_keyword_frequency)



if __name__ == '__main__':
      x = Keyword_Extractor()
      x.modify_extractor(min_keyword_frequency=1)

      txt = 'My favourite areas are dynamic programming and Internet of Things' \
            ' Im haskell fan. I love programming in java'
      print x.extract(txt)