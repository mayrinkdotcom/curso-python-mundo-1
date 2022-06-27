from pygame import mixer

mixer.init()
mixer.music.load('Chopin - Nocturne op.9 No.2 - Andante.mp3')
mixer.music.play()
input('Agora você escuta? ')
