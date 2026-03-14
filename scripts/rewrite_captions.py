#!/usr/bin/env python3
"""
Rewrite all captions in zulu_dataset.json to full narrative paragraph style,
matching ACE-Step 1.5's training data format (no comma tag dumps).

ACE-Step 1.5 base model was trained on descriptive paragraphs like:
  "An explosive, high-energy pop-rock track driven by a powerful drum beat...
   A passionate male vocal soars over the top... The track concludes with..."

NOT comma tag lists like:
  "zulu, maskandi, female vocal, upbeat, mid tempo, hopeful"
"""

import json
from pathlib import Path

DATASET_JSON = Path("/Users/gideongyimah/Desktop/Inlaks-api/musicGen/ACE-Step-1.5/datasets/zulu_dataset.json")

# Full narrative captions keyed by filename stem (without .mp3)
CAPTIONS = {
    # ── Asimi_sodwa ────────────────────────────────────────────────────────
    "Asimi_sodwa_1": (
        "A Zulu musical fusion song that opens with bass drum, snare, and djembe interlocking "
        "in a tight, march-like groove, accentuated by crisp cowbell and unified handclaps. "
        "Male choral vocals deliver the melody in a powerful, unified style rooted in mbaqanga "
        "and world music traditions. The arrangement maintains a driving communal energy with "
        "call-and-response patterns, all sung in Zulu. The overall mood is jovial and lively, "
        "carrying a spirit of protest, fearlessness, and collective courage."
    ),
    "Asimi_sodwa_2": (
        "A Zulu musical fusion song that opens with bass drum, snare, and djembe interlocking "
        "in a tight, march-like groove, accentuated by crisp cowbell and unified handclaps. "
        "Male choral vocals deliver the melody in a powerful, unified style rooted in mbaqanga "
        "and world music traditions. The arrangement maintains a driving communal energy with "
        "call-and-response patterns, all sung in Zulu. The overall mood is jovial and lively, "
        "carrying a spirit of protest, fearlessness, and collective courage."
    ),
    "Asimi_sodwa_3": (
        "A Zulu musical fusion song that opens with bass drum, snare, and djembe interlocking "
        "in a tight, march-like groove, accentuated by crisp cowbell and unified handclaps. "
        "Male choral vocals deliver the melody in a powerful, unified style rooted in mbaqanga "
        "and world music traditions. The arrangement maintains a driving communal energy with "
        "call-and-response patterns, all sung in Zulu. The overall mood is jovial and lively, "
        "carrying a spirit of protest, fearlessness, and collective courage."
    ),
    "Asimi_sodwa_4": (
        "A Zulu musical fusion song that opens with bass drum, snare, and djembe interlocking "
        "in a tight, march-like groove, accentuated by crisp cowbell and unified handclaps. "
        "Male choral vocals deliver the melody in a powerful, unified style rooted in mbaqanga "
        "and world music traditions. The arrangement maintains a driving communal energy with "
        "call-and-response patterns, all sung in Zulu. The overall mood is jovial and lively, "
        "carrying a spirit of protest, fearlessness, and collective courage."
    ),

    # ── Bhuti ─────────────────────────────────────────────────────────────
    "Bhuti": (
        "A soulful afropop and electro track about betrayal and heartbreak, sung in Zulu. "
        "The arrangement moves at a mid-tempo pace, built on soft syncopated drums, "
        "hard-hitting synth lines, and atmospheric percussive elements. Soft vocals and "
        "choral riffs are harmonized throughout, creating an intimate and emotionally layered "
        "texture. The vocal delivery is restrained and pensive, conveying deep sadness and "
        "quiet heartbreak rooted in the world music and soul traditions."
    ),

    # ── Ekhaya ────────────────────────────────────────────────────────────
    "Ekhaya_1": (
        "A vibrant Zulu jazz fusion that opens with lively maskandi guitar picking and "
        "pulsating isicathamiya harmonies as the rhythmic backbone. Rich jazz brass and "
        "upright bass intertwine with swinging drums, forming a sophisticated, layered texture. "
        "The arrangement dynamically blends Sophiatown swing with traditional Zulu melodic "
        "sensibilities. An expressive female jazz vocalist sings in Zulu, delivering the "
        "melody with soulful confidence and depth."
    ),
    "Ekhaya_2": (
        "A vibrant Zulu jazz fusion that opens with lively maskandi guitar picking and "
        "pulsating isicathamiya harmonies as the rhythmic backbone. Rich jazz brass and "
        "upright bass intertwine with swinging drums, forming a sophisticated, layered texture. "
        "The arrangement dynamically blends Sophiatown swing with traditional Zulu melodic "
        "sensibilities. An expressive female jazz vocalist sings in Zulu, delivering the "
        "melody with soulful confidence and depth."
    ),
    "Ekhaya_3": (
        "The song opens with intricate acoustic guitar picking in traditional maskandi style, "
        "joined by deep bass and indigenous Zulu percussion using drums and shakers. Accordion "
        "and concertina add bright, textured harmonics through the verses, while layered vocal "
        "harmonies highlight the traditional Zulu character of the arrangement. Sung in Zulu, "
        "the track carries a sombre and meditative quality at a soft, unhurried tempo, with "
        "dreamy, atmospheric vocal textures creating a deeply soothing and reflective mood."
    ),
    "Ekhaya_4": (
        "The song opens with intricate acoustic guitar picking in traditional maskandi style, "
        "joined by deep bass and indigenous Zulu percussion using drums and shakers. Accordion "
        "and concertina add bright, textured harmonics through the verses, while layered vocal "
        "harmonies highlight the traditional Zulu character of the arrangement. Sung in Zulu, "
        "the track carries a sombre and meditative quality at a soft, unhurried tempo, with "
        "dreamy, atmospheric vocal textures creating a deeply soothing and reflective mood."
    ),

    # ── Emuva_Kwam_Kukho_Abadala ──────────────────────────────────────────
    "Emuva_Kwam_Kukho_Abadala_1": (
        "The track opens with hypnotic Zulu tribal chants layered over polyrhythmic percussion, "
        "immediately establishing a fast-paced, electrifying energy. Deep kwaito bass grooves "
        "and crisp amapiano log drums drive the beat, blending seamlessly with maskandi guitar "
        "riffs. Mumble rap verses in Zulu drift through the verses before a husky female voice "
        "takes command in the chorus. The overall mood is lively, danceable, and joyfully funky."
    ),
    "Emuva_Kwam_Kukho_Abadala_2": (
        "The track opens with hypnotic Zulu tribal chants layered over polyrhythmic percussion, "
        "immediately establishing a fast-paced, electrifying energy. Deep kwaito bass grooves "
        "and crisp amapiano log drums drive the beat, blending seamlessly with maskandi guitar "
        "riffs. Mumble rap verses in Zulu drift through the verses before a husky female voice "
        "takes command in the chorus. The overall mood is lively, danceable, and joyfully funky."
    ),

    # ── Illanga ───────────────────────────────────────────────────────────
    "Illanga_1": (
        "A Zulu folk storytelling track that opens with delicate acoustic fingerpicking and a "
        "supportive upright bass. Sparse percussion underpins the verses, keeping the atmosphere "
        "intimate and close. Subtle string swells lift the bridge, and background harmonies "
        "appear selectively to heighten climactic moments without disturbing the personal focus. "
        "A soulful male vocalist sings in Zulu with a pensive, reflective delivery at a slow, "
        "contemplative pace, evoking a sense of quiet hope and emotional honesty."
    ),
    "Illanga_2": (
        "A Zulu folk storytelling track that opens with delicate acoustic fingerpicking and a "
        "supportive upright bass. Sparse percussion underpins the verses, keeping the atmosphere "
        "intimate and close. Subtle string swells lift the bridge, and background harmonies "
        "appear selectively to heighten climactic moments without disturbing the personal focus. "
        "A soulful male vocalist sings in Zulu with a pensive, reflective delivery at a slow, "
        "contemplative pace, evoking a sense of quiet hope and emotional honesty."
    ),
    "Illanga_3": (
        "A Zulu folk storytelling track that opens with delicate acoustic fingerpicking and a "
        "supportive upright bass. Sparse percussion underpins the verses, keeping the atmosphere "
        "intimate and close. Subtle string swells lift the bridge, and background harmonies "
        "appear selectively to heighten climactic moments without disturbing the personal focus. "
        "A soulful male vocalist sings in Zulu with a pensive, reflective delivery at a slow, "
        "contemplative pace, evoking a sense of quiet hope and emotional honesty."
    ),
    "Illanga_4": (
        "A Zulu folk storytelling track that opens with delicate acoustic fingerpicking and a "
        "supportive upright bass. Sparse percussion underpins the verses, keeping the atmosphere "
        "intimate and close. Subtle string swells lift the bridge, and background harmonies "
        "appear selectively to heighten climactic moments without disturbing the personal focus. "
        "A soulful male vocalist sings in Zulu with a pensive, reflective delivery at a slow, "
        "contemplative pace, evoking a sense of quiet hope and emotional honesty."
    ),
    "Illanga_5": (
        "A Zulu folk storytelling track that opens with delicate acoustic fingerpicking and a "
        "supportive upright bass. Sparse percussion underpins the verses, keeping the atmosphere "
        "intimate and close. Subtle string swells lift the bridge, and background harmonies "
        "appear selectively to heighten climactic moments without disturbing the personal focus. "
        "A soulful male vocalist sings in Zulu with a pensive, reflective delivery at a slow, "
        "contemplative pace, evoking a sense of quiet hope and emotional honesty."
    ),
    "Illanga_6": (
        "A Zulu folk storytelling track that opens with delicate acoustic fingerpicking and a "
        "supportive upright bass. Sparse percussion underpins the verses, keeping the atmosphere "
        "intimate and close. Subtle string swells lift the bridge, and background harmonies "
        "appear selectively to heighten climactic moments without disturbing the personal focus. "
        "A soulful male vocalist sings in Zulu with a pensive, reflective delivery at a slow, "
        "contemplative pace, evoking a sense of quiet hope and emotional honesty."
    ),

    # ── Imali_eJozi ───────────────────────────────────────────────────────
    "Imali_eJozi_1": (
        "Driven by a syncopated kwaito rhythm, this Zulu street music track layers punchy "
        "90s rap drums, deep basslines, and infectious marimba stabs. Slick rapped verses "
        "in Zulu flow atop crowd-call vocal hooks, creating a propulsive and energetic groove. "
        "The percussion is crisp yet earthy throughout, while classic analog synths weave in "
        "a retro texture. A male vocalist alternates fluidly between rapping and singing, "
        "maintaining a confident and lively energy from start to finish."
    ),
    "Imali_eJozi_2": (
        "Driven by a syncopated kwaito rhythm, this Zulu street music track layers punchy "
        "90s rap drums, deep basslines, and infectious marimba stabs. Slick rapped verses "
        "in Zulu flow atop crowd-call vocal hooks, creating a propulsive and energetic groove. "
        "The percussion is crisp yet earthy throughout, while classic analog synths weave in "
        "a retro texture. A male vocalist alternates fluidly between rapping and singing, "
        "maintaining a confident and lively energy from start to finish."
    ),

    # ── Izulu ─────────────────────────────────────────────────────────────
    "Izulu_1": (
        "A traditional Zulu a cappella composition that opens with a robust men's bassline "
        "establishing a deep rhythmic pulse. Clear, resonant female voices enter in close "
        "harmony, creating intricate call-and-response patterns sung entirely in Zulu. "
        "Dynamic vocal layering intensifies through the chorus, incorporating group ululations "
        "and tight choral textures. The overall mood is positive, uplifting, and nostalgic, "
        "deeply rooted in the communal singing traditions of Zulu culture."
    ),
    "Izulu_2": (
        "A traditional Zulu a cappella composition that opens with a robust men's bassline "
        "establishing a deep rhythmic pulse. Clear, resonant female voices enter in close "
        "harmony, creating intricate call-and-response patterns sung entirely in Zulu. "
        "Dynamic vocal layering intensifies through the chorus, incorporating group ululations "
        "and tight choral textures. The overall mood is positive, uplifting, and nostalgic, "
        "deeply rooted in the communal singing traditions of Zulu culture."
    ),
    "Izulu_3": (
        "Rich maskandi guitar lines intertwine with smooth, layered isicathamiya vocal harmonies "
        "over a steady, percussive rhythm created by muted drums and handclaps. The arrangement "
        "alternates between call-and-response choral sections sung in Zulu and expressive lead "
        "guitar breaks, maintaining an uplifting and organically textured Zulu soundscape "
        "throughout. Male voices carry the choral harmonies with warmth and depth, and the "
        "mood is nostalgic and gently sombre."
    ),
    "Izulu_4": (
        "Rich maskandi guitar lines intertwine with smooth, layered isicathamiya vocal harmonies "
        "over a steady, percussive rhythm created by muted drums and handclaps. The arrangement "
        "alternates between call-and-response choral sections sung in Zulu and expressive lead "
        "guitar breaks, maintaining an uplifting and organically textured Zulu soundscape "
        "throughout. Male voices carry the choral harmonies with warmth and depth, and the "
        "mood is nostalgic and gently sombre."
    ),

    # ── Izwi_Lomculo ──────────────────────────────────────────────────────
    "Izwi_Lomculo_1": (
        "A lively Zulu afrobeat and electronic jazz fusion that kicks off with syncopated "
        "percussion and bubbling bass, layered with sparkling synths and jazzy Rhodes stabs. "
        "Saxophone improvisations weave through the electronic beats and polyrhythms, adding "
        "an improvisational warmth to the production. The bridge features a breakdown with "
        "muted trumpets before building back to a vibrant, dance-ready finale. A soulful female "
        "vocalist sings in Zulu with a chilled, inspiring delivery that floats effortlessly "
        "over the groovy mid-tempo beat."
    ),
    "Izwi_Lomculo_2": (
        "A lively Zulu afrobeat and electronic jazz fusion that kicks off with syncopated "
        "percussion and bubbling bass, layered with sparkling synths and jazzy Rhodes stabs. "
        "Saxophone improvisations weave through the electronic beats and polyrhythms, adding "
        "an improvisational warmth to the production. The bridge features a breakdown with "
        "muted trumpets before building back to a vibrant, dance-ready finale. A soulful female "
        "vocalist sings in Zulu with a chilled, inspiring delivery that floats effortlessly "
        "over the groovy mid-tempo beat."
    ),

    # ── MASKANDI_Ngihamba_Nezikhathi ──────────────────────────────────────
    "MASKANDI_Ngihamba_Nezikhathi_1": (
        "A modern Zulu band fuses punchy mbaqanga guitar, syncopated basslines, and driving "
        "drum kit patterns with traditional maskandi picking and rhythmic vocal harmonies sung "
        "in Zulu. Accordion and occasional synth textures layer in to create a fresh, danceable "
        "groove enriched by vibrant call-and-response passages. The overall feel is upbeat, "
        "mid-tempo, and hopeful, presenting a contemporary yet deeply rooted take on traditional "
        "South African Zulu musical forms, led by an expressive female vocalist."
    ),
    "MASKANDI_Ngihamba_Nezikhathi_2": (
        "A modern Zulu band fuses punchy mbaqanga guitar, syncopated basslines, and driving "
        "drum kit patterns with traditional maskandi picking and rhythmic vocal harmonies sung "
        "in Zulu. Accordion and occasional synth textures layer in to create a fresh, danceable "
        "groove enriched by vibrant call-and-response passages. The overall feel is upbeat, "
        "mid-tempo, and hopeful, presenting a contemporary yet deeply rooted take on traditional "
        "South African Zulu musical forms, led by an expressive female vocalist."
    ),

    # ── Ngihamba_Nezikhathi ───────────────────────────────────────────────
    "Ngihamba_Nezikhathi_1": (
        "A fast-paced Zulu fusion of mbaqanga and maskandi that opens with rhythmic acoustic "
        "guitar, deep bass, and lively drums overlaid by elastic lead guitar licks. Accordion "
        "and snare rolls punctuate the transitions with expressive flair, while a band of male "
        "and female voices deliver vibrant call-and-response passages sung in Zulu. The energy "
        "is relentless and joyful, deeply rooted in the living traditions of South African "
        "township music."
    ),
    "Ngihamba_Nezikhathi_2": (
        "A fast-paced Zulu fusion of mbaqanga and maskandi that opens with rhythmic acoustic "
        "guitar, deep bass, and lively drums overlaid by elastic lead guitar licks. Accordion "
        "and snare rolls punctuate the transitions with expressive flair, while a band of male "
        "and female voices deliver vibrant call-and-response passages sung in Zulu. The energy "
        "is relentless and joyful, deeply rooted in the living traditions of South African "
        "township music."
    ),

    # ── Ngipholile ────────────────────────────────────────────────────────
    "Ngipholile_1": (
        "A lively Zulu fusion that bursts open with punchy big band brass, syncopated drums, "
        "and dazzling piano. Maskandi-inspired guitar lines wind through layered vocal harmonies, "
        "while mbaqanga bass grooves keep the momentum driving forward. Percussion featuring "
        "bells, shakers, and claps adds theatrical flair well-suited for stage performance. "
        "A male rapper delivers confident verses in Zulu over kwaito and old-school trap "
        "influences, creating a lively, funky, and dance-floor-ready mood full of joy."
    ),
    "Ngipholile_2": (
        "A lively Zulu fusion that bursts open with punchy big band brass, syncopated drums, "
        "and dazzling piano. Maskandi-inspired guitar lines wind through layered vocal harmonies, "
        "while mbaqanga bass grooves keep the momentum driving forward. Percussion featuring "
        "bells, shakers, and claps adds theatrical flair well-suited for stage performance. "
        "A male rapper delivers confident verses in Zulu over kwaito and old-school trap "
        "influences, creating a lively, funky, and dance-floor-ready mood full of joy."
    ),

    # ── Ngiseyinthombi ────────────────────────────────────────────────────
    "Ngiseyinthombi_1": (
        "A Zulu amapiano and maskandi fusion that blends rolling log drums and syncopated "
        "percussion with traditional maskandi guitar riffs and indigenous rhythms. Verses flow "
        "with dynamic rap delivered in Zulu over electronic synth lines, led by a female "
        "vocalist. An explosive chorus erupts with a powerful multi-voice choir, amplifying "
        "the revolutionary and anthemic spirit of the track. The arrangement shifts dramatically "
        "between intimate rap verses and grand, cinematic choral moments."
    ),
    "Ngiseyinthombi_2": (
        "A Zulu amapiano and maskandi fusion that blends rolling log drums and syncopated "
        "percussion with traditional maskandi guitar riffs and indigenous rhythms. Verses flow "
        "with dynamic rap delivered in Zulu over electronic synth lines, led by a female "
        "vocalist. An explosive chorus erupts with a powerful multi-voice choir, amplifying "
        "the revolutionary and anthemic spirit of the track. The arrangement shifts dramatically "
        "between intimate rap verses and grand, cinematic choral moments."
    ),
    "Ngiseyinthombi_3": (
        "A Zulu amapiano and maskandi fusion that blends rolling log drums and syncopated "
        "percussion with traditional maskandi guitar riffs and indigenous rhythms. Verses flow "
        "with dynamic rap delivered in Zulu over electronic synth lines, led by a female "
        "vocalist. An explosive chorus erupts with a powerful multi-voice choir, amplifying "
        "the revolutionary and anthemic spirit of the track. The arrangement shifts dramatically "
        "between intimate rap verses and grand, cinematic choral moments."
    ),
    "Ngiseyinthombi_4": (
        "A Zulu amapiano and maskandi fusion that blends rolling log drums and syncopated "
        "percussion with traditional maskandi guitar riffs and indigenous rhythms. Verses flow "
        "with dynamic rap delivered in Zulu over electronic synth lines, led by a female "
        "vocalist. An explosive chorus erupts with a powerful multi-voice choir, amplifying "
        "the revolutionary and anthemic spirit of the track. The arrangement shifts dramatically "
        "between intimate rap verses and grand, cinematic choral moments."
    ),
    "Ngiseyinthombi_5": (
        "A Zulu amapiano and maskandi fusion that blends rolling log drums and syncopated "
        "percussion with traditional maskandi guitar riffs and indigenous rhythms. Verses flow "
        "with dynamic rap delivered in Zulu over electronic synth lines, led by a female "
        "vocalist. An explosive chorus erupts with a powerful multi-voice choir, amplifying "
        "the revolutionary and anthemic spirit of the track. The arrangement shifts dramatically "
        "between intimate rap verses and grand, cinematic choral moments."
    ),

    # ── Ngiyakhala ────────────────────────────────────────────────────────
    "Ngiyakhala_1": (
        "A Zulu kwaito and maskandi fusion that opens with a pulsating groove built from "
        "interlocking kwaito beats and maskandi guitar riffs. Traditional Zulu percussion and "
        "layered harmonies add richness and depth, while soaring, soulful female vocals weave "
        "through folk-inspired melodies sung in Zulu. The epic arrangement builds to a crescendo "
        "featuring rhythmic ululation and dynamic call-and-response vocals, supported by rich, "
        "organic textures and subtle electronic accents."
    ),
    "Ngiyakhala_2": (
        "A Zulu kwaito and maskandi fusion that opens with a pulsating groove built from "
        "interlocking kwaito beats and maskandi guitar riffs. Traditional Zulu percussion and "
        "layered harmonies add richness and depth, while soaring, soulful female vocals weave "
        "through folk-inspired melodies sung in Zulu. The epic arrangement builds to a crescendo "
        "featuring rhythmic ululation and dynamic call-and-response vocals, supported by rich, "
        "organic textures and subtle electronic accents."
    ),
    "Ngiyakhala_4": (
        "Amapiano keys and log drums establish the groove as intricate maskandi guitar introduces "
        "the verses, carried by soulful Zulu vocal phrasing from a male vocalist. The chorus "
        "erupts with an explosive multi-voice choir and electrified synths, seamlessly blending "
        "traditional Zulu textures with electronic production. The outro swells into epic, "
        "layered soul harmonies sung in Zulu. The energy is fast-paced, lively, and "
        "revolutionary in spirit throughout."
    ),
    "Ngiyakhala_5": (
        "Amapiano keys and log drums establish the groove as intricate maskandi guitar introduces "
        "the verses, carried by soulful Zulu vocal phrasing from a female vocalist. The chorus "
        "erupts with an explosive multi-voice choir and electrified synths, seamlessly blending "
        "traditional Zulu textures with electronic production. The outro swells into epic, "
        "layered soul harmonies sung in Zulu. The energy is fast-paced, lively, and "
        "revolutionary in spirit throughout."
    ),
    "Ngiyakhala_6": (
        "Amapiano keys and log drums establish the groove as intricate maskandi guitar introduces "
        "the verses, carried by soulful Zulu vocal phrasing from a female vocalist. The chorus "
        "erupts with an explosive multi-voice choir and electrified synths, seamlessly blending "
        "traditional Zulu textures with electronic production. The outro swells into epic, "
        "layered soul harmonies sung in Zulu. The energy is fast-paced, lively, and "
        "revolutionary in spirit throughout."
    ),

    # ── Qhakuva ───────────────────────────────────────────────────────────
    "Qhakuva": (
        "A Zulu electro and rap fusion built on syncopated synth lines, dark basslines, and "
        "a fast, driving drum pattern. Soft synth textures provide atmospheric depth beneath "
        "a dynamic arrangement that moves between spoken word passages and sung vocal sections. "
        "Male and female vocalists trade parts throughout in Zulu, blending contemporary "
        "electronic production with elements rooted in traditional South African music. "
        "The mood is intense, hypnotic, and layered with cultural identity."
    ),

    # ── Sikhona ───────────────────────────────────────────────────────────
    "Sikhona_1": (
        "A lively Zulu fusion that bursts open with punchy big band brass, syncopated drums, "
        "and dazzling piano. Maskandi-inspired guitar lines wind through layered vocal harmonies, "
        "while mbaqanga bass grooves maintain the driving momentum. Percussion featuring bells, "
        "shakers, and claps adds a theatrical, celebratory energy. A female vocalist delivers "
        "the lead with infectious joy in Zulu over kwaito, pop, and house influences, creating "
        "a mood that is jovial, hopeful, and vibrantly uplifting."
    ),
    "Sikhona_2": (
        "A lively Zulu fusion that bursts open with punchy big band brass, syncopated drums, "
        "and dazzling piano. Maskandi-inspired guitar lines wind through layered vocal harmonies, "
        "while mbaqanga bass grooves maintain the driving momentum. Percussion featuring bells, "
        "shakers, and claps adds a theatrical, celebratory energy. A female vocalist delivers "
        "the lead with infectious joy in Zulu over kwaito, pop, and house influences, creating "
        "a mood that is jovial, hopeful, and vibrantly uplifting."
    ),

    # ── Siphuma_Emsamo ────────────────────────────────────────────────────
    "Siphuma_Emsamo_1": (
        "A Zulu club fusion that blends kwaito's laid-back groove with punchy electronic synths, "
        "tight house kick-clap combinations, and gqom's dark, repetitive bass stabs. Layers of "
        "chopped vocal samples from a female vocalist singing in Zulu interplay over syncopated "
        "percussion, creating a hypnotic energy that evolves and shifts with each drop. The mood "
        "is mellow and smooth at a mid-tempo pace, with an undercurrent of emotional depth that "
        "draws the listener inward."
    ),
    "Siphuma_Emsamo_2": (
        "A Zulu club fusion that blends kwaito's laid-back groove with punchy electronic synths, "
        "tight house kick-clap combinations, and gqom's dark, repetitive bass stabs. Layers of "
        "chopped vocal samples from a female vocalist singing in Zulu interplay over syncopated "
        "percussion, creating a hypnotic energy that evolves and shifts with each drop. The mood "
        "is mellow and smooth at a mid-tempo pace, with an undercurrent of emotional depth that "
        "draws the listener inward."
    ),

    # ── Soweto_female ─────────────────────────────────────────────────────
    "Soweto_female_1": (
        "A Zulu kwaito and hip-hop fusion that blends deep house-inspired bass, syncopated "
        "percussion, and marimba riffs over spacious synth chords. Vocal lines alternate "
        "between rapped verses and chanted hooks sung in Zulu, layered with group call-and-response "
        "patterns that give the track a communal, street-level energy. The mood is jovial and "
        "chilled, with an optimistic and hopeful spirit that carries through the entire track."
    ),
    "Soweto_female_2": (
        "A Zulu kwaito and hip-hop fusion that blends deep house-inspired bass, syncopated "
        "percussion, and marimba riffs over spacious synth chords. Vocal lines alternate "
        "between rapped verses and chanted hooks sung in Zulu, layered with group call-and-response "
        "patterns that give the track a communal, street-level energy. The mood is jovial and "
        "chilled, with an optimistic and hopeful spirit that carries through the entire track."
    ),

    # ── Soweto_male ───────────────────────────────────────────────────────
    "Soweto_male_1": (
        "A Zulu kwaito and hip-hop fusion that blends deep house-inspired bass, syncopated "
        "percussion, and marimba riffs over spacious synth chords. A male vocalist alternates "
        "between rapped verses and chanted hooks sung in Zulu, layered with group call-and-response "
        "patterns that give the track a communal, street-level energy. The mood is jovial and "
        "chilled, with an optimistic and hopeful spirit that carries through the entire track."
    ),
    "Soweto_male_2": (
        "A Zulu kwaito and hip-hop fusion that blends deep house-inspired bass, syncopated "
        "percussion, and marimba riffs over spacious synth chords. A male vocalist alternates "
        "between rapped verses and chanted hooks sung in Zulu, layered with group call-and-response "
        "patterns that give the track a communal, street-level energy. The mood is jovial and "
        "chilled, with an optimistic and hopeful spirit that carries through the entire track."
    ),

    # ── Umhlaba ───────────────────────────────────────────────────────────
    "Umhlaba_1": (
        "A Zulu kwaito and maskandi fusion that opens with traditional Zulu percussion and "
        "maskandi guitar establishing a vibrant and grounded groove. Lush choral harmonies enter "
        "to add fullness and richness, while marabi-inspired keyboards and rolling bass lines "
        "propel the rhythm forward. Call-and-response vocals sung in Zulu bring an anthemic "
        "communal spirit to the arrangement, with layered hand percussion and electric elements "
        "woven in for modern energy. A female vocalist leads the choral arrangement with "
        "warmth and conviction."
    ),
    "Umhlaba_2": (
        "A Zulu kwaito and maskandi fusion that opens with traditional Zulu percussion and "
        "maskandi guitar establishing a vibrant and grounded groove. Lush choral harmonies enter "
        "to add fullness and richness, while marabi-inspired keyboards and rolling bass lines "
        "propel the rhythm forward. Call-and-response vocals sung in Zulu bring an anthemic "
        "communal spirit to the arrangement, with layered hand percussion and electric elements "
        "woven in for modern energy. A female vocalist leads the choral arrangement with "
        "warmth and conviction."
    ),

    # ── Umhlaba_wa_bo_Koko ────────────────────────────────────────────────
    "Umhlaba_wa_bo_Koko_1": (
        "A Zulu maskandi and isicathamiya fusion that opens with punchy big band brass, "
        "syncopated drums, and dazzling piano. Maskandi guitar lines weave through layered "
        "vocal harmonies rooted in traditional Zulu and country influences, while mbaqanga "
        "bass grooves keep the energy moving forward. Percussion featuring bells, shakers, "
        "and claps adds theatrical warmth and a sense of celebration. A female vocalist sings "
        "in Zulu with a heartfelt and sombre delivery, navigating the emotional space between "
        "grief and quiet hope."
    ),
    "Umhlaba_wa_bo_Koko_2": (
        "A Zulu maskandi and isicathamiya fusion that opens with punchy big band brass, "
        "syncopated drums, and dazzling piano. Maskandi guitar lines weave through layered "
        "vocal harmonies rooted in traditional Zulu and country influences, while mbaqanga "
        "bass grooves keep the energy moving forward. Percussion featuring bells, shakers, "
        "and claps adds theatrical warmth and a sense of celebration. A female vocalist sings "
        "in Zulu with a heartfelt and sombre delivery, navigating the emotional space between "
        "grief and quiet hope."
    ),
    "Umhlaba_wa_bo_Koko_3": (
        "A Zulu maskandi and isicathamiya fusion that opens with punchy big band brass, "
        "syncopated drums, and dazzling piano. Maskandi guitar lines weave through layered "
        "vocal harmonies rooted in traditional Zulu and country influences, while mbaqanga "
        "bass grooves keep the energy moving forward. Percussion featuring bells, shakers, "
        "and claps adds theatrical warmth and a sense of celebration. A female vocalist sings "
        "in Zulu with a heartfelt and sombre delivery, navigating the emotional space between "
        "grief and quiet hope."
    ),
    "Umhlaba_wa_bo_Koko_4": (
        "A Zulu maskandi and isicathamiya fusion that opens with punchy big band brass, "
        "syncopated drums, and dazzling piano. Maskandi guitar lines weave through layered "
        "vocal harmonies rooted in traditional Zulu and country influences, while mbaqanga "
        "bass grooves keep the energy moving forward. Percussion featuring bells, shakers, "
        "and claps adds theatrical warmth and a sense of celebration. A female vocalist sings "
        "in Zulu with a heartfelt and sombre delivery, navigating the emotional space between "
        "grief and quiet hope."
    ),
    "Umhlaba_wa_bo_Koko_5": (
        "A Zulu maskandi and isicathamiya fusion that opens with punchy big band brass, "
        "syncopated drums, and dazzling piano. Maskandi guitar lines weave through layered "
        "vocal harmonies rooted in traditional Zulu and country influences, while mbaqanga "
        "bass grooves keep the energy moving forward. Percussion featuring bells, shakers, "
        "and claps adds theatrical warmth and a sense of celebration. A male vocalist sings "
        "in Zulu with a heartfelt and sombre delivery, navigating the emotional space between "
        "grief and quiet hope."
    ),
    "Umhlaba_wa_bo_Koko_6": (
        "Opening with intricate acoustic guitar picking and concertina characteristic of "
        "maskandi, the groove is established by gently syncopated percussion and upright bass. "
        "Isicathamiya-style vocal harmonies enter, layered for depth and blending with country "
        "pedal steel influences. Traditional Zulu musical elements punctuate the arrangement "
        "throughout, with interlocking guitar parts and expressive vocal interplay sung in Zulu "
        "leading into richly textured instrumental breaks."
    ),
    "Umhlaba_wa_bo_Koko_7": (
        "Opening with intricate acoustic guitar picking and concertina characteristic of "
        "maskandi, the groove is established by gently syncopated percussion and upright bass. "
        "Isicathamiya-style vocal harmonies enter, layered for depth and blending with country "
        "pedal steel influences. Traditional Zulu musical elements punctuate the arrangement "
        "throughout, with interlocking guitar parts and expressive vocal interplay sung in Zulu "
        "leading into richly textured instrumental breaks."
    ),

    # ── Uthando ───────────────────────────────────────────────────────────
    "Uthando_1": (
        "A traditional Zulu maskandi ballad led by expressive guitar picking and concertina "
        "lines, underscored by steady percussion using African drums and rattles. "
        "Call-and-response vocal patterns in Zulu carry the verses, with layered harmonies "
        "accentuating the hooks throughout. The organic, earthy textures give the track a raw "
        "and rhythmic pulse. A female vocalist delivers with meditative depth at a slow, chilled "
        "tempo, evoking heartfelt nostalgia and a deep connection to Zulu musical heritage."
    ),
    "Uthando_2": (
        "A traditional Zulu maskandi ballad led by expressive guitar picking and concertina "
        "lines, underscored by steady percussion using African drums and rattles. "
        "Call-and-response vocal patterns in Zulu carry the verses, with layered harmonies "
        "accentuating the hooks throughout. The organic, earthy textures give the track a raw "
        "and rhythmic pulse. A female vocalist delivers with meditative depth at a slow, chilled "
        "tempo, evoking heartfelt nostalgia and a deep connection to Zulu musical heritage."
    ),

    # ── Zulu ──────────────────────────────────────────────────────────────
    "Zulu_1": (
        "The song opens with rhythmic acoustic guitar typical of maskandi style, accented by "
        "percussive isiZulu drum patterns. Male and female choral vocals enter in layered "
        "call-and-response, supported by bass and concertina, all sung in Zulu. Sections "
        "feature traditional mouth bow and intermittent handclaps that add a luminous, resonant "
        "texture to the arrangement. The mood is meditative and chilled, moving at a slow, "
        "thoughtful tempo with heartfelt, poetic warmth rooted in Zulu musical tradition."
    ),
    "Zulu_2": (
        "The song opens with rhythmic acoustic guitar typical of maskandi style, accented by "
        "percussive isiZulu drum patterns. Male and female choral vocals enter in layered "
        "call-and-response, supported by bass and concertina, all sung in Zulu. Sections "
        "feature traditional mouth bow and intermittent handclaps that add a luminous, resonant "
        "texture to the arrangement. The mood is meditative and chilled, moving at a slow, "
        "thoughtful tempo with heartfelt, poetic warmth rooted in Zulu musical tradition."
    ),
}


def main():
    data = json.loads(DATASET_JSON.read_text(encoding="utf-8"))
    samples = data["samples"]

    updated = 0
    missing = []

    for s in samples:
        stem = s["filename"].replace(".mp3", "")
        if stem in CAPTIONS:
            s["caption"] = CAPTIONS[stem]
            updated += 1
        else:
            missing.append(s["filename"])

    data["samples"] = samples
    DATASET_JSON.write_text(json.dumps(data, indent=2, ensure_ascii=False), encoding="utf-8")

    print(f"Updated {updated} / {len(samples)} captions to full narrative style.")
    if missing:
        print(f"WARNING — no caption written for: {missing}")
    else:
        print("All 63 captions updated successfully.")


if __name__ == "__main__":
    main()
