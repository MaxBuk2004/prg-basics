facebook = True
twitter = False
instagram = False
good_inf = 0

if facebook:
    good_inf += 1
if twitter:
    good_inf += 1
if instagram:
    good_inf += 1
if good_inf >= 2:
    print('You are a good influencer!')