"""
This sample demonstrates a simple skill built with the Amazon Alexa Skills Kit.
The Intent Schema, Custom Slots, and Sample Utterances for this skill, as well
as testing instructions are located at http://amzn.to/1LzFrj6

For additional samples, visit the Alexa Skills Kit Getting Started guide at
http://amzn.to/1LGWsLG
"""

from __future__ import print_function
import urllib2, json, random

def lambda_handler(event, context):

    """ Route the incoming request based on type (LaunchRequest, IntentRequest,
    etc.) The JSON body of the request is provided in the event parameter.
    """
    print("event.session.application.applicationId=" +
          event['session']['application']['applicationId'])

    # TODO
    """
    Uncomment this if statement and populate with your skill's application ID to
    prevent someone else from configuring a skill that sends requests to this
    function.
    """
    # if (event['session']['application']['applicationId'] !=
    #         "amzn1.echo-sdk-ams.app.[unique-value-here]"):
    #     raise ValueError("Invalid Application ID")

    if event['session']['new']:
        on_session_started({'requestId': event['request']['requestId']},
                           event['session'])

    if event['request']['type'] == "LaunchRequest":
        return on_launch(event['request'], event['session'])
    elif event['request']['type'] == "IntentRequest":
        return on_intent(event['request'], event['session'])
    elif event['request']['type'] == "SessionEndedRequest":
        return on_session_ended(event['request'], event['session'])


def on_session_started(session_started_request, session):
    # Called when the session starts
    print("on_session_started requestId=" + session_started_request['requestId']
          + ", sessionId=" + session['sessionId'])


def on_launch(launch_request, session):
    # Called when the user launches the skill without specifying what they want
    print("on_launch requestId=" + launch_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    return get_welcome_response()


def on_intent(intent_request, session):
    """ Called when the user specifies an intent for this skill """

    print("on_intent requestId=" + intent_request['requestId'] +
          ", sessionId=" + session['sessionId'])

    intent = intent_request['intent']
    intent_name = intent_request['intent']['name']

    # Dispatch to your skill's intent handlers
    if intent_name == "getCounter":
        return get_counter_hero(intent, session)
    elif intent_name == "randomHero":
        return get_random_hero(intent, session)
    elif intent_name == "serverStatus":
        return get_steam_status(intent, session)
    else:
        raise ValueError("Invalid intent")


def on_session_ended(session_ended_request, session):
    # Called when the user ends the session.
    #Is not called when the skill returns should_end_session=true
    print("on_session_ended requestId=" + session_ended_request['requestId'] +
          ", sessionId=" + session['sessionId'])
    # add cleanup logic here

# --------------- Functions that control the skill's behavior ------------------


def get_welcome_response():
    # If we wanted to initialize the session to have some attributes we could add those here

    session_attributes = {}
    card_title = "Welcome"
    speech_output = "Your Dota Guy at your service. \n" \
                    "Trouble connecting? Check if Steam is doing fine:  " \
                    "how are the steam servers doing"
    # If the user either does not reply to the welcome message or says something
    # that is not understood, they will be prompted again with this text.
    reprompt_text = "I can even help you pick heroes and counter-picks." \
                    "pick me a hero to counter Axe!"
    should_end_session = False
    return build_response(session_attributes, build_speechlet_response(
        card_title, speech_output, reprompt_text, should_end_session))



def get_counter_hero(intent, session):
    session_attributes = {}
    reprompt_text = None

    hero_lst = ['Razor', 'Rubick', 'Phantom Lancer', 'Legion Commander', 'Brewmaster', 'Outworld Devourer', 'Sniper', 'Lina', 'Sven', 'Visage', 'Undying', 'Tiny', 'Tidehunter', 'Puck', 'Ursa', 'Magnus', 'Earthshaker', 'Windrunner', 'Techies', 'Crystal Maiden', 'Batrider', 'Riki', 'Invoker', 'Venomancer', 'Timbersaw', 'Wraithking', 'Anti Mage', 'Ancient Apparition', 'Troll Warlord', 'Lich', 'Enchantress', 'Bristleback', 'Pudge', 'Faceless Void', 'Tinker', 'Mirana', 'Bounty Hunter', 'Treant Protector', 'Gyrocopter', 'Slardar', 'Lifestealer', 'Jakiro', 'Terrorblade', 'Dazzle', 'Chaos Kinght', 'Abaddon', 'Shadow Demon', 'Axe', 'Zeus', 'Alchemist', 'Elder Titan', 'Pugna', 'Vengeful Spirit', 'Broodmother', 'Sand King', 'Lion', 'Witch Doctor', 'Ember Spirit', 'Clockwerk', 'Phantom Assassin', 'Warlock', 'Chen', 'Keeper of the Light', 'Beastmaster', 'Centaur Warruner', 'Naga Siren', 'Kunkka', 'Phoenix', 'Silencer', 'Morphling', 'Slark', 'Meepo', 'Shadow Shaman', 'Templar Assassin', 'Juggernaut', 'Natures Prophet', 'Necrolyte', 'Earth Spirit', 'Doom', 'Shadow Fiend', 'Omniknight', 'Skywrath Mage', 'Weaver', 'Wisp', 'Medusa', 'Nightstalker', 'Ogre Magi', 'Tusk', 'Spectre', 'Nyx Assassin', 'Drow Ranger', 'Clinkz', 'Disruptor', 'Bane', 'Enigma', 'Dragon Knight', 'Viper', 'Queen of Pain', 'Luna', 'Huskar', 'Death Prophet', 'Storm Spirit', 'Spirit Breaker', 'Dark Seer', 'Bloodseeker', 'Lone Druid', 'Lycan', 'Leshrac']

    opponent = intent["slots"]["Hero"]["value"]

    speech_output = random.choice(hero_lst) + " should be a good pick against " + opponent
    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))



