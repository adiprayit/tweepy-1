#!/usr/bin/env python
#------------------------------------------------------------------------------
# Disclaimer: For educational purpose ONLY. Use at your own risk.
# Note      : Just comment out the app that you don't wanna use, it'll save
#             your time approving all of them.
#------------------------------------------------------------------------------
# Perhatian : Hanya untuk tujuan pembelajaran semata. Pembuat script ini tidak
#             bertanggungjawab atas penggunaan/penyalahgunaan script ini.
# Catatan   : Cukup gunakan aplikasi yang diinginkan, yang tidak digunakan bisa
#             di-comment untuk mempercepat proses approval.
#------------------------------------------------------------------------------
import sys
import tweepy

app = [
{
 'cl':'UberSocial',
 'ck':'xy2SjfpKMhDZSECIlgpS7g',
 'cs':'n2rHTrtQeuxNCJYk3l2cxM7Jf1J1mTZTfJVersSlzU',
 'ak':'',
 'as':''
},
{
 'cl':'UberSocial for Blackberry',
 'ck':'6XIk781PMICfV2w19BfQLw',
 'cs':'RoxBuNOkrln51abF0XT9IXevKCmbyo3dCJb435SOc4',
 'ak':'',
 'as':''
},
{
 'cl':'Twidroyd',
 'ck':'0YCqwPFyKUGYEZKIUrh6CA',
 'cs':'CLsIH4fMdA8nHf2jqTjGBk42MRrgyPmj2tzCwBSeU',
 'ak':'',
 'as':''
},
{
 'cl':'Twidroyd for android',
 'ck':'pCun0Kilhc6VF7fno2g',
 'cs':'3gGiWlgvMWHYy3RrFqj8jWw00kGOg9eIIqOwGiBa1c',
 'ak':'',
 'as':''
},
{
 'cl':'Twitter for Mac',
 'ck':'3rJOl1ODzm9yZy63FACdg',
 'cs':'5jPoQ5kQvMJFDYRNE8bQ4rHuds4xJqhvgNJM4awaE8',
 'ak':'',
 'as':''
},
{
 'cl':'Twitter for iPad',
 'ck':'CjulERsDeqhhjSme66ECg',
 'cs':'IQWdVyqFxghAtURHGeGiWAsmCAGmdW3WmbEx6Hck',
 'ak':'',
 'as':''
},
{
 'cl':'Twitter for iPhone',
 'ck':'IQKbtAYlXLripLGPWd0HUA',
 'cs':'GgDYlkSvaPxGxC4X8liwpUoqKwwr3lCADbz8A7ADU',
 'ak':'',
 'as':''
},
{
 'cl':'TwitBird iPad',
 'ck':'xsOKAIRcGlO8iRC5eADcw',
 'cs':'LKYXHWUbbC2MO01o7chocE2XFraSDdhurxsBXkurEK8',
 'ak':'',
 'as':''
},
{
 'cl':'TweetDeck',
 'ck':'yT577ApRtZw51q4NPMPPOQ',
 'cs':'3neq3XqN5fO3obqwZoajavGFCUrC42ZfbrLXy5sCv8',
 'ak':'',
 'as':''
},
{
 'cl':'Echofon',
 'ck':'yqoymTNrS9ZDGsBnlFhIuw',
 'cs':'OMai1whT3sT3XMskI7DZ7xiju5i5rAYJnxSEHaKYvEs',
 'ak':'',
 'as':''
},
{
 'cl':'HootSuite',
 'ck':'w1Gybt9LP9zG46mS1X3UAw',
 'cs':'hRIK4RWjAO4pokQCvmNCynRAY8Jc8edV1kcV2go6g',
 'ak':'',
 'as':''
},
{
 'cl':'Seesmic Twhirl',
 'ck':'nvyZCpiELVuWhBvPh3Sw',
 'cs':'scTemkSBpESGKBlSSCYQuinaQjpf5Hc0BBUBZpFbNsw',
 'ak':'',
 'as':''
},
{
 'cl':'Seesmic for Android',
 'ck':'WMztNBVHsW9S4QKf6S1Rg',
 'cs':'b2k7ccc9TATOqhKrB2eJpPoZabATy2yXtjJ8LlG0',
 'ak':'',
 'as':''
},
{
 'cl':'Bad Kitty',
 'ck':'U2wlL59B1VSoncuM5g',
 'cs':'470qgAWiz2Wq8zH1oTCyHol3TTwpOml4U8yeyZmxNtg',
 'ak':'',
 'as':''
},
{
 'cl':'DestroyTwitter',
 'ck':'40iqOgCcXcJYwqoa02D7nQ',
 'cs':'o0emdpQvijub2tMXpA7wAVwt3tI4FSx447NfWECS8',
 'ak':'',
 'as':''
},
{
 'cl':'Tweetcaster',
 'ck':'rvCsVGIl2etwokzk0rZ3w',
 'cs':'DeyIhM6lJKEXhutMyRWuHiAbEG7ITs12J03i0Xm4',
 'ak':'',
 'as':''
},
{
 'cl':'Tweetcaster for Android',
 'ck':'279MLYOwrFyFFcU6J68u6w',
 'cs':'ck62P6E731zXWKZgNcwu0cJh6K3LTtTOlCQfgOg',
 'ak':'',
 'as':''
},
{
 'cl':'moTweets',
 'ck':'7DIGBXQCmgR28M8AR9Q',
 'cs':'Cc2dQkA4TdMXoeuB9sedA1uxGB1zrrNmHjF3jfbhSo',
 'ak':'',
 'as':''
},
{
 'cl':'ChromedBird',
 'ck':'KkrTiBu0hEMJ9dqS3YCxw',
 'cs':'MsuvABdvwSn2ezvdQzN4uiRR44JK8jESTIJ1hrhe0U',
 'ak':'',
 'as':''
},
{
 'cl':'TwittAMP',
 'ck':'XHOuZ5bBMAMleIpm4h28JA',
 'cs':'nZ0IsdMUSdSSuSIDojjpVxYqCeXIBCPii5o565DKs',
 'ak':'',
 'as':''
},
{
 'cl':'Mixero',
 'ck':'bJaKx0V8hdDAfQFXK4P08g',
 'cs':'DRSZv2Bc1Qgl0HDe7gGjZXYuQwkwk9gZAYgEFNnWJs',
 'ak':'',
 'as':''
},
{
 'cl':'detikcom for Blackberry',
 'ck':'SWtEBuWHarToHiCP7o1uUA',
 'cs':'gJJtTr3x5Jpv8dGjXKksgkmSrWUxk3TGEOj0DXCc4gg',
 'ak':'',
 'as':''
},
{
 'cl':'detikcom for iPhone',
 'ck':'pYHDVBc04K4EAhUyImw',
 'cs':'CpLMtELKahoqhSli1ZrEaZt6EvJevCSZ1XDoGdBU',
 'ak':'',
 'as':''
},
{
 'cl':'detikcom for Android',
 'ck':'kD5eBZypDVLPlXJVuxmaUw',
 'cs':'PekMoIZkcYy63JCdEdej5CVaxywIJsjrxPjjXX9qGI',
 'ak':'',
 'as':''
},
{
 'cl':'A.Plus App',
 'ck':'DC2XbSUhfLntKJX2XhSBg',
 'cs':'Vd0CL3NFXgQdfg0qxPRLybuBfR6wj58R5Dl7fbJw',
 'ak':'',
 'as':''
},
{
 'cl':'Jing',
 'ck':'9tGyVimyayvyqUlz7L7JYA',
 'cs':'PcBO252zXfSh4SljRY0kp7rZvWeF4lq2k0lYycu0',
 'ak':'',
 'as':''
},
{
 'cl':'Blaq for Playbook',
 'ck':'lRFo1RRPXusr9GAORfms7w',
 'cs':'uqujPqX6YRNT2BZ7zPu0IdIZCk3DYojpIPr3Vwgk',
 'ak':'',
 'as':''
},
{
 'cl':'Instagram',
 'ck':'7YBPrscvh0RIThrWYVeGg',
 'cs':'sMO1vDyJ9A0xfOE6RyWNjhTUS1sNqsa7Ae14gOZnw',
 'ak':'',
 'as':''
},
{
 'cl':'Mindtalk for Android',
 'ck':'SGvBZnSxHbBdwcNncowOBQ',
 'cs':'ZmimffOX0ObOFD2piPUY22U3mTZKEtbm2nUP61QHp8',
 'ak':'',
 'as':''
},
{
 'cl':'twitbot for iOS',
 'ck':'8AeR93em84Pyum5i1QGA',
 'cs':'ugCImRuw376Y9t9apIq6bgWGNbb1ymBrx2K5NK0ZI',
 'ak':'',
 'as':''
},
{
  'cl':'MivoTV',
  'ck':'7A6TSGzUKxGSIxZKCsXsmA',
  'cs':'4PgJEFC7ovURlrkS9qWtAIrpyHKddsZfq00GVw962o',
  'ak':'',
  'as':''
},
{
  'cl':'Path 2.0',
  'ck':'9UiCHv8e9fXfdYiIK26Jfg',
  'cs':'qFcIA6Jo7mNURwzpdw1ieXkSzK4vwtF2O6NKo7i8',
  'ak':'',
  'as':''
},
]

