import syncedlyrics
#-------------------------------------------------------
name = "Mahika"
artist = "Adie"
#-------------------------------------------------------

link = "not found"

lrc = syncedlyrics.search(name + " " + artist)

#print(lrc)

lrc = lrc.replace('[', '"')
lrc = lrc.replace(']', '": "')
lrc = lrc.replace('\n', '",\n')
lrc = lrc.replace('00:0', '')
lrc = lrc.replace('00:', '')
lrc = lrc.replace('01:', '1:')
lrc = lrc.replace('02:', '2:')
lrc = lrc.replace('03:', '3:')
lrc = lrc.replace('.', ':')
lrc = lrc.replace('" ', '"')
lrc = lrc + '(The end)",'

music_link = link
lol = ", {"
name = f'                          name: "{name + " - " + artist}"'
src = f'                          src: "{music_link}",'
sync = '                          sync: {'
last = '                         },'
last_2 = '                      }'

whole = f'''
{lol}
{name}
{src}
{sync}
{lrc}
{last}
{last_2}
'''

print(whole)
#if lrc[6] == ":":
    #print(lrc[0] + lrc[1] + lrc[2] + lrc[3]+  lrc[4] + lrc[5] + lrc[6])
#elif lrc[7] == ":":
    #print(lrc[0] + lrc[1] + lrc[2] + lrc[3]+  lrc[4] + lrc[5] + lrc[6] + lrc[7])
#elif lrc[8] == ":":
    #print(lrc[0] + lrc[1] + lrc[2] + lrc[3]+  lrc[4] + lrc[5] + lrc[6] + lrc[7] + lrc[8])
#elif lrc[9] == ":":
    #print(lrc[0] + lrc[1] + lrc[2] + lrc[3]+  lrc[4] + lrc[5] + lrc[6] + lrc[7] + lrc[8] + lrc[9])