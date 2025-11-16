from videodownloader import download_singular
from insta_upload import python_call_insta_upload as upload_ig
import tomllib
import sys

def main():

    # Path video goes into is
    # Videos/submission.title

    # read from attempted sub list
    # if we can

    with open('used_submissions.txt', 'r') as file:
        previously_used_posts_pre_trim = file.readlines()
        previously_used_posts = [line.rstrip('\n') for line in previously_used_posts_pre_trim]  # NoQa

    with open('config.toml', 'rb',) as file:
        config = tomllib.load(file)

        subs = config['gen_config']['subs']

    search_concluded = False
    for time_period in ['hour', 'day', 'week', 'month']:
        if search_concluded is True:
            break
        for sub_reddit in subs:
            # Attempt to download if not move to next sub
            success, submission_title = download_singular(sub_reddit, time_period)  # NoQa
            if success is False:
                continue
            else:
                if submission_title not in previously_used_posts:
                    # Not sure if this edge case is possible but
                    previously_used_posts.append(submission_title)
                    # For the long term
                    write_to_prev_used(submission_title)
                    final_title = submission_title
                    search_concluded = True
                    break
                else:
                    continue

    if search_concluded is False:
        sys.exit(1)  # No video was able to be found

    upload_ig(f'videos/{final_title}')
    sys.exit(0)

def write_to_prev_used(title: str):
    line_to_append = f'{title}\n'
    with open('used_submissions.txt', 'a') as file:
        file.write(line_to_append)