loc = [
['Jakarta, Setiabudi',-6.217503,106.832385],
['Jakarta, Kebayoran',-6.256175,106.812301],
['Magelang, Borobudur',-7.603182,110.204067],
['Turki, Istanbul',40.976922,28.81460],
['Libya, Tripoli',32.876174,13.187507],
['Libya, Secretariat of Land Reclamation',32.8646,13.2153],
['Mt.Fuji',35.3624000549,138.725997925],
['Mt.Aso',32.86961476482221,131.0673704725062],
['Fountain of Youth',41.978469,-122.709753],
['Hang Nadim Batam',1.12575,104.112]
]

def get_auth(a):
    try:
        auth = tweepy.OAuthHandler(a['ck'], a['cs'])
        auth_url = auth.get_authorization_url()
        print 'Please authorize: ' + auth_url
        verify = raw_input('PIN: ').strip()
        auth.get_access_token(verify)
        print "'cl':'%s'\n'ak':'%s'\n'as':'%s'" % (a['cl'], auth.access_token.key, auth.access_token.secret)
        sys.exit()
    except KeyboardInterrupt:
        print "\nAborted!"

if __name__ == '__main__':
    try:
        for a in app:
            if (not a['ak']) or (not a['as']): get_auth(a)

        if len(sys.argv) < 2:
            msg = raw_input('[*] Enter status: ')
        else:
            msg = sys.argv[1]

        if len(msg) > 140:
            raise Exception('[-] status message is too long!')

        i = 0
        print '[*] Update Via:'
        for v in app:
            print "[*] %s. %s" % (i+1 , v['cl'])
            i += 1

        x = int(raw_input('[?] Update Via: '))
        if x > i:
            print '[-] Choose valid apps!'
            sys.exit()
        x -= 1

        i = 0
        print '[*] Choose Location:'
        for l in loc:
            print "[*] %s. %s" % (i+1 , l[0])
            i += 1

        p = int(raw_input('[?] Location Number: '))
        if p > i:
            print '[-] Invalid location!'
            sys.exit()
        p -= 1

        auth = tweepy.OAuthHandler(app[x]['ck'], app[x]['cs'])
        auth.set_access_token(app[x]['ak'], app[x]['as'])
        api = tweepy.API(auth)
        result = api.update_status(msg, lat=loc[p][1], long=loc[p][2])
        if result:
            print '[*] Status updated from ' + loc[p][0] + '!'
        else:
            print "[-] Update failed!"

    except KeyboardInterrupt:
        print "\n[-] aborted!"
        sys.exit()
