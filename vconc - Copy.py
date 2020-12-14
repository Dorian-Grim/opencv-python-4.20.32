embed_simulator2 = {}

def make_embed_obj(poll_id, answer, author):
    if poll_id not in embed_simulator2: # if poll is not in embed obj
        embed_simulator2[poll_id] = {answer:[author]} # instantiate it with the author
    else: # poll is in embed obj
        for inner_answer in embed_simulator2[poll_id]: # for every answer given
            for inner_author in embed_simulator2[poll_id][inner_answer]: # for every author recorded
                if author == inner_author: # if author is found in object, remove him
                    embed_simulator2[poll_id][inner_answer].remove(author)
                    break
        if answer in embed_simulator2[poll_id]: # check if answers is already given
            if author in embed_simulator2[poll_id][answer]: # if author has given answer, remove him from old, put him with new
                pass 
            else: # author has not given answer
                embed_simulator2[poll_id][answer].append(author) # append this author
        else: # answer is not given
            embed_simulator2[poll_id][answer] = [author]
    return embed_simulator2

# TEST: same answer same user

make_embed_obj(1, 'asd', 1)
make_embed_obj(1, 'asd', 1)

# ======= PASSED =========

# TEST: same user, diff answer

make_embed_obj(1, 'asd', 1)
make_embed_obj(1, 'asdf', 1)

# ======= PASSED =========

# TEST: other user, same answer

make_embed_obj(1, 'asd', 2)
make_embed_obj(1, 'asd', 1)

# ======= PASSED =========

# TEST: third user, same answer

make_embed_obj(1, 'asd', 3)

# ======= PASSED =========

# FINALLY RECREATE EMBED NO MATTER WHAT
# calculate votes for each answer
field_holder = {}
for answer in embed_simulator2[1]:
    i = 1
    for author in embed_simulator2[1][answer]:
        i += 1