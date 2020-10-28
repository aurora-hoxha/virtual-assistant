import requests

from utils.template_renderer import TemplateRender


def search_users(query_param):
    ig_response = requests.get('https://www.instagram.com/web/search/topsearch/?query={}'.format(query_param))
    json_response = ig_response.json()
    users = json_response['users']
    places = json_response['places']
    hashtags = json_response['hashtags']

    for user in users:
        user_ig = user['user']
        print('{}------------------------------------------'.format(user['position']))
        print('Username {}'.format(user_ig['username']))
        print('Profile photo {}'.format(user_ig['profile_pic_url']))

    context_data = {
        'template_name': 'profile-list.html',
        'data': [user['user'] for user in users],
        'output': 'output.html'
    }
    # Klasa TemplateRender ka nevoje per nje dict si param.
    new = TemplateRender(context_data)

    return True


# search_users('Marsel beqiri')
# search_users('Aurora Hoxha')
# abs_path = os.path.abspath((inspect.stack()[0])[1])
# directory_of_1py = os.path.dirname(abs_path)

# context_data = {
#     'template_name': 'profile-list.html',
#     'data': {},
#     'output': 'output.html'
# }
#
# new = TemplateRender(context_data)
