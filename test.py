
# new_string = ''
# for x in neet:
#     new_string += '%s ' % (x[7:])

# print(new_string.rstrip())
#
#
# option_select = v.get()

ep_directory = '/Users/justinlaureano/Movies/Its Always Sunny In ' \
               'Philadelphia/All/'

neet = ['S10E02 Charlie Work.mp4',
        'S10E03 Pig Latin.mp4',
        'S10E04 Pig Sheep.mp4']


def cast_playlist(current_playlist, ep_directory):
    # if option_select == 1:
        new_string = ''
        for file in current_playlist:
            new_string += '%s%s ' % (ep_directory, file[7:])
        print(new_string.rstrip())


cast_playlist(neet, ep_directory)



castnow --address 192.168.2.178 /Users/justinlaureano/Movies/Its\ Always\
Sunny\ In\ Philadelphia/All/Charlie\ and\ Dee\ Find\ Love.mp4