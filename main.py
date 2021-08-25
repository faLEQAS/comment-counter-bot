import praw
import time

while True:



    reddit = praw.Reddit(client_id = ",
                                client_secret = "",
                                username = "",
                                password = "",
                                user_agent = "")

    #url or id of the post
    submission = reddit.submission(url="")

    commentcount = 0


    print("checking comments again ! \n")

    for comment in submission.comments:
        commentcount = commentcount + 1


    submission.edit("this post has {} comments!".format(str(commentcount)))


    print("\nedited post successfully !")

    commentcount = 0


    time.sleep(300)
