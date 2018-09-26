# OpenStack current cycle information
CYCLE = 'stein'                 # Cycle name/code
# Date format [YYYY, MM, DD] without any leading zero :))
START_DATE = [2018, 8, 31]       # First date of the cycle
RELEASE_DATE = [2019, 4, 10]    # Last date of the cycle

# Output markdown filename
MARKDOWN_FILE = 'fvl-contribution-stein-{}-{}.md'

# URL to contribution API of Stackalytics
CONTRIBUTION_API = ('http://stackalytics.com/api/1.0/contribution?'
                    'release={}&company=fujitsu&user_id={}')

# Overall team target for commit/review
TEAM_TARGET = {
    'commit': 178,
    'review': 607,
}

# Member information and commit/review target for each member
MEMBERS = [
    # Format: user id, member name, target commit, target review
    {'user_id': 'phuongnh', 'name': 'Phuong', 'commit': 44, 'review': 152},
    {'user_id': 'donghm', 'name': 'Dong', 'commit': 44, 'review': 152},
    {'user_id': 'ducnv95', 'name': 'Duc', 'commit': 44, 'review': 152},
    {'user_id': 'reiichannn', 'name': 'Trang', 'commit': 44, 'review': 152},
]

# Table headers for team contribution summary
# See comment for the calculation
TEAM_HEADERS = [
    'No.',
    'Item',
    'Target',
    'Actual',
    'Actual remain',            # = Target - Actual
    'Target to date',           # = Target to date
    'Target to date remain',    # = Target - Target to date
    'Behind schedule',    # = Target to date - Actual
]

# Table headers for detail team member's contribution
# See comment for the calculation
MEMBER_HEADERS = [
    'No.',
    'Member',
    'Target',
    'Actual',
    'Actual remain',            # = Target - Actual
    'Target to date',           # = Target to date
    'Target to date remain',    # = Target - Target to date
    'Behind schedule',    # = Target to date - Actual
]
