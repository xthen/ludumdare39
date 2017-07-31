# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

init:
    
    $ god_pos = Position(xpos=0.7, ypos=0.6)
    $ config.keymap['dismiss'].remove('mouseup_1')
    $ config.keymap['dismiss'].remove('K_RETURN')
    $ config.keymap['dismiss'].remove('K_SPACE')
    $ config.keymap['dismiss'].remove('K_KP_ENTER')
    $ config.keymap['dismiss'].remove('K_SELECT')
    $ config.keymap['dismiss'].append('=')
    
    python:
        
        config.gl_resize = False
        
        renpy.music.register_channel("power", mixer="sound", loop=False)
        renpy.music.register_channel("jump", mixer="sound", loop=False)
        renpy.music.register_channel("coin", mixer="sound", loop=False)
        renpy.music.register_channel("door", mixer="sound", loop = False)
        renpy.music.register_channel("steps", mixer="sound", loop=True)
        renpy.music.register_channel("breath", mixer="sound", loop=True)
        
        def beepy_voice(event, interact=True, **kwargs):
            if not interact:
                return
                
            if event == "show":
                renpy.music.play("sound/beep.mp3", channel="sound", loop=True)
            elif event == "slow_done" or event == "end":
                renpy.music.stop(channel="sound")
                
    
define g = Character("", color="#ffffff", callback=beepy_voice)
                                            
# The game starts here.