def get_random_hero(intent, session):
    session_attributes = {}
    reprompt_text = None

    hero_lst = ['Razor', 'Rubick', 'Phantom Lancer', 'Legion Commander', 'Brewmaster', 'Outworld Devourer', 'Sniper', 'Lina', 'Sven', 'Visage', 'Undying', 'Tiny', 'Tidehunter', 'Puck', 'Ursa', 'Magnus', 'Earthshaker', 'Windrunner', 'Techies', 'Crystal Maiden', 'Batrider', 'Riki', 'Invoker', 'Venomancer', 'Timbersaw', 'Wraithking', 'Anti Mage', 'Ancient Apparition', 'Troll Warlord', 'Lich', 'Enchantress', 'Bristleback', 'Pudge', 'Faceless Void', 'Tinker', 'Mirana', 'Bounty Hunter', 'Treant Protector', 'Gyrocopter', 'Slardar', 'Lifestealer', 'Jakiro', 'Terrorblade', 'Dazzle', 'Chaos Kinght', 'Abaddon', 'Shadow Demon', 'Axe', 'Zeus', 'Alchemist', 'Elder Titan', 'Pugna', 'Vengeful Spirit', 'Broodmother', 'Sand King', 'Lion', 'Witch Doctor', 'Ember Spirit', 'Clockwerk', 'Phantom Assassin', 'Warlock', 'Chen', 'Keeper of the Light', 'Beastmaster', 'Centaur Warruner', 'Naga Siren', 'Kunkka', 'Phoenix', 'Silencer', 'Morphling', 'Slark', 'Meepo', 'Shadow Shaman', 'Templar Assassin', 'Juggernaut', 'Natures Prophet', 'Necrolyte', 'Earth Spirit', 'Doom', 'Shadow Fiend', 'Omniknight', 'Skywrath Mage', 'Weaver', 'Wisp', 'Medusa', 'Nightstalker', 'Ogre Magi', 'Tusk', 'Spectre', 'Nyx Assassin', 'Drow Ranger', 'Clinkz', 'Disruptor', 'Bane', 'Enigma', 'Dragon Knight', 'Viper', 'Queen of Pain', 'Luna', 'Huskar', 'Death Prophet', 'Storm Spirit', 'Spirit Breaker', 'Dark Seer', 'Bloodseeker', 'Lone Druid', 'Lycan', 'Leshrac']

    speech_output = "Why dont you play " + random.choice(hero_lst)
    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))



def get_steam_status(intent, session):
    session_attributes = {}
    reprompt_text = None

    # Call the isSteamRip API
    url = "http://is.steam.rip/api/v1/?request=IsSteamRip"
    req = urllib2.Request(url, headers={ 'User-Agent': 'Mozilla/5.0' })
    data = json.loads(urllib2.urlopen(req).read())
    #print (json.dumps(data, indent=4, sort_keys=True))

    if data['result']["isSteamRip"]:
        speech_output = "Oh my God! Steam Servers are Down!"
    else:
        speech_output = "Steam Servers are up. All Systems Go!"

    should_end_session = False

    return build_response(session_attributes, build_speechlet_response(
        intent['name'], speech_output, reprompt_text, should_end_session))



# --------------- Helpers that build all of the responses ----------------------


def build_speechlet_response(title, output, reprompt_text, should_end_session):
    return {
        'outputSpeech': {
            'type': 'PlainText',
            'text': output
        },
        'card': {
            'type': 'Simple',
            'title': 'SessionSpeechlet - ' + title,
            'content': 'SessionSpeechlet - ' + output
        },
        'reprompt': {
            'outputSpeech': {
                'type': 'PlainText',
                'text': reprompt_text
            }
        },
        'shouldEndSession': should_end_session
    }


def build_response(session_attributes, speechlet_response):
    return {
        'version': '1.0',
        'sessionAttributes': session_attributes,
        'response': speechlet_response
    }
