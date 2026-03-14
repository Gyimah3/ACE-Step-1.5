#!/usr/bin/env python3
"""
Fix two things in zulu_dataset.json:

1. genre field: was incorrectly set to "Zulu" (which is the language, not the genre).
   Correct genres are: Maskandi, Amapiano, Isicathamiya, Kwaito, Mbaqanga, Gqom, etc.

2. captions: phrases like "A Zulu kwaito fusion" made Zulu sound like a genre.
   Rewritten so genre is named explicitly and language is clearly "sung in Zulu".
"""

import json
from pathlib import Path

DATASET_JSON = Path("/Users/gideongyimah/Desktop/Inlaks-api/musicGen/ACE-Step-1.5/datasets/zulu_dataset.json")

# ── Correct genre + rewritten caption per song stem ───────────────────────────
SONG_DATA = {

    "Asimi_sodwa_1": {
        "genre": "Mbaqanga",
        "caption": (
            "An mbaqanga and world music fusion that opens with bass drum, snare, and djembe "
            "interlocking in a tight, march-like groove, accentuated by crisp cowbell and "
            "unified handclaps. Male choral vocals deliver the melody in a powerful, unified "
            "style with call-and-response patterns, all sung in Zulu. The overall mood is "
            "jovial and lively, carrying a spirit of protest, fearlessness, and collective "
            "courage rooted in South African township tradition."
        ),
    },
    "Asimi_sodwa_2": {
        "genre": "Mbaqanga",
        "caption": (
            "An mbaqanga and world music fusion that opens with bass drum, snare, and djembe "
            "interlocking in a tight, march-like groove, accentuated by crisp cowbell and "
            "unified handclaps. Male choral vocals deliver the melody in a powerful, unified "
            "style with call-and-response patterns, all sung in Zulu. The overall mood is "
            "jovial and lively, carrying a spirit of protest, fearlessness, and collective "
            "courage rooted in South African township tradition."
        ),
    },
    "Asimi_sodwa_3": {
        "genre": "Mbaqanga",
        "caption": (
            "An mbaqanga and world music fusion that opens with bass drum, snare, and djembe "
            "interlocking in a tight, march-like groove, accentuated by crisp cowbell and "
            "unified handclaps. Male choral vocals deliver the melody in a powerful, unified "
            "style with call-and-response patterns, all sung in Zulu. The overall mood is "
            "jovial and lively, carrying a spirit of protest, fearlessness, and collective "
            "courage rooted in South African township tradition."
        ),
    },
    "Asimi_sodwa_4": {
        "genre": "Mbaqanga",
        "caption": (
            "An mbaqanga and world music fusion that opens with bass drum, snare, and djembe "
            "interlocking in a tight, march-like groove, accentuated by crisp cowbell and "
            "unified handclaps. Male choral vocals deliver the melody in a powerful, unified "
            "style with call-and-response patterns, all sung in Zulu. The overall mood is "
            "jovial and lively, carrying a spirit of protest, fearlessness, and collective "
            "courage rooted in South African township tradition."
        ),
    },

    "Bhuti": {
        "genre": "Afropop",
        "caption": (
            "A soulful afropop and electro track about betrayal and heartbreak, with lyrics "
            "sung in Zulu. The arrangement moves at a mid-tempo pace built on soft syncopated "
            "drums, hard-hitting synth lines, and atmospheric percussive elements. Soft vocals "
            "and choral riffs are harmonized throughout, creating an intimate and emotionally "
            "layered texture. The vocal delivery is restrained and pensive, conveying deep "
            "sadness and quiet heartbreak."
        ),
    },

    "Ekhaya_1": {
        "genre": "Maskandi Jazz",
        "caption": (
            "A vibrant maskandi jazz fusion that opens with lively maskandi guitar picking and "
            "pulsating isicathamiya harmonies as the rhythmic backbone. Rich jazz brass and "
            "upright bass intertwine with swinging drums, forming a sophisticated, layered "
            "texture. The arrangement dynamically blends Sophiatown swing with traditional "
            "South African melodic sensibilities. An expressive female jazz vocalist sings in "
            "Zulu, delivering the melody with soulful confidence and depth."
        ),
    },
    "Ekhaya_2": {
        "genre": "Maskandi Jazz",
        "caption": (
            "A vibrant maskandi jazz fusion that opens with lively maskandi guitar picking and "
            "pulsating isicathamiya harmonies as the rhythmic backbone. Rich jazz brass and "
            "upright bass intertwine with swinging drums, forming a sophisticated, layered "
            "texture. The arrangement dynamically blends Sophiatown swing with traditional "
            "South African melodic sensibilities. An expressive female jazz vocalist sings in "
            "Zulu, delivering the melody with soulful confidence and depth."
        ),
    },
    "Ekhaya_3": {
        "genre": "Maskandi",
        "caption": (
            "A traditional maskandi track that opens with intricate acoustic guitar picking, "
            "joined by deep bass and indigenous percussion using drums and shakers. Accordion "
            "and concertina add bright, textured harmonics through the verses, while layered "
            "vocal harmonies build depth throughout the arrangement. Sung in Zulu, the track "
            "carries a sombre and meditative quality at a soft, unhurried tempo, with dreamy "
            "atmospheric vocal textures creating a deeply soothing and reflective mood."
        ),
    },
    "Ekhaya_4": {
        "genre": "Maskandi",
        "caption": (
            "A traditional maskandi track that opens with intricate acoustic guitar picking, "
            "joined by deep bass and indigenous percussion using drums and shakers. Accordion "
            "and concertina add bright, textured harmonics through the verses, while layered "
            "vocal harmonies build depth throughout the arrangement. Sung in Zulu, the track "
            "carries a sombre and meditative quality at a soft, unhurried tempo, with dreamy "
            "atmospheric vocal textures creating a deeply soothing and reflective mood."
        ),
    },

    "Emuva_Kwam_Kukho_Abadala_1": {
        "genre": "Amapiano",
        "caption": (
            "An amapiano and kwaito track that opens with hypnotic tribal chants in Zulu layered "
            "over polyrhythmic percussion, immediately establishing a fast-paced, electrifying "
            "energy. Deep kwaito bass grooves and crisp amapiano log drums drive the beat, "
            "blending seamlessly with maskandi guitar riffs. Mumble rap verses drift through in "
            "Zulu before a husky female voice takes command in the chorus. The overall mood is "
            "lively, danceable, and joyfully funky."
        ),
    },
    "Emuva_Kwam_Kukho_Abadala_2": {
        "genre": "Amapiano",
        "caption": (
            "An amapiano and kwaito track that opens with hypnotic tribal chants in Zulu layered "
            "over polyrhythmic percussion, immediately establishing a fast-paced, electrifying "
            "energy. Deep kwaito bass grooves and crisp amapiano log drums drive the beat, "
            "blending seamlessly with maskandi guitar riffs. Mumble rap verses drift through in "
            "Zulu before a husky female voice takes command in the chorus. The overall mood is "
            "lively, danceable, and joyfully funky."
        ),
    },

    "Illanga_1": {
        "genre": "Afro Folk",
        "caption": (
            "An afro folk storytelling track that opens with delicate acoustic fingerpicking "
            "and a supportive upright bass. Sparse percussion underpins the verses, keeping "
            "the atmosphere intimate and close. Subtle string swells lift the bridge, and "
            "background harmonies appear selectively to heighten climactic moments. A soulful "
            "male vocalist sings in Zulu with a pensive, reflective delivery at a slow, "
            "contemplative pace, evoking a sense of quiet hope and emotional honesty."
        ),
    },
    "Illanga_2": {
        "genre": "Afro Folk",
        "caption": (
            "An afro folk storytelling track that opens with delicate acoustic fingerpicking "
            "and a supportive upright bass. Sparse percussion underpins the verses, keeping "
            "the atmosphere intimate and close. Subtle string swells lift the bridge, and "
            "background harmonies appear selectively to heighten climactic moments. A soulful "
            "male vocalist sings in Zulu with a pensive, reflective delivery at a slow, "
            "contemplative pace, evoking a sense of quiet hope and emotional honesty."
        ),
    },
    "Illanga_3": {
        "genre": "Afro Folk",
        "caption": (
            "An afro folk storytelling track that opens with delicate acoustic fingerpicking "
            "and a supportive upright bass. Sparse percussion underpins the verses, keeping "
            "the atmosphere intimate and close. Subtle string swells lift the bridge, and "
            "background harmonies appear selectively to heighten climactic moments. A soulful "
            "male vocalist sings in Zulu with a pensive, reflective delivery at a slow, "
            "contemplative pace, evoking a sense of quiet hope and emotional honesty."
        ),
    },
    "Illanga_4": {
        "genre": "Afro Folk",
        "caption": (
            "An afro folk storytelling track that opens with delicate acoustic fingerpicking "
            "and a supportive upright bass. Sparse percussion underpins the verses, keeping "
            "the atmosphere intimate and close. Subtle string swells lift the bridge, and "
            "background harmonies appear selectively to heighten climactic moments. A soulful "
            "male vocalist sings in Zulu with a pensive, reflective delivery at a slow, "
            "contemplative pace, evoking a sense of quiet hope and emotional honesty."
        ),
    },
    "Illanga_5": {
        "genre": "Afro Folk",
        "caption": (
            "An afro folk storytelling track that opens with delicate acoustic fingerpicking "
            "and a supportive upright bass. Sparse percussion underpins the verses, keeping "
            "the atmosphere intimate and close. Subtle string swells lift the bridge, and "
            "background harmonies appear selectively to heighten climactic moments. A soulful "
            "male vocalist sings in Zulu with a pensive, reflective delivery at a slow, "
            "contemplative pace, evoking a sense of quiet hope and emotional honesty."
        ),
    },
    "Illanga_6": {
        "genre": "Afro Folk",
        "caption": (
            "An afro folk storytelling track that opens with delicate acoustic fingerpicking "
            "and a supportive upright bass. Sparse percussion underpins the verses, keeping "
            "the atmosphere intimate and close. Subtle string swells lift the bridge, and "
            "background harmonies appear selectively to heighten climactic moments. A soulful "
            "male vocalist sings in Zulu with a pensive, reflective delivery at a slow, "
            "contemplative pace, evoking a sense of quiet hope and emotional honesty."
        ),
    },

    "Imali_eJozi_1": {
        "genre": "Kwaito",
        "caption": (
            "A kwaito track driven by a syncopated kwaito rhythm, layering punchy 90s rap "
            "drums, deep basslines, and infectious marimba stabs. Slick rapped verses in Zulu "
            "flow atop crowd-call vocal hooks, creating a propulsive and energetic groove. "
            "The percussion is crisp yet earthy throughout, while classic analog synths weave "
            "in a retro texture. A male vocalist alternates fluidly between rapping and singing "
            "in Zulu, maintaining a confident street energy from start to finish."
        ),
    },
    "Imali_eJozi_2": {
        "genre": "Kwaito",
        "caption": (
            "A kwaito track driven by a syncopated kwaito rhythm, layering punchy 90s rap "
            "drums, deep basslines, and infectious marimba stabs. Slick rapped verses in Zulu "
            "flow atop crowd-call vocal hooks, creating a propulsive and energetic groove. "
            "The percussion is crisp yet earthy throughout, while classic analog synths weave "
            "in a retro texture. A male vocalist alternates fluidly between rapping and singing "
            "in Zulu, maintaining a confident street energy from start to finish."
        ),
    },

    "Izulu_1": {
        "genre": "Isicathamiya",
        "caption": (
            "A traditional isicathamiya a cappella composition sung entirely in Zulu that opens "
            "with a robust men's bassline establishing a deep rhythmic pulse. Clear, resonant "
            "female voices enter in close harmony, creating intricate call-and-response patterns. "
            "Dynamic vocal layering intensifies through the chorus, incorporating group ululations "
            "and tight choral textures. The overall mood is positive, uplifting, and nostalgic, "
            "deeply rooted in the communal singing traditions of South African Zulu culture."
        ),
    },
    "Izulu_2": {
        "genre": "Isicathamiya",
        "caption": (
            "A traditional isicathamiya a cappella composition sung entirely in Zulu that opens "
            "with a robust men's bassline establishing a deep rhythmic pulse. Clear, resonant "
            "female voices enter in close harmony, creating intricate call-and-response patterns. "
            "Dynamic vocal layering intensifies through the chorus, incorporating group ululations "
            "and tight choral textures. The overall mood is positive, uplifting, and nostalgic, "
            "deeply rooted in the communal singing traditions of South African Zulu culture."
        ),
    },
    "Izulu_3": {
        "genre": "Maskandi",
        "caption": (
            "A maskandi and isicathamiya fusion where rich maskandi guitar lines intertwine with "
            "smooth, layered isicathamiya vocal harmonies over a steady, percussive rhythm "
            "created by muted drums and handclaps. The arrangement alternates between "
            "call-and-response choral sections sung in Zulu and expressive lead guitar breaks, "
            "maintaining an uplifting and organic soundscape throughout. Male voices carry the "
            "choral harmonies with warmth and depth, and the mood is nostalgic and gently sombre."
        ),
    },
    "Izulu_4": {
        "genre": "Maskandi",
        "caption": (
            "A maskandi and isicathamiya fusion where rich maskandi guitar lines intertwine with "
            "smooth, layered isicathamiya vocal harmonies over a steady, percussive rhythm "
            "created by muted drums and handclaps. The arrangement alternates between "
            "call-and-response choral sections sung in Zulu and expressive lead guitar breaks, "
            "maintaining an uplifting and organic soundscape throughout. Male voices carry the "
            "choral harmonies with warmth and depth, and the mood is nostalgic and gently sombre."
        ),
    },

    "Izwi_Lomculo_1": {
        "genre": "Afrobeat",
        "caption": (
            "A lively afrobeat and electronic jazz fusion that kicks off with syncopated "
            "percussion and bubbling bass, layered with sparkling synths and jazzy Rhodes stabs. "
            "Saxophone improvisations weave through the electronic beats and polyrhythms, adding "
            "improvisational warmth to the production. The bridge features a breakdown with muted "
            "trumpets before building back to a vibrant, dance-ready finale. A soulful female "
            "vocalist sings in Zulu with a chilled, inspiring delivery that floats effortlessly "
            "over the groovy mid-tempo beat."
        ),
    },
    "Izwi_Lomculo_2": {
        "genre": "Afrobeat",
        "caption": (
            "A lively afrobeat and electronic jazz fusion that kicks off with syncopated "
            "percussion and bubbling bass, layered with sparkling synths and jazzy Rhodes stabs. "
            "Saxophone improvisations weave through the electronic beats and polyrhythms, adding "
            "improvisational warmth to the production. The bridge features a breakdown with muted "
            "trumpets before building back to a vibrant, dance-ready finale. A soulful female "
            "vocalist sings in Zulu with a chilled, inspiring delivery that floats effortlessly "
            "over the groovy mid-tempo beat."
        ),
    },

    "MASKANDI_Ngihamba_Nezikhathi_1": {
        "genre": "Maskandi",
        "caption": (
            "A modern maskandi and mbaqanga track where a full band fuses punchy mbaqanga guitar, "
            "syncopated basslines, and driving drum kit patterns with traditional maskandi picking "
            "and rhythmic vocal harmonies sung in Zulu. Accordion and occasional synth textures "
            "layer in, creating a fresh and danceable groove enriched by vibrant call-and-response "
            "passages. The overall feel is upbeat, mid-tempo, and hopeful, led by an expressive "
            "female vocalist delivering a contemporary take on traditional South African forms."
        ),
    },
    "MASKANDI_Ngihamba_Nezikhathi_2": {
        "genre": "Maskandi",
        "caption": (
            "A modern maskandi and mbaqanga track where a full band fuses punchy mbaqanga guitar, "
            "syncopated basslines, and driving drum kit patterns with traditional maskandi picking "
            "and rhythmic vocal harmonies sung in Zulu. Accordion and occasional synth textures "
            "layer in, creating a fresh and danceable groove enriched by vibrant call-and-response "
            "passages. The overall feel is upbeat, mid-tempo, and hopeful, led by an expressive "
            "female vocalist delivering a contemporary take on traditional South African forms."
        ),
    },

    "Ngihamba_Nezikhathi_1": {
        "genre": "Mbaqanga",
        "caption": (
            "A fast-paced mbaqanga and maskandi track that opens with rhythmic acoustic guitar, "
            "deep bass, and lively drums overlaid by elastic lead guitar licks. Accordion and "
            "snare rolls punctuate the transitions with expressive flair, while a band of male "
            "and female voices deliver vibrant call-and-response passages sung in Zulu. The "
            "energy is relentless and joyful, deeply rooted in the living traditions of South "
            "African township music."
        ),
    },
    "Ngihamba_Nezikhathi_2": {
        "genre": "Mbaqanga",
        "caption": (
            "A fast-paced mbaqanga and maskandi track that opens with rhythmic acoustic guitar, "
            "deep bass, and lively drums overlaid by elastic lead guitar licks. Accordion and "
            "snare rolls punctuate the transitions with expressive flair, while a band of male "
            "and female voices deliver vibrant call-and-response passages sung in Zulu. The "
            "energy is relentless and joyful, deeply rooted in the living traditions of South "
            "African township music."
        ),
    },

    "Ngipholile_1": {
        "genre": "Kwaito",
        "caption": (
            "A kwaito and maskandi fusion that bursts open with punchy big band brass, syncopated "
            "drums, and dazzling piano. Maskandi-inspired guitar lines wind through layered vocal "
            "harmonies, while mbaqanga bass grooves keep the momentum driving forward. Percussion "
            "featuring bells, shakers, and claps adds theatrical flair well-suited for stage "
            "performance. A male rapper delivers confident verses in Zulu over kwaito and "
            "old-school trap influences, creating a lively, funky, and dance-floor-ready mood."
        ),
    },
    "Ngipholile_2": {
        "genre": "Kwaito",
        "caption": (
            "A kwaito and maskandi fusion that bursts open with punchy big band brass, syncopated "
            "drums, and dazzling piano. Maskandi-inspired guitar lines wind through layered vocal "
            "harmonies, while mbaqanga bass grooves keep the momentum driving forward. Percussion "
            "featuring bells, shakers, and claps adds theatrical flair well-suited for stage "
            "performance. A male rapper delivers confident verses in Zulu over kwaito and "
            "old-school trap influences, creating a lively, funky, and dance-floor-ready mood."
        ),
    },

    "Ngiseyinthombi_1": {
        "genre": "Amapiano",
        "caption": (
            "An amapiano and maskandi fusion that blends rolling log drums and syncopated "
            "percussion with traditional maskandi guitar riffs and indigenous rhythms. Verses "
            "flow with dynamic rap delivered in Zulu over electronic synth lines, led by a "
            "female vocalist. An explosive chorus erupts with a powerful multi-voice choir, "
            "amplifying a revolutionary and anthemic spirit. The arrangement shifts dramatically "
            "between intimate rap verses and grand, cinematic choral moments."
        ),
    },
    "Ngiseyinthombi_2": {
        "genre": "Amapiano",
        "caption": (
            "An amapiano and maskandi fusion that blends rolling log drums and syncopated "
            "percussion with traditional maskandi guitar riffs and indigenous rhythms. Verses "
            "flow with dynamic rap delivered in Zulu over electronic synth lines, led by a "
            "female vocalist. An explosive chorus erupts with a powerful multi-voice choir, "
            "amplifying a revolutionary and anthemic spirit. The arrangement shifts dramatically "
            "between intimate rap verses and grand, cinematic choral moments."
        ),
    },
    "Ngiseyinthombi_3": {
        "genre": "Amapiano",
        "caption": (
            "An amapiano and maskandi fusion that blends rolling log drums and syncopated "
            "percussion with traditional maskandi guitar riffs and indigenous rhythms. Verses "
            "flow with dynamic rap delivered in Zulu over electronic synth lines, led by a "
            "female vocalist. An explosive chorus erupts with a powerful multi-voice choir, "
            "amplifying a revolutionary and anthemic spirit. The arrangement shifts dramatically "
            "between intimate rap verses and grand, cinematic choral moments."
        ),
    },
    "Ngiseyinthombi_4": {
        "genre": "Amapiano",
        "caption": (
            "An amapiano and maskandi fusion that blends rolling log drums and syncopated "
            "percussion with traditional maskandi guitar riffs and indigenous rhythms. Verses "
            "flow with dynamic rap delivered in Zulu over electronic synth lines, led by a "
            "female vocalist. An explosive chorus erupts with a powerful multi-voice choir, "
            "amplifying a revolutionary and anthemic spirit. The arrangement shifts dramatically "
            "between intimate rap verses and grand, cinematic choral moments."
        ),
    },
    "Ngiseyinthombi_5": {
        "genre": "Amapiano",
        "caption": (
            "An amapiano and maskandi fusion that blends rolling log drums and syncopated "
            "percussion with traditional maskandi guitar riffs and indigenous rhythms. Verses "
            "flow with dynamic rap delivered in Zulu over electronic synth lines, led by a "
            "female vocalist. An explosive chorus erupts with a powerful multi-voice choir, "
            "amplifying a revolutionary and anthemic spirit. The arrangement shifts dramatically "
            "between intimate rap verses and grand, cinematic choral moments."
        ),
    },

    "Ngiyakhala_1": {
        "genre": "Kwaito",
        "caption": (
            "A kwaito and maskandi track that opens with a pulsating groove built from "
            "interlocking kwaito beats and maskandi guitar riffs. Traditional percussion and "
            "layered harmonies add richness and depth, while soaring soulful female vocals "
            "weave through folk-inspired melodies sung in Zulu. The epic arrangement builds "
            "to a crescendo featuring rhythmic ululation and dynamic call-and-response vocals, "
            "supported by rich, organic textures and subtle electronic accents."
        ),
    },
    "Ngiyakhala_2": {
        "genre": "Kwaito",
        "caption": (
            "A kwaito and maskandi track that opens with a pulsating groove built from "
            "interlocking kwaito beats and maskandi guitar riffs. Traditional percussion and "
            "layered harmonies add richness and depth, while soaring soulful female vocals "
            "weave through folk-inspired melodies sung in Zulu. The epic arrangement builds "
            "to a crescendo featuring rhythmic ululation and dynamic call-and-response vocals, "
            "supported by rich, organic textures and subtle electronic accents."
        ),
    },
    "Ngiyakhala_4": {
        "genre": "Amapiano",
        "caption": (
            "An amapiano and maskandi track where amapiano keys and log drums establish the "
            "groove as intricate maskandi guitar introduces the verses, carried by soulful "
            "vocal phrasing from a male vocalist singing in Zulu. The chorus erupts with an "
            "explosive multi-voice choir and electrified synths, seamlessly blending traditional "
            "South African textures with electronic production. The outro swells into epic, "
            "layered soul harmonies. The energy is fast-paced, lively, and revolutionary in "
            "spirit throughout."
        ),
    },
    "Ngiyakhala_5": {
        "genre": "Amapiano",
        "caption": (
            "An amapiano and maskandi track where amapiano keys and log drums establish the "
            "groove as intricate maskandi guitar introduces the verses, carried by soulful "
            "vocal phrasing from a female vocalist singing in Zulu. The chorus erupts with an "
            "explosive multi-voice choir and electrified synths, seamlessly blending traditional "
            "South African textures with electronic production. The outro swells into epic, "
            "layered soul harmonies. The energy is fast-paced, lively, and revolutionary in "
            "spirit throughout."
        ),
    },
    "Ngiyakhala_6": {
        "genre": "Amapiano",
        "caption": (
            "An amapiano and maskandi track where amapiano keys and log drums establish the "
            "groove as intricate maskandi guitar introduces the verses, carried by soulful "
            "vocal phrasing from a female vocalist singing in Zulu. The chorus erupts with an "
            "explosive multi-voice choir and electrified synths, seamlessly blending traditional "
            "South African textures with electronic production. The outro swells into epic, "
            "layered soul harmonies. The energy is fast-paced, lively, and revolutionary in "
            "spirit throughout."
        ),
    },

    "Qhakuva": {
        "genre": "Electro Rap",
        "caption": (
            "An electro and kwaito rap track built on syncopated synth lines, dark basslines, "
            "and a fast, driving drum pattern. Soft synth textures provide atmospheric depth "
            "beneath a dynamic arrangement that moves between spoken word passages and sung "
            "vocal sections. Male and female vocalists trade parts throughout in Zulu, blending "
            "contemporary electronic production with elements rooted in traditional South "
            "African music. The mood is intense, hypnotic, and layered with cultural identity."
        ),
    },

    "Sikhona_1": {
        "genre": "Kwaito",
        "caption": (
            "A kwaito and maskandi fusion that bursts open with punchy big band brass, syncopated "
            "drums, and dazzling piano. Maskandi-inspired guitar lines wind through layered vocal "
            "harmonies, while mbaqanga bass grooves maintain the driving momentum. Percussion "
            "featuring bells, shakers, and claps adds a theatrical, celebratory energy. A female "
            "vocalist delivers the lead in Zulu over kwaito, pop, and house influences, creating "
            "a mood that is jovial, hopeful, and vibrantly uplifting."
        ),
    },
    "Sikhona_2": {
        "genre": "Kwaito",
        "caption": (
            "A kwaito and maskandi fusion that bursts open with punchy big band brass, syncopated "
            "drums, and dazzling piano. Maskandi-inspired guitar lines wind through layered vocal "
            "harmonies, while mbaqanga bass grooves maintain the driving momentum. Percussion "
            "featuring bells, shakers, and claps adds a theatrical, celebratory energy. A female "
            "vocalist delivers the lead in Zulu over kwaito, pop, and house influences, creating "
            "a mood that is jovial, hopeful, and vibrantly uplifting."
        ),
    },

    "Siphuma_Emsamo_1": {
        "genre": "Gqom",
        "caption": (
            "A gqom and kwaito club track that fuses kwaito's laid-back groove with punchy "
            "electronic synths, tight house kick-clap combinations, and gqom's dark, repetitive "
            "bass stabs. Layers of chopped vocal samples from a female vocalist singing in Zulu "
            "interplay over syncopated percussion, creating a hypnotic energy that evolves and "
            "shifts with each drop. The mood is mellow and smooth at a mid-tempo pace, with an "
            "undercurrent of emotional depth that draws the listener inward."
        ),
    },
    "Siphuma_Emsamo_2": {
        "genre": "Gqom",
        "caption": (
            "A gqom and kwaito club track that fuses kwaito's laid-back groove with punchy "
            "electronic synths, tight house kick-clap combinations, and gqom's dark, repetitive "
            "bass stabs. Layers of chopped vocal samples from a female vocalist singing in Zulu "
            "interplay over syncopated percussion, creating a hypnotic energy that evolves and "
            "shifts with each drop. The mood is mellow and smooth at a mid-tempo pace, with an "
            "undercurrent of emotional depth that draws the listener inward."
        ),
    },

    "Soweto_female_1": {
        "genre": "Kwaito",
        "caption": (
            "A kwaito and hip-hop track that blends deep house-inspired bass, syncopated "
            "percussion, and marimba riffs over spacious synth chords. Vocal lines alternate "
            "between rapped verses and chanted hooks sung in Zulu, layered with group "
            "call-and-response patterns that give the track a communal, street-level energy. "
            "The mood is jovial and chilled, with an optimistic and hopeful spirit that carries "
            "through the entire track."
        ),
    },
    "Soweto_female_2": {
        "genre": "Kwaito",
        "caption": (
            "A kwaito and hip-hop track that blends deep house-inspired bass, syncopated "
            "percussion, and marimba riffs over spacious synth chords. Vocal lines alternate "
            "between rapped verses and chanted hooks sung in Zulu, layered with group "
            "call-and-response patterns that give the track a communal, street-level energy. "
            "The mood is jovial and chilled, with an optimistic and hopeful spirit that carries "
            "through the entire track."
        ),
    },
    "Soweto_male_1": {
        "genre": "Kwaito",
        "caption": (
            "A kwaito and hip-hop track that blends deep house-inspired bass, syncopated "
            "percussion, and marimba riffs over spacious synth chords. A male vocalist alternates "
            "between rapped verses and chanted hooks sung in Zulu, layered with group "
            "call-and-response patterns that give the track a communal, street-level energy. "
            "The mood is jovial and chilled, with an optimistic and hopeful spirit that carries "
            "through the entire track."
        ),
    },
    "Soweto_male_2": {
        "genre": "Kwaito",
        "caption": (
            "A kwaito and hip-hop track that blends deep house-inspired bass, syncopated "
            "percussion, and marimba riffs over spacious synth chords. A male vocalist alternates "
            "between rapped verses and chanted hooks sung in Zulu, layered with group "
            "call-and-response patterns that give the track a communal, street-level energy. "
            "The mood is jovial and chilled, with an optimistic and hopeful spirit that carries "
            "through the entire track."
        ),
    },

    "Umhlaba_1": {
        "genre": "Kwaito",
        "caption": (
            "A kwaito and maskandi track that opens with traditional percussion and maskandi "
            "guitar establishing a vibrant and grounded groove. Lush choral harmonies enter "
            "to add fullness, while marabi-inspired keyboards and rolling bass lines propel "
            "the kwaito rhythm forward. Call-and-response vocals sung in Zulu bring an anthemic "
            "communal spirit to the arrangement, with layered hand percussion and electric "
            "elements interwoven for modern energy. A female vocalist leads the choral "
            "arrangement with warmth and conviction."
        ),
    },
    "Umhlaba_2": {
        "genre": "Kwaito",
        "caption": (
            "A kwaito and maskandi track that opens with traditional percussion and maskandi "
            "guitar establishing a vibrant and grounded groove. Lush choral harmonies enter "
            "to add fullness, while marabi-inspired keyboards and rolling bass lines propel "
            "the kwaito rhythm forward. Call-and-response vocals sung in Zulu bring an anthemic "
            "communal spirit to the arrangement, with layered hand percussion and electric "
            "elements interwoven for modern energy. A female vocalist leads the choral "
            "arrangement with warmth and conviction."
        ),
    },

    "Umhlaba_wa_bo_Koko_1": {
        "genre": "Maskandi",
        "caption": (
            "A maskandi and isicathamiya fusion that opens with punchy big band brass, syncopated "
            "drums, and dazzling piano. Maskandi guitar lines weave through layered vocal "
            "harmonies rooted in traditional South African and country influences, while mbaqanga "
            "bass grooves keep the energy moving forward. Percussion featuring bells, shakers, "
            "and claps adds theatrical warmth. A female vocalist sings in Zulu with a heartfelt "
            "and sombre delivery, navigating the emotional space between grief and quiet hope."
        ),
    },
    "Umhlaba_wa_bo_Koko_2": {
        "genre": "Maskandi",
        "caption": (
            "A maskandi and isicathamiya fusion that opens with punchy big band brass, syncopated "
            "drums, and dazzling piano. Maskandi guitar lines weave through layered vocal "
            "harmonies rooted in traditional South African and country influences, while mbaqanga "
            "bass grooves keep the energy moving forward. Percussion featuring bells, shakers, "
            "and claps adds theatrical warmth. A female vocalist sings in Zulu with a heartfelt "
            "and sombre delivery, navigating the emotional space between grief and quiet hope."
        ),
    },
    "Umhlaba_wa_bo_Koko_3": {
        "genre": "Maskandi",
        "caption": (
            "A maskandi and isicathamiya fusion that opens with punchy big band brass, syncopated "
            "drums, and dazzling piano. Maskandi guitar lines weave through layered vocal "
            "harmonies rooted in traditional South African and country influences, while mbaqanga "
            "bass grooves keep the energy moving forward. Percussion featuring bells, shakers, "
            "and claps adds theatrical warmth. A female vocalist sings in Zulu with a heartfelt "
            "and sombre delivery, navigating the emotional space between grief and quiet hope."
        ),
    },
    "Umhlaba_wa_bo_Koko_4": {
        "genre": "Maskandi",
        "caption": (
            "A maskandi and isicathamiya fusion that opens with punchy big band brass, syncopated "
            "drums, and dazzling piano. Maskandi guitar lines weave through layered vocal "
            "harmonies rooted in traditional South African and country influences, while mbaqanga "
            "bass grooves keep the energy moving forward. Percussion featuring bells, shakers, "
            "and claps adds theatrical warmth. A female vocalist sings in Zulu with a heartfelt "
            "and sombre delivery, navigating the emotional space between grief and quiet hope."
        ),
    },
    "Umhlaba_wa_bo_Koko_5": {
        "genre": "Maskandi",
        "caption": (
            "A maskandi and isicathamiya fusion that opens with punchy big band brass, syncopated "
            "drums, and dazzling piano. Maskandi guitar lines weave through layered vocal "
            "harmonies rooted in traditional South African and country influences, while mbaqanga "
            "bass grooves keep the energy moving forward. Percussion featuring bells, shakers, "
            "and claps adds theatrical warmth. A male vocalist sings in Zulu with a heartfelt "
            "and sombre delivery, navigating the emotional space between grief and quiet hope."
        ),
    },
    "Umhlaba_wa_bo_Koko_6": {
        "genre": "Maskandi",
        "caption": (
            "A maskandi and isicathamiya track opening with intricate acoustic guitar picking "
            "and concertina characteristic of the maskandi style, with the groove established "
            "by gently syncopated percussion and upright bass. Isicathamiya-style vocal harmonies "
            "enter, layered for depth and blending with country pedal steel influences. Traditional "
            "South African musical elements punctuate the arrangement throughout, with interlocking "
            "guitar parts and expressive vocal interplay sung in Zulu leading into richly textured "
            "instrumental breaks."
        ),
    },
    "Umhlaba_wa_bo_Koko_7": {
        "genre": "Maskandi",
        "caption": (
            "A maskandi and isicathamiya track opening with intricate acoustic guitar picking "
            "and concertina characteristic of the maskandi style, with the groove established "
            "by gently syncopated percussion and upright bass. Isicathamiya-style vocal harmonies "
            "enter, layered for depth and blending with country pedal steel influences. Traditional "
            "South African musical elements punctuate the arrangement throughout, with interlocking "
            "guitar parts and expressive vocal interplay sung in Zulu leading into richly textured "
            "instrumental breaks."
        ),
    },

    "Uthando_1": {
        "genre": "Maskandi",
        "caption": (
            "A traditional maskandi ballad led by expressive guitar picking and concertina lines, "
            "underscored by steady percussion using African drums and rattles. Call-and-response "
            "vocal patterns sung in Zulu carry the verses, with layered harmonies accentuating "
            "the hooks throughout. The organic, earthy textures give the track a raw and rhythmic "
            "pulse. A female vocalist delivers with meditative depth at a slow, chilled tempo, "
            "evoking heartfelt nostalgia and a deep connection to South African Zulu musical "
            "heritage."
        ),
    },
    "Uthando_2": {
        "genre": "Maskandi",
        "caption": (
            "A traditional maskandi ballad led by expressive guitar picking and concertina lines, "
            "underscored by steady percussion using African drums and rattles. Call-and-response "
            "vocal patterns sung in Zulu carry the verses, with layered harmonies accentuating "
            "the hooks throughout. The organic, earthy textures give the track a raw and rhythmic "
            "pulse. A female vocalist delivers with meditative depth at a slow, chilled tempo, "
            "evoking heartfelt nostalgia and a deep connection to South African Zulu musical "
            "heritage."
        ),
    },

    "Zulu_1": {
        "genre": "Maskandi",
        "caption": (
            "A maskandi track that opens with rhythmic acoustic guitar accented by traditional "
            "isiZulu drum patterns. Male and female choral vocals enter in layered call-and-response "
            "patterns sung in Zulu, supported by bass and concertina. Sections feature traditional "
            "mouth bow and intermittent handclaps that add a luminous, resonant texture to the "
            "arrangement. The mood is meditative and chilled, moving at a slow, thoughtful tempo "
            "with heartfelt, poetic warmth rooted in Zulu musical tradition."
        ),
    },
    "Zulu_2": {
        "genre": "Maskandi",
        "caption": (
            "A maskandi track that opens with rhythmic acoustic guitar accented by traditional "
            "isiZulu drum patterns. Male and female choral vocals enter in layered call-and-response "
            "patterns sung in Zulu, supported by bass and concertina. Sections feature traditional "
            "mouth bow and intermittent handclaps that add a luminous, resonant texture to the "
            "arrangement. The mood is meditative and chilled, moving at a slow, thoughtful tempo "
            "with heartfelt, poetic warmth rooted in Zulu musical tradition."
        ),
    },
}


def main():
    data = json.loads(DATASET_JSON.read_text(encoding="utf-8"))
    samples = data["samples"]

    updated = 0
    missing = []

    for s in samples:
        stem = s["filename"].replace(".mp3", "")
        if stem in SONG_DATA:
            s["genre"] = SONG_DATA[stem]["genre"]
            s["caption"] = SONG_DATA[stem]["caption"]
            updated += 1
        else:
            missing.append(s["filename"])

    data["samples"] = samples
    DATASET_JSON.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Updated {updated} / {len(samples)} samples.")
    if missing:
        print(f"WARNING — not found in map: {missing}")
    else:
        print("All 63 samples updated successfully.\n")

    # Print genre distribution
    genres = {}
    for s in samples:
        g = s.get("genre", "Unknown")
        genres[g] = genres.get(g, 0) + 1
    print("Genre distribution:")
    for g, count in sorted(genres.items(), key=lambda x: -x[1]):
        print(f"  {g:25s} {count} songs")


if __name__ == "__main__":
    main()
