import numpy as np  # useful for many scientific computing in Python
#matplotlib inline
import matplotlib as mpl
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches # needed for waffle Charts
# import package and its set of stopwords
from wordcloud import WordCloud, STOPWORDS ### Make sure you don't hava a file named wordcloud.py
print ('Wordcloud is installed and imported!')
# download file and save as alice_novel.txt
# !wget --quiet https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Data_Files/alice_novel.txt

# open the file and read it into a variable alice_novel
#alice_novel = open('alice_novel.txt', 'r').read()
#alice_novel = open('billofrights.txt', 'r').read()
alice_novel = open('bible.txt', 'r').read()
#where to put the image
x = 'books_read.png'

# # download image
# !wget --quiet https://s3-api.us-geo.objectstorage.softlayer.net/cf-courses-data/CognitiveClass/DV0101EN/labs/Images/alice_mask.png
    
# save mask to alice_mask
# alice_mask = np.array(Image.open('alice_mask.png'))
    
print('Image downloaded and saved!')

stopwords = set(STOPWORDS) #We use the function set to remove any redundant stopwords.
stopwords.add('said') # add the words said to stopwords
stopwords.add('ye') # add the words said to stopwords
stopwords.add('thee') # add the words said to stopwords
stopwords.add('unto') # add the words said to stopwords
stopwords.add('shalt') # add the words said to stopwords
stopwords.add('thou') # add the words said to stopwords
stopwords.add('thy') # add the words said to stopwords
# Create a word cloud object and generate a word cloud. For simplicity, let's generate a word cloud using only the first 2000 words in the novel.
# instantiate a word cloud object
alice_wc = WordCloud(
    background_color='white',
    max_words=2000,
    stopwords=stopwords,
    width=480,
    height= 480
)

# generate the word cloud
alice_wc.generate(alice_novel)
# display the word cloud

plt.imshow(alice_wc, interpolation='bilinear')
plt.axis('off')
# plt.show()
plt.savefig(x)