label start:
    
    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.
    
    play music "<loop 3>sound/intro.mp3"
    
    scene bg room blur
    with Dissolve(2)
    
    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.
    
    $renpy.pause(2)
    
    show mokona open at god_pos
    
    # These display lines of dialogue.
    
    g "Hi! Welcome to Magical Girl Minako-chan's Jump-Jump Festival™!{w=3}{nw}"
    
    g "Magical Girl Minako-chan© needs your help!{w=3}{nw}"
    
    show iphone7 at Position(xpos=.35, ypos=.9)
    
    init python:
        
        import pygame
        import random
        
        def minako_update(st):
            
            global is_jump
            global vel
            global yval
            global vel
            global grav
            global basePos
            global score
            global batt
            global i_count
            global coin_speed
            global mute
            
            update_speed = .01
            
            # Update the Text
            score_disp.set_child(Text("{color=#ffffff}Score: [score]{/color}", slow=False))
            
            if (batt > 5):
                batt_disp.set_child(Text("{color=#ffffff}[batt]%{/color}", slow=False))
            else:
                batt_disp.set_child(Text("{color=#ff0000}[batt]%{/color}", slow=False))
            
            # Moving Minako
            if is_jump:
                yval+=vel
                vel-=grav
                
                if yval < 0:
                    yval = 0
                    is_jump=False
                    
                msprite.y = int(basePos - yval)
                
            # Moving coin
            csprite.x-=coin_speed
                
            if csprite.x > 0 and csprite.x - 310 <= coin_speed:
                csprite.x = 540
                csprite.y = random.randint(120,310)
                
            # Check for Collision
            if csprite.x > msprite.x + 80 or csprite.x + 51 < msprite.x:
                return update_speed
            if csprite.y + 51 < msprite.y or csprite.y > msprite.y + 125:
                return update_speed
                
            if not mute:
                renpy.play("sound/coin get.mp3", channel="coin")
            
            score+=1
            csprite.x = 540
            csprite.y = random.randint(120,360)
            coin_speed = random.randint(2,6)
                
            return update_speed
            
        def minako_event(ev, x, y, st):
            
            global is_jump
            global vel
            
            if ev.type == pygame.MOUSEBUTTONDOWN and ev.button == 1:
                if is_jump == False:
                    is_jump = True
                    vel=20
                    
                    if not mute:
                        renpy.play("sound/jump.mp3", channel="jump")
                                            
        is_jump=False
        minako_sp = SpriteManager(update=minako_update, event=minako_event)
        minako = Image("images/mgirl.png")
        coin = Image("images/coin.png")
        
        vel=0
        yval=0
        grav=.7
        basePos=425
        is_jump=False
        i_count = 0
        
        score = 0
        batt = 19
        
        mute = False
        
        msprite = minako_sp.create(minako)
        msprite.x = 405
        msprite.y = basePos
        
        coin_speed=2
        csprite = minako_sp.create(coin)
        csprite.x=-100
        csprite.y=300
        
        score_disp = minako_sp.create(Text("{color=#fff}Score: [score]{/color}", slow=False))
        score_disp.x = 318
        score_disp.y = 92
        
        batt_disp = minako_sp.create(Text("{color=#fff}[batt]%{/color}", slow=False))
        batt_disp.x = 530
        batt_disp.y = 92
        
    $ global score
    $ global batt
    $ global csprite
    
    show expression minako_sp as minako_sp
    
    g "Tap on your phone to jump!{w=3}{nw}"
    
    $ csprite.x=540
    $ renpy.pause(2)
    
    g "Help Minako-chan collect coins to fund the ongoing campaign against the evil god Moloch!{w=3}{nw}"
    
    $ renpy.pause(2)
    
    g "Hey, you're not half bad.{w=3}{nw}"
    
    $ renpy.pause(2)
    
    show mokona closed
    
    $ renpy.pause(2)
    
    $ batt = 18
    
    g "Hey, uh...{w=2}{nw}"
    
    $ renpy.pause(2)
    
    g "I know things have been...{w=.5}{nw}"
    g "You know, a little off, ever since...{w=3}{nw}"
    g "Anyway, I just wanted to say thanks for spending time with me and my game.{w=3}{nw}"
    
    show mokona open
    
    g "I think you're getting better!{w=1}{nw}"
    
    $ batt = 17
    $ renpy.pause(4)
    
    g "You're not very talkative, are you?{w=3}{nw}"
    g "No, that's okay, I don't mind.{w=3}{nw}"
    g "It suits you, actually.{w=3}{nw}"
    
    show mokona closed
    
    $ renpy.pause(3)
    
    g "There's not really a lot to this game, is there?{w=3}{nw}"
    g "I mean, you can't even use the coins on anything...{w=1.2}{nw}"
    g "Oh! Not to say you're not doing a great job.{w=3}{nw}"
    g "I just wish I came attached to a better game, is all...{w=1}{nw}"
    
    $ batt = 16
    $ renpy.pause(5)
    
    show mokona open
    
    g "What do you think she needs all those coins for, anyway?{w=3}{nw}"
    g "I mean she's a Magical Girl, so like-{w=1}{nw}"
    g "What can money get that magic powers can't?{w=2}{nw}"
    
    $ renpy.pause(2)
    
    g "And while we're wondering, do you think she's the one moving?{w=1}{nw}"
    g "Or are the coins going by above her?{w=2}{nw}"
    
    $ renpy.pause(.5)
    $ batt = 15
    $ renpy.pause(.5)
    
    g "You know, that reminds me-{nw}"
    
    # The power goes out
    stop music
    play power "sound/power off.mp3"
    show bg room night blur
    show mokona closed
    
    $ renpy.pause(.5)
    
    g "...{w=2}{nw}"
    g "Looks like you lost power...{w=3}{nw}"
    g "You think your parents will fix it?{w=2}{nw}"
    
    $ renpy.pause(1)
    
    g "Oh... was that not a good question to ask?{w=2}{nw}"
    g "Sorry...{w=1}{nw}"
    
    $ renpy.pause(2)
    $ batt = 14
    $ renpy.pause(2)
    
    g "...{w=1}{nw}" 
    g "What was I talking about before?{w=2}{nw}"
    
    $ renpy.pause(1)
    
    g "Oh yeah! Talking about whether Minako-chan or the coins are moving.{w=2}{nw}"
    g "It reminded me of one of those old Zen riddles.{w=2}{nw}"
    
    show mokona open
    
    g "So there's two monks watching a flag wave, right?{w=1}{nw}"
    g "One says, \"The flag is moving.\"{w=1}{nw}"
    g "The other says, \"No, it's the wind that's moving!\"{w=1}{nw}"
    
    $ batt = 13
    
    g "Then their master comes out, and he says:{w=1}{nw}"
    g "\"It's not the flag or the wind. It's your {i}minds{/i} that are moving.\"{w=3}{nw}"
    
    $ renpy.pause(2)
    
    show mokona closed
    
    g "Well, I thought it was cool.{w=3}{nw}"
    g "Not the most enlightening thing, I guess...{w=3}{nw}"
    
    $ batt = 12
    $ renpy.pause(2)
    
    g "Man, this game's really draining your battery, huh?{w=3}{nw}"
    
    $ batt = 11
    $renpy.pause(.5)
    
    g "Woah! No way all of that's from the game...{w=3}{nw}"
    g "What all do you have running on that thing?{w=3}{nw}"
    
    $ renpy.pause(3)
    
    g "Oh, you don't have a way to charge, do you...?{w=1}{nw}"
    g "That means...{nw}"
    g "No, you'll definitely find a way to charge before it comes to that. Right?{w=2}{nw}"
    
    $ renpy.pause(.3)
    $ batt = 10
    $ renpy.pause(1)
    
    g "Yeah...{w=2}{nw}"
    g "Hey, you don't mind leaving the game open, do you?{w=2}{nw}"
    g "You don't have to play, just-{w=3.5}{nw}"
    g "I'd like to stay here.{w=3}{nw}"
    
    # Footsteps start to play
    
    play steps "<loop 0.0>sound/steps.mp3"
    
    $ renpy.pause(2)
    $ batt = 9
    $ renpy.pause(2)
    
    g "You hear that, right...?{w=3}{nw}"
    
    $ batt = 8
    
    g "Do you think it's someone here to fix the power?{w=1}{nw}"
    
    $ renpy.pause(2)
    
    g "Yeah, me either...{w=2}{nw}"
    
    $ renpy.pause(2)
    
    stop steps fadeout 1.0
    
    $ renpy.pause(1.5)
    
    g "They stopped...{w=1}{nw}"
    g "It sounded like they were... outside?{w=2}{nw}"
    
    # Door opens
    play door "sound/door.mp3"
    
    $ renpy.pause(.7)
    $ batt = 7
    
    g "Quick! Hide! {nw}"
    g "Get under the bed!{nw}"
    
    show bg black
    with Dissolve(.5)
    
    $ batt = 6
    
    $ renpy.pause(.2)
    
    play breath "<loop 0.0>sound/breathing.mp3"
    
    g "Turn your volume off!{w=1}{nw}"
    
    $ mute = True
    $ renpy.pause(2)
    $ batt = 5
    $ renpy.pause(2)
    
    g "Do you think it'll leave soon?{w=2}{nw}"
    g "You're not going to try something, are you?{w=2}{nw}"
    
    $ batt = 4
    
    g "It can't find you in here.{w=2}{nw}"
    g "It'll leave eventually.{w=2}{nw}"
    g "It'll leave...{w=2}{nw}"
    
    $ renpy.pause(1)
    $ batt = 3
    $ renpy.pause(1)
    
    g "You're really losing power now, aren't you?{w=2}{nw}"
    g "I guess that makes sense...{w=2}{nw}"
    g "We should've known when the power went out, huh?{w=2}{nw}"
    g "We'll know better next time.{w=2}{nw}"
    
    $ renpy.pause(2)
    
    g "It seems kind of pointless now, but...{w=1}{nw}"
    g "Thanks for playing the game.{w=1}{nw}"
    g "I know it wasn't very good, but not many people play games these days.{w=3}{nw}"
    g "You might be the last{nw}"
    
    $ batt = 2
    
    show mokona open
    
    g "Ha ha, what am I saying! It'll be fine!{w=2}{nw}"
    
    $ renpy.pause(2)
    
    # Breathing goes away
    
    stop breath fadeout 3.5
    
    play steps "sound/steps.mp3"
    
    $ renpy.pause(1)
    
    show mokona closed
    
    $ renpy.pause(1)
    
    stop steps fadeout 2
    
    $ renpy.pause(2)
    
    g "Hey... I think it left!{w=2}{nw}"
    g "Okay, this is your chance!{w=2}{nw}"
    
    $ batt = 1
    
    g "If it's not in the room, you need to make a run for it.{w=1}{nw}"
    g "You can make it!{w=1}{nw}"
    g "Just get out of the house and find a safer place.{w=1}{nw}"
    
    show mokona open
    
    g "I'm glad I got to play with you!{w=1}{nw}"
    g "It's been a lot of fun!{w=1}{nw}"
    g "Now go for it!{w=1}{nw}"
    g "I believe in y{nw}"
    
    # Get everything out of there!
    hide minako_sp
    scene bg black
    
    $ renpy.pause(5)
    
    # Credits go here
    call credits from _call_credits
    
    # This ends the game.
    
    return
    
label credits:
    
    init python:
        credits = ('Game by', 'Will Walters'), ('Music by', 'Will Walters'), ('All Images Used Belong to their Respective Creators','')
        credits_s = ''
        c1 = ''
        for c in credits:
            if not c1==c[0]:
                credits_s += "\n{size=40}" + c[0] + "\n"
            credits_s += "{size=60}" + c[1] + "\n"
            c1=c[0]
        credits_s += "\n{size=40}Engine\n{size=60}Ren'py\n6.99.12.42187"
        
    init:
        image cred = Text(credits_s, text_align=0.5)
    
    $ credits_speed = 15
    show cred at Move((0.5, 5.0), (0.5, 0.0), credits_speed, repeat=False, bounce=False, xanchor="center", yanchor="bottom")
    with Pause(credits_speed)
    with dissolve
    with Pause(3)
    return
