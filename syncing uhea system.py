import syncedlyrics
#-------------------------------------------------------
name = "Down & out SpySki, raspi" # Choose your own
artist = "Landon Cube" # Choose your own
#-------------------------------------------------------

link = "not found"
lrc = syncedlyrics.search(name + " " + artist)

#print(lrc)

lrc = lrc.replace('"', '')
lrc = lrc.replace('\n', '" },\n ')
lrc = lrc.replace('00:0', '')
lrc = lrc.replace('00:', '')
lrc = lrc.replace('01:', '1:')
lrc = lrc.replace('02:', '2:')
lrc = lrc.replace('03:', '3:')
lrc = lrc.replace('.', ':')
lrc = lrc.replace(':', '')
lrc = lrc + '(The end)"'
lrc = lrc.replace(']', '0, "say": "')
lrc = lrc.replace('[', '{"time": ')
lrc = lrc.replace('" ', '"')

lrc = f'let {name} = [\n' + lrc + ', "end": true}\n]'

print(lrc)
#if lrc[6] == ":":
    #print(lrc[0] + lrc[1] + lrc[2] + lrc[3]+  lrc[4] + lrc[5] + lrc[6])
#elif lrc[7] == ":":
    #print(lrc[0] + lrc[1] + lrc[2] + lrc[3]+  lrc[4] + lrc[5] + lrc[6] + lrc[7])
#elif lrc[8] == ":":
    #print(lrc[0] + lrc[1] + lrc[2] + lrc[3]+  lrc[4] + lrc[5] + lrc[6] + lrc[7] + lrc[8])
#elif lrc[9] == ":":
    #print(lrc[0] + lrc[1] + lrc[2] + lrc[3]+  lrc[4] + lrc[5] + lrc[6] + lrc[7] + lrc[8] + lrc[9])