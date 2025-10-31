import praw
from videodownloader import download_from_sub
from insta_upload import python_call_insta_upload as upload_ig


def main():
    # Initialize the Reddit instance\

    # Path video goes into is
    # Videos/submission.title

    new_vid_found = False
    for i in range(0,5):  # Try 5 times before breaking out of loop
        submission_title, new_vid_found = download_from_sub(1,"nextfuckinglevel")
        if new_vid_found:
            break
    if new_vid_found == False:  # Still false
        raise Exception("Wasn't able to find new video. But thats ok")
    else:
        relative_path = f'videos/{submission_title}'
        
        upload_ig(relative_path, submission_title)
        
    
    
        
    
    
    

