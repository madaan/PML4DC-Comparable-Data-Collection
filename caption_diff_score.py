"""For each image, calculates a caption difficulty score
"""
from collections import defaultdict
import nltk
from tqdm import tqdm 

def caption_score(caption):
    words = caption.split()
    num_uniq_words = len(set(words))
    return num_uniq_words, len(caption)


def combined_caption_score(res):
    """Takes the per caption score and returns a collective score
    for the image. The score is calculated as follows:
        * Total length of all the captions (L)
        * Total number of unique words (W)
        * 
    
    Arguments:
        captions_score {[type]} -- [description]
    """
    final_caption_score = {}
    for img, per_caption_stats in  res.items():
        W, L, i = 0, 0, 0
        captions = [] # all the captions for a given image
        for c, (caption, (num_uniq_words, total_len)) in per_caption_stats.items():
            W += num_uniq_words
            L += total_len
            captions.append(caption)
            i += 1
        assert i == 5
        edit_dist = 0
        for i in range(5):
            for j in range(i + 1, 5):
                edit_dist += nltk.edit_distance(captions[i], captions[j])
        final_caption_score[img] = edit_dist
    return final_caption_score


def read_captions(pth):
    res = defaultdict(lambda: defaultdict(str))
    with open(pth, "r") as f:
        for line in f:
            img, caption = line.strip().split("\t")
            img_name, caption_num = img.split("#")
            res[img_name][int(caption_num)] = (caption, caption_score(caption))

    final_caption_score = combined_caption_score(res)
    return final_caption_score

if __name__ == '__main__':
    import sys
    caption_score = read_captions(sys.argv[1])
    caption_score = sorted(caption_score.items(), key=lambda x: -x[1])
    for k, v in caption_score:
        print(k, v)