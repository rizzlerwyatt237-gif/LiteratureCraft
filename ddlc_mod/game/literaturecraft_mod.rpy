# LiteratureCraft - a small DDLC fan-mod story
# Drop this file into DDLC's game/ folder (after backing up your save directory).
# This mod intentionally contains no DDLC game assets.

init python:
    lc_title = "LiteratureCraft"

label literaturecraft_start:
    scene bg club_day
    with dissolve

    show sayori 1a at t11
    s "Hey! You came!"
    s "I've been thinking about the Literature Club..."

    show sayori 1c at t11
    s "What if we made a place where our stories could actually become worlds?"

    show monika 1b at t21
    show sayori 1c at t22
    m "A world built from words?"
    m "I like that idea."

    show natsuki 1c at t21
    show monika 1b at t22
    n "As long as nobody makes me read a 500-page instruction manual."

    show yuri 1a at t21
    show natsuki 1c at t22
    y "Perhaps we could begin with something simple..."
    y "A small home. A small garden. And a place to write."

    hide yuri
    hide natsuki
    hide monika
    show sayori 1d at t11
    s "Then it's settled!"
    s "Welcome to LiteratureCraft!"

    menu:
        "Build the club house":
            jump literaturecraft_build
        "Ask Monika what she has planned":
            jump literaturecraft_monika

label literaturecraft_build:
    show sayori 1a at t11
    s "First, we need a table, some books, and lots of snacks!"
    s "Then we'll make the biggest club house ever."
    "The Literature Club gets to work."
    "To continue the story, return to the clubroom another day."
    return

label literaturecraft_monika:
    show monika 1d at t11
    m "I have a feeling our little project might become something much bigger."
    m "For now, let's just enjoy building it together."
    "Monika smiles."
    return
