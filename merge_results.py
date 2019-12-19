"""Merges the results of both image caption and the translation tasks.

Usage:
    merge_results.py    --orig-captions-file=<str>   --captions-res=<str>    --xlate-res=<str>   --outpath=<str>

Options:
        --orig-captions-file=<str>   The path to the file that has the captions
        --captions-res=<str>    The path to the results for the captions task
        --xlate-res=<str>       The path to the results for the xlation task
        --outpath=<str>         Path to the output
"""
import pandas as pd
from collections import defaultdict
from docopt import docopt


def get_en_caption_to_url(captions_file_path):
    """Reads the captions file to a map
    
    Arguments:
        captions_file_path {[str]} -- [A file that has the mapping from URL to caption]
    
    Returns:
        [map] -- [caption -> URL of the file]
    """
    res = []
    with open(captions_file_path, "r") as f:
        for line in f:
            url, caption = line.strip().split("\t")
            img_name, caption_num = url.split("#")
            res.append({"en_caption": caption, "img_url": img_name})
            
    return pd.DataFrame(res)


def get_url_to_fr_caption(img_xlations_path):
    """Gets a dict from the image url to the caption of the image
    
    Arguments:
        img_xlations_path {[type]} -- [description]
    
    Returns:
        [str] -- [description]
    """
    img_xlations = pd.read_csv(img_xlations_path)
    img_xlations = img_xlations[img_xlations["RequesterFeedback"].isnull()]
    tmp = img_xlations[["Input.image_url", "Answer.summary"]]
    tmp.rename(columns={"Input.image_url": "img_url", "Answer.summary": "fr_caption"}, index=str, inplace=True)
    return tmp
    #return dict(zip(img_xlations["Input.image_url"], img_xlations["Answer.summary"]))


def get_en_caption_to_fr_xlation(text_xlations_path):
    text_xlations = pd.read_csv(text_xlations_path)
    text_xlations = text_xlations[text_xlations["RequesterFeedback"].isnull()]
    tmp = text_xlations[["Input.xlate_input", "Answer.xlation"]]
    tmp.rename(columns={"Input.xlate_input": "en_caption", "Answer.xlation": "fr_xlation"}, index=str, inplace=True)
    return tmp
    # return dict(zip(text_xlations["Input.xlate_input"], text_xlations["Answer.xlation"]))


if __name__ == '__main__':
    args = docopt(__doc__)
    en_caption_to_fr_xlation = get_en_caption_to_fr_xlation(args["--xlate-res"])
    en_caption_to_fr_xlation.to_csv("en_caption_to_fr_xlation.tsv", sep="\t", index=None)

    en_caption_to_url = get_en_caption_to_url(args["--orig-captions-file"])
    en_caption_to_url.to_csv("en_caption_to_url.tsv", sep="\t", index=None)

    url_to_fr_caption = get_url_to_fr_caption(args["--captions-res"])
    url_to_fr_caption.to_csv("url_to_fr_caption.tsv", sep="\t", index=None)

    """
    en_caption_to_fr_xlation_url = pd.merge(left=en_caption_to_fr_xlation, right=en_caption_to_url, on="en_caption")
    print(len(en_caption_to_fr_xlation_url))
    merged = pd.merge(left=en_caption_to_fr_xlation_url, right=url_to_fr_caption, on="img_url")
    print(merged.head())
    print(len(merged))
    """

