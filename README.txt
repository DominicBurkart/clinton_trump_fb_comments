#Dominic's pipeline for training a naive bayes classifier to encode the similarity of comments on clinton/trump's fb posts to the posts themselves.

#get into the directory with these files / programs
#	data etc: https://drive.google.com/drive/folders/0Bzv7WkKe99GcQ2pTR1hnVFo0MkU
cd /Users/dominicburkart/Desktop/Classifier #change as appropriate

#train naive bayes
python3 train-word-features.py

#encode comments
python3 encode-equal-word-features-bayes.py trump_fb_post_comments_ordered.csv
python3 encode-equal-word-features-bayes.py clinton_fb_post_comments_ordered.csv

#sequentialize ids
python3 id_sequentializer.py trump_fb_post_comments_ordered.csv
python3 id_sequentializer.py clinton_fb_post_comments_ordered.csv

#send folder to billy and eat some trailmix
