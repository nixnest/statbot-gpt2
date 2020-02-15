import json
import sys

zack_owner_date = 1543017600000


def process_json(channel: str):
    with open('data/%s.json' % channel, 'r') as f:
        data = json.loads(f.read())

    messages = [message for message in data['results'][0]['series'][0]['values'] if message[0] > zack_owner_date]

    txt = ''
    for message in messages:
        txt += '[[%s|%s]]:\n%s\n\n' % (message[1], message[2], message[5])

    print('number of messages: %s' % len(messages))

    with open('data/%s.txt' % channel, 'w') as f:
        f.write(txt)


if __name__ == '__main__':
    if len(sys.argv) < 2:
        print('must specify channel name')
        sys.exit(1)

    process_json(sys.argv[1])
