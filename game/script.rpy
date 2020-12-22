# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define m = Character("Mitsuru")
define y = Character("Yukari")
define nar = Character(" ")

label start:


    # image ySUMnormClosed = "YukariSum1Closed.png"
    # image ySUMsmileClosed = "YukariSum2Closed.png"
    # image ySUMangryClosed = "YukariSum3Closed.png"
    # image ySUManxiousClosed = "YukariSum4Closed.png"
    # image ySUMsurpriseClosed = "YukariSum5Closed.png"
    image ySUMcry = "YukariSum6.png"
    image ySUMsmileblush = "YukariSum7.png"
    # image ySUMsmileblushClosed = "YukariSum7Closed.png"

    image mSUMnorm flip = "MitsuruSum1.png"
    image mSUMbashful flip = "MitsuruSum3.png"
    image mSUMblush = im.Flip("MitsuruSum4.png", horizontal=True)
    image mSUMblush flip = "MitsuruSum4.png"
    image mSUMangry flip = "MitsuruSum8.png"

    #image mSUMnormClosed = "MitsuruSum1Closed.png"
    #image mSUMsmileClosed = "MitsuruSum2Closed.png"
    #image mSUMbashfulClosed = "MitsuruSum3Closed.png"
    #image mSUMblushClosed = "MitsuruSum4Closed.png"

    image yBedroom = "YukariBedroom.png"
    show yBedroom

    #image ySEESnormal = "YukariSEES1.png"
    #image ySEESnormalClosed = "YukariSEES1Closed.png"
    #image ySEEShappy = "YukariSEES2.png"
    #image ySEEShappyClosed = "YukariSEES2Closed.png"
    #image ySEESangry = "YukariSEES3.png"
    #image ySEESangryClosed = "YukariSEES3Closed.png"
    #image ySEESanxious = "YukariSEES4.png"
    #image ySEESanxiousClosed = "YukariSEES4Closed.png"
    #image ySEESsurprise = "YukariSEES5.png"
    #image ySEESsurpriseClosed = "YukariSEES5Closed.png"
    #image ySEESblush = "YukariSEES6.png"
    #image ySEESblushClosed = "YukariSEES6Closed.png"
    #image ySEESsnood = "YukariSEES7.png"


    image ySUMnorm = "YukariSum1.png"
    show ySUMnorm:
        xalign 0.75
        yalign 0.8

    #Current: Yukari in her bedroom.

    nar "So it's been a bit of a long day."
    nar "And Yukari now sits here, looking at herself in the mirror, slowly removing her makeup."
    nar "It's a monotonous but necessary pattern, something she has grown used to and succumbed to, not a part of the entirety of womanhood but definitely part of hers."
    nar "Her mind flashes through the day."
    nar "A set, a costume, she's in a kids show. Pink Argus."
    nar "That's who she is right now: an actress."
    nar "It pays, she gets money. She is self-sustaining. And she's on the road to where she wants to go:"
    nar "Fame?"
    nar "..."
    nar "She also maintains her studies, she's majoring in acting."
    nar "She's fine at the major, but the gen eds..."
    hide ySUMnorm
    image ySUMangry = "YukariSum3.png"
    show ySUMangry:
        xalign 0.75
        yalign 0.8
    nar "She shines more in preformance than with paper and pen."
    hide ySUMangry
    show ySUMnorm:
        xalign 0.75
        yalign 0.8
    nar "..."
    nar "Anyway, Yukari is ready for bed. She lives in an apartment alone now."
    nar "She goes to college, comes back to an empty home, save for the thought of adopting a cat."
    y "Maybe I should get a cat."
    nar "See? She thinks about it."
    nar "Other stuff she thinks about:"
    nar "highschool, her father, what she eats during the day."
    nar "The life of a first year college student, unfulfilled."
    nar "Her biggest problem is navigating the social scape of a place without the support of her SEES peers, without a family to lean on in the nights."
    nar "But enough."
    nar "To sleep, Yukari."
    nar "To sleep, my dear."
    nar "..."
    hide ySUMnorm
    image transitionBG = "Transition Background.png"
    show transitionBG
    nar "..."

    image coffeeShop = "CoffeeShop.png"
    show coffeeShop

    #Current: Yukari at a cafe near her college, Mitsuru enters
    show ySUMnorm:
        xalign 0.75
        yalign 0.8

    nar "..."
    nar "In this moment: Yukari's is SUPPOSED to be studying for her anthropology gen ed..."
    y "Yeah, anyway, that's what I heard about the agency, can you even believe it?"
    nar "But she's on the phone with a new friend she's met in her acting class."
    y "So anyway what's up with you?"
    nar "She sits in a coral reef of human behavior, the coffee shop next to campus. Students from all around interact, flirt and flutter like little birds, social cliques form and fade."
    nar "Although it may be a little bit less dramatic than that descriptions, these are really just young adults getting coffee and studying."
    y "Yeah, so anyway I was talking to Kitsume and-"
    image ySUMsurprise = "YukariSum5.png"
    hide ySUMnorm
    show ySUMsurprise:
        xalign 0.75
        yalign 0.8
    nar "A stop?"
    nar "Why a stop?"
    nar "..."
    nar "Yukari stops mid-sentence because a specific woman has entered and changed the shop atmosphere Yukari was just gaily ignoring a moment ago."
    nar "A woman she has not seen in a long time."
    image mSUMsmile flip = "MitsuruSum2.png"
    show mSUMsmile flip:
        xalign 0.0
        yalign 0.7
    nar "Mitsuru Kirijo."
    nar "A long lost... companion?"
    nar "They were friends once, in high school,"
    nar "when everything was so incredibly complex."
    image ySUManxious = "YukariSum4.png"
    hide ySUMsurprise
    show ySUManxious:
        xalign 0.75
        yalign 0.8
    y "Oh..."
    y "It's her..."
    nar "Yukari quickly takes out a pocket mirror."
    hide ySUManxious
    show ySUMangry:
        xalign 0.75
        yalign 0.8
    y "What does my hair look like right now?"
    y "I'm a mess!"
    nar "She is a bit of a mess, just having gotten back from acting for Phoenix Ranger Featherman Victory."
    nar "But in reality, Yukari's mess is the average person's greatest day, looks-wise."
    hide ySUMangry
    show ySUManxious:
        xalign 0.75
        yalign 0.8
    y "..."
    y "Should I approach her?"
    y "Or should I let her approach me?"
    y "I feel like it's more proper that way."
    y "She's the senpai, after all."
    nar "Interesting use of senpai, Yukari."
    nar "Given how long its been since either woman had been upper or underclassmen to the other."
    y "..."
    hide ySUManxious
    show ySUMsurprise:
        xalign 0.75
        yalign 0.8
    y "I-"
    hide ySUMsurprise
    show ySUMangry:
        xalign 0.75
        yalign 0.8
    nar "She tries to croak a greeting."
    hide ySUMangry
    show ySUMsurprise:
        xalign 0.75
        yalign 0.8
    y "Sen-"
    nar "Mitsuru Kirijo has yet to see her. She is stil at the counter, ordering."
    hide ySUMsurprise
    show ySUMangry:
        xalign 0.75
        yalign 0.8
    y "Fuck."
    y "What do I do?"
    image mSUMsmile = im.Flip("MitsuruSum2.png", horizontal=True)
    hide mSUMsmile flip
    show mSUMsmile:
        xalign 0.0
        yalign 0.7
    m "..."
    hide mSUMsmile
    show mSUMnorm:
        xalign 0.0
        yalign 0.7
    m "..."
    m "...Takeba?"
    hide mSUMnorm
    show mSUMbashful:
        xalign 0.0
        yalign 0.7
    m "How long have you been standing there?"
    hide mSUMbashful
    show mSUMsmile:
        xalign 0.0
        yalign 0.7
    m "..."
    hide ySUMangry
    show ySUMsurprise:
        xalign 0.75
        yalign 0.8
    m "Let me get my drink and I'll come sit with you."
    hide mSUMsmile
    show mSUMnorm:
        xalign 0.0
        yalign 0.7
    m "As long as you'll have me."
    hide mSUMnorm
    show mSUMsmile flip:
        xalign 0.0
        yalign 0.7
    nar "Before Yukari has a chance to answer, Mitsuru has already turned around, negging the barista."
    hide ySUMsurprise
    show ySUManxious:
        xalign 0.75
        yalign 0.8
    y "Oh my god."
    y "What do I do?"
    y "What should we talk about?"
    y "I have to leave right now."
    hide ySUManxious
    show ySUMangry:
        xalign 0.75
        yalign 0.8
    y "Something came up! Exactly!"
    nar "But before Yukari can execute her escape..."
    image mSUMnorm = im.Flip("MitsuruSum1.png", horizontal=True)
    hide mSUMsmile flip
    show mSUMnorm:
        xalign 0.25
        yalign 0.7
    m "Yukari Takeba!"
    m "It has been forever."
    nar "Mitsuru Kirijo's voice is curiously stilted."
    hide ySUMangry
    show ySUMnorm:
        xalign 0.75
        yalign 0.8
    y "Senpai!"
    y "I was almost afraid you wouldn't see me."
    m "Well, I guess we're lucky I did."
    y "Yeah."
    y "..."
    m "..."
    y "..."
    nar "A harrowing exchange of silence."
    y "So..."
    m "Yes?"
    y "How have you been?"
    y "What's new in your life?"
    m "Well I'm still in charge of the Kirijo Group... hmm..."
    m "...and you know... college. As I assume you are also attending."
    m "You haven't dropped out, have you?"
    hide ySUMnorm
    show ySUMangry:
        xalign 0.75
        yalign 0.8
    y "Of course I haven't!"
    y "I'm a little offended you even ask that!"
    image mSUMbashful = im.Flip("MitsuruSum3.png", horizontal=True)
    hide mSUMnorm
    show mSUMbashful:
        xalign 0.25
        yalign 0.7
    m "Oh... I didn't mean..."
    m "I guess it was out of habit."
    m "It really isn't my responsiblity anymore, is it..."
    m "To chastise you or anyone else about academics or,"
    m "anything, for that matter."
    m "..."
    hide ySUMangry
    show ySUManxious:
        xalign 0.75
        yalign 0.8
    y "No! Wait-"
    y "Sorry it's okay."
    y "..."
    y "I think I have to run to class soon."
    nar "She doesn't."
    m "Oh, okay."
    y "Yeah, okay."
    y "Bye, I guess."
    image mSUMangry = im.Flip("MitsuruSum8.png",horizontal=True)
    hide mSUMbashful
    show mSUMangry:
        xalign 0.25
        yalign 0.7
    m "Wait!"
    hide ySUManxious
    show ySUMnorm:
        xalign 0.75
        yalign 0.8
    y "Yeah?"
    hide mSUMangry
    show mSUMbashful:
        xalign 0.25
        yalign 0.7
    m "I'd love to catch up some more with you Takeba."
    m "I'm incredibly serious about this."
    m "I know we haven't seen one another in a long time..."
    m "But I used to consider you one of my closest friends."
    m "And having a chance to re-enter your life..."
    m "would mean the world to me."
    hide ySUMnorm
    show ySUMsurprise:
        xalign 0.75
        yalign 0.8
    y "Senpai..."
    image ySUMsmile = "YukariSum2.png"
    hide mSUMbashful
    show mSUMsmile:
        xalign 0.25
        yalign 0.7
    m "This weekend, let's watch a movie at my apartment."
    y "..."
    m "I'll make popcorn, we can do facials and paint our nails."
    m "Sort of like we used to in the dorm."
    hide ySUMsurprise
    show ySUMnorm:
        xalign 0.75
        yalign 0.8
    y "That actually... sounds so lovely, Senpai."
    hide ySUMnorm
    show ySUMsmile:
        xalign 0.75
        yalign 0.8
    y "I will definitely come over."
    nar "But under Yukari's smile is a dull, aching pain."
    nar "Any reminder of days past bring her this."
    nar "In Yukari's mind, high school equates to death. Specifically, the death of her best friend: Minako Arisato."
    nar "But in Yukari's head she says to herself: I'll get over it, I can get over it."
    nar "She says: I can get over it, if it can mean rekindling what Mitsuru and I used to have... whatever it was..."
    nar "It meant so much to me, she says."
    y "Here's my phone number. Text me your address?"
    m "I will. Saturday night."
    m "Takeba, I'm elated."
    nar "So the two exchange numbers, Yukari pretends to run to the class she lied about,"
    nar "Mitsuru stays in the cafe to study."
    nar "..."
    hide coffeeShop
    hide ySUMsmile
    hide mSUMsmile
    show transitionBG
    nar "..."
    image mLivingroom = "MitsuruLivingroom.png"
    image mBedroom = "MitsuruBedroom.png"
    show mLivingroom
    nar "..."
    nar "Mitsuru Kirijo's living room. Her sense of luxury has changed a bit since she's started college."
    nar "My guess is because she's now renting and doesn't want to settle any roots too easily, even with her almost infinite budget."
    # This ends the game.
    show mSUMnorm:
        xalign 0.25
        yalign 0.7
    nar "It's her."
    nar "The heiress."
    return
